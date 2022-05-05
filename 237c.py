x=[i for i in input()]


from collections import deque

S=deque(x)

if len(x)<=3:
    if x==x[::-1]:
        print("Yes")
        exit()
    else:
        x=x.insert(0,"a")
        if x==x[::-1]:
            print("Yes")
            exit()
        else:
            x=x.insert(0,"a")
            if x==x[::-1]:
                print("Yes")
                exit()
            else:
                x=x.insert(0,"a")
                if x==x[::-1]:
                    print("Yes")
                    exit()
                else:
                    print("No")
                    exit()


A=S.count("a")
count_R=0
flag_R=True
count_L=0
flag_L=True
for i in range(10**6):
    if A==count_R+count_L:
        break

    p=S.pop()
    q=S.popleft()
    if p=="a" and flag_R:
        count_R+=1
    else:
        flag_R=False
        S.append(p)

    if q=="a" and flag_L:
        count_L+=1
    else:
        flag_L=False
        S.appendleft(q)
    if flag_R==False and flag_L==False:
        break


if count_L>count_R:
    print("No")
    exit()


F="a"*(count_R-count_L)+"".join(x)


if F==F[::-1]:
    print("Yes")
else:
    print("No")