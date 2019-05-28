#include <stdio.h>
#include "primes.h"

/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Solution:
Every whole number can be written as the product of its prime factors. Problem can be solved recursively,
# by finding smallest prime factor of the number and dividing the starting number with the returned prime factor. Problem is solved when the smallest prime factor of the number is the number itself.
*/

long long biggest_prime_factor(long long num)
{
    long long smallest_prime_fac = smallest_prime_factor(num);
    if (smallest_prime_fac == num)
    {
        return num;
    }
    else
    {
        return biggest_prime_factor(num / smallest_prime_fac);
    }
    
}

int main()
{
    printf("The biggest prime factor of 13195: %d\n", biggest_prime_factor(13195));
    printf("%d \n",sizeof(short));
    printf("%d \n",sizeof(int));
    printf("%d \n",sizeof(long));
    printf("%d \n",sizeof(long long));
    printf("The biggest prime factor of 600851475143: %d", biggest_prime_factor(600851475143));

    return 0;
}