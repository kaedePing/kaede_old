# -*- coding: utf-8 -*-
# @Time : 2023/1/5 16:43
# @Author : kaede
# @File : json_use.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
#
#
# -*- Description -*-
# -*-编码：utf-8-*-
import json

a = {
    'sing': 'letting go',
    'songer': '才押金'
}
b = []
for i in range(2):
    b.append(a)
print(a)
print(b)
c = json.dumps(a, ensure_ascii=False)
d = json.dumps(b, ensure_ascii=False)
print(c)
print(d)

with open('1.json', 'w') as f:
    json.dump(b, f, ensure_ascii=False, indent=2)
