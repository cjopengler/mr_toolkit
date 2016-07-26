# coding:utf-8

import sys
sys.path.append('../../')

from join.mapper import JoinMapper


for line in sys.stdin:
    test_mapper = JoinMapper()
    test_mapper.execute(line.decode('utf-8').rstrip())


