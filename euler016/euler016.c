//
// Created by ruben on 27-1-18.
//
/*215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>



int sumDigits(long number){
    int sum = 0, digit;
    while (number>0){
        digit = number%10;
        sum+=digit;
        number = number/10;
    }
    while(0){
    }
    return sum;
}


int main(){
    time_t start,end;
    double dif;
    time (&start);

    long exponent = (long) pow(2, 1000);
    printf("Number is:%ld\n\n",exponent);
    printf("Sum of digits: %d",sumDigits(exponent));


    time (&end);
    dif = difftime (end,start);
    printf ("\nYour calculations took %.6lf seconds to run.\n", dif );

    return 0;
}
