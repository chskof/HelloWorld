"""
命名空间和作用域:
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

Python的查找变量顺序为：局部的命名空间去 -> 全局命名空间 -> 内置命名空间
"""

# var1 是全局名称
var1 = 5


def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7


g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


"""
Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
也就是说这些语句内定义的变量，外部也可以访问\

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域
"""

total = 0  # 这是一个全局变量


# 可写函数说明
def sum2(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum2(10, 20)
print("函数外是全局变量 : ", total)



"""
global 和 nonlocal关键字:
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了
"""

num = 1
def fun1():
    global num          # 需要使用global关键字声明
    print(num)
    num = 123
    print(num)

fun1()
print(num)


"""
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
"""

def outer():
    num = 10

    def inner():
        nonlocal num        # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)

outer()



a = 10
def test():
    #a = a + 1       # 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改
    print(a)
test()