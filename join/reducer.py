# coding:utf-8
'''
交集的reducer
'''

from base.key_factory import KeyFactory
from base.reducer import Reducer
from base.default_key_factory import DefaultKeyFactory

class JoinReducer(Reducer):
    def __init__(self, kf=DefaultKeyFactory()):
        '''
        初始化reducer
        :param kf: key产生的工厂
        :return:
        '''
        self._key_factory = kf

        self._join_key = None
        # value的list
        self._join_values = None

    def set_key_factory(self, kf):
        '''
        设置产生key的工厂
        :param kf:
        :return:
        '''
        self._key_factory = kf

    def get_key_factory(self):
        '''
        返回key的工厂
        :return: key的工厂
        '''
        return self._key_factory

    def _create_value(self, line):
        '''
        产生key后面的value, 子类可以实现这个函数产生value
        :param line: 行数据
        :return: key产生的value, 返回的类型必须是字符串
        '''
        return line.rstrip()


    def _output_merge_values(self):
        '''
        将同一个key的value合并在一起并输出字符串
        默认返回key
        :return: merge的字符串
        '''
        print self._join_key

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
