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
        if j>=length:
            break
        if s[i]==s[j] and dp[i+1][j-1]:
            dp[i+1][j-1] = 1
            left, right = i,j
        else:
            dp[i+1][j-1] = 0

print(s[left: right+1])



