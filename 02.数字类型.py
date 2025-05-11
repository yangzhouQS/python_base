# 整型
a = 10
print(type(a))  # <class 'int'>

# 浮点型
b = 3.14
print(type(b))  # <class 'float'>

# 复数型
c = 1 + 2j
print(type(c))  # <class 'complex'>

# 类型转换
d = int(3.14)  # 将浮点数转换为整数，结果为 3
d = int(3.66)  # 将浮点数转换为整数，结果为 3
print("d = %d" % d)
e = float(10)  # 将整数转换为浮点数，结果为 10.0

# 数学运算
f = a + b  # 结果为 13.14
g = a * b  # 结果为 31.4
h = pow(2, 3)  # 计算 2^3，结果为 8

# 常用函数
i = abs(-10)  # 返回 10
j = round(3.14159, 2)  # 四舍五入到两位小数，结果为 3.14
k = divmod(10, 3)  # 商为 3，余数为 1，结果为 (3, 1)

print("a: {a}, b:{b}, c:{c}".format(c=c, a=a, b=b))
print("a = {}, b = {}, c = {}".format(a, b, c))
print(f"a = {a}, b = {b}, c = {c}")
