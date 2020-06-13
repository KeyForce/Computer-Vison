def matrixMul(A, B):
    sum = 0
    if len(A[0]) == len(B):
        res = [[0] * 1 for i in range(len(A))]
        for i in range(len(A)):
            for k in range(len(B)):
                a = A[i][k] * B[k]
                sum = sum + a
            res[i]=sum
        return res

def relu(x):    
    return (abs(x) + x) / 2

def softmax(x):
    import math
    max_num = max(x)
    for i in range(len(x)):
        x[i] = x[i] - max_num
    
    for i in range(len(x)):
        x[i] = math.exp(x[i])

    low = sum(x)

    for i in range(len(x)):
        x[i] = x[i]/low

    return x

n, m = map(int,input().split())

a = map(int,input().split())
x =[i for i in a]

b = map(float,input().split())
weight_1 = [i for i in b]

c = map(float,input().split())
weight_2 = [i for i in c]

w1 = []
for i in range(m):
    a = i*n
    b = (i+1)*n
    c = weight_1[a:b]
    w1.append(c)

w2 = []  
for i in range(10):
    a = i*m
    b = (i+1)*m
    c = weight_2[a:b]
    w2.append(c)

A = matrixMul(w1,x)
relu_out = []
for i in range(len(A)):
    relu_out.append(relu(A[i]))

Z = matrixMul(w2, relu_out)

Y = softmax(Z)

def net(w1, w2, x):
    A = matrixMul(w1,x)
    
    relu_out = []
    for i in range(len(A)):
        relu_out.append(relu(A[i]))

    Z = matrixMul(w2, relu_out)

    Y = softmax(Z)

    return Y

max_index = Y.index(max(Y))
my = []
for p in range(n):
    for i in range(-128, 127, 1):
        change_num = x
        change_num[p]=i
        res = net(w1, w2, change_num)
        res_index = res.index(max(res))
        if res_index != max_index:
            # print(p+1,i)