import os
table = []
f = open("J:\\Main Project\\Computer-Vison\\Leetcode\\Focus\\a.txt")
table = []
for i in f:
    data=i.split()
    table.append(data)



tabel_utt = {}
for i in table:
    if i[1] not in tabel_utt:
        tabel_utt[i[1]] = []
    
    tabel_utt[i[1]].append([i[0], i[2]])
print(tabel_utt)

