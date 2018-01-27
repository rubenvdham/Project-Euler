"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def find_triplet_with_sum_of(number):
    sum = number
    number = int(number/2)
    for a in range(1,number):
        for b in range (a,number):
            for c in range(b,number):
                if (a**2 +b**2) == c**2:
                    if a+b+c == sum:
                        return a,b,c



def multiply(list):
    answer = 1
    for i in range (0,len(list)):
        answer*=result[i]
    return answer

if __name__ == '__main__':
    result = find_triplet_with_sum_of(1000)
    print("Triplet %s %s %s"%(result[0],result[1],result[2]))
    print("product:%s"%(multiply(result)))

