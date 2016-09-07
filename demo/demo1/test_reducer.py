# coding:utf-8

import sys
sys.path.append('../../')

from join.reducer import JoinReducer

class TestReducer(JoinReducer):
    def _output_result(self, key, id_codes, values):
        print key, id_codes, values

test_reducer = TestReducer()

for line in sys.stdin:
    test_reducer.execute(line.decode('utf-8').rstrip())


test_reducer.output_merge_values()
