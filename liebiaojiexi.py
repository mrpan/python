res=[ord(x) for x in "panxiaoming"]
print res
a=[x**2 for x in range(10)]
print a
b= list(map((lambda x:x**2),range(10)))
print b

#列表解析有方括号封装起来，在方括号中编写一个表达式，其中的变量在 类似for循环中