total_k = int(input())
# [[1, 3], [2, 4]]
num_k = []
for i in range(total_k):
    a, b = map(int,input().split())
    num_k.append([int(a), int(b)])

    # num_k.append([int(input()), int(input())])

res = [1]
for i in range(total_k):
    if num_k[i][0]==1:
        res.append(res[-1]+num_k[i][1])
    elif num_k[i][0]==2:
        res.append(res[-1]*num_k[i][1])
    elif num_k[i][0]==3:
        s = res[-1]//num_k[i][1]
        if s*num_k[i][1]>=res[-1]:
            res.append(s)
        else:
            res.append(s+1)

        

print(res[-1])