#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#


class Solution:
    def reverseWords(self, s: str) -> str:
        
        s_split = s.split()
        s_out = ''
        for string in s_split:
            string = string[::-1]
            s_out = ' '.join([s_out, string])
        
        return s_out.strip()


if __name__ == "__main__":
    a = Solution()
    a.reverseWords("Let's take LeetCode contest")
