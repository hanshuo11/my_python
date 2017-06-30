#!/user/bin/env python
# -*- coding: utf-8 -*-
# Author:HanShuo
class people(object):
    def eat(self):
        print( "i like eat food!")

class Student(people):
    pass
s=Student()
s.eat()