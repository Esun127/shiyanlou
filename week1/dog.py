#!/usr/bin/env python3

class Dog(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name.lower().capitalize()

    def set_name(self, value):
        self._name = value

    def sound(self):
        return 'wang wang wang ...'
        

    def bark(self):
        print(self.get_name() + ' is making sound ' + self.sound())

