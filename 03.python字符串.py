# 创建字符串
s1 = "hello"
s2 = """word"""

# 字符串拼接
s = s1 + " " + s2
print("s = ", s)

print(s * 3)

print("hello" in s)

# 字符串切片操作
s3 = "hello word"
print(s3[0:5])
print(s3[:5])
print(s3[6:])

# 字符串查找操作
print(s3.find("o"))
print(s3.find("o", 6))
print(s3.index("o", ))
print(s3.index("o", 6))

# 字符串替换操作
print(s3.replace("o", "#"))

# 字符串分割
s4 = "hello word"
print("s4 = ", s4)
print(s4.split())

# 大小写转换
print(s4.upper())
print(s4.lower())
print(s4.title())

# 字符串长度
print(len(s4))

# 字符串格式化
print("hello %s" % "world")
print("hello %s, my age is %d" % ("world", 18))
print("hello {0}, my age is {1}".format("world", 18))
print("hello {name}, my age is {age}".format(name="world", age=18))
print("hello {name}, my age is {age}".format_map({"name": "world", "age": 18}))
print("hello {name}, my age is {age}".format_map(dict(name="world", age=18)))

print("$".join(['1', '2', '3', '4', '5']))

print('##'.join(['a', 'b', 'c', 'd']))

print("#".join(map(str, range(20))))

ss = "hello"
print(ss.startswith('he'))
print(ss.startswith('hh'))
print(ss.endswith("lo"))
print(ss.endswith("ll"))

print("你好".encode())
print("你好".encode('gbk'))
print("你好".encode('utf8'))

print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode())
print(b'\xc4\xe3\xba\xc3'.decode('gbk'))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
import urllib.parse

print(urllib.parse.unquote('%E4%BD%A0%E5%A5%BD'))
print(urllib.parse.unquote('%E4%B8%96%E7%95%8C%E4%BD%A0%E5%A5%BD'))
