"""
单继承:
需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
class DerivedClassName(modname.BaseClassName):
"""


# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))


# 单继承实例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构造函数
        People.__init__(self, n, a, w)
        self.grade = g

    # 重写父类的方法
    def speak(self):
        print("%s说:我今年%d岁了,我在读%d年级"%(self.name, self.age, self.grade))


s = Student('ken', 10, 60, 3)
s.speak()
