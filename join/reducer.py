# coding:utf-8
'''
交集的reducer
'''

from base.key_factory import KeyFactory
from base.reducer import Reducer
from base.default_key_factory import DefaultKeyFactory
from abc import ABCMeta, abstractmethod

class JoinReducer(Reducer):
    _KEY_INDEX = 0
    _ID_CODE_INDEX = 1
    _VALUE_INDEX = 2

    def __init__(self):
        '''
        初始化reducer
        :return:
        '''
        self._join_key = None

        # value的list
        self._join_values = None
        self._join_id_codes = None


    def _create_key(self, line):
        '''
        从line中产生key
        :param line:
        :return:
        '''
        return line.rstrip().split('\t')[JoinReducer._KEY_INDEX]

    def _create_id_code(self, line):
        '''
        从line中产生id_code
        :param line:
        :return:
        '''
        return line.rstrip().split('\t')[JoinReducer._ID_CODE_INDEX]

    def _create_value(self, line):
        '''
        产生key后面的value, 子类可以实现这个函数产生value
        :param line: 行数据
        :return: key产生的value, 返回的类型必须是字符串
        '''
        key_len = len(self._create_key(line))
        id_code_len = len(self._create_id_code(line))
        return line.rstrip()[key_len+1+id_code_len+1:]


    @abstractmethod
    def _output_result(self, key, id_codes, values):
        '''
        子类中自己定义处理交集的函数
        :param key: key
        :param id_codes: id_code
        :param values:
        :return:
        '''
        pass

    def __output_merge_values(self):
        '''
        将同一个key的value合并在一起并输出字符串
        默认返回key
        :return: merge的字符串
        '''
        if (len(self._join_values) > 1):
            self._output_result(self._join_key, self._join_id_codes, self._join_values)



    def execute(self,line):

        key = self._create_key(line)
        id_code = self._create_id_code(line)
        value = self._create_value(line)

        if self._join_key is None:
            self._join_key = key
            self._join_values = [value]
            self._join_id_codes = [id_code]

        elif key == self._join_key:
            self._join_values.append(value)
            self._join_id_codes.append(id_code)

        else:
            self.__output_merge_values()
            self._join_key = key
            self._join_values = [value]
            self._join_id_codes = [id_code]


    def output_merge_values(self):
        self.__output_merge_values()
