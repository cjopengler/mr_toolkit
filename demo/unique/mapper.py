# coding:utf-8
import sys
sys.path.append('../../')

from unique.mapper import UniqueMapper

class DemoMapper(UniqueMapper):
    def _create_kv(self, line):
        infos = line.rstrip().decode('utf-8').split('\t')
        key = infos[0]
        value = int(infos[1])
        return key, value

if __name__ == '__main__':
    demo_mapper = DemoMapper()

    for line in sys.stdin:
        demo_mapper.execute(line)

