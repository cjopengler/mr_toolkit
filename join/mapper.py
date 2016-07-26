# coding:utf-8
'''
交集的mapper
'''

from mapper import Mapper
from key_factory import KeyFactory

class JoinMapper(Mapper):
    def __init__(self, kf):
        '''
        初始化mapper
        :param kf: key factory
        '''
        self._key_factory = kf

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

    def _output(self, key, value):
        '''
        输出key和value,可以自定义该函数
        :param key:
        :param value:
        :return:
        '''
        print '%s\t%s' % (key, value)

    def execute(self, line):
        key = self._key_factory.create(line)
        value = self._create_value(line)
        self._output(key, value)


