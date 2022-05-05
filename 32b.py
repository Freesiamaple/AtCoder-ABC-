s=[i for i in input()]
t=[j for j in input()]
s.sort()
t.sort(reverse=True)
if s<t:
    print("Yes")
else:
    print("No")