#choice函数
#可随机从列表中选出元素
from random import choice
x=choice(['hello world',[1,2,'e','e',4]])
print(x.count('e'))

#创建一个类
class Person:

    def setName(self,name):
        self.name=name

    def getNmae(self):
        return self.name

    def greet(self):
        print("hello,world! I'm %s."%self.name)

foo=Person()
bar=Person()
foo.setName("challenger")
bar.setName("CY")
foo.greet()
bar.greet()
print(foo.name)
bar.name='cc'
bar.greet()
#类的作用就是执行代码块，并不局限于def
class demo:
    print("challenger")