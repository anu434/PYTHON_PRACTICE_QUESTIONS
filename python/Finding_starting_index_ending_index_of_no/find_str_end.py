li=[1,3,9,2,0,7]
k=2
li2=[2,3,4,5,2]
li3=[2]

"""
len(li) is 6--0 1,2,3,4,5
we start index at 0---total 7- so len-1
i can use two for loop to traverse list to find first index and last index

i will reverse the list and my last index start from -1 ---
so range will include -1,len(rev)

if the list has only one element -1

"""
s=e=-1
for i in range(len(li2)-1):
    if li2[i]==k:
        s=i
        break
rev=li2[::-1]
print(rev)
for i in range(-1,len(rev)):
    if rev[i]==k:
        e=i
        break


print(s,e)