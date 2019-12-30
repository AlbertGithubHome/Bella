// MultipleInherit.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
using namespace std;

class CBase0
{
public:
    void func0() {}
    virtual void func1() {}
    virtual void func2() {}
    virtual void func3() {}
public:
    int m_var0;
};

class CBase1
{
public:
    void func0() {}
    virtual void func2() {}
    virtual void func3() {}
    virtual void func4() {}
public:
    int m_var1;
};

class CDerived : public CBase0, public CBase1
{
public:
    virtual void func1() {}
    virtual void func2() {}
    virtual void func4() {}
    virtual void func5() {}
    void func6() {}
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
1>  class CBase0	size(8):
1>  	+---
1>   0	| {vfptr}
1>   4	| m_var0
1>  	+---
1>
1>  CBase0::$vftable@:
1>  	| &CBase0_meta
1>  	|  0
1>   0	| &CBase0::func1
1>   1	| &CBase0::func2
1>   2	| &CBase0::func3
1>
1>  CBase0::func1 this adjustor: 0
1>  CBase0::func2 this adjustor: 0
1>  CBase0::func3 this adjustor: 0
1>
1>
1>  class CBase1	size(8):
1>  	+---
1>   0	| {vfptr}
1>   4	| m_var1
1>  	+---
1>
1>  CBase1::$vftable@:
1>  	| &CBase1_meta
1>  	|  0
1>   0	| &CBase1::func2
1>   1	| &CBase1::func3
1>   2	| &CBase1::func4
1>
1>  CBase1::func2 this adjustor: 0
1>  CBase1::func3 this adjustor: 0
1>  CBase1::func4 this adjustor: 0
1>
1>
1>  class CDerived	size(20):
1>  	+---
1>  	| +--- (base class CBase0)
1>   0	| | {vfptr}
1>   4	| | m_var0
1>  	| +---
1>  	| +--- (base class CBase1)
1>   8	| | {vfptr}
1>  12	| | m_var1
1>  	| +---
1>  16	| m_var2
1>  	+---
1>
1>  CDerived::$vftable@CBase0@:
1>  	| &CDerived_meta
1>  	|  0
1>   0	| &CDerived::func1
1>   1	| &CDerived::func2
1>   2	| &CBase0::func3
1>   3	| &CDerived::func5
1>
1>  CDerived::$vftable@CBase1@:
1>  	| -8
1>   0	| &thunk: this-=8; goto CDerived::func2
1>   1	| &CBase1::func3
1>   2	| &CDerived::func4
1>
1>  CDerived::func1 this adjustor: 0
1>  CDerived::func2 this adjustor: 0
1>  CDerived::func4 this adjustor: 8
1>  CDerived::func5 this adjustor: 0
*/


