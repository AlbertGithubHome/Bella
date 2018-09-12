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

// operator*,operator bool,operator->,release,reset,swap,get
void test1()
{
	unique_ptr<Example> ptr1(new Example(1));	// Example: 1(输出内容)
	if (ptr1.get())								// 调用get函数，判断内部指针的有效性
	{
		ptr1.get()->test_print();				// in test print: number = 1(输出内容)
		ptr1->set_number(2);					// 调用了operator->
		(*ptr1).test_print();					// in test print: number = 2(输出内容)
	}

	if (ptr1)									// 调用operator bool 检测内部对象的有效性
		cout << "ptr1 is valid\n";				// ptr1 is valid(输出内容)

	Example *p = ptr1.release();				// 调用release函数，取出内部对象
	if (!ptr1)									// 调用operator bool 检测内部对象的有效性
		cout << "ptr1 is invalid\n";			// ptr1 is invalid(输出内容)

	ptr1.reset(p);								// 调用reset函数，重新设置内部对象
	if (ptr1)									// 调用operator bool 检测内部对象的有效性
		cout << "ptr1 is valid\n";				// ptr1 is valid(输出内容)

	ptr1->test_print();							// in test print: number = 2(输出内容)
	unique_ptr<Example> ptr2(new Example(20));	// Example: 20(输出内容)

	ptr1.swap(ptr2);							// 调用swap函数，重新设置内部对象
	ptr1->test_print();							// in test print: number = 20(输出内容)
	ptr2->test_print();							// in test print: number = 2(输出内容)

	ptr1.reset();								// ~Example: 20(输出内容)// 重置内部对象被销毁
}												// ~Example: 2(输出内容) // 出作用域被析构

// operator=
void test2()
{
	//unique_ptr<Example> ptr2 = new Example(2);// 编译错误，不支持原始指针到智能指针的隐式转换
	unique_ptr<Example> ptr2(new Example(2));	// Example: 2(输出内容)

	//unique_ptr<Example> ptr3 = ptr2;			// 编译错误，...: 尝试引用已删除的函数
	//unique_ptr<Example> ptr4(ptr2);			// 编译错误，...: 尝试引用已删除的函数
	unique_ptr<Example> ptr5(std::move(ptr2));	// 正常编译，使用move移动语义，符合预期效果
	ptr5->test_print();							// in test print: number = 2(输出内容)
}												// ~Example: 2(输出内容) // 出作用域被析构


void test3_inner1(unique_ptr<Example> ptr3_1)
{
	ptr3_1->test_print();						// in test print: number = 3（输出内容）
}												// ~Example: 3(输出内容) // 出作用域被析构

unique_ptr<Example> test3_inner2()
{
	unique_ptr<Example> ptr3_2(new Example(32));// Example:32（输出内容）
	ptr3_2->test_print();						// in test print: number = 32（输出内容）
	return ptr3_2;
}

void test3()
{
	unique_ptr<Example> ptr3(new Example(3));	// Example:3（输出内容）
	ptr3->test_print();							// in test print: number = 3（输出内容）
	
	//test3_inner1(ptr3);						// 直接作为参数传递会报编译错误,不存在拷贝构造
	test3_inner1(std::move(ptr3));				// 但是可以使用std::move的移动语义来实现

	if (!ptr3)
		cout << "ptr3 is invalid\n";			// ptr1 is valid(输出内容),移动之后ptr3无效

	ptr3 = test3_inner2();						// 由于不允许调用构造或者赋值，此处使用了移动语义move
	ptr3->test_print();							// in test print: number = 32（输出内容）
}												// ~Example: 32（输出内容）,出定义域ptr3释放内部对象

void test4_inner1(unique_ptr<Example>* ptr4_1)
{
	(*ptr4_1)->test_print();					// in test print: number = 4（输出内容）	
}												// 指针传递没有析构

void test4_inner2(unique_ptr<Example>& ptr4_2)
{
	ptr4_2->test_print();						// in test print: number = 4（输出内容）
}												// 引用传递没有析构

void  test4()
{
	unique_ptr<Example> ptr4(new Example(4));	// Example:4（输出内容）
	ptr4->test_print();							// in test print: number = 4（输出内容）
	
	test4_inner1(&ptr4);						// 取地址作为参数
	test4_inner2(ptr4);							// 引用作为参数
}												// ~Example: 4（输出内容）,出定义域ptr4释放内部对象
									
void test5()
{
	vector<unique_ptr<Example>> v(7);
	for (int i = 0; i < 6; i++)
	{
		v[i] = unique_ptr<Example>(new Example(50 + i)); // 依次输出Example:70,...Example:75
	}
	
	// 直接赋值，迷之成功，不是不能operator=吗,这里实际上调用的还是std::move类似的移动语义
	v[6] = unique_ptr<Example>(new Example(56));// Example:56（输出内容）

	// 直接将unique_ptr对象push_back
	v.push_back(unique_ptr<Example>(new Example(57)));	// Example:57（输出内容）

	// 利用移动语义push_back
	v.push_back(std::move(unique_ptr<Example>(new Example(58)))); // Example:58（输出内容）

	// 利用make_unique创建unique_ptr,C++14才支持
	v.push_back(make_unique<Example>(59));		// Example:59（输出内容）
	

	 // 循环调用
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// 依次输出in test print: number = 50....in test print: number = 59

}// 依次输出~Example: 50,~Example: 51...~Example: 59


// a custom deleter
class custom_deleter {  
	int flag;
public:
	custom_deleter(int val) : flag(val) {}
	
	template <class T>
	void operator()(T* p) 
	{
		std::cout << "use custom deleter, flag=" << flag ;
		delete p;
	}
};

void test6()
{
	custom_deleter dlter(666);

	unique_ptr<Example, custom_deleter> ptr6(new Example(6), dlter); // Example:6（输出内容）
	ptr6->test_print();							// in test print: number = 6（输出内容）

	unique_ptr<Example, custom_deleter> ptr7(new Example(7), ptr6.get_deleter()); // 调用get_deleter

	// 重置智能指针，内部对象使用自定义删除器删除
	ptr6.reset();								// 输出：use custom deleter, flag = 666~Example: 6
	ptr7->test_print();							// in test print: number = 7（输出内容）
}												// 输出：use custom deleter, flag = 666~Example: 7


// operator=,operator*,operator bool,operator->,release,reset,swap,get,get_deleter
int main()
{
	test1();	// 测试常用函数operator*,operator bool,operator->,release,reset,swap,get

	test2();	// 测试常用函数operator=

	test3();	// 作为参数或者返回值

	test4();	// 指针或者引用类型作为参数

	test5();	// 作为容器参数

	test6();	// 测试函数get_deleter

	getchar();
    return 0;
}

