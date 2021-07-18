"""
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""
s = "cbbd"
length = len(s)
dp = [[1]*length for _ in range(length)]
left, right = 0, 0
# 枚举字串长度
for len in range(1, length):
    # 枚举子串起始位置
    for i in range(length):
        j = i+len
        # j不能超过length，字符串是从0开始索引的
        if j>=length:
            break
        # 状态转移矩阵 1.头尾相同 2.子串也是回文
        if s[i]==s[j] and dp[i+1][j-1]:
            dp[i][j] = 1
            left, right = i,j
        else:
            dp[i][j] = 0
# 字符串切片包括开头，不包括结尾
print(s[left: right+1])



