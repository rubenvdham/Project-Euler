"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

max = 1000
x = 1
sum = 0
numbers_added = []
while(True):
    answer = 5*x
    if answer < max and numbers_added.count(answer) == 0:
        sum+=answer
        numbers_added.append(answer)
    answer = 3*x
    if answer < max and numbers_added.count(answer) == 0:
        sum+=answer
        numbers_added.append(answer)
    elif answer > max:
        break
    x+=1
print(sum)
