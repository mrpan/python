def action(x):
	return (lambda y:x+y)
act=action(99)
act
print(act(2))
m=((lambda x:(lambda y:x+y))(99))(4)
print(m)
#Ƕ�׵�lambda���ʽ���ܻ�ȡ�ϲ㺯���еı���