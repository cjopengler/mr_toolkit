# coding:utf-8
import sys
sys.path.append('../../')

from unique.mapper import UniqueMapper


class DemoMapper(UniqueMapper):
    def _create_kv(self, line):
        infos = line.rstrip().decode('utf-8').split('\t')
        key = infos[0]

        value = None
        if len(infos) == 2:
            value = int(infos[1])

        return key, value

if __name__ == '__main__':
    mapper = DemoMapper()
    mapper.execute(sys.stdin)

