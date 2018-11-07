#!/usr/bin/env python3

class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def sound(self):
        return 
    
    def makesound(self):
        print('{} is makesound {}'.format(self.name, self.sound()))
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError

        
    @classmethod
    def get_owner(cls):
        return cls.owner


    @staticmethod
    def buy_food():
        print('ording...')
        print('ok')
