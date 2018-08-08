// auto_ptr.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <memory>
#include <vector>
using namespace std;


class Example
{
public:
	Example(int param = 0)
	{
		number = param;
		cout << "Example: " << number << endl;
	}

	~Example() { cout << "~Example: " << number << endl; }

	void test_print() { cout << "in test print: number = " << number << endl; }

	void set_number(int num) { number = num; }

private:
	int number;
};

void test1()
{
	auto_ptr<Example> ptr1(new Example(6));		// Example: 6(输出内容)
	if (ptr1.get())								// 判断内部指针的有效性
	{
		// 以下为访问成员的3种方法
		ptr1.get()->test_print();				// in test print: number = 6(输出内容)
		ptr1->set_number(8);
		(*ptr1).test_print();					// in test print: number = 8(输出内容)
	}
}												// ~Example: 8(输出内容) // 出作用域被析构

void test2()
{
	//auto_ptr<Example> ptr2 = new Example(6);	// 编译错误，不支持不同指针到智能指针的隐式转换
	auto_ptr<Example> ptr2(new Example(6));		// Example: 6(输出内容)
	if (ptr2.get())								// 判断内部指针的有效性
	{
		ptr2.release();							// release函数调用之后会释放内存的所有权，但是不会析构内部的内存，会造成内存泄漏
		if (!ptr2.get())
			cout << "ptr2 is invalid" << endl;	// ptr2 is invalid(输出内容)

		ptr2.release();							// 多写一遍没有任何作用
	}

}												// 出了ptr2的作用域不会析构Example

void test3()
{
	auto_ptr<Example> ptr3(new Example(3));		// Example: 3(输出内容)
	if (ptr3.get())								// 判断内部指针的有效性
	{
		Example *p = ptr3.release();			// release函数调用之后会释放内存的所有权，并且返回原始指针
		if (!ptr3.get())
			cout << "ptr3 is invalid" << endl;	// ptr3 is invalid(输出内容)

		delete p;								// ~Example: 3(输出内容) // 主动析构Example对象
	}
}

void test4()
{
	auto_ptr<Example> ptr4(new Example(4));		// Example: 4(输出内容)
	cout << "after declare ptr4" << endl;		// after declare ptr4 
	ptr4.reset(new Example(5));					// Example: 5
												// ~Example: 4 
	cout << "after function reset" << endl;		// after function reset
}												// ~Example: 5(输出内容) // 主动析构Example对象

void test5()
{
	auto_ptr<Example> ptr5(new Example(5));		// Example: 5(输出内容)
	auto_ptr<Example> ptr6 = ptr5;				// 没有输出

	if (ptr5.get())
		cout << "ptr5 is valid" << endl;		// 没有输出，说明ptr5已经无效，如果再调用就会崩溃

	if (ptr6.get())
		cout << "ptr6 is valid" << endl;		// ptr6 is valid(输出内容)

	ptr6->test_print();							// in test print: number = 5(输出内容)
	//ptr5->test_print();						// 直接崩溃 
}

auto_ptr<Example> test6_inner()
{
	auto_ptr<Example> ptr6(new Example(6));		// Example: 6(输出内容)
	return ptr6;
}

void test6()
{
	auto_ptr<Example> ptr6 = test6_inner();		// 测试auto_ptr类型返回值
	ptr6->test_print();							// in test print: number = 6(输出内容)
}												// ~Example: 6(输出内容) // 主动析构Example对象

void test7_inner(auto_ptr<Example> ptr7)
{
	ptr7->test_print();							// in test print: number = 6(输出内容)
}												// ~Example: 7(输出内容) // 主动析构Example对象

void test7()
{
	auto_ptr<Example> ptr7(new Example(7));		// Example: 7(输出内容)
	test7_inner(ptr7);							// 传递参数
	//ptr7->test_print();							// 直接崩溃
}

void test8()
{
	Example *p = new Example(8);				// Example: 7(输出内容)	
	auto_ptr<Example> ptr8(p);
	auto_ptr<Example> ptr9(p);
}												//~Example: 8(输出内容) // 主动析构Example对象
												//~Example: -572662307(输出内容) // 第二次析构崩溃



/*/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/bits/stl_construct.h:73: 错误：对‘std::auto_ptr<Example>::auto_ptr(const std::auto_ptr<Example>&)’的调用没有匹配的函数
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:258: 附注：备选为： std::auto_ptr<_Tp>::auto_ptr(std::auto_ptr_ref<_Tp>) [with _Tp = Example]
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:110: 附注：         std::auto_ptr<_Tp>::auto_ptr(std::auto_ptr<_Tp>&) [with _Tp = Example]
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:101: 附注：         std::auto_ptr<_Tp>::auto_ptr(_Tp*) [with _Tp = Example]
*/
void test9()
{
	vector<auto_ptr<Example>> v(10);
	int i = 0;
	for (; i < 10; i++)
	{
		v[i] = auto_ptr<Example>(new Example(i));// windows下正常构造、析构，linux下无法通过编译
	}
}

void test10_inner(auto_ptr<Example>& ptr10)
{
	ptr10->test_print();						// in test print: number = 6(输出内容)
}												// 这里没有析构

void test10()
{
	auto_ptr<Example> ptr10(new Example(10));	// Example: 10(输出内容)
	test10_inner(ptr10);						// 传递引用参数
	ptr10->test_print();						// in test print: number = 10(输出内容)
}												//~Example: 10(输出内容) // 主动析构Example对象

void test11_inner(auto_ptr<Example>* ptr11)
{
	(*ptr11)->test_print();						// in test print: number = 11(输出内容)
}												// 这里没有析构

void test11()
{
	auto_ptr<Example> ptr11(new Example(11));	// Example:11(输出内容)
	test11_inner(&ptr11);						// 传递地址参数
	ptr11->test_print();						// in test print: number = 11(输出内容)
}												// ~Example: 11(输出内容) // 主动析构Example对象

// 一共6个函数
// get release reset operator* operator-> operator=
int main()
{
	test1(); // 测试函数get operator* operator-> 

	test2(); // 测试函数release错误用法

	test3(); // 测试函数release正确用法

	test4(); // 测试函数reset用法 

	test5(); // 测试函数operator=用法 

	test6(); // 测试auto_ptr类型返回值

	test7(); // 测试auto_ptr作为参数

	//test8(); // 两个auto_ptr管理一个指针

	test9(); // 测试auto_ptr作为容器元素

	test10();// 测试auto_ptr的引用作为参数传递

	test11();// 测试auto_ptr的指针作为参数传递

    return 0;
}

