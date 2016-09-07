# coding:utf-8
'''
reducer接口
'''

class Reducer(object):
    def execute(self, input_content):
        '''
        逐行执行
        :param input_content: 行信息
        :return:
        '''
        pass

    def output_merge_values(self):
        '''
        按行执行完 执行完成
        :return:
        '''
        pass