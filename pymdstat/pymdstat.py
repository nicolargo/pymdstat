#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyMDstat
# ...
#
# Copyright (C) 2014 Nicolargo <nicolas@nicolargo.com>

from re import split
try:
    from functools import reduce
except:
    pass

# Limit import to class...
__all__ = ['MdStat']


# Classes
class MdStat(object):
    """
    Main mdstat class
    """

    def __init__(self, path='/proc/mdstat'):
        self.path = path
        self.content = ''

        # Stats will be stored in a dict
        self.stats = self.load()

    def __str__(self):
        '''Return the content of the file'''
        return self.content

    def __repr__(self):
        '''Return the content of the file'''
        return self.content

    def get_path(self):
        '''Return the mdstat file path'''
        return self.path

    def get_stats(self):
        '''Return the stats'''
        return self.stats

    def personalities(self):
        '''Return the personalities (list)'''
        return self.get_stats()['personalities']

    def arrays(self):
        '''Return the arrays (list)'''
        return self.get_stats()['arrays'].keys()

    def type(self, array):
        '''Return the array's type'''
        return self.get_stats()['arrays'][array]['type']

    def status(self, array):
        '''Return the array's status'''
        return self.get_stats()['arrays'][array]['status']

    def components(self, array):
        '''Return the componant of the arrays (list)'''
        return self.get_stats()['arrays'][array]['components'].keys()

    def available(self, array):
        '''Return the array's available componants number'''
        return int(self.get_stats()['arrays'][array]['available'])

    def used(self, array):
        '''Return the array's used componants number'''
        return int(self.get_stats()['arrays'][array]['used'])

    def config(self, array):
        '''Return the array's config/status
        U mean OK
        _ mean Failed'''
        return self.get_stats()['arrays'][array]['config']

    def load(self):
        '''Return a dict of stats'''
        ret = {}

        # Read the mdstat file
        with open(self.get_path(), 'r') as f:
            # lines is a list of line (with \n)
            lines = f.readlines()

        # First line: get the personalities
        # The "Personalities" line tells you what RAID level the kernel currently supports.
        # This can be changed by either changing the raid modules or recompiling the kernel.
        # Possible personalities include: [raid0] [raid1] [raid4] [raid5] [raid6] [linear] [multipath] [faulty]
        ret['personalities'] = self.get_personalities(lines[0])

        # Second to last before line: Array definition
        ret['arrays'] = self.get_arrays(lines[1:-1], ret['personalities'])

        # Save the file content as it for the __str__ method
        self.content = reduce(lambda x, y: x+y, lines)

        return ret

    def get_personalities(self, line):
        '''Return a list of personalities readed from the input line'''
        return [split('\W+', i)[1] for i in line.split(':')[1].split(' ') if i.startswith('[')]

    def get_arrays(self, lines, personalities=[]):
        '''Return a dict of arrays'''
        ret = {}

        i = 0
        while i < len(lines):
            try:
                # First array line: get the md device
                md_device = self.get_md_device_name(lines[i])
            except IndexError:
                # No array detected
                pass
            else:
                # Array detected
                if md_device is not None:
                    # md device line
                    ret[md_device] = self.get_md_device(lines[i], personalities)
                    # md config/status line
                    i += 1
                    ret[md_device].update(self.get_md_status(lines[i]))
            i += 1

        return ret

    def get_md_device(self, line, personalities=[]):
        '''Return a dict of md device define in the line'''
        ret = {}

        splitted = split('\W+', line)
        # Raid status
        # Active or 'started'. An inactive array is usually faulty.
        # Stopped arrays aren't visible here.
        ret['status'] = splitted[1]
        if splitted[2] in personalities:
            # Raid type (ex: RAID5)
            ret['type'] = splitted[2]
            # Array's components
            ret['components'] = self.get_components(line, with_type=True)
        else:
            # Raid type (ex: RAID5)
            ret['type'] = None
            # Array's components
            ret['components'] = self.get_components(line, with_type=False)

        return ret

    def get_md_status(self, line):
        '''Return a dict of md status define in the line'''
        ret = {}

        splitted = split('\W+', line)
        if len(splitted) < 7:
            ret['available'] = None
            ret['used'] = None
            ret['config'] = None
        else:
            # The final 2 entries on this line: [n/m] [UUUU_]
            # [n/m] means that ideally the array would have n devices however, currently, m devices are in use.
            # Obviously when m >= n then things are good.
            ret['available'] = splitted[-4]
            ret['used'] = splitted[-3]
            # [UUUU_] represents the status of each device, either U for up or _ for down.
            ret['config'] = splitted[-2]

        return ret

    def get_components(self, line, with_type=True):
        '''Return a dict of componants in the line
        key: device name (ex: 'sdc1')
        value: device role number
        '''
        ret = {}

        # Ignore (F) (see test 08)
        line2 = reduce(lambda x, y: x+y, split('\(.+\)', line))
        if with_type:
            splitted = split('\W+', line2)[3:]
        else:
            splitted = split('\W+', line2)[2:]
        ret = dict(zip(splitted[0::2], splitted[1::2]))

        return ret

    def get_md_device_name(self, line):
        '''Return the md device name from the input line'''
        ret = split('\W+', line)[0]
        if ret.startswith('md'):
            return ret
        else:
            return None
