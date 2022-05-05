n=int(input())
s=[i for i in input()]
if "W" not in s:
    print(0)
    exit()
if "R" not in s:
    print(0)
    exit()
r_num=s.count("R")
r_now=s[0:r_num].count("R")
print(r_num-r_now)