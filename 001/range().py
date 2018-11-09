# range 为python内置函数，用于创建一个整数列表，一般用在for循环中。
# 函数： range（start, stop[, step]）
# 说明：start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

# 例1
range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
range(0)
[]
range(1, 0)
[]



# 例2， range 在 for 中的使用，循环出runoob 的每个字母:
x = 'runoob'
for i in range(len(x)) :
      print(x[i])
