"""
Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中:
from modname import name1[, name2[, ... nameN]]
"""

from myModule import myPrint, myPrint2

myPrint("abc")
myPrint2("def")


"""
把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from modname import *

一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
"""


"""
__name__属性:
一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。

每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
   
dir() 函数
内置的函数 dir() 可以找到模块内定义的所有名称:
dir(myModule)
dir() #得到当前模块中定义的属性列表
"""

print(dir())