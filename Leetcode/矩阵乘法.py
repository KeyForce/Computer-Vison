while True:
    try:
        x = int(input())
y = int(input())
z = int(input())

a = []
b = []
# 输入矩阵 [[],[],...]
for i in range(x):
    num = list(map(int, input().split()))
    a.append(num)

for i in range(y):
    num = list(map(int, input().split()))
    b.append(num)


def matrix_mul(a, b):
    res_row = len(a)
    res_col = len(b[0])

    if res_row == res_col:
        # 初始化矩阵
        res = [[0]*res_col for i in range(res_row)]
        for i in range(res_row):
            for j in range(res_col):
                for k in range(len(b)):
                    res[i][j] += a[i][k]*b[k][j]

    return res


res = matrix_mul(a, b)

# 输出
for i in range(len(res)):
    c = []
    for j in range(len(res[0])):
        c.append(res[i][j])
    c = list(map(str, c))
    print(' '.join(c))

except:
    break
