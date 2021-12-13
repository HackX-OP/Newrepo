def fact(p):
    if(p==1):
        return 1
    else:
        return p*fact(p-1)
n=5
r=2
c=fact(n)/fact(n-r)
print(c)
