#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo

# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# 过滤回数
# def is_palindrome(n):
#     if n>11:
#         return str(n)==str(n)[::-1]
#     else:
#         next
#
# outprint=filter(is_palindrome,range(1,1000))
# print(list(outprint))

#请用sorted()对上述列表分别按名字排序：
#itemgetter选择排序对象的维度
from operator import itemgetter
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


print(sorted(L,key=itemgetter(1,0)))


