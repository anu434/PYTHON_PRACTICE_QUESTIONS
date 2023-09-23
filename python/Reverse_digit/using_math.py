"""
we can Get the last digit
we can add last digit to reversed number
remove last digit

initiaaly rev_no is 0
rm=12345%10 =5
rev_no=rev_no*10+rm= 0*10+5=5
no=no//10 =1234

rev_no=5
rm=1234%10= 4
rev_no=5*10+4=54
.
..
.
remainder = 1 % 10 gives 1.
reversed_num = (5432 * 10) + 1 becomes 54321.
number = 1 // 10 gives 0.
When the loop finishes, the reversed_num is 54321, which is the reverse of the original number 12345.




"""







def reverse_digits(number):
    reversed_num = 0

    while number > 0:
        remainder = number % 10  # Get the last digit
        reversed_num = reversed_num * 10 + remainder  # Add the last digit to the reversed number
        number = number // 10  # Remove the last digit

    return reversed_num

original_number = 12345
reversed_number = reverse_digits(original_number)
print(reversed_number)
