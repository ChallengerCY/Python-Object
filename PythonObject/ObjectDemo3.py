#多继承
class Calculator:
    def calculate(self,experession):
        self.value=eval(experession)

class Talker:
    def talk(self):
        print("values=",self.value)

class TalkingCalculator(Calculator,Talker):
    pass

tc=TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

#如果多继承过程中有重名的方法，先继承的类中的方法会重写后继承的类的方法


#检查当前对象是否有指定特性
print(hasattr(tc,'talk'))