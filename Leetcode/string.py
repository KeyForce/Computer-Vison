def func(s1, s2, s3):
    # 固定窗口滑动
    j = len(s1)
    i = 0
    while i<j:      
        
        if s1[i:i+len(s2)] == s2:
            s1 = s1[:i] + s3 + s1[i+len(s2):len(s1)]

        i+=1
        j = len(s1)
        

    return s1  


s1 = "aaabbbcccc"
s2 = "cc"
s3 = 'hello'

print(func(s1, s2, s3))
