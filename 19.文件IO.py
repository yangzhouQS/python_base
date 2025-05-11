from datetime import datetime

# 获取当前日期和时间
now = datetime.now()

f = open("test.txt", "a", encoding="utf8")

# for i in range(10):
#     # 写入操作
#     f.write("%s This is line %d\n" % (now.strftime("%Y-%m-%d %H:%M:%S"), i + 1))

for i in range(5):
    # 写入操作
    f.writelines(["Line 1\n", f"Line 2 时间: {now.strftime('%H:%M:%S')}\n"])

# 逐行读取
# with open("test.txt", "r") as file:
#     for line in file:
#         print(line)

# 一次性读取
# with open("test.txt", "r") as file:
#     content = file.read()
#     print(content)


# 按行读取为列表
with open("test.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

f.close()
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化时间：", formatted_time)
