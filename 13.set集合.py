s1 = set()
s2 = {1, 2, 3, 4}
s3 = set(range(10))
print(s1, s2, s3)
print(type(s1), type(s2), type(s3))

# 集合添加元素
s1.add("a")
s1.add(1)
print(s1)

# 删除不存在会报错
# s1.remove('b')

# 删除时，不存在不会报错
s1.discard('b')
if 'b' in s1:
    s1.remove('b')
else:
    print('b not in s1')


print(len(s1))
user_a_likes = {'book', 'music', 'movie'}
user_b_likes = {'music', 'sport', 'movie'}

common_likes = user_a_likes & user_b_likes
print(common_likes)  # {'music', 'movie'}
