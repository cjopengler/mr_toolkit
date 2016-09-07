# coding:utf-8

import sys
sys.path.append('../../')

from unique.reducer import UniqueReducer

class DemoReducer(UniqueReducer):
    def _output_result(self, key, values):
        if None not in values:
            print key, values
        else:
            print key

if __name__ == '__main__':

    reducer = DemoReducer()
    reducer.execute(sys.stdin)