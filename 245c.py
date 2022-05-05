from numpy import true_divide


n,k=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
num_A=True
num_B=True
n_num_A=True
n_num_B=True

for i in range(n-1):
    if num_A==True:
        if abs(A[i]-A[i+1])<=k:
            n_num_A=True
        else:
            n_num_A=False
        if abs(A[i]-B[i+1])<=k:
            n_num_B=True
        else:
            n_num_B=False
    


    if num_B==True:
        if abs(B[i]-A[i+1])<=k:
            n_num_A=True
        else:
            if n_num_A==False:
                n_num_A=False
        if abs(B[i]-B[i+1])<=k:
            n_num_B=True
        else:
            if n_num_B==False:
                n_num_B=False

    num_A=n_num_A
    num_B=n_num_B
    n_num_A=False
    n_num_B=False


    if num_A or num_B:
        continue
    else:
        print("No")
        exit()
print("Yes")