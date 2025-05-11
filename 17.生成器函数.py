def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
print(next(g))
print(next(g))
print(next(g))


print('--------循环遍历生成器函数--------')
for value in my_generator():
    print(value)
