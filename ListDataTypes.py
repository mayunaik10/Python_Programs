my_list = ['Mayuri',63,98.35,True,'A',5,8.3,False,'M','T','Leena','sudha',22]
i=s=f=c=b=0
l_int=[]
l_float=[]
l_boolean=[]
l_str=[]
l_char=[]
for item in my_list:
 if type(item)==int:
  i+=1
  l_int.append(item)
 elif type(item)==float:
  f+=1
  l_float.append(item)
 elif type(item)==bool:
  b+=1
  l_boolean.append(item)
 elif type(item)==str and len(item)>1:
  s+=1
  l_str.append(item)
 else:
  c+=1
 l_char.append(item)
print(f"The number of Integers in the list are {i} and elements are {l_int}")
print(f"The number of Float in the list are {f} and elements are {l_float}")
print(f"The number of Boolean in the list are {b} and elements are {l_boolean}")
print(f"The number of Strings in the list are {s} and elements are {l_str}")
print(f"The number of Characters in the list are {c} and elements are{l_char}")