nums = ['a', 'b', 'c']
res = [[]]
visitd = [0]*len(nums)

def backtrack(nums, index, cur, n):
    for i in range(index, n):
        if i > index and nums[i] == nums[i - 1]:#剪枝
            continue
        cur.append(nums[i])
        res.append(cur[:])
        if len(cur) < n:
            backtrack(nums, i + 1, cur, n)
        cur.pop()

backtrack(nums, 0, [], len(nums))

print(res)