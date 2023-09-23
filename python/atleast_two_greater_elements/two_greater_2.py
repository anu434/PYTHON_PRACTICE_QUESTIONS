"""
or
i will compare first element with

1] 
"""
li=[1,8,9,5,6,7,4]
first_element=li[0]
second_element=li[0]
for i in range(len(li)):
    if li[i]>first_element:
        first_element=second_element
        first_element=li[i]
    if li[i]>second_element and first_element!=second_element:
        second_element=li[i]
print(first_element,second_element)






