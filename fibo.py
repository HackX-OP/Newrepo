
def fibo(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        c=fibo(n-1)+fibo(n-2)
        return c

for i in range(0,6):
    print(fibo(i))