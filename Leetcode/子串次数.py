a = "abababc"
b = "ab"
# 方法 1
count_a = a.count(b)
print(count_a)

# 方法 2 
# 双指针
i = 0
j = 0
count_b = 0
while i<len(a):
    if a[i]==b[j]:
        i+=1
        j+=1
    else:
        i+=1
        j=0
    if j == len(b):
        count_b += 1
        j = 0

print(count_b)

        
# 方法 3
# 固定滑动窗口
j = len(b)
count_c = 0
for i in range(len(a)):
    if a[i:i+j] == b:
        count_c += 1
print(count_c)

assert 1
print('ok')

def s():
    assert 0
    print('ok')

s()
print("sss")