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
        key, value = line.rstrip().decode('utf-8').split('\t')

        key = json.loads(key)

        value = json.loads(value,
                        object_pairs_hook=OrderedDict)

        return key, value

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

    def _append_value(self, key, value_list, value):
        """
        对key产生的数组追加数据, 当数据规模太大时,子类可以通过重新实现该方法来限制数量
        :param key: 当前的key
        :param value_list: 存放所有value的list数组
        :return:
        """
        value_list.append(value)

    def __execute_by_line(self, line):
        key, value = self._create_kv(line)

        if self._join_key is None:
            self._join_key = key
            self._join_values = list()
            self._append_value(key, self._join_values, value)

        elif key == self._join_key:
            self._append_value(key, self._join_values, value)

        else:
            self.__output_merge_values()
            self._join_key = key
            self._join_values = list()
            self._append_value(key, self._join_values, value)

    def execute(self, input_file):
        for line in input_file:
            self.__execute_by_line(line)

        self.__output_merge_values()


