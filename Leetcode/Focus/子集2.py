nums = [1, 2]

res = []
visitd = [0]*len(nums)
n= 2

def base_backtrack(nums, track=[]):
    if sum(track) == n:
        res.append(track.copy())
        return
    if sum(track) > n:
        return

    for i in nums:
        track.append(i)
        base_backtrack(nums, track)
        track.pop()


base_backtrack(nums)

print(res)
