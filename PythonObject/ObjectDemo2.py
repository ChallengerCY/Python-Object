#继承
class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked=['A']

f=Filter()
f.init()
print(f.filter([1,2,3]))

s=SPAMFilter()
s.init()
print(s.filter(['A','B']))

#issubclass
# 检查一个类是否是另一个类的子类
print(issubclass(SPAMFilter,Filter))
print(issubclass(Filter,SPAMFilter))

#如果已知类的基类，可以直接使用他的特殊特性__bases__:
print(SPAMFilter.__bases__)
print(Filter.__bases__)

#确定对象是否是类的实例
s=SPAMFilter()
print(isinstance(s,SPAMFilter))
print(isinstance(s,Filter))
print(isinstance(s,str))

#如果想知道对象属于哪个类，可以使用__class__
print(s.__class__)
