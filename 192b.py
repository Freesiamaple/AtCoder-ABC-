S = input()
A=str("abcdefghijklmnopqrstuvwxyz")

for i in range(len(S)):
    if i%2==1:
        if S[i]  in A:
            print("No")
            exit()
    else:
        if S[i] not in A:
            print("No")
            exit()

print("Yes")