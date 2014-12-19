#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PyMDstat
# Unitary test
#
# Copyright (C) 2013 Nicolargo <nicolas@nicolargo.com>

import unittest

from pymdstat import mdstat


class TestPyMDstat(unittest.TestCase):
    '''Test PyMDstat module'''

    def test_000_init(self):
        for i in range(1, 8):
            mdstat_test = mdstat('./tests/mdstat.0%s' % i)
            print('%s' % mdstat_test.get_stats())
            self.assertNotEqual(mdstat_test.get_stats(), {})

if __name__ == '__main__':
    unittest.main()
