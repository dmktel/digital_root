'''Sum of Digits / Digital Root
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
 continue reducing in this way until a single-digit number is produced.
  The input will be a non-negative integer.
'''
n = int(input('Number: '))
def sum_of_digits(num):
    if num < 0:
        print("The input will be a non-negative integer!")
    else:
        while num > 9:
            num = sum(map(int, str(num)))
        return num

print(sum_of_digits(n))


        
