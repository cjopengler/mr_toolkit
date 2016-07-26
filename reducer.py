# coding:utf-8
'''
reducer接口
'''

class Reducer(object):
    def execute(self,line):
        '''
        逐行执行
        :param line: 行信息
        :return:
        '''
        pass

    def complete(self):
        '''
        按行执行完 执行完成
        :return:
        '''
        pass