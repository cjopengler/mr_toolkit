# coding:utf-8

import json

a = u'你\t好'

print a

a_json = json.dumps(a, ensure_ascii=False).encode('utf-8')
print a_json

b = json.loads(a_json)
print b, type(b), b == u'你\t好'
