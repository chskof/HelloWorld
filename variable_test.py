"""
变量就像一个小容器,变量保存的数据可以发生多次改变,只要程序对变量重新赋值即可
    Python是弱类型语言,弱类型语言有两个典型特征:
    1、变量无须声明即可直接赋值:对一个不存在的变量赋值就相当于定义了一个新变量
    2、变量的数据可以动态改变:同一个变量可以一会儿被赋值为整数值,一会儿可以赋值为字符串
"""

a = 5
b = "hello"

a = "mike"
c = 100

# 数字的类型是int 字符串的类型是str
# 如果想查看变量的类型,可以使用python内置函数type()

type(c)
type(b)

print("c的类型:", type(c))
print("b的类型:", type(b))


"""
变量(标识符)的命名规则:
    Python语言的变量必须以字母、下划线_开头,不能以数字开头,后面可以跟任意数目的字母、数字和下划线
    变量不可以是Python关键字
    变量不能包含空格
    变量可以用驼峰命名法或者下划线区分每个单词首字母
    变量区分大小写
"""
abc_xyz = 1
abc2 = "hello"
userName = "Jack"
_teachName = "chen"
userFirstName = "chen"  # 驼峰命名法 第一个单词首字母小写 后面单词首字母大写
user_first_name = "chen"

# abc#xyz 不合法 变量名不能出现井号
# 1abc 不合法 变量名不能以数字开头

"""
Python还包含一系列关键字和内置函数,避免使用他们作为变量名
    如果开发者尝试使用关键字作为变量名,python解释器会报错
    如果开发者使用内置函数名字作为变量名,Python解释器不会报错,但是会把该内置函数覆盖导致该内置函数无法使用

Python关键字:
    'False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 
    'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
     'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
     
保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：
>>> import keyword
>>> keyword.kwlist   


python内置函数:
    abs()	 str()   print()    type()    input()  open()     divmod()	    	    
    all()	     enumerate() 	int()	        ord()	    	staticmethod()
    any()   	    eval()	        isinstance()	pow()	    sum()
    basestring()	execfile()	    issubclass()		    super()
    bin()	    file()  	iter()	    property()	    tuple()
    bool()  	filter()	len()	    range()	        
    bytearray()	    float() 	list()	    raw_input() 	unichr()
    callable()	format()	    locals()	reduce()	unicode()
    chr()	    frozenset()	    long()	    reload()	vars()
    classmethod()	    getattr()	map()	repr()	xrange()
    cmp()	    globals()	max()	reverse()	zip()
    compile()	hasattr()	memoryview()	round()	    __import__()
    complex()	hash()	min()	set()	
    delattr()	help()	next()	setattr()	
    dict()	hex()	object()	slice()	
    dir()	id()	oct()	sorted()  
    ...
"""
