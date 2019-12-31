// SingleInherit.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
using namespace std;

class CBase
{
public:
    void func0() {}
    virtual void func1() {}
    virtual void func2() {}
public:
    int m_var1;
};

class CDerived : public CBase
{
public:
    virtual void func2() {}
    virtual void func3() {}
    void func4() {}
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
1>  class CBase	size(8):
1>  	+---
1>   0	| {vfptr}
1>   4	| m_var1
1>  	+---
1>
1>  CBase::$vftable@:
1>  	| &CBase_meta
1>  	|  0
1>   0	| &CBase::func1
1>   1	| &CBase::func2
1>
1>  CBase::func1 this adjustor: 0
1>  CBase::func2 this adjustor: 0
1>
1>
1>  class CDerived	size(12):
1>  	+---
1>  	| +--- (base class CBase)
1>   0	| | {vfptr}
1>   4	| | m_var1
1>  	| +---
1>   8	| m_var2
1>  	+---
1>
1>  CDerived::$vftable@:
1>  	| &CDerived_meta
1>  	|  0
1>   0	| &CBase::func1
1>   1	| &CDerived::func2
1>   2	| &CDerived::func3
1>
1>  CDerived::func2 this adjustor: 0
1>  CDerived::func3 this adjustor: 0
*/

