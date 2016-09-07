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
        :return: key, value元组
        '''
        pass

    def _output(self, key, value):
        """
        输出key和value,可以自定义该函数
        :param key:
        :param value:
        :return:
        """
        output_tuple = (key, value)

        print (json.dumps(output_tuple, ensure_ascii=False).encode('utf-8'))

    def execute(self, line):
        key, value = self._create_kv(line)
        self._output(key, value)


