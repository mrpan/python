# -*- coding: cp936 -*-
f=lambda x,y,z:x+y+z
f(2,3,4)
x=(lambda a="aaa",b="bbb",c="cccc":a+b+c)
x("abc")
#��ת����Ϊ���б���ֵ�
L=[lambda x:x**2,lambda x:x**3,lambda x:x**4]
for f in L:
	print(f(2))
print(L[1](2))
