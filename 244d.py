T=list(map(str, input().split()))
S=list(map(str, input().split()))




if T[0]=="R"and T[1]=="G" and T[2]=="B":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("Yes")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("No")
    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("No")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("Yes")
    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("No")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("Yes")


if T[0]=="R"and T[1]=="B" and T[2]=="G":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("No")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("Yes")

    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("Yes")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("No")

    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("Yes")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("No")

if T[0]=="G"and T[1]=="R" and T[2]=="B":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("No")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("Yes")

    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("Yes")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("No")

    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("Yes")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("No")

if T[0]=="G"and T[1]=="B" and T[2]=="R":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("Yes")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("No")

    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("No")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("Yes")

    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("No")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("Yes")

if T[0]=="B"and T[1]=="R" and T[2]=="G":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("Yes")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("No")

    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("No")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("Yes")

    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("No")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("Yes")

if T[0]=="B"and T[1]=="G" and T[2]=="R":
    if S[0]=="R"and S[1]=="G" and S[2]=="B":
        print("No")
    if S[0]=="R"and S[1]=="B" and S[2]=="G":
        print("Yes")

    if S[0]=="G"and S[1]=="R" and S[2]=="B":
        print("Yes")
    if S[0]=="G"and S[1]=="B" and S[2]=="R":
        print("No")

    if S[0]=="B"and S[1]=="G" and S[2]=="R":
        print("Yes")
    if S[0]=="B"and S[1]=="R" and S[2]=="G":
        print("No")