a=int(input("Enter 2d metrix size: "))
A=[]
print("Enter elements of matrix 1: ")
for i in range(a):
    R=[]
    for j in range(a):
        R.append(int(input()))
    A.append(R)

print("A=\n",A)

b=int(input("Enter element to multiply with matrix"))

for i in range(a):
    for j in range(a):
        A[i][j]*=b

print("A after multiplication=\n",A)
