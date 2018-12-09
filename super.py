# coding: utf-8
# Your code here!
class MyClass:
    def __init__(self, name):
        self.name=name
    def say(self):
        print(self.name)
class UltraClass(MyClass):
    def __init__(self, name, year):
        super(UltraClass, self).__init__(name)
        self.year=year
    def say(self):
        print(self.name, "was born in", self.year)

uc=UltraClass("John", 1990)
uc.say()