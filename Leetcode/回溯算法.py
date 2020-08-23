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
        res.append(track.copy())
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            track.append(nums[i])
            backtrack(nums, track)
            used[i] = False
            track.pop()
            
        
def backtrack(nums, track=[]):
    if len(track) == n:
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
used = [False for _ in range(n)]
base2_backtrack(a_list, used)

print(res)



