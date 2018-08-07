// testTemplate.cpp
//
#include <stdio.h>
#include "testTemplate.h"

int main()
{
	TestTemStatic<int> test;
	A a;
	test.n = 1;
	printf("0\n");
	printf("%d, %d, %d\n", test.n, A::i, a.i);
	printf("%d, %d, %d\n", TestTemStatic<int>::knownTypeVar, TestTemStatic<float>::knownTypeVar, TestTemStatic<int>::unKnownTypeVar);
	printf("%f", TestTemStatic<float>::unKnownTypeVar);
	return 0;   
}
