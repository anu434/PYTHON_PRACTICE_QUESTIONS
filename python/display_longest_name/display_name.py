li=["anu","abcdef","aithal","shivananda"]
"""
find the length of first name
i will traverse list i will compare current element with first name
if it is greater then i will update first_name and name
"""
name=li[0]
first_name=len(li[0])
for i in li:
    if len(i)>first_name:
        first_name=len(i)
        name=i
print(first_name,name)