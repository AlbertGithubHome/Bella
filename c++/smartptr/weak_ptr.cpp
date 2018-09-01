#include <iostream>
#include <memory>
using namespace std;

class CB;
class CA
{
public:
	CA() { cout << "CA() called! " << endl; }
	~CA() { cout << "~CA() called! " << endl; }
	void set_ptr(shared_ptr<CB>& ptr) { m_ptr_b = ptr; }
	void b_use_count() { cout << "b use count : " << m_ptr_b.use_count() << endl; }
	void show() { cout << "this is class CA!" << endl; }
private:
	shared_ptr<CB> m_ptr_b;
};

class CB
{
public:
	CB() { cout << "CB() called! " << endl; }
	~CB() { cout << "~CB() called! " << endl; }
	void set_ptr(shared_ptr<CA>& ptr) { m_ptr_a = ptr; }
	void a_use_count() { cout << "a use count : " << m_ptr_a.use_count() << endl; }
	void show() { cout << "this is class CB!" << endl; }
private:
	weak_ptr<CA> m_ptr_a;
};

void test_refer_to_each_other()
{
	shared_ptr<CA> ptr_a(new CA());
	shared_ptr<CB> ptr_b(new CB());

	cout << "a use count : " << ptr_a.use_count() << endl;
	cout << "b use count : " << ptr_b.use_count() << endl;

	ptr_a->set_ptr(ptr_b);
	ptr_b->set_ptr(ptr_a);


	cout << "a use count : " << ptr_a.use_count() << endl;
	cout << "b use count : " << ptr_b.use_count() << endl;
}

// 测试weak_ptr用法
void test1()
{
	// 编译错误 // error C2665: “std::weak_ptr<CA>::weak_ptr”: 3 个重载中没有一个可以转换所有参数类型
	// weak_ptr<CA> ptr_1(new CA());

	shared_ptr<CA> ptr_1(new CA());

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // 输出：ptr_1 use count : 1

	shared_ptr<CA> ptr_2 = ptr_1;

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // 输出：ptr_1 use count : 2
	cout << "ptr_2 use count : " << ptr_2.use_count() << endl; // 输出：ptr_1 use count : 2

	weak_ptr<CA> wk_ptr = ptr_1;

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // 输出：ptr_1 use count : 2
	cout << "ptr_2 use count : " << ptr_2.use_count() << endl; // 输出：ptr_1 use count : 2

	// 编译错误
	// error C2440 : “初始化”: 无法从“std::weak_ptr<CA>”转换为“std::shared_ptr<CA>”
	// shared_ptr<CA> ptr_3 = wk_ptr;
}

// 
// 测试weak_ptr常用函数用法
void test2()
{
	shared_ptr<CA> ptr_a(new CA());		// 输出：CA() called!
	shared_ptr<CB> ptr_b(new CB());		// 输出：CB() called!

	cout << "ptr_a use count : " << ptr_a.use_count() << endl; // 输出：ptr_a use count : 1
	cout << "ptr_b use count : " << ptr_b.use_count() << endl; // 输出：ptr_b use count : 1
	
	weak_ptr<CA> wk_ptr_a = ptr_a;
	weak_ptr<CB> wk_ptr_b = ptr_b;

	if (!wk_ptr_a.expired())
	{
		wk_ptr_a.lock()->show();		// 输出：this is class CA!
	}

	if (!wk_ptr_b.expired())
	{
		wk_ptr_b.lock()->show();		// 输出：this is class CB!
	}

	// 编译错误
	// 编译必须作用于相同的指针类型之间
	// wk_ptr_a.swap(wk_ptr_b);			// 调用交换函数

	wk_ptr_b.reset();					// 将wk_ptr_b的指向清空
	if (wk_ptr_b.expired())
	{
		cout << "wk_ptr_b is invalid" << endl;	// 输出：wk_ptr_b is invalid 说明改指针已经无效
	}

	wk_ptr_b = ptr_b;
	if (!wk_ptr_b.expired())
	{
		wk_ptr_b.lock()->show();		// 输出：this is class CB! 调用赋值操作后，wk_ptr_b恢复有效
	}

	// 编译错误
	// 编译必须作用于相同的指针类型之间
	// wk_ptr_b = wk_ptr_a;


	// 最后输出的引用计数还是1，说明之前使用weak_ptr类型赋值，不会影响引用计数
	cout << "ptr_a use count : " << ptr_a.use_count() << endl; // 输出：ptr_a use count : 1
	cout << "ptr_b use count : " << ptr_b.use_count() << endl; // 输出：ptr_b use count : 1
}

int main(int argc, char* argv[])
{

	test_refer_to_each_other();

	test1();

	test2();

	getchar();
	return 0;
}
