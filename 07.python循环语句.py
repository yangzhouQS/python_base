# 示例：遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 示例：遍历字符串
for char in "hello":
    print(char)

# 示例：简单 while 循环
i = 1
while i <= 5:
    print(i)
    i += 1

print("----------")
# 示例：带 else 子句的 while 循环
i = 10
while i:
    print(i)
    i -= 1
else:
    print("循环结束", i)

# 示例：使用 break
for num in range(2, 10):
    if num > 5:
        break
    print(num)

# 示例：使用 continue
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# 示例：使用 else
for num in range(2, 5):
    print(num)
else:
    print("循环结束")

# 示例：嵌套 for 循环
print('示例：嵌套 for 循环')
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 示例：嵌套 while 循环
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

print("range ---------")
# 默认从 0 开始，每次增加 1，直到 stop - 1
for i in range(5):
    print(i)  # 输出 0, 1, 2, 3, 4

print("(2) 两个参数（start 和 stop）")

# 从 start 开始，每次增加 1，直到 stop - 1
for i in range(2, 10):
    print(i)  # 输出 2, 3, 4, 5

print("(3) 三个参数（start、stop 和 step）")
# 从 start 开始，每次增加 step，直到小于 stop（如果 step > 0）
for i in range(0, 10, 2):
    print(i)  # 输出 1, 3, 5, 7, 9

numbers = list(range(1, 6))
print(range(1, 6))
print(numbers)  # 输出 [1, 2, 3, 4, 5]

for i in range(5, 0, -1):
    print(i)  # 输出 5, 4, 3, 2, 1

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"第 {i} 个水果是：{fruits[i]}")
