# encoding:utf-8

import addressbook_pb2
import sys

# 获取类型
address_book = addressbook_pb2.AddressBook()
# 添加数据
person = address_book.people.add()

# 添加值
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
# enum的数据引用
phone.type = addressbook_pb2.Person.HOME

# 检查是否所有required的Filed都有赋值
print person.IsInitialized()

# 序列化
res = person.SerializeToString()
# 反序列化
a = addressbook_pb2.Person()
a.ParseFromString(res)

# 从其它message载入，会覆盖当前的值
b = addressbook_pb2.Person()
b.name = "Tom"
b.CopyFrom(a)

# 清除所有的Filed
a.Clear()
# 打印出来


