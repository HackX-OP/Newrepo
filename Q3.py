Tuple=(1,2,'A','B',True,False,3+4j,[2,3,4],(2,3,4),{2,3})
#(a)
tuple1=[]
tuple1.extend(Tuple)
tuple1=list(tuple1)
tuple1[7][1]=5
k=tuple1[8]
k=list(k)
k[0]=5
k=tuple(k)
tuple1[8]=k
tuple1=tuple(tuple1)
print("ANS1=",tuple1)


#(b)
Tuple=list(Tuple)
b=Tuple[0:3:2]+Tuple[5::2]
b=tuple(b)
print("Ans2=",b)

#(c)
c=Tuple[:2:-2]
c=tuple(c)
print("Ans3=",c)
#(d)
Tuple=list(Tuple)
d=Tuple[0:5:4]
d.append(Tuple[9])
d=tuple(d)
print("Ans4=",d)
