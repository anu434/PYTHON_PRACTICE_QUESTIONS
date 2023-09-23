li=10890

"""
we assign a variable ‘temp’ to 0, we get the last digit using mod operator ‘%’. If the digit is 0, we replace it with 5, otherwise, keep it as it is. Then we multiply the ‘temp’ with 10 and add the digit got by mod operation. After that, we divide the original number by 10 to get the other digits
For example, when processing a number like 2020:

You start with multiplier as 1.
The last digit (0) is replaced with 5, and temp becomes 5.
You multiply temp (5) by multiplier (1), which is essentially the same as leaving it as 5.
You then increase the multiplier to 10 to handle the tens position.
The next digit (2) is processed and retained in the tens position, so it becomes 50.
You multiply it by the new multiplier (10), and it correctly becomes 50.
The process continues for the other digits

# Test case 1: Replace '0' with '5' in a number with multiple zeros
# Test case 2: Number with no '0's, should remain unchanged
# Test case 3: Number with all '0's, should become all '5's
# Test case 4: Large number with '0's at the beginning and end
"""
# temp=0
# last_no=li%10
# if last_no==0:
#     no=temp*10+temp
#     last_no=li//10



def replace_zeros_with_fives(number):
    temp = 0
    multiplier = 1

    while number > 0:
        last_no = number % 10 #0
        if last_no == 0:
            last_no = 5 #replace it with 5
        temp = last_no *multiplier+temp # 5*1+0=5
        multiplier = multiplier*10 #5*10=50
        
        number = number // 10 # 20

    return temp

original_number = 2020
new_number = replace_zeros_with_fives(original_number)
print(new_number)

        


        