a=int(input("Enter 2d metrix size: "))
A=[]
print("Enter elements of matrix 1: ")
for i in range(a):
    R=[]
    for j in range(a):
        R.append(int(input()))
    A.append(R)
B=[]
print("Enter elements of matrix 2: ")
for i in range(a):
    R=[]
    for j in range(a):
        R.append(int(input()))
    B.append(R)
C=[]

for i in range(a):
    R=[]
    for j in range(a):
        R.append(0)
    C.append(R)


for i in range(a):
    for j in range(a):
        for k in range(a):
            C[i][j]+=A[i][k]*B[k][j]

print("A=\n",A)
print("B=\n",B)
print("Multiplied matrix:")
print(C)

