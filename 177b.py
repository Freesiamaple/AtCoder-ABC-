s=[i for i in input()]
t=[i for i in input()]
count=0
for i in range(len(s)):
    if s[i]!=t[i]:
        count+=1
print(count)