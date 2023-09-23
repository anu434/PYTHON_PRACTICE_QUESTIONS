li = [1, 4, 7, 9, 3, 2, 2]
target = 4
pairs = set()  # Use a set to store unique pairs

for i in li:
    complement = target - i
    
    if complement in li:
        # Check if the pair already exists in the set to ensure uniqueness
        if (complement, i) not in pairs and (i, complement) not in pairs:
            pairs.add((i, complement))

# Convert the set of pairs to a list for the desired output format
pairs_list = list(pairs)
print(pairs_list)




# li = [1, 4, 7, 9, 3, 2, 2]
# target = 4
# pairs = set()  # Use a set to store unique pairs

# for b in li:
#     a = target - b
    
#     if a in li:
#         # Check if the pair already exists in the set to ensure uniqueness
#         if (a, b) not in pairs and (b, a) not in pairs:
#             pairs.add((b, a))

# # Convert the set of pairs to a list for the desired output format
# pairs_list = list(pairs)
# print(pairs_list)