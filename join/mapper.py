# coding:utf-8
'''
交集的mapper
'''

from base.mapper import Mapper
from base.key_factory import KeyFactory
from base.default_key_factory import DefaultKeyFactory

class JoinMapper(Mapper):
    def __init__(self, id_code, kf=DefaultKeyFactory()):
        '''
        初始化mapper
        :param id_code: 用来区分是哪个数据集的标识,例如计算数据集1和数据集2的交集,需要用id_code来标识和区分
        以便在reduce的时候,能够知道交集的数据是来自哪个数据集.这个标志位用来处理不同格式的数据集.如果数据集的格式
        相同,则可以不用设置成同一个字符串即可.
        :param kf: key factory
        '''
        self._key_factory = kf
        self._id_code = id_code

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
        print '%s\t%s\t%s' % (key, str(self._id_code), value)

    def execute(self, line):
        key = self._key_factory.create(line)
        value = self._create_value(line)
        self._output(key, value)


