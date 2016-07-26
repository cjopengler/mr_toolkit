# coding:utf-8
'''
交集的reducer
'''

from key_factory import KeyFactory
from reducer import Reducer

class JoinReducer(Reducer):
    def __init__(self, kf):
        '''
        初始化reducer
        :param kf: key产生的工厂
        :return:
        '''
        self._key_factory = kf

        self._join_key = None
        # value的list
        self._join_values = None

    def _create_value(self, line):
        return line.rstrip()

    def _output_merge_values(self):
        '''
        将同一个key的value合并在一起并输出字符串
        默认返回key
        :return: merge的字符串
        '''
        return self._join_key

    def execute(self,line):
        key = self._key_factory.create(line)
        value = self._create_value(line)

        if self._join_key is None:
            self._join_key = key
            self._join_values = [value]

        elif key == self._join_key:
            self._join_values.append(value)

        else:
            self._output_merge_values()
            self._join_key = key
            self._join_values = [value]


    def complete(self):
        self._output_merge_values()
