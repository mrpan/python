def action(x):
	return (lambda y:x+y)
act=action(99)
act
print(act(2))
m=((lambda x:(lambda y:x+y))(99))(4)
print(m)
#嵌套的lambda表达式，能获取上层函数中的变量