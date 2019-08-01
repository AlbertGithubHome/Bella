// testBind.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include <iostream>
#include <functional>
using namespace std;

void func1(int n1, int n2, int n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3  << endl;
}

void test1_1()
{
    auto f1 = std::bind(func1, placeholders::_1, 101, placeholders::_2);
    f1(11, 22);   // same as call func1(11, 101, 22)
}

void test1_2()
{
    auto f1 = std::bind(func1, placeholders::_2, 101, placeholders::_1);
    f1(11, 22);   // same as call func1(22, 101, 11)
}




void func2(int n1, int n2, int n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3 << endl;
}

void test2_1()
{
    auto f2 = std::bind(func2, placeholders::_3, 101, placeholders::_1);
    f2(11, 22, 33);   // same as call func2(33, 101, 11)
}

void test2_2()
{
    auto f2 = std::bind(func2, placeholders::_1, 101, placeholders::_1);
    f2(11);   // same as call func2(11, 101, 11)
}

void test2_3()
{
    auto f2 = std::bind(func2, placeholders::_1, 101, placeholders::_2);
    //f2(11);   // ���������Ϊû�в�������placeholders::_2
}




void func3(int n1, int n2, int n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3 << endl;
}

void test3_1()
{
    auto f3 = std::bind(func3, placeholders::_1, 101);
    //f3(11);   // ���������Ϊbind����������һ������
}

void test3_2()
{
    auto f3 = std::bind(func3, placeholders::_1, 101, 102, 103);
    //f3(11);   // ���������Ϊbind�����ж���һ������
}

void test3_3()
{
    auto f3 = std::bind(func3, placeholders::_1, "test", placeholders::_1);
    //f3(11);   // ������󣬵ڶ����������Ͳ�ƥ�䣬�޷������� 2 �ӡ�const char *��ת��Ϊ��int��
}



void func4(int n1, int n2, int& n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3 << endl;
    n3 = 101;
}

void test4_1()
{
    int n = 10;
    auto f4 = std::bind(func4, 11, 22, 10);
    n = 33;
    f4();   // same as call func4(11, 22, 10)
    cout << "n = " << n << endl;
}

void test4_2()
{
    const int n = 30;
    auto f4 = std::bind(func4, 11, 22, n);
    f4();   // same as call func4(11, 22, 30)
}

void test4_3()
{
    int n = 30;
    auto f4 = std::bind(func4, 11, 22, ref(n));
    n = 33;
    f4();   // same as call func4(11, 22, n)
    cout << "n = " << n << endl;
}

void test4_4()
{
    const int n = 30;
    auto f4 = std::bind(func4, 11, 22, ref(n));
    //f4();   // ��������޷������� 3 �ӡ�const int��ת��Ϊ��int &��
}



void func5(int n1, int n2, const int& n3)
{
    cout << n1 << ' ' << n2 << ' ' << n3 << endl;
}


int main(int argc, char* argv[])
{
    test1_1();
    test1_2();
    putchar('\n');
    test2_1();
    test2_2();
    test2_3();
    putchar('\n');
    test3_1();
    test3_2();
    test3_3();
    putchar('\n');
    test4_1();
    test4_2();
    test4_3();
    test4_4();
    putchar('\n');
    func5(1, 2, 3);

    getchar();
    return 0;
}

/*
11 101 22
22 101 11

33 101 11
11 101 11


11 22 10
n = 33
11 22 30
11 22 33
n = 101

1 2 3
*/
