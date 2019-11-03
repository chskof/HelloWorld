"""
方法重写(覆盖):
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
"""

# 定义父类
class Parent:
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):
    def myMethod(self):
        print('调用子类方法')


c = Child()     # 创建子类对象
c.myMethod()    # 调用子类重写的方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法
