"""
    读取文件练习
"""
# 直接读取文件中字符
# file = open("/home/tarena/month02/day01/111.txt","r")
# file = open("/home/tarena/month02/day01/111.txt","rb")#二进制
# data = file.read(5)
# print(data,end="")
# while True:
#   data = file.read(5)
#   # if not data:
#   if data == "":
#       break
#   print(data,end="")


# 按行读取
# file = open("/home/tarena/month02/day01/111.txt","r")
# # data = file.readline()
# # print(data)
# # data = file.readline(3)
# # print(data)
# while True:
#   data = file.read(5)
#   # if not data:
#   if data == "":
#       break
#   print(data,end="")


# 将文件内容读取为一个列表
# file = open("/home/tarena/month02/day01/111.txt","r")
# data = file.readlines(2)
# print(data)

# 迭代获取
file = open("/home/tarena/month02/day01/111.txt","r")
for data in file:
   print(data)

# 关闭文件
file.close()