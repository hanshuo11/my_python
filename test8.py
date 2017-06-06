#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo
#切片1
# r=[]
# l=[1,2,3,4,5,6,7,8,9]
# for i in range(3):
#     r.append(l[i])
# print(r)
# 切片二
# l=[1,2,3,4,5,6,7,8,9]
# print(l[:3])

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key,v in d.items():
    print(key,v)

# 列表生成式
# l=[x*x*x for x in range(1,11)]
# print(l)

# L = ['Hello',1, 'World', 'Apple']
# s=[s.lower() for s in L]
# print(s)
# print([x * x for x in range(1, 11) if x % 2 == 0])


# list中的大写变成小写
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

# import os # 导入os模块，模块的概念后面讲到
# l=[d for d in os.listdir('.')]
# print(l)


# 如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# g=(x*x for x in range(10))
#
# for n in g:
#     print(n)
#斐波那契数列
def fib(x):
    if x==1 or x==0:
        return 1
    else:
        return fib(x-2)+fib(x-1)
print(fib(3))