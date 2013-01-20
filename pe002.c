/* Calculates the sum of even Fibonacci terms which do not exceed n. */

#include <stdio.h>

int fib(int n) {
    int curr = 1;
    int prev = 0;
    int next;
    int sum = 0;

    while (curr < n) {
        if (curr % 2 == 0) sum += curr;
        next = curr + prev;
        prev = curr;
        curr = next;
    }

    return sum;
}

int main() {
    printf("%d\n", fib(4000000));
    return 0;
}
