#!/user/bin/env python
# Author:HanShuo
# name='函数'
# print('hello 韩硕',name)
name = input("name:")
age = int(input("age:"))
print(type(age))
job = input("job:")
info = '''
----------info of {_name}------------
name:{_name}
age:{_age}
job:{_job}
'''.format(_name=name, _age=age, _job=job)
print(info)
