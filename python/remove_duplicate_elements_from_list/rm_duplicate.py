li=[1,4,5,7,0,0,7,5,4,3]
"""
first using set--remove duplicate
second --traverse list--use another list to add element
third---


"""
k=[]
for i in li:
    if i not in k:
        k.append(i)
    
print(k)