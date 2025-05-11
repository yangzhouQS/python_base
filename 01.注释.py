


def add(a, b):
    # 返回两个数的和
    return a + b

# 测试 add 函数
if __name__ == "__main__":
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("所有测试通过！")


def multiply(a, b):
    '''
    返回两个数的乘积

    参数:
    a (int): 第一个数
    b (int): 第二个数

    返回:
    int: 两个数的乘积

    示例:
    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    '''
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(multiply(2, 3))
    print(multiply(8, 13))



