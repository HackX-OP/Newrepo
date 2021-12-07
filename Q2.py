#2(b)
#using for loop 
list=[1,1,2,2,3,3,4,4]
ls=[]
for i in list:
    if i not in ls:
        ls.append(i)

print(ls)

#using set 
list=set(list)
print(list)