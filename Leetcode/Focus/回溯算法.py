# n, l, r = map(int,input().split())
n, l, r = 3, 2, 2
# 选择列表
a_list = [i for i in range(1,3+1)]
print(a_list)


def base_backtrack(nums, track=[]):
    if len(track) == n:
        res.append(track.copy())
        return

    for i in nums:
        track.append(i)
        backtrack(nums, track)
        track.pop()

# 带记录
def base2_backtrack(nums, used, track=[]):
    if len(track) == n:
        res.append(track[:])
        return

    for i in range(n):
        if not used[i]:
            used[i] = 1
            track.append(nums[i])
            base2_backtrack(nums, used, track)
            used[i] = 0
            track.pop()
            
        
def backtrack(nums, track=[]):
    if len(track) == (n-1):
        sum = 0
        for i in track:
            sum += i
        
        if(sum%3==0):
            res.append(track.copy())

        return

    for i in nums:
        track.append(i)
        backtrack(nums, track)
        track.pop()
 
res = []
base_backtrack(a_list)

print('1：', res)

res = []
used = [0 for _ in range(n)]
base2_backtrack(a_list, used)

print('2：', res)

res = []
backtrack(a_list)
print('3：', res)
print(len(res)%(10^9+7))