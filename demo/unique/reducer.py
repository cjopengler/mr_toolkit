# coding:utf-8

import sys
sys.path.append('../../')

from unique.line_reducer import LineUniqueReducer
from framework.unique_reducer import UniqueReducer


class DemoReducer(LineUniqueReducer):
    def _output_result(self, key, values):
        if None not in values:
            print key, values
        else:
            print key

if __name__ == '__main__':

    reducer = UniqueReducer(DemoReducer())
    reducer.execute(sys.stdin)