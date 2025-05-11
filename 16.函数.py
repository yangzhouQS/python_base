def hello(name) -> str:
    """
    打印hello world
    :param name:
    :return:
    """
    print(f'hello world {name}')
    return f'hello world {name}'


print("函数返回值:", hello("李四"))
print(hello.__doc__)

print("-------------位置参数-------------")


def add(a, b):
    return a + b


print(add(1, 4))
print(add(100, 33 + 27))

print("-------------默认参数-------------")


def power(x, n=2):  # n 默认值为 2
    return x ** n


print(power(3))  # 输出: 9（使用默认 n=2）
print(power(3, 3))  # 输出: 27（指定 n=3）

print("-------------可变参数-------------")


def print_args(*args):
    print(args)


print_args(1, 2, 3)


def print_kwargs(*args, **kwargs):
    print_args("位置参数:", args)
    print("关键字参数:", kwargs)


print_kwargs(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="lisi", age=18)

print("-------------仅限关键字参数-------------")


def user_info(name, *, age, city):  # age 和 city 必须用关键字传递
    print(f"{name}，年龄 {age}，城市 {city}")


user_info("Alice", age=25, city="Beijing")  # 正确


# user_info("Alice", 25, "Beijing")  # 错误，未使用关键字


def foo(y=[]):
    y.append(1)
    print(y)


l = []
foo(l)
foo(l)
foo(l)

numbers = [1, 2, 3, 4, 5]

l1 = map(lambda x: x * 2, numbers)
l2 = filter(lambda x: x % 2 == 0, numbers)
print(l1)
print(l2)

print(list(l1))
print(list(l2))

for  i in l1:
    print(i)

for i in l2:
    print(i)