"""*215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?"""
import math

power = 1000


def sum_digits(num):
    sum = 0
    for c in str(num):
        sum+= int(c)
    return sum

def main():
    number = int(math.pow(2,power))
    print("Number is: %d"% number)
    print("Sum of digits:%d"%sum_digits(number))


if __name__ == '__main__':
    main()