def calculate_fibonacci_with_n_digits(n):
    fib = []
    fib.append(1)
    fib.append(1)
    i = 3
    while(1):
        fib.append(fib[i-2] + fib[i-3])

        if digits(fib[i-1]) == n:

            return i
        i+=1


def digits(number):
    j = 1
    while number//10 >= 1:
        number = number//10
        j+=1
    return j



assert digits(4) == 1
assert digits(444) == 3
assert digits(44444) == 5
print (calculate_fibonacci_with_n_digits(1000))