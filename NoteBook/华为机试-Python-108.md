## 字符串最后一个单词的长度

```
s = input()
lst = s.split(' ')
print(len(lst[-1]))
```

## 计算字符个数

```
input_str = str(input()).upper()
input_chr = str(input()).upper()
print(input_str.count(input_chr))
```

## 明明的随机数

```
while True:
    try:
        n = int(input())
        l = [int(input()) for _ in range(n)]
        l = sorted(set(l))
        for i in l:
            print(i)
    except:
        break
```

## 字符串分隔

```
string1 = input()
string2 = input()
 
def string_out(string):
    if len(string) <= 8:
        print(string+"0"*(8-len(string)))
    else:
        while len(string) > 8:
            print(string[:8])
            string = string[8:]
        print(string+"0"*(8-len(string)))
    return
 
string_out(string1)
string_out(string2)
```

## 进制转换

```
while True:
    try:
        string = input()
        print(int(string, 16))
    except:
        break
```

## 质数因子

```
a = int(input())
def q(x):
    zhi = 1
    for i in range(2,int(x**0.5+2)):
        if x%i == 0:
            zhi = 0
            print(str(i),end = ' ')
            q(int(x/i))
            break
    if zhi == 1:
        print(str(x),end = ' ')
 
q(a)
```

## 取近似值

```
try:
    while True:
        a = eval(input())
        if (a-int(a)) >= 0.5:
            print(int(a)+1)
        else:
            print(int(a))
except:
    pass
```

## 合并表记录

```
num = int(input())
 
def change(num):
    key_value ={}
    for i in range(num):
        key,value = input().split(' ')
        key = int(key)
        value = int(value)
        if(key in key_value):
            key_value[key]+=value
        else:
            key_value[key]=value
    for x,y in key_value.items():
        print(x,y)
change(num)
 
```

## 提取不重复的整数

```
a= int(input())
a = str(a)[::-1]
res = ''
for i in a:
    if i not in res:
        res +=i
print(int(res))
```

## 字符个数统计

```
str = input()
str_list = list(set(list(str)))
countChar = 0
for letter in str_list:
    if ord(letter)>0 and ord(letter)<128:
        countChar +=1
print(countChar)
```

## 数字颠倒

```
print(input()[::-1])
```

## 字符串反转

```
print(input()[::-1])
```

## 句子逆序

```
input = input()
input = input.split(' ')
print(' '.join(input[::-1]))
```

## 字串的连接最长路径查找

```
n = input()
a = []
for i in range(int(n)):
    a.append(input())
a.sort()
for i in range(int(n)):
    print(a[i],end = '\n')
```

## 求int型正整数在内存中存储时1的个数

```
num = int(input())
print(bin(num).count('1'))
```

## 购物单