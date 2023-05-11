# coding=utf-8

#!/usr/bin/python3
import keyword
# print(keyword.kwlist)
# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
# print("Hello, Python!", "this is a line with \n"*2)
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
str = '123456789'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# if expression:
#     suite
# elif expression:
#     suite
# else:
#     suite
#!/usr/bin/python3

# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)

# print('---------')
# # 不换行输出
# print(x, end="")
# print(y, end="")


#!/usr/bin/python3

counter = miles = 100          # 整型变量
# miles = 1000.0       # 浮点型变量
name = "runoob"     # 字符串

print(counter)
print(miles)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))
