========
PyMDstat
========

.. image:: https://scrutinizer-ci.com/g/nicolargo/pymdstat/badges/build.png?b=master
        :target: https://scrutinizer-ci.com/g/nicolargo/pymdstat/?branch=master
.. image:: https://scrutinizer-ci.com/g/nicolargo/pymdstat/badges/quality-score.png?b=master
        :target: https://scrutinizer-ci.com/g/nicolargo/pymdstat/?branch=master
.. image:: https://img.shields.io/pypi/v/pymdstat.svg
    :target: https://pypi.python.org/pypi/pymdstat/
    :alt: Latest Version


A pythonic library to parse Linux /proc/mdstat file.

.. code-block:: python

    >>> from pymdstat import MdStat

    >>> mds = MdStat() # Read the /proc/mdstat file

    >>> mds
    Personalities : [raid1] [raid6] [raid5] [raid4]
    md1 : active raid1 sdb2[1] sda2[0]
          136448 blocks [2/2] [UU]

    md2 : active raid1 sdb3[1] sda3[0]
          129596288 blocks [2/2] [UU]

    md3 : active raid5 sdl1[9] sdk1[8] sdj1[7] sdi1[6] sdh1[5] sdg1[4] sdf1[3] sde1[2] sdd1[1] sdc1[0]
          1318680576 blocks level 5, 1024k chunk, algorithm 2 [10/10] [UUUUUUUUUU]

    md0 : active raid1 sdb1[1] sda1[0]
          16787776 blocks [2/2] [UU]

    unused devices: <none>

    >>> mds.get_stats()
    {'arrays': {'md0': {'available': '2',
       'components': {'sda1': '0', 'sdb1': '1'},
       'config': 'UU',
       'status': 'active',
       'type': 'raid1',
       'used': '2'},
      'md1': {'available': '2',
       'components': {'sda2': '0', 'sdb2': '1'},
       'config': 'UU',
       'status': 'active',
       'type': 'raid1',
       'used': '2'},
      'md2': {'available': '2',
       'components': {'sda3': '0', 'sdb3': '1'},
       'config': 'UU',
       'status': 'active',
       'type': 'raid1',
       'used': '2'},
      'md3': {'available': '10',
       'components': {'sdc1': '0',
        'sdd1': '1',
        'sde1': '2',
        'sdf1': '3',
        'sdg1': '4',
        'sdh1': '5',
        'sdi1': '6',
        'sdj1': '7',
        'sdk1': '8',
        'sdl1': '9'},
       'config': 'UUUUUUUUUU',
       'status': 'active',
       'type': 'raid5',
       'used': '10'}},
     'personalities': ['raid1', 'raid6', 'raid5', 'raid4']}

    >>> mds.personalities()
    ['raid1', 'raid6', 'raid5', 'raid4']

    >>> mds.arrays()
    ['md2', 'md3', 'md0', 'md1']

    >>> mds.type('md3')
    'raid6'

    >>> mds.status('md3')
    'active'

    >>> mds.components('md3')
    ['sdk1', 'sdj1', 'sde1', 'sdl1', 'sdg1', 'sdf1', 'sdh1', 'sdc1', 'sdd1', 'sdi1']

    >>> mds.available('md3')
    10

    >>> mds.used('md3')
    10

    >>> mds.config('md3')
    'UUUUUUUUUU'
