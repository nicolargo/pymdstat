#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyMDstat
# ...
#
# Copyright (C) 2013 Nicolargo <nicolas@nicolargo.com>

from re import split

# Limit import to class...
__all__ = ['mdstat']


# Classes
class mdstat(object):
    """
    Main mdstat class
    """

    def __init__(self, path='/proc/mdstat'):
        self.path = path

        # Stats will be stored in a dict
        self.stats = self.load()

    def get_path(self):
        '''Return the mdstat file path'''
        return self.path

    def get_stats(self):
        '''Return the stats'''
        return self.stats

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
        ret['arrays'] = self.get_arrays(lines[1:-1])

        return ret

    def get_personalities(self, line):
        '''Return a list of personalities readed from the input line'''
        return [split('\W+', i)[1] for i in line.split(':')[1].split(' ') if i.startswith('[')]

    def get_arrays(self, lines):
        '''Return a dict of arrays'''
        ret = {}

        for line in lines:
            try:
                # First array line: get the md device
                md_device = self.get_md_device(line)
            except IndexError:
                # No array detected
                pass
            else:
                # Array detected
                if md_device is not None:
                    ret[md_device] = self.get_array(line)

        return ret

    def get_array(self, line):
        '''Return a dict of array stats define in the line'''
        ret = {}

        splitted = split('\W+', line)
        # Raid status
        # Active or 'started'. An inactive array is usually faulty.
        # Stopped arrays aren't visible here.
        ret['status'] = splitted[1]
        # Raid type (ex: RAID5)
        ret['type'] = splitted[2]
        # Array's components
        ret['components'] = self.get_components(line)

        return ret

    def get_components(self, line):
        '''Return a dict of componants in the line
        key: device name (ex: 'sdc1')
        value: device role number
        '''
        ret = {}

        splitted = split('\W+', line)[3:]
        ret = dict(zip(splitted[0::2], splitted[1::2]))

        return ret

    def get_md_device(self, line):
        '''Return a list of personalities readed from the input line'''
        ret = split('\W+', line)[0]
        if ret.startswith('md'):
            return ret
        else:
            return None
