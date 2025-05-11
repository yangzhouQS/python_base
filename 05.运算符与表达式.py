a = 10
b = 3

print(a + b)  # 加法: 13
print(a - b)  # 减法: 7
print(a * b)  # 乘法: 30
print(a / b)  # 除法: 3.333...
print(a // b)  # 整除: 3
print(a % b)  # 取余: 1
print(a ** b)  # 幂运算: 1000

# 比较运算符
print('---------------比较运算符')
x = 5
y = 8

print(x == y)  # 相等比较: False
print(x != y)  # 不等比较: True
print(x > y)  # 大于比较: False
print(x < y)  # 小于比较: True
print(x >= y)  # 大于等于比较: False
print(x <= y)  # 小于等于比较: True

# 逻辑运算符
print('---------------逻辑运算符')
x = True
y = False
print(x and y)  # and: False
print(x or y)  # or: True
print(not x)  # not: False

# 赋值运算符
print('---------------赋值运算符')
x = 10
x += 5
print(x)
x *= 2
print(x)
x /= 2
print(x)
x %= 2
print(x)
x **= 2
print(x)
x //= 2
print(x)

# 位运算符
print('---------------位运算符')

a = 5  # 二进制表示为 0101
b = 3  # 二进制表示为 0011

print(a & b)  # 按位与: 0001 (十进制为1)
print(a | b)  # 按位或: 0111 (十进制为7)
print(a ^ b)  # 按位异或: 0110 (十进制为6)
print(~a)  # 按位取反: -0110 (十进制为-6，在Python中负数用补码表示)
print(a << 1)  # 左移一位: 1010 (十进制为10)
print(a >> 1)  # 右移一位: 0010 (十进制为2)
