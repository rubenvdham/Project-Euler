"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

number = 600851475143
x = 1
dividable_primes = []
while(number>1):
    x+=2
    if number%x == 0:
        number/=x
        dividable_primes.append(x)
print(dividable_primes)
print("Last prime factor is %s"%(dividable_primes[len(dividable_primes)-1]))
