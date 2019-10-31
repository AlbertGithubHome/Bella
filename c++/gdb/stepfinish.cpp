#include <iostream>
using namespace std;

int son_func()
{
	int a = 100;
	int b = 1;
	return a + b;
}

int main()
{
	int i = 10;
	cout << i << endl;

	int result = son_func();

	cout << result << endl;
}
