a=int(input("Enter 2d metrix size: "))
A=[]
print("Enter elements of matrix 1: ")
for i in range(a):
    R=[]
    for j in range(a):
        R.append(int(input()))
    A.append(R)
print("A=\n",A)
C=[]
for i in range(a):
    r=[]
    for j in range(a):
        r.append(A[j][i])
    C.append(r)
print("Transpose of matrix=:\n",C)