#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo

# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
# s=Student()
# s.score=110
# print(s.score)


# 读写属性的运用
class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def resolution(self):
        return self._width * self._height
    def resolution2(self):
        return self.width * self.height

s=Screen()
s.width=10
s.height=100
print(s.resolution)
print(s.resolution2())