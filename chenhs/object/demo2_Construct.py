"""
类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
 __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上
 类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法
"""


class Complex:
	def __init__(self,realpart,imagpart):
		self.r = realpart
		self.i = imagpart


c = Complex(3.0, -4.5)
print(c.r, c.i)
