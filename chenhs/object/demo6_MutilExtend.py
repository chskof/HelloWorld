"""
多继承:

"""


class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我%d岁"%(self.name,self.age))


# 单继承示例
class Student(People):
    grade  = ''

    def __init__(self,n, a, w, g):
        # 调用父类的构造函数
        People.__init__(self,n, a ,w)
        self.grade = g

    # 重写父类的方法
    def speak(self):
        print("%s说: 我%d岁了,在读%d年级"%(self.name, self.age,self.grade))


# 另一个类,多重继承之前的准备
class Teacher:
    subject = ''
    name = ''

    def __init__(self, n, s):
        self.name = n
        self.subject = s

    def speak(self):
        print("我叫%s,我是一位老师,我教的科目是%s"%(self.name,self.subject))


# 多重继承
class Sample(Student, Teacher):
    a = ''

    def __init__(self, n, a, w, g, s):
        # 调用父类构造方法
        Student.__init__(self, n, a, w, g)
        Teacher.__init__(self, n, s)


test = Sample("Tim", 25, 80, 4, "python")
test.speak()  # 方法名相同，默认调用的是在括号中排前地父类的方法
