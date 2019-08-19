// testBind.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <functional>
using namespace std;

void func(int n1, int n2, int n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3 << endl;
}

int calc_value(int c1)
{
    return c1 * c1;
}

void calc_value2(int c1)
{
    int result = c1 * c1;
}

void test1_1()
{
    auto f1 = std::bind(func, placeholders::_1, 101, std::bind(calc_value, placeholders::_2));
    f1(11, 2);   // same as call func(11, 101, calc_value(2))
}

void test1_2()
{
    int n = 3;
    auto f1 = std::bind(func, placeholders::_1, 101, std::bind(calc_value, std::ref(n)));
    n = 4;
    f1(11, 2);   // same as call func(11, 101, calc_value(44)) 多出的参数2无人使用
}

void test1_3()
{
    auto f1 = std::bind(func, placeholders::_1, 101, std::bind(calc_value2, placeholders::_2));
    //f1(11, 2);   // 编译出错，无法将参数 3 从“void”转换为“int”
}


class CTest 
{
public:
    CTest() {}
    ~CTest() {}
public:
    void    func1(int n1, int n2)
    {
        cout << "func1 " << n1 << ' ' << n2 << endl;
    }

    int     n_public;
	
private:
    void    func2(int n1, int n2)
    {
        cout << "func2 " << n1 << ' ' << n2 << endl;
    }

    int n_private;
};


void test2_1()
{
    CTest testObj;
    auto f2 = std::bind(&CTest::func1, testObj, 101, placeholders::_1);
    f2(1);   // same as call testObj.func1(101, 1)
}

void test2_2()
{
    CTest testObj;
    auto f2 = std::bind(&CTest::func1, &testObj, 101, placeholders::_1);
    f2(2);   // same as call testObj.func1(101, 2)
}

void test2_3()
{
    CTest testObj;
    CTest& obj = testObj;
    auto f2 = std::bind(&CTest::func1, obj, 101, placeholders::_1);
    f2(3);   // same as call testObj.func1(101, 3)
}


void test2_4()
{
    CTest testObj;
    auto f2 = std::bind(&CTest::func1, placeholders::_1, placeholders::_2, 101);
    f2(testObj, 4);   // same as call testObj.func1(4, 101)
}

void test2_5()
{
    CTest testObj;
    // auto f2 = std::bind(&CTest::func2, &testObj, 101, placeholders::_1);
    // 编译错误，func2不可访问
}

//func1 101 1
//func1 101 2
//func1 101 3
//func1 4 101



void test3_1()
{
    CTest testObj;
    auto f3 = std::bind(&CTest::n_public, testObj);
    f3(1) = 10;
    cout << f3(1) << endl;
    cout << testObj.n_public << endl;
}


void test3_2()
{
    CTest testObj;
    auto f4 = std::bind(&CTest::n_public, placeholders::_1);
    f4(testObj) = 4;
    cout << f4(testObj) << endl;
    cout << testObj.n_public << endl;
}


void test3_3()
{
    CTest testObj;
    auto f3 = std::bind(&CTest::n_public, std::ref(testObj));
    f3(1) = 11;
    cout << f3(1) << endl;
    cout << testObj.n_public << endl;
}

//10
//-858993460
//4
//4
//11
//11



int main(int argc, char* argv[])
{
    test1_1();
    test1_2();
    test1_3();
    putchar('\n');
    test2_1();
    test2_2();
    test2_3();
    test2_4();
    putchar('\n');
    test3_1();
    test3_2();
    test3_3();
    putchar('\n');
    
    
    getchar();
    return 0;
}

/*
11 101 4
11 101 16

func1 101 1
func1 101 2
func1 101 3
func1 4 101

10
-858993460
4
4
11
11
*/
