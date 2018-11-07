#!/usr/bin/env python3

class UserData:


    def __init__(self, id_, name):
        self.id_ = id_
        self._name = name

    def __repr__(self):
        return "UserData: {} - {}".format(self.id_, self._name)


class NewUser(UserData):

    
    group = 'shiyanlou-louplus'
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 3:
            print('Error')
            return 
        self._name = value


    def __repr__(self):
        return "{}'s id is {}".format(self.get_name(), self.id_)

    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id_, name):
        return "{}'s id is {}".format(id_, name)

if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    #user1.set_name('Jackie')
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
    
    user1.group = 'China plus'   # 此处实际是给实例user1绑定一个新的实例变量
    user2.group = 'Word plus'
    print(user1.get_group())    # 通过调用实例的类方法，能访问类属性
    print(user2.get_group())
    print(NewUser.get_group())  # 通过调用类的类方法, 也能访问类属性
    print(user1.group, user2.group)  # 打印的是实例变量
    print(NewUser.format_userdata(100, 'Lucy'))  # 调用类的静态方法

