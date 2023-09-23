
"""
create one empty list
append.pairs(())-bec tuple
target=a+b
compliment of this is
i have target and b i have find a   if there is a sum this a should present in org
if i minus a=target-b
           a=4-1=3 (a,b)(3,1)
           a=4-4=0 ()
           a=4-7=3 ()
           a=4-9=5
           a=4-3=6
           a=4-2=2 (2,2)
           
"""
li=[1,4,7,9,3,2,2]
target=4
pairs=[]
for i in li:
    compliment=target-i
    #compliment=i-target
    if compliment in li:
        pairs.append((compliment,i))
print(pairs)