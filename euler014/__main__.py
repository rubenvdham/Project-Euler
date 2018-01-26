"""" The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""
import time

def longest_collatz_chain(maximum_start_term):
    max_terms = 1
    max_start_value = 1
    for i in range(2,maximum_start_term):
        result = collatz_sequences_recursive(i)
        if result > max_terms:
            max_start_value = i
            max_terms = result
    return max_start_value, max_terms


def collatz_sequences_looped(number):
    terms = 0
    while True:
        terms +=1
        if number <= 1:
            break
        else:
            if number%2 == 0:
                number = number/2
            else:
                number = 3*number+1
    return terms




def collatz_sequences_recursive(number):
    if number <= 1:
        return 1
    else:
        if number%2 == 0:
            number = number/2
        else:
            number = 3*number+1
        return 1+collatz_sequences_recursive(number)




def main():
    print("Expected runtime: 1 minute")
    start_time =  time.time()
    result = longest_collatz_chain(1000000)
    print("Number: %d generates the longest sequence of %d terms"% (result[0],result[1]))
    print("Runtime: %s S"% str(round(time.time()-start_time,5)))

if __name__ == '__main__':
    main()