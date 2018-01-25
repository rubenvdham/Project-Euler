"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""
def generate_largest_palindrome():
    palindromes = []
    for factor1 in range(100,999):
        for factor2 in range(100,999):
            answer = factor1 * factor2
            if palindrome(answer):
                palindromes.append(answer)
    palindromes.sort()
    return palindromes[len(palindromes)-1]

def palindrome(number):
    number_string = str(number)
    if len(number_string)%2 == 0:
        first_half_number = number_string[:int(len(number_string)/2)]
        last_half_number = number_string[int(len(number_string)/2):]
        if first_half_number == reverse(last_half_number):
            return True
    else:

        first_half_number = number_string[:int(len(number_string)/2)]

        last_half_number = number_string[int(len(number_string)/2)+1:]

        if first_half_number == reverse(last_half_number):
            return True
    return False


def reverse(chars):
    reversed = ""
    for i in range(0,len(chars)):
        j = len(chars)-i-1
        reversed = reversed[:i]+ chars[j]
    return reversed

def main():
    print (generate_largest_palindrome())
if __name__ == "__main__":
    main()