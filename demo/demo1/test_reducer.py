# coding:utf-8

import sys
sys.path.append('../../')

from join.reducer import JoinReducer

test_reducer = JoinReducer()

for line in sys.stdin:
    test_reducer.execute(line.decode('utf-8').rstrip())


test_reducer.complete()
