#include <stdio.h>

int main()
{
    int sum = 0;
    // find sum of all the number up to 1000, which are divisible with 3 or 5
    for(int i = 0; i < 1000; i++)
    {
        if ((i % 3 == 0) || (i % 5 == 0))
        {
            sum += i;
        }
    }
    printf("Wanted sum is equal to: %d.", sum);


    return 0;
}