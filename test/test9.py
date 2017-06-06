#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo
# 高阶函数
# f=abs
# print(f(-100))


# def add(x,y,f):
#     f=abs
#     return f(x)+f(y)
#
# print(add(-5,-6,abs))


# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))

# str=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(str)

# from functools import reduce
#
#
# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 2, 3, 5, 9, 5, 6, 7]))


# from functools import reduce
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# print(reduce(fn, [1, 2, 4, 5, 6]))

# str={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# print(str['0'])

# 把用户输入的不规范的英文名字，变为首字母大写
# def normalize(name):
#     def fn(x):
#         return x.capitalize()
#     return list(map(fn,name))
#
#
# L1 = ['Adam', 'Lisa', 'Bart']
# print(normalize(L1 ))


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
sdsd


