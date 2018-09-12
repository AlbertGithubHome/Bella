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
	unique_ptr<Example> ptr1(new Example(1));	// Example: 1(�������)
	if (ptr1.get())								// ����get�������ж��ڲ�ָ�����Ч��
	{
		ptr1.get()->test_print();				// in test print: number = 1(�������)
		ptr1->set_number(2);					// ������operator->
		(*ptr1).test_print();					// in test print: number = 2(�������)
	}

	if (ptr1)									// ����operator bool ����ڲ��������Ч��
		cout << "ptr1 is valid\n";				// ptr1 is valid(�������)

	Example *p = ptr1.release();				// ����release������ȡ���ڲ�����
	if (!ptr1)									// ����operator bool ����ڲ��������Ч��
		cout << "ptr1 is invalid\n";			// ptr1 is invalid(�������)

	ptr1.reset(p);								// ����reset���������������ڲ�����
	if (ptr1)									// ����operator bool ����ڲ��������Ч��
		cout << "ptr1 is valid\n";				// ptr1 is valid(�������)

	ptr1->test_print();							// in test print: number = 2(�������)
	unique_ptr<Example> ptr2(new Example(20));	// Example: 20(�������)

	ptr1.swap(ptr2);							// ����swap���������������ڲ�����
	ptr1->test_print();							// in test print: number = 20(�������)
	ptr2->test_print();							// in test print: number = 2(�������)

	ptr1.reset();								// ~Example: 20(�������)// �����ڲ���������
}												// ~Example: 2(�������) // ������������

// operator=
void test2()
{
	//unique_ptr<Example> ptr2 = new Example(2);// ������󣬲�֧��ԭʼָ�뵽����ָ�����ʽת��
	unique_ptr<Example> ptr2(new Example(2));	// Example: 2(�������)

	//unique_ptr<Example> ptr3 = ptr2;			// �������...: ����������ɾ���ĺ���
	//unique_ptr<Example> ptr4(ptr2);			// �������...: ����������ɾ���ĺ���
	unique_ptr<Example> ptr5(std::move(ptr2));	// �������룬ʹ��move�ƶ����壬����Ԥ��Ч��
	ptr5->test_print();							// in test print: number = 2(�������)
}												// ~Example: 2(�������) // ������������


void test3_inner1(unique_ptr<Example> ptr3_1)
{
	ptr3_1->test_print();						// in test print: number = 3��������ݣ�
}												// ~Example: 3(�������) // ������������

unique_ptr<Example> test3_inner2()
{
	unique_ptr<Example> ptr3_2(new Example(32));// Example:32��������ݣ�
	ptr3_2->test_print();						// in test print: number = 32��������ݣ�
	return ptr3_2;
}

void test3()
{
	unique_ptr<Example> ptr3(new Example(3));	// Example:3��������ݣ�
	ptr3->test_print();							// in test print: number = 3��������ݣ�
	
	//test3_inner1(ptr3);						// ֱ����Ϊ�������ݻᱨ�������,�����ڿ�������
	test3_inner1(std::move(ptr3));				// ���ǿ���ʹ��std::move���ƶ�������ʵ��

	if (!ptr3)
		cout << "ptr3 is invalid\n";			// ptr1 is valid(�������),�ƶ�֮��ptr3��Ч

	ptr3 = test3_inner2();						// ���ڲ�������ù�����߸�ֵ���˴�ʹ�����ƶ�����move
	ptr3->test_print();							// in test print: number = 32��������ݣ�
}												// ~Example: 32��������ݣ�,��������ptr3�ͷ��ڲ�����

void test4_inner1(unique_ptr<Example>* ptr4_1)
{
	(*ptr4_1)->test_print();					// in test print: number = 4��������ݣ�	
}												// ָ�봫��û������

void test4_inner2(unique_ptr<Example>& ptr4_2)
{
	ptr4_2->test_print();						// in test print: number = 4��������ݣ�
}												// ���ô���û������

void  test4()
{
	unique_ptr<Example> ptr4(new Example(4));	// Example:4��������ݣ�
	ptr4->test_print();							// in test print: number = 4��������ݣ�
	
	test4_inner1(&ptr4);						// ȡ��ַ��Ϊ����
	test4_inner2(ptr4);							// ������Ϊ����
}												// ~Example: 4��������ݣ�,��������ptr4�ͷ��ڲ�����
									
void test5()
{
	vector<unique_ptr<Example>> v(7);
	for (int i = 0; i < 6; i++)
	{
		v[i] = unique_ptr<Example>(new Example(50 + i)); // �������Example:70,...Example:75
	}
	
	// ֱ�Ӹ�ֵ����֮�ɹ������ǲ���operator=��,����ʵ���ϵ��õĻ���std::move���Ƶ��ƶ�����
	v[6] = unique_ptr<Example>(new Example(56));// Example:56��������ݣ�

	// ֱ�ӽ�unique_ptr����push_back
	v.push_back(unique_ptr<Example>(new Example(57)));	// Example:57��������ݣ�

	// �����ƶ�����push_back
	v.push_back(std::move(unique_ptr<Example>(new Example(58)))); // Example:58��������ݣ�

	// ����make_unique����unique_ptr,C++14��֧��
	v.push_back(make_unique<Example>(59));		// Example:59��������ݣ�
	

	 // ѭ������
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// �������in test print: number = 50....in test print: number = 59

}// �������~Example: 50,~Example: 51...~Example: 59


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

	unique_ptr<Example, custom_deleter> ptr6(new Example(6), dlter); // Example:6��������ݣ�
	ptr6->test_print();							// in test print: number = 6��������ݣ�

	unique_ptr<Example, custom_deleter> ptr7(new Example(7), ptr6.get_deleter()); // ����get_deleter

	// ��������ָ�룬�ڲ�����ʹ���Զ���ɾ����ɾ��
	ptr6.reset();								// �����use custom deleter, flag = 666~Example: 6
	ptr7->test_print();							// in test print: number = 7��������ݣ�
}												// �����use custom deleter, flag = 666~Example: 7


// operator=,operator*,operator bool,operator->,release,reset,swap,get,get_deleter
int main()
{
	test1();	// ���Գ��ú���operator*,operator bool,operator->,release,reset,swap,get

	test2();	// ���Գ��ú���operator=

	test3();	// ��Ϊ�������߷���ֵ

	test4();	// ָ���������������Ϊ����

	test5();	// ��Ϊ��������

	test6();	// ���Ժ���get_deleter

	getchar();
    return 0;
}

