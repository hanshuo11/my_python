#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo

# 返回函数
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
#
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f())

# 闭包问题
def count():
    def fn(j):
        def g():
            return j * j
        return g
    s = []
    for i in range(4):
        #循环后立即调运
        s.append(fn(i))
    return s
f1, f2, f3,f4 = count()
print(f2())