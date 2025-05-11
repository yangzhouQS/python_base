my_list = [10, 1, 2, 4, 5, 6, 7, 1]  # 假设这是当前列表
print(my_list[0:3])

print(my_list[3:])

print(my_list[:5])  # 从开始到索引 4 → [10, 1, 2, 4, 5]
print(my_list[3:])  # 从索引 3 到末尾 → [4, 5, 6, 7, 1]

print(my_list[::2])  # 从开始到末尾，步长为 2 → [10, 2, 5, 7]

print(my_list[::-1])  # 整个列表反转 → [1, 7, 6, 5, 4, 2, 1, 10]
print(my_list[::-2])  # 反转并每隔一个元素取一个 → [1, 6, 4, 1]

# 从range()函数创建的列表
print(list(range(10)))
print(list(range(2, 14)))
print(list(range(2, 20, 2)))




