li=[1,8,9,5,6,7,4]
k=2
k1=8
"""
in a list find two greater elements
use set
use max
then remove
use max
-----------------------------------------------------------
can i modify binary serach algo


------------------------------------------------------------

"""

li.sort()
li=set(li)
k=max(li)
li.remove(k)
l=max(li)
print(k,l)
