# coding:utf-8
'''
实现数据集制定key的去重
'''

from base.mapper import Mapper
from abc import ABCMeta, abstractmethod
import json


class UniqueMapper(Mapper):
    def __init__(self):
        '''
        初始化mapper
        '''
        pass

    @abstractmethod
    def _create_kv(self, line):
        '''
        产生key,value结构
        :param line: 行数据
        :return: key, value元组; 失败情况下,key返回None; 成功情况下,key不能为None, value任意.
        '''
        pass

    def _output(self, key, value):
        """
        输出key和value,可以自定义该函数, 建议一般要重新定义, 这个格式的约定在reduce中使用
        所以如果重新实现这个函数,需要在reduce的_create_kv要注意重写.
        :param key:
        :param value:
        :return:
        """
        output_tuple = (key, value)

        print (json.dumps(output_tuple, ensure_ascii=False).encode('utf-8'))

    def __execute_by_line(self, line):
        key, value = self._create_kv(line)

        if key is not None:
            self._output(key, value)

    def execute(self, input_file):
        for line in input_file:
            self.__execute_by_line(line)

