li=[1,6,7,"anu","aithl",9,8,0]
"""
traverse the list 
how u vl idetify its integer
use isintance 
or check type
"""
# count=0
# for i in li:
#     if isinstance(i,int):
#         count+=1
# print(count)


count = sum(isinstance(x, int) for x in li)
print(count)
