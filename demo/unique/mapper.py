# coding:utf-8
import sys
sys.path.append('../../')

from unique.line_mapper import LineUniqueMapper
from framework.unique_mapper import UniqueMapper

class DemoMapper(LineUniqueMapper):
    def _create_kv(self, line):
        infos = line.rstrip().decode('utf-8').split('\t')
        key = infos[0]

        value = None
        if len(infos) == 2:
            value = int(infos[1])

        return key, value

if __name__ == '__main__':
    mapper = UniqueMapper(DemoMapper())
    mapper.execute(sys.stdin)

