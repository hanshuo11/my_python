#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo
# class Student(object):
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return self.name
#     __repr__=__str__
#
# s=Student("hanhsuo")
# print(s)

# __iter__的使用
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 1000:  # 退出循环的条件
#             raise StopIteration()
#         return self.a  # 返回下一个值
#
#
# for n in Fib():
#     print(n)


# __getitem__第二种写法
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:

                    L.append(a)
                    a,b=b,a+b



f = Fib()
print(f[2])
