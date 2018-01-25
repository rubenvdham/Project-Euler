"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

def find_prime(prime_number_max):
    prime_numbers = []
    n=1
    while (True):
        n+=1;
        if is_prime(n):
            prime_numbers.append(n)
        if len(prime_numbers) >= prime_number_max:
            print(prime_numbers)
            return prime_numbers[prime_number_max-1]

def is_prime(number):
    for n in range(2,number): #Bruteforce
        if number%n == 0:
            return False

    return True


def main():
    print(find_prime(10001))

if __name__ == '__main__':
    main()