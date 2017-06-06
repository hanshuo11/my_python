#!/user/bin/env python
# Author:HanShuo
# name='函数'
# print('hello 韩硕',name)
name = input("name:")
age = int(input("age:"))
print(type(age))
job = input("job:")
info = '''
----------info of %s------------
name:%s
age:%d
job:%s
'''%(name,name,age,job)
print(info)
