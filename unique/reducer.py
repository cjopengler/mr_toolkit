# coding:utf-8
'''
去重的reducer
'''


from base.reducer import Reducer
from abc import ABCMeta, abstractmethod
import json
from collections import OrderedDict


class UniqueReducer(Reducer):

    _key_index = 0
    _value_index = 1

    def __init__(self):
        """
        初始化reducer
        :return:
        """
        self._join_key = None

        # value的list
        self._join_values = None

    def _create_kv(self, line):
        """
        产生key和value,子类可以重写这个函数生成key 和value
        :param line: 行数据
        :return: key, value元组
        """
        kv = json.loads(line.rstrip().decode('utf-8'),
                        object_pairs_hook=OrderedDict)
        return kv[self._key_index], kv[self._value_index]

    @abstractmethod
    def _output_result(self, key, values):
        """
        子类中自己定义处理交集的函数
        :param key: key
        :param id_codes: id_code
        :param values:
        :return:
        """
        pass

    def __output_merge_values(self):
        """
        将同一个key的value合并在一起并输出字符串
        默认返回key
        :return: merge的字符串
        """
        if self._join_key is not None:
            self._output_result(self._join_key, self._join_values)

    def __execute_by_line(self, line):
        key, value = self._create_kv(line)

        if self._join_key is None:
            self._join_key = key
            self._join_values = [value]

        elif key == self._join_key:
            self._join_values.append(value)

        else:
            self.__output_merge_values()
            self._join_key = key
            self._join_values = [value]

    def execute(self, input_file):
        for line in input_file:
            self.__execute_by_line(line)

        self.__output_merge_values()


