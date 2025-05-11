t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = tuple([1, 2, 3])
t5 = 1, 2, 3
t6 = 1,
print(type(t1), type(t5))

t = (10, 20, 30, 20)
print(t.index(20))  # 输出 1


print(t.count(20))
