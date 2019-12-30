// SingleClass.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
using namespace std;

class CBase
{
public:
    void func() {}
public:
    int m_var1;
};

class CDerived : public CBase
{
public:
    void func() {}
public:
    int m_var2;
};


int main(int argc, char* argv[])
{
    cout << sizeof(CDerived) << endl;
    int *p;
    cout << sizeof(p) << endl;

	return 0;
}

/*
1>  class CBase	size(4):
1>  	+---
1>   0	| m_var1
1>  	+---
1>
1>
1>
1>  class CDerived	size(8):
1>  	+---
1>  	| +--- (base class CBase)
1>   0	| | m_var1
1>  	| +---
1>   4	| m_var2
1>  	+---
1>
*/