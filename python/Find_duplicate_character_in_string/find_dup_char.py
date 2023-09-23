st="ananya Aithal xyz"
"""
i will traverse the string
i store that character in dict
key--character value--(count)how many times its repeated
key,value item()
if the value!=1 


print(key,value)
"""
di={}
count=1
for i in st:
    if i in di:
        di[i]=count+1
    else:
         di[i]=count
    
    
print(di)
for k,v in di.items():
     if v!=1:
        print(f"{k}: {v}")

