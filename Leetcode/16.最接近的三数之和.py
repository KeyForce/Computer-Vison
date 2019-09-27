#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.66%)
# Likes:    258
# Dislikes: 0
# Total Accepted:    45K
# Total Submissions: 108K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]
        len_num = len(nums)
        for num1 in range(len_num-2):
            num2,num3 = num1+1, len_num-1
            
            while(num2 != num3):
                thisSum = nums[num1]+nums[num2]+nums[num3]
                if thisSum == target:
                    return thisSum
                elif thisSum < target:
                    num2 += 1
                elif thisSum > target:
                    num3 -= 1
                if abs(thisSum-target) < abs(best-target):
                    best = thisSum
        return best

