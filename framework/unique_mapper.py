# coding:utf-8

from base.mapper import Mapper
from unique.line_mapper import LineUniqueMapper


class UniqueMapper(Mapper):
    def __init__(self, line_unique_mapper):
        self._line_unique_mapper = line_unique_mapper

    def execute(self, input_file):
        for line in input_file:
            self._line_unique_mapper.execute(line)
