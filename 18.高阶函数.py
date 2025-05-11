print("1.函数作为参数传递")
numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)

event_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(event_numbers))

print("2.函数作为返回值")


def foo(x):
    def bar(y):
        return x * y

    return bar


print(foo(10)(20))

print("3.装饰器")


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def hello(a, b, c, *, name, age):
    print("hello 函数", a, b, c, name, age)


hello(1, 2, 3, age=33, name="tom")












