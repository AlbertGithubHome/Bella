// testInherit.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

class A
{
public:
    A()
    {
        cout << "A constructor" << endl;
    }
    ~A()
    {
        cout << "A destructor" << endl;
    }

    void func1()
    {
        cout << "A func1" << endl;
    }

    virtual void func2()
    {
        cout << "A func2" << endl;
    }

    virtual void func3()
    {
        cout << "A func3" << endl;
    }

private:
    int a;
};

class B : public A
{
public:
    B()
    {
        cout << "B constructor" << endl;
    }
    ~B()
    {
        cout << "B destructor" << endl;
    }

    void func1()
    {
        cout << "B func1" << endl;
    }

    virtual void func2()
    {
        cout << "B func2" << endl;
    }

    virtual void func3()
    {
        A::func3();
        //B::func3();
        cout << "B func3" << endl;
    }
private:
    int b;
};

class C : public B
{
public:
    C()
    {
        cout << "C constructor" << endl;
    }
    ~C()
    {
        cout << "C destructor" << endl;
    }

    void func1()
    {
        cout << "C func1" << endl;
    }

    virtual void func2()
    {
        cout << "C func2" << endl;
    }

    virtual void func3()
    {
        B::func3();
        cout << "C func3" << endl;
    }
private:
    int c;
};

void test1()
{
    cout << "test1" << endl;
    A aa;
    B bb;
    C cc;
}

void test2()
{
    cout << "test2" << endl;
    C cc;

    cc.func1();
    cc.func2();

    cc.A::func1();
    cc.A::func2();

    cc.B::func1();
    cc.B::func2();
}

void test3()
{
    cout << "test3" << endl;
    C cc;
    cc.func3();
}

int main()
{
    test1();
    test2();
    test3();
    return 0;
}

/*
test1
A constructor
A constructor
B constructor
A constructor
B constructor
C constructor
C destructor
B destructor
A destructor
B destructor
A destructor
A destructor
test2
A constructor
B constructor
C constructor
C func1
C func2
A func1
A func2
B func1
B func2
C destructor
B destructor
A destructor
test3
A constructor
B constructor
C constructor
A func3
B func3
C func3
C destructor
B destructor
A destructor
*/