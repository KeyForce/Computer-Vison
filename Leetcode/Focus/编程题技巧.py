# 随机输出
import random

t = input()
for i in range(int(t)):
    if random.randint(1, 100) > 50:
        print('yes')
    else:
        print('no')

# 数据输入
a, b = map(int, input().split())
