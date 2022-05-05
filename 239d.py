a,b,c,d=map(int, input().split())

import math
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


for i in range(a,b+1):
    flag=True
    for j in range(c,d+1):
        if is_prime(i+j):
            flag=False

    if flag==True:
        print("Takahashi")
        exit()
print("Aoki")        