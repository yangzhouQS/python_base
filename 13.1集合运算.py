user_a_likes = {'book', 'music', 'movie'}
user_b_likes = {'music', 'sport', 'movie'}

# 1. 交集：找出两个人共同喜欢的内容
common = user_a_likes & user_b_likes
print("共同喜好:", common)  # 输出: {'music', 'movie'}
print("intersection:", user_a_likes.intersection(user_b_likes))
print("共有:", len(common))

# 2. 并集：两个人所有喜欢的内容去重
all_likes = user_a_likes | user_b_likes
print("所有喜好:", all_likes)  # 输出: {'book', 'music', 'movie', 'sport'}
print("合集 union:",user_a_likes.union(user_b_likes))



# 3. 差集：user_a 喜欢但 user_b 不喜欢的
diff_a_b = user_a_likes - user_b_likes
print("A喜欢但B不喜欢:", diff_a_b)  # 输出: {'book'}

# 4. 对称差集：只在其中一个集合中出现的元素
sym_diff = user_a_likes ^ user_b_likes
print("对称差集:", sym_diff)  # 输出: {'book', 'sport'}

# 5. 子集判断：判断 user_a_likes 是否是 {'book', 'music', 'movie', 'sport'} 的子集
is_subset = user_a_likes.issubset({'book', 'music', 'movie', 'sport'})
print("user_a_likes 是更大集合的子集吗？", is_subset)  # True

# 6. 超集判断
is_superset = user_a_likes.issuperset({'music', 'movie'})
print("user_a_likes 是包含 music 和 movie 的超集吗？", is_superset)  # True
