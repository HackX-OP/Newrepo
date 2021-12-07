dict1={"brand":"Ford","model":"Mustang","year":1964}

#(A)
dict2={}
dict2.update(dict1)
print(dict2)

#(B)
dict1.pop("brand")
del dict1["model"]
print(dict1)