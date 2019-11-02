"""
print()的语法  print(value, ..., sep=' ', end='\n', file=sys.stdout,flush=False)
    sep 多个变量之间的分隔符 默认是一个空格
    end print()函数输出后总会换行,因为end参数默认值是换行符'\n'
    file 指定print()函数的输出目标 默认值为sys.stdout(屏幕) 可以指定为计算机的某个文件
"""
name1 = 'mike'
age1 = 8
name2 = 'tom'
age2 = 10


# 同时输出多个变量和字符串
print("名字:", name1, '年龄:', age1)  # 逗号后面需要空格 不然会出现警告
print("名字:", name2, "年龄:", age2)

# 每次输出后结尾符号
print(10, '岁', end='')
print(20, '岁', end='')
print(30, '岁', end='')

# sep指定多个变量之间的连接符
print()  # 默认换行
print('我在', '中国', '江西', '南昌', sep='', end='')

# 输出内容到文件中
# f = open('C:/Users/Administrator/Desktop/poem.txt', 'w')  # 打开文件以便写入
# f = open('poem.txt', 'w')
# print('白日依山尽', '黄河入海流', '欲穷千里目', '更上一层楼', sep='\n', file=f)
