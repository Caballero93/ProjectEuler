#include <stdio.h>
#include "primes.h"

long long is_prime(long long num)
/* 
Checks if number is prime or not
*/
{
    // 2 and 3 are prime numbers
    if (num == 2 || num==3)
    {
        return 1;
    }
    // prime number should be in form of 6n-1 or 6n+1
    else if (num % 6 != 1 && num % 6 != 5)
    {
        return 0;
    }
    else
    {
        for(long long i=2; i<=(long long)(num/2+1); i++)
        {
            if (num % i == 0)
            {
                return 0;
            }
        }
        return 1;
    }
}

long long smallest_prime_factor(long long num)
/*
Returns the smallest prime factor of integer num
*/
{
    for(long long i=2; i<=(long long)(num/2+1); i++)
    {
        if(is_prime(i) && num%i == 0)
        {
            return i;
        }
    }
    return num;
}