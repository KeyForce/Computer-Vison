#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.14%)
# Likes:    1400
# Dislikes: 0
# Total Accepted:    130.5K
# Total Submissions: 474.8K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="":return ""
        s1 = '$#'+'#'.join(s)+'#@'
        mx = 0#已遍历的最大右边界
        mid = 0#对应的中心点
        l = len(s1)
        dp = [0]*l
        for i in range(1,l-1):
            if i<mx:#可以利用之前保存的值
                dp[i] = min(mx-i,dp[mid*2-i])#不能超过已遍历的右边界
            t = 0
            while 1:#继续扩张
                if s1[i+dp[i]+t]!=s1[i-dp[i]-t]:
                    break
                t+=1
            dp[i]+=t-1
            if i+dp[i]>mx:#更新边界值
                mx = i+dp[i]
                mid = i
        maxlen,maxidx=0,0
        for i in range(l):#找最大子串
            if dp[i]>maxlen:
                maxlen = dp[i]
                maxidx = i
        return s1[maxidx-maxlen:maxidx+maxlen+1].replace('#',"")
        
# @lc code=end
