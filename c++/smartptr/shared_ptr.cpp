#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
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

	int  get_number() { return number; }

private:
	int number;
};

void test1()
{
	//error C2440: “初始化”: 无法从“Example *”转换为“std::shared_ptr<Example>”
	//shared_ptr<Example> ptr1 = new Example(1);

	shared_ptr<Example> ptr1(new Example(1));	// Example: 1（输出内容）
	if (ptr1.get())								// 调用函数get，获取原始指针，判断有效性
	{
		cout << "ptr1 is valid" << endl;		// 原始指针有效
	}
	ptr1->test_print();			// in test print: number = 1（输出内容），调用operator->

	ptr1.reset();				// ~Example: 1（输出内容）,调用函数reset，设置为空，释放原内部对象

	ptr1.reset(new Example(2));	// Example: 2（输出内容）,重新申请对象并设置

	(*ptr1).test_print();		// in test print: number = 1（输出内容），调用operator*
}								// ~Example: 1（输出内容）,出定义域，释放内部对象

void test2()
{
    shared_ptr<Example> ptr2(new Example(2));   // Example: 2（输出内容）
    if (ptr2)                                   // 调用operator bool
        cout << "ptr2 is valid" << endl;        // ptr2 is valid（输出内容），说明ptr2是有效的

    ptr2.reset();                               // ~Example: 2（输出内容），设置内部对象为空

    if (ptr2)                                   // 调用operator bool
        cout << "ptr2 is valid" << endl;        // 没有输出，说明ptr2已经无效
} 

void test3()
{
	shared_ptr<Example> ptr3(new Example(3));	// Example: 3（输出内容）
	shared_ptr<Example> ptr4(new Example(4));	// Example: 4（输出内容）
	ptr3->test_print();				// in test print: number = 3（输出内容）
	ptr4->test_print();				// in test print: number = 4（输出内容）

	ptr3.swap(ptr4);				// 调用函数swap

	ptr3->test_print();				// in test print: number = 4（输出内容）
	ptr4->test_print();				// in test print: number = 3（输出内容）
}									// ~Example: 3（输出内容）,出定义域，释放内部对象
									// ~Example: 4（输出内容）,出定义域，释放内部对象

void test4()
{
	shared_ptr<Example> ptr4(new Example(4));	// Example: 4（输出内容）
	if (ptr4.unique())
	{
		cout << "ptr4 is unique" << endl;		// ptr4 is unique（输出内容）
		cout << "ptr4 use count : " << ptr4.use_count() << endl;// ptr4 use count : 1（输出内容）
	}

	shared_ptr<Example> ptr5 = ptr4;
	if (ptr4)
		cout << "ptr4 is valid" << endl;// ptr4 is valid(输出内容）说明赋值之后两个智能指针对象都有效

	if (ptr5)
		cout << "ptr5 is valid" << endl;// ptr5 is valid(输出内容）说明赋值之后两个智能指针对象都有效

	if (ptr4.unique())
		cout << "ptr4 is unique" << endl;	// 没有输出，说明ptr4不是唯一管理内部对象的智能指针了

	cout << "ptr4 use count : " << ptr4.use_count() << endl;	// ptr4 use count : 2（输出内容）
	cout << "ptr5 use count : " << ptr5.use_count() << endl;	// ptr4 use count : 2（输出内容）
}													// ~Example: 4（输出内容）,出定义域，释放内部对象

void test5()
{
	Example *p = new Example(5);	// Example: 5（输出内容）
	shared_ptr<Example> ptr5(p);
	shared_ptr<Example> ptr6(p);

	cout << "ptr4 use count : " << ptr5.use_count() << endl;// ptr4 use count : 1（输出内容）
	cout << "ptr5 use count : " << ptr6.use_count() << endl;// ptr5 use count : 1（输出内容）
}			// ~Example: 3（输出内容）,出定义域，ptr5释放内部对象
			// ~Example : -572662307（输出内容）,出定义域，ptr6释放内部对象，程序崩溃

void test6_inner1(shared_ptr<Example> ptr6_1)
{
	ptr6_1->test_print();		// in test print: number = 6（输出内容）
	cout << "ptr6_1 use count : " << ptr6_1.use_count() << endl;// ptr6 use count : 2（输出内容）
}

shared_ptr<Example> test6_inner2()
{
	shared_ptr<Example> ptr6_2(new Example(62));	// Example:62（输出内容）
	ptr6_2->test_print();			// in test print: number = 62（输出内容）
	cout << "ptr6_2 use count : " << ptr6_2.use_count() << endl;// ptr6_2 use count : 1（输出内容）
	return ptr6_2;
}

void test6()
{
	shared_ptr<Example> ptr6(new Example(6));	// Example:6（输出内容）
	ptr6->test_print();			// in test print: number = 6（输出内容）
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1（输出内容）
	test6_inner1(ptr6);
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1（输出内容）

	ptr6 = test6_inner2();		// ~Example: 6（输出内容）,ptr6接管新的对象，原来对象被析构
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1（输出内容）
}								// ~Example: 62（输出内容）,出定义域，ptr6释放内部对象

bool comp(shared_ptr<Example> a, shared_ptr<Example> b) // 一般会写成只读引用类型，这里为了说明问题才这样定义
{
	return a->get_number() > b->get_number();
}

void test7()
{
	vector<shared_ptr<Example>> v(10);
	for (int i = 0; i < 10; i++)
	{
		v[i] = shared_ptr<Example>(new Example(70+i));
	}// 依次输出Example:70,Example:71,Example:72...Example:79

	// 循环调用
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// 依次输出in test print: number = 70....in test print: number = 79

	sort(v.begin(), v.end(), comp); // 这可以正常运行，但是使用auto_ptr会死的很难看

	// 循环调用
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// 依次输出in test print: number = 79....in test print: number = 70
}// 依次输出~Example: 79,~Example: 78...~Example: 70


void test8_inner1(shared_ptr<Example>* ptr8_1)
{
	(*ptr8_1)->test_print();	// in test print: number = 8（输出内容）
	cout << "ptr8_1 use count : " << (*ptr8_1).use_count() << endl;// ptr8_1 use count : 1（输出内容）
}

void test8_inner2(shared_ptr<Example>& ptr8_2)
{
	ptr8_2->test_print();	// in test print: number = 8（输出内容）
	cout << "ptr8_2 use count : " << ptr8_2.use_count() << endl;// ptr8_2 use count : 1（输出内容）
}

void  test8()
{
	shared_ptr<Example> ptr8(new Example(8));	// Example:8（输出内容）
	ptr8->test_print();			// in test print: number = 8（输出内容）
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1（输出内容)
	test8_inner1(&ptr8);
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1（输出内容)
	test8_inner2(ptr8);
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1（输出内容)
}											// ~Example: 8（输出内容）,出定义域，ptr8释放内部对

// 一共9个函数
// get reset swap unique use_count operator* operator-> operator=  operator bool
int main(int argc, char**argv)
{
	test1(); // 测试get reset operator* operator->函数 

	test2(); // 测试operator bool函数

	test3(); // 测试swap函数

	test4(); // 测试函数unique use_count operator=

	//test5(); // 测试用同一个对象指针生成两个对象

	test6(); // 测试作为函数参数和返回值

	test7(); // 测试作为容器元素

	test8(); // 测试使用指针或者引用作为参数

	getchar();
	return 0;
}