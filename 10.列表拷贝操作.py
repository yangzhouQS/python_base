original = [1, 2, 3]
copy_list = original[:]
original[0] = -1
print(copy_list)

# 浅拷贝
copy_list = list(original)
original[0] = -1

print(copy_list)

# copy()拷贝方法 (深拷贝)
c2 = original.copy()
original[0] = -2
original.append(33)
original.append(2)
original.sort()
c2.append(1)
print(c2, original)
print(id(c2), id(original))
