res=[ord(x) for x in "panxiaoming"]
print res
a=[x**2 for x in range(10)]
print a
b= list(map((lambda x:x**2),range(10)))
print b

#�б�����з����ŷ�װ�������ڷ������б�дһ�����ʽ�����еı����� ����forѭ����
c=[x+y for x in 'pan' for y in 'xiaoming']
print c