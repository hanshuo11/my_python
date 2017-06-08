#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}
L=[std1,std2]
def print_peoples(std):
    return ('%s: %s' % (std['name'], std['score']))

# print(L)

# print(print_peoples(std1))
print(list(i for i in L)[0])
