#include <stdio.h>
#define A 100

// calc sum
int sum(int a, int b)
{
	return a + b;
}

int main()
{
	int b = 1;
	int c = sum(A, b);
	printf("sum = %d\n", c);

	return 0;
}
