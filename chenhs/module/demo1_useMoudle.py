"""
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
模块可以被别的程序引入，以使用该模块中的函数等功能
"""

import sys

print('命令参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython路径为: ', sys.path, '\n')        # sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。


"""
import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]
"""