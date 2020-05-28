import itertools
data = [i for i in range(10)]

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
a=data[:5]
b=data[5:10]

nums_a = itertools.permutations(a)
print(len(list(nums_a)))

