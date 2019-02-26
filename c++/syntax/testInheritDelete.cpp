// testInherit2.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
using namespace std;

class A
{
public:
    A()
    {
        cout << "A construction" << endl;
    }
    ~A()
    {
        cout << "A destruction" << endl;
    }
};

class B : public A
{
public:
    B()
    {
        cout << "B construction" << endl;
    }
    ~B()
    {
        cout << "B destruction" << endl;
    }
};

class C
{
public:
    C()
    {
        cout << "C construction" << endl;
    }
    virtual  ~C()
    {
        cout << "C destruction" << endl;
    }
};


class D : public C
{
public:
    D()
    {
        cout << "D construction" << endl;
    }
    ~D()
    {
        cout << "D destruction" << endl;
    }
};

void test1()
{
    cout << "test1" << endl;
    A* a = new B;
    delete a;
}

void test2()
{
    cout << "test2" << endl;
    B* b = new B;
    delete b;
}

void test3()
{
    cout << "test3" << endl;
    C* c = new D;
    delete c;
}

int main()
{
    test1();

    test2();

    test3();

    return 0;
}

//test1
//A construction
//B construction
//A destruction
//test2
//A construction
//B construction
//B destruction
//A destruction
//test3
//C construction
//D construction
//D destruction
//C destruction