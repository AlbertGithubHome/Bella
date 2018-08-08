// auto_ptr.cpp : �������̨Ӧ�ó������ڵ㡣
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
	auto_ptr<Example> ptr1(new Example(6));		// Example: 6(�������)
	if (ptr1.get())								// �ж��ڲ�ָ�����Ч��
	{
		// ����Ϊ���ʳ�Ա��3�ַ���
		ptr1.get()->test_print();				// in test print: number = 6(�������)
		ptr1->set_number(8);
		(*ptr1).test_print();					// in test print: number = 8(�������)
	}
}												// ~Example: 8(�������) // ������������

void test2()
{
	//auto_ptr<Example> ptr2 = new Example(6);	// ������󣬲�֧�ֲ�ָͬ�뵽����ָ�����ʽת��
	auto_ptr<Example> ptr2(new Example(6));		// Example: 6(�������)
	if (ptr2.get())								// �ж��ڲ�ָ�����Ч��
	{
		ptr2.release();							// release��������֮����ͷ��ڴ������Ȩ�����ǲ��������ڲ����ڴ棬������ڴ�й©
		if (!ptr2.get())
			cout << "ptr2 is invalid" << endl;	// ptr2 is invalid(�������)

		ptr2.release();							// ��дһ��û���κ�����
	}

}												// ����ptr2�������򲻻�����Example

void test3()
{
	auto_ptr<Example> ptr3(new Example(3));		// Example: 3(�������)
	if (ptr3.get())								// �ж��ڲ�ָ�����Ч��
	{
		Example *p = ptr3.release();			// release��������֮����ͷ��ڴ������Ȩ�����ҷ���ԭʼָ��
		if (!ptr3.get())
			cout << "ptr3 is invalid" << endl;	// ptr3 is invalid(�������)

		delete p;								// ~Example: 3(�������) // ��������Example����
	}
}

void test4()
{
	auto_ptr<Example> ptr4(new Example(4));		// Example: 4(�������)
	cout << "after declare ptr4" << endl;		// after declare ptr4 
	ptr4.reset(new Example(5));					// Example: 5
												// ~Example: 4 
	cout << "after function reset" << endl;		// after function reset
}												// ~Example: 5(�������) // ��������Example����

void test5()
{
	auto_ptr<Example> ptr5(new Example(5));		// Example: 5(�������)
	auto_ptr<Example> ptr6 = ptr5;				// û�����

	if (ptr5.get())
		cout << "ptr5 is valid" << endl;		// û�������˵��ptr5�Ѿ���Ч������ٵ��þͻ����

	if (ptr6.get())
		cout << "ptr6 is valid" << endl;		// ptr6 is valid(�������)

	ptr6->test_print();							// in test print: number = 5(�������)
	//ptr5->test_print();						// ֱ�ӱ��� 
}

auto_ptr<Example> test6_inner()
{
	auto_ptr<Example> ptr6(new Example(6));		// Example: 6(�������)
	return ptr6;
}

void test6()
{
	auto_ptr<Example> ptr6 = test6_inner();		// ����auto_ptr���ͷ���ֵ
	ptr6->test_print();							// in test print: number = 6(�������)
}												// ~Example: 6(�������) // ��������Example����

void test7_inner(auto_ptr<Example> ptr7)
{
	ptr7->test_print();							// in test print: number = 6(�������)
}												// ~Example: 7(�������) // ��������Example����

void test7()
{
	auto_ptr<Example> ptr7(new Example(7));		// Example: 7(�������)
	test7_inner(ptr7);							// ���ݲ���
	//ptr7->test_print();							// ֱ�ӱ���
}

void test8()
{
	Example *p = new Example(8);				// Example: 7(�������)	
	auto_ptr<Example> ptr8(p);
	auto_ptr<Example> ptr9(p);
}												//~Example: 8(�������) // ��������Example����
												//~Example: -572662307(�������) // �ڶ�����������



/*/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/bits/stl_construct.h:73: ���󣺶ԡ�std::auto_ptr<Example>::auto_ptr(const std::auto_ptr<Example>&)���ĵ���û��ƥ��ĺ���
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:258: ��ע����ѡΪ�� std::auto_ptr<_Tp>::auto_ptr(std::auto_ptr_ref<_Tp>) [with _Tp = Example]
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:110: ��ע��         std::auto_ptr<_Tp>::auto_ptr(std::auto_ptr<_Tp>&) [with _Tp = Example]
/usr/lib/gcc/x86_64-redhat-linux/4.4.7/../../../../include/c++/4.4.7/backward/auto_ptr.h:101: ��ע��         std::auto_ptr<_Tp>::auto_ptr(_Tp*) [with _Tp = Example]
*/
void test9()
{
	vector<auto_ptr<Example>> v(10);
	int i = 0;
	for (; i < 10; i++)
	{
		v[i] = auto_ptr<Example>(new Example(i));// windows���������졢������linux���޷�ͨ������
	}
}

void test10_inner(auto_ptr<Example>& ptr10)
{
	ptr10->test_print();						// in test print: number = 6(�������)
}												// ����û������

void test10()
{
	auto_ptr<Example> ptr10(new Example(10));	// Example: 10(�������)
	test10_inner(ptr10);						// �������ò���
	ptr10->test_print();						// in test print: number = 10(�������)
}												//~Example: 10(�������) // ��������Example����

void test11_inner(auto_ptr<Example>* ptr11)
{
	(*ptr11)->test_print();						// in test print: number = 11(�������)
}												// ����û������

void test11()
{
	auto_ptr<Example> ptr11(new Example(11));	// Example:11(�������)
	test11_inner(&ptr11);						// ���ݵ�ַ����
	ptr11->test_print();						// in test print: number = 11(�������)
}												// ~Example: 11(�������) // ��������Example����

// һ��6������
// get release reset operator* operator-> operator=
int main()
{
	test1(); // ���Ժ���get operator* operator-> 

	test2(); // ���Ժ���release�����÷�

	test3(); // ���Ժ���release��ȷ�÷�

	test4(); // ���Ժ���reset�÷� 

	test5(); // ���Ժ���operator=�÷� 

	test6(); // ����auto_ptr���ͷ���ֵ

	test7(); // ����auto_ptr��Ϊ����

	//test8(); // ����auto_ptr����һ��ָ��

	test9(); // ����auto_ptr��Ϊ����Ԫ��

	test10();// ����auto_ptr��������Ϊ��������

	test11();// ����auto_ptr��ָ����Ϊ��������

    return 0;
}

