# li=[1]
li=[1,9,7,6,9,0]
# li=[]
# print(len(li))
# k=min(li)
# z=max(li)
if len(li)==0:
    print(-1)

else:
    min=li[0]
    max=li[0]
    for i in li:
  
        if i>max:
            max=i
        min=i
    print(max,min)


    