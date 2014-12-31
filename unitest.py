#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyMDstat
# Unitary test
#
# Copyright (C) 2014 Nicolargo <nicolas@nicolargo.com>

import unittest

from pymdstat import MdStat

# In Python 3, assertItemsEqual method is named assertCountEqual
try:
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
except AttributeError:
    pass


class TestPyMdStat(unittest.TestCase):

    """Test PyMDstat module."""

    def test_000_loadall(self):
        for i in range(1, 10):
            mdstat_test = MdStat('./tests/mdstat.0%s' % i)
            # print('%s' % mdstat_test.get_stats())
            self.assertNotEqual(mdstat_test.get_stats(), {})

    def test_099_didnotexist(self):
        try:
            mdstat_test = MdStat('/proc/NOmdstat')
        except IOError:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_099_model(self):
        i = 4
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.personalities(), ['raid1', 'raid6', 'raid5', 'raid4'])
        self.assertCountEqual(mdstat_test.arrays(), ['md2', 'md3', 'md0', 'md1'])
        self.assertEqual(mdstat_test.type('md3'), 'raid5')
        self.assertEqual(mdstat_test.status('md3'), 'active')
        self.assertEqual(mdstat_test.available('md3'), 10)
        self.assertEqual(mdstat_test.used('md3'), 10)
        self.assertCountEqual(mdstat_test.components('md3'), ['sdk1', 'sdj1', 'sde1', 'sdl1', 'sdg1', 'sdf1', 'sdh1', 'sdc1', 'sdd1', 'sdi1'])
        self.assertEqual(mdstat_test.config('md3'), 'UUUUUUUUUU')

    def test_001(self):
        i = 1
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertEqual(mdstat_test.get_stats()['personalities'], [])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {})

    def test_002(self):
        i = 2
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid1', 'raid6', 'raid5', 'raid4'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md_d0': {'status': 'active', 'available': '5', 'used': '5', 'components': {'sdc1': '1', 'sdb1': '5', 'sde1': '0', 'sdd1': '2', 'sdf1': '4'}, 'config': 'UUUUU', 'type': 'raid5'}})

    def test_003(self):
        i = 3
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid6', 'raid5', 'raid4'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md0': {'status': 'active', 'available': '4', 'used': '3', 'components': {'sdb1': '1', 'sdd1': '2', 'sda1': '0'}, 'config': 'UUU_', 'type': 'raid5'}})

    def test_004(self):
        i = 4
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid1', 'raid6', 'raid5', 'raid4'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md2': {'status': 'active', 'available': '2', 'used': '2', 'components': {'sdb3': '1', 'sda3': '0'}, 'config': 'UU', 'type': 'raid1'}, 'md3': {'status': 'active', 'available': '10', 'used': '10', 'components': {'sdk1': '8', 'sdj1': '7', 'sde1': '2', 'sdl1': '9', 'sdg1': '4', 'sdf1': '3', 'sdh1': '5', 'sdc1': '0', 'sdd1': '1', 'sdi1': '6'}, 'config': 'UUUUUUUUUU', 'type': 'raid5'}, 'md0': {'status': 'active', 'available': '2', 'used': '2', 'components': {'sdb1': '1', 'sda1': '0'}, 'config': 'UU', 'type': 'raid1'}, 'md1': {'status': 'active', 'available': '2', 'used': '2', 'components': {'sdb2': '1', 'sda2': '0'}, 'config': 'UU', 'type': 'raid1'}})

    def test_005(self):
        i = 5
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid1', 'raid6', 'raid5', 'raid4'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md127': {'status': 'active', 'available': '6', 'used': '5', 'components': {'sde1': '2', 'sdg1': '4', 'sdf1': '3', 'sdh1': '6', 'sdc1': '0', 'sdd1': '1'}, 'config': 'UUUUU_', 'type': 'raid5'}})

    def test_006(self):
        i = 6
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['linear', 'raid0', 'raid1', 'raid5', 'raid4', 'raid6'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md0': {'status': 'active', 'available': '7', 'used': '7', 'components': {'sde1': '1', 'sdf1': '0', 'sdc1': '3', 'sdb1': '4', 'hdb1': '6', 'sdd1': '2', 'sda1': '5'}, 'config': 'UUUUUUU', 'type': 'raid6'}})

    def test_007(self):
        i = 7
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid1'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md1': {'status': 'active', 'available': '6', 'used': '4', 'components': {'sdc1': '2', 'sdb1': '4', 'sde1': '6', 'sdd1': '3', 'sdg1': '1'}, 'config': '_UUUU_', 'type': 'raid1'}})

    def test_008(self):
        i = 8
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['raid5'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md0': {'status': 'inactive', 'available': '4', 'used': '4', 'components': {'sdd1': '3', 'sdc1': '2', 'sda1': '0'}, 'config': 'UUUU', 'type': 'raid5'}})

    def test_009(self):
        i = 9
        mdstat_test = MdStat('./tests/mdstat.0%s' % i)
        self.assertCountEqual(mdstat_test.get_stats()['personalities'], ['linear', 'multipath', 'raid0', 'raid1', 'raid6', 'raid5', 'raid4', 'raid10'])
        self.assertEqual(mdstat_test.get_stats()['arrays'], {'md2': {'status': 'inactive', 'available': None, 'used': None, 'components': {'sdb': '0'}, 'config': None, 'type': None}, 'md0': {'status': 'active', 'available': '2', 'used': '2', 'components': {'sde1': '0', 'sdf1': '1'}, 'config': 'UU', 'type': 'raid1'}, 'md1': {'status': 'active', 'available': '2', 'used': '2', 'components': {'sde2': '0', 'sdf2': '1'}, 'config': 'UU', 'type': 'raid1'}})

if __name__ == '__main__':
    unittest.main()
