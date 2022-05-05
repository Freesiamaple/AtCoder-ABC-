count=0
for i in range(12):
    x=[i for i in input()]
    if "r" in x:
        count+=1
print(count)