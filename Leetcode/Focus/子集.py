# (23条消息)求集合的所有子集——思路+Python实现（两种方法）_Faye_Gu的博客-CSDN博客_pytho 求集合的所有子集: https://blog.csdn.net/weixin_43509127/article/details/104394075?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.channel_param
nums = ['a', 'b', 'c']
res = [[]]
for num in nums:
    for i in res:
        res = res+[list(i)+[num]]

print(res)


def backtrack(nums, size, used, track=[]):
    if size==0:
        return
    
    
    
    for k,v in enumerate(nums):
        if not used[k]:
            track.append(v)
            result.append(track.copy())
            used[k]= True
            backtrack(nums, size-1, used, track)
            track.pop()
            used[k]= False

result = []
used = [False for i in range(len(nums))]
backtrack(nums, len(nums), used)
print(result)
