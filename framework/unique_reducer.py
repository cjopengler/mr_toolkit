# coding:utf-8

from unique.line_reducer import LineUniqueReducer
from base.reducer import Reducer


class UniqueReducer(Reducer):

    def __init__(self, line_unique_reducer):
        self._line_unique_reducer = line_unique_reducer

    def execute(self, input_file):
        for line in input_file:
            self._line_unique_reducer.execute(line)

        self._line_unique_reducer.output_merge_values()