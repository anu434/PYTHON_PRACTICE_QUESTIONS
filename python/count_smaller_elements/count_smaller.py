li=[1,8,9,6,5,7,3]
k=6
"""
count the number which are smaller than 6
6--1,3,5--3
i will traverse the list
check condition element <6
then i increment the count
"""
count=0
for i in li:
    if i<k:
        count+=1
print(count)