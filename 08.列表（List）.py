print("1. 创建列表")
my_list = [1, 2, 3, 4]
empty_list = []

print("列表 my_list:", my_list)

print('2. 添加元素')
my_list.append(5)
# my_list: [1, 2, 3, 4, 5]
print("列表 my_list:", my_list)
my_list.insert(0, 10)
print("列表 my_list:", my_list)
my_list.extend([6, 7, 8])
print("列表 my_list:", my_list)

print('3. 删除元素')
my_list.remove(3)
print("列表 my_list:", my_list)
print(my_list.pop())
print("列表 my_list:", my_list)

print('4. 修改元素')
my_list[0] = 100
print("列表 my_list:", my_list)

print('5. 获取元素')
print("列表 my_list:", my_list.index(5))
my_list.append(1)
print(my_list.count(1))

print('6. 排序')
my_list.sort()
print(my_list)

print('7. 逆序')
my_list.reverse()
print(my_list)

print('8. 列表切片')
print("my_list = ", my_list)
print(my_list[0:3])
print(my_list[::-1])
print(my_list[::2])
print(my_list[::-2])
