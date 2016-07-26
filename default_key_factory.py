# coding:utf-8
'''
default key factory
'''
import re
from key_factory import KeyFactory

class DefaultKeyFactory(KeyFactory):
    _SPLIT_PATTERN = '\t'
    _KEY_INDEX = 0

    def create(self, line):
        key_infos = re.split(DefaultKeyFactory._SPLIT_PATTERN, line.rstrip())
        return key_infos[DefaultKeyFactory._KEY_INDEX]

