# import itertools
# data = [i for i in range(10)]

# count=0
# for i in nums:
#     a=i[:5]
#     b=i[5:10]
#     flag=True
#     for j in range(5):
#         if b[j]>a[j]:
#             flag=False
#     if flag:
#         count+=1
    
#     # print(a)
#     # print(b)

# print(count)
# a=data[:5]
# b=data[5:10]

# nums_a = itertools.permutations(a)
# print(len(list(nums_a)))


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# dict_items([(1, 2), (3, 4), (4, 3), (2, 1), (0, 0)])
print(x.items())

# [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
print(sorted(x.items(), key=lambda b: b[1]))

# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
print(dict(sorted(x.items(), key=lambda b: b[1])))

# 键值对换在使用sorted函数 还要再对换一次键值
print(sorted([(value, key) for (key, value) in x.items()]))

# lambda b ：b就是items()方法返回的每个参数 lambda [parameter_list] ： 表达式
