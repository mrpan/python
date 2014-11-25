counters=[1,2,3,4]
L=list(map((lambda x:x+3),counters))
print(L)
pow(3,4) #81
C=list(map(pow,[2,3,5],[2,3,4]))#多个序列的参数，以每个序列对应元素作为函数对应参数得到的结果
print(C)