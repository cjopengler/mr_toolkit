# coding:utf-8

import sys
sys.path.append('../../')

from unique.reducer import UniqueReducer


class DemoReducer(UniqueReducer):
    def _output_result(self, key, values):
        print key, values

if __name__ == '__main__':
    demo_reducer = DemoReducer()

    for line in sys.stdin:
        demo_reducer.execute(line)

    demo_reducer.complete()