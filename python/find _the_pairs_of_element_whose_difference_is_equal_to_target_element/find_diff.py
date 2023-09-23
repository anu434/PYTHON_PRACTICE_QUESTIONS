li=[2,4,5,6]
"""
we need to find two pairs whose difference should be equal to target
(2,4) and (4,6)
target = 2
a = 4
b = 2
target = a - b, which simplifies to 2 = 4 - 2
a = b + target, which simplifies to 4 = 2 + 2


create one empty list
and find the compliement
traverse the list
check that complement of is present in original list
we have to find difference a-b
compliment of t=a-b is a=b+t 
target we know--using both i,j---finding difference between elements 2-4,2-5,4-2,4-5 etc
compliment using target ,i(b)--this is first element if we add these two we get j(a)--this is the 2nd element

we are checking target+i = (j)2nd element(aftr aading value the result is in org list if it is there
means we find pair) i,j (a,b)

compliment_plus--acending order   target + i
minus--decending order              i - target


"""


# print(pairs)
def find_pairs_with_difference(li, target):
    pairs = []  # Create a list to store pairs

    for i in li:
        # complement_plus = target + i
        complement_minus = i - target

        # Check if either complement exists in the list
        # if complement_plus in li:
        #     pairs.append((i, complement_plus))
        if complement_minus in li:
            pairs.append((i, complement_minus))

    return pairs

# Test case 1: Pairs with a target difference of 2
li1 = [1, 2, 3, 4, 5, 6]
target1 = 2
result1 = find_pairs_with_difference(li1, target1)
# Expected output: [(1, 3), (3, 1), (2, 4), (4, 2), (3, 5), (5, 3)]
print(result1)

# Test case 2: No pairs with the target difference in the list
li2 = [1, 2, 3, 4, 5]
target2 = 7
result2 = find_pairs_with_difference(li2, target2)
# Expected output: []
print(result2)

# Test case 3: Pairs with a target difference of 0 (same elements)
li3 = [3, 3, 3, 3, 3]
target3 = 0
result3 = find_pairs_with_difference(li3, target3)
# Expected output: [(3, 3), (3, 3), (3, 3), (3, 3), (3, 3), (3, 3)]
print(result3)





