str="ananya"

"""
empty string
traverse on original string
a+''=a
y+a=ay
n+ay=ayn
a+ayn=ayna
n+ayna=aynan
..
..
aynana

"""
rev=""
for i in str:
    rev=i+rev
print(rev)
