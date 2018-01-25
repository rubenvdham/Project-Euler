"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
import time
def sum_primes_until(prime_number_max): #Sieve of Eratosthenes
    numbers = []
    for i in range (2,prime_number_max):
        numbers.append(i)
    p=2
    while (True):
        i = 2
        anything_marked = False
        while (i*p < prime_number_max):
            if not numbers[i*p-2] == 0:
                numbers[i*p-2] = 0
                anything_marked = True
            i+=1
        if not anything_marked:
            break
        temp_p = p
        for j in range(0,len(numbers)):
            if numbers[j] > p:
                p = numbers[j]
                break
        if temp_p == p:
            break
    prime_numbers = numbers
    return sum(prime_numbers)




def main():
    start = time.time()
    print(sum_primes_until(2000000))
    print("\nRuntime: %s seconds" % str(round(time.time()-start,5)))
if __name__ == '__main__':
    main()