"""
基本变量类型
"""

"""
整型
"""

# 定义变量a
a = 56
print(a)

# 为b赋值一个大整数
b = -9999999999999999999999
print(b)

# 输出变量的类型
print(type(a))

# 判断a是否为整型
print(isinstance(a, int))

# 整型支持None值
c = None
print(c)

# 允许为数值增加下画线做分隔符 以提高可读性
d = 1_23_456
print(d)


"""
浮点型:用于保存带小数点的数值
"""

# 浮点数必须包含一个小数点,否则会当成整数类型处理
f1 = 12.3
f2 = 10.0
print(f1, f2)

# 浮点型可以用科学计数形式表示
f3 = 5.12e2  # 5.12e2 或 5.12E2  表示5.12乘10的2次方
print(f3)
f4 = 3e4
print(f4)

# 数值类型不可以除以0   ZeroDivisionError: division by zero
# n1 = 4
# n2 = 0
# n1/n2


"""
字符串
"""

# 字符串的内容可以包含任何字符,因为字符也行,中文字符也行  (python2.x要求在程序头增加"#coding:utf-8"才能支持中文字符)

string1 = 'hello'
string2 = "你好"   # 字符串内容用单引号或者双引号括起来 没有任何区别
print(string1)
print(string2)

# 如果字符串内容本身包含了单引号或双引号需要特殊处理
# str3 = 'I'm groot'

# 第一种处理方式:用双引号把字符串括起来
str4 = "I'm groot!"
print(str4)

# 如果字符串本身包含双引号,则可用单引号将字符串括起来
str5 = '小明说:"春天到了!"'
print(str5)

# 第二种处理方式:如果字符串既包含单引号,又包含双引号,此时必须用转义符  Python允许使用反斜线\将字符串中的特殊字符进行转义
str6 = '"We are scared,Let\'s hide in the shade",syss the bird'
print(str6)


# 可以使用加号+拼接字符串
str8 = "Python "
str9 = "is interesting!"
str10 = str8 + str9
print(str10)
print(str8 + str9)
print("python is funny!")


# python不允许直接将数值和字符串拼接 必须先把数值转换成字符串
num1 = 98
s1 = "这本书的价格是:"
# print(s1 + num1)	#字符串直接拼接数值,程序报错  can only concatenate str (not "float") to str

# 使用str()或repr()函数将数值转换成字符串
print(s1 + str(num1))
print(s1 + repr(num1))

# str()和repr的区别:如果直接使用print()函数输出字符串,将直接输出内容,没有引号;使用repr()处理后再输出 会看到带引号的字符串 这就是Python的表达式形式
st = "I will paly my life"
print(st)
print(repr(st))

# 三个引号可以注释多行内容 ,其实这是长字符串的写法 如果长字符串没有赋值给任何变量就会被Python解释器忽略 相当于注释了
# 可以使用三个引号括起来的长字符串赋值给变量
ls = '''"Lst's go fishing",said Mary.
"OK,Let's go",said her brother.
they walked to a lake'''
print(ls)
# 当程序中有大段文本内容要定义成长字符串时,优先推荐使用长字符串形式,可以让字符串包含任何内容,既可包含单引号,也可包含双引号


# 如果需要对表达式换行,可以使用转义字符\进行转义
sp = '白日依山尽 \
黄河入海流'
print(sp)

exp = 10 + 3 * 2 + \
	4
print(exp)


# 原始字符串:由于字符串中的反斜线都有特殊的作用,因此当字符串中包含反斜线时,就需要对其进行转义
# 比如写一条Windows的路径: D:\note\demo.py 如果在python中直接写时不行的 需要写成 D:\\note\\demo.py
print("D:\note\demo.py")
print("D:\\note\\demo.py")
# 如果借助原始字符串可以更方便解决这个问题 原始字符串以"r"开头 原始字符串不会把反斜线当成特殊字符
print(r'D:\note\demo.py')

# 如果原始字符串中包含引号 程序同样需要对引号进行转义(否则Python同样无法对字符串的引号精确配对) 但此时用于转义的反斜线会变成字符串的一部分
sty = r'"Let\'s go",said tom'
print(sty)  # "Let\'s go",said tom
# 由于原始字符串中的反斜线会对引号进行转义,因此原始字符串的结尾处不能是反斜线 否则字符串结尾处的引号就被转义了 这样导致字符串不能正确结束
# sty2 = r'Good Morning\'
sty2 = r'Good Morning' '\\' # 将反斜线单独写 再连接
print(sty2)



"""
字节串
"""
# 字节串(bytes)是python3新增的类型
# 字符串(str)由多个字符组成,以字符为单位进行操作; 字节串(bytes)由多个字节组成,以字节为单位进行操作
# bytes保存的是原始的字节(二进制格式)数据,因此bytes对象可用于再网络上传输数据,也可以存储各种二进制格式文件,比如图片、音乐
# 字节串和字符串都是不可变序列


# 创建一个空的bytes
b1 = bytes()
# 创建一个空的bytes
b2 = b''

# 通过b前缀指定hello时bytes类型的值
b3 = b'hello'
print(b3)      # b'hello'
print(b3[0])   # 104
print(b3[2:4]) # b'll'
# 调用bytes方法将字符串转换成bytes对象
b4 = bytes('我爱python编程', encoding='utf-8')  # 如果不指定字符集默认为utf-8
print(b4)
# 利用字符串的encode()方法编码成bytes,默认使用UTF-8字符集
b5 = "学习Pythion很有趣".encode('utf-8')   # 如果不指定字符集默认为utf-8
print(b5)

"""
计算机底层有两个基本概念:为(bit)和字节(Byte),其中bit代表1位,要么是0要么是1;Byte代表1字节,1字节包含8位
在字节串中每个数据单元都是字节,也就是8位,其中每4位(相当于4位二进制数,最小值为0,最大值为15)可以用一个十六进制数来表示,
因此每字节需要两个十六进制数标书,比如反斜线xe6表示1字节,其中反斜线x表示十六进制,e6就是两位的十六进制
"""

# 将bytes对象解码成字符串,默认使用UTF-8进行编码
sd = b5.decode('UTF-8')
print(sd)

