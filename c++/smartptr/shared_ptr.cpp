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
	//error C2440: ����ʼ����: �޷��ӡ�Example *��ת��Ϊ��std::shared_ptr<Example>��
	//shared_ptr<Example> ptr1 = new Example(1);

	shared_ptr<Example> ptr1(new Example(1));	// Example: 1��������ݣ�
	if (ptr1.get())								// ���ú���get����ȡԭʼָ�룬�ж���Ч��
	{
		cout << "ptr1 is valid" << endl;		// ԭʼָ����Ч
	}
	ptr1->test_print();			// in test print: number = 1��������ݣ�������operator->

	ptr1.reset();				// ~Example: 1��������ݣ�,���ú���reset������Ϊ�գ��ͷ�ԭ�ڲ�����

	ptr1.reset(new Example(2));	// Example: 2��������ݣ�,���������������

	(*ptr1).test_print();		// in test print: number = 1��������ݣ�������operator*
}								// ~Example: 1��������ݣ�,���������ͷ��ڲ�����

void test2()
{
    shared_ptr<Example> ptr2(new Example(2));   // Example: 2��������ݣ�
    if (ptr2)                                   // ����operator bool
        cout << "ptr2 is valid" << endl;        // ptr2 is valid��������ݣ���˵��ptr2����Ч��

    ptr2.reset();                               // ~Example: 2��������ݣ��������ڲ�����Ϊ��

    if (ptr2)                                   // ����operator bool
        cout << "ptr2 is valid" << endl;        // û�������˵��ptr2�Ѿ���Ч
} 

void test3()
{
	shared_ptr<Example> ptr3(new Example(3));	// Example: 3��������ݣ�
	shared_ptr<Example> ptr4(new Example(4));	// Example: 4��������ݣ�
	ptr3->test_print();				// in test print: number = 3��������ݣ�
	ptr4->test_print();				// in test print: number = 4��������ݣ�

	ptr3.swap(ptr4);				// ���ú���swap

	ptr3->test_print();				// in test print: number = 4��������ݣ�
	ptr4->test_print();				// in test print: number = 3��������ݣ�
}									// ~Example: 3��������ݣ�,���������ͷ��ڲ�����
									// ~Example: 4��������ݣ�,���������ͷ��ڲ�����

void test4()
{
	shared_ptr<Example> ptr4(new Example(4));	// Example: 4��������ݣ�
	if (ptr4.unique())
	{
		cout << "ptr4 is unique" << endl;		// ptr4 is unique��������ݣ�
		cout << "ptr4 use count : " << ptr4.use_count() << endl;// ptr4 use count : 1��������ݣ�
	}

	shared_ptr<Example> ptr5 = ptr4;
	if (ptr4)
		cout << "ptr4 is valid" << endl;// ptr4 is valid(������ݣ�˵����ֵ֮����������ָ�������Ч

	if (ptr5)
		cout << "ptr5 is valid" << endl;// ptr5 is valid(������ݣ�˵����ֵ֮����������ָ�������Ч

	if (ptr4.unique())
		cout << "ptr4 is unique" << endl;	// û�������˵��ptr4����Ψһ�����ڲ����������ָ����

	cout << "ptr4 use count : " << ptr4.use_count() << endl;	// ptr4 use count : 2��������ݣ�
	cout << "ptr5 use count : " << ptr5.use_count() << endl;	// ptr4 use count : 2��������ݣ�
}													// ~Example: 4��������ݣ�,���������ͷ��ڲ�����

void test5()
{
	Example *p = new Example(5);	// Example: 5��������ݣ�
	shared_ptr<Example> ptr5(p);
	shared_ptr<Example> ptr6(p);

	cout << "ptr4 use count : " << ptr5.use_count() << endl;// ptr4 use count : 1��������ݣ�
	cout << "ptr5 use count : " << ptr6.use_count() << endl;// ptr5 use count : 1��������ݣ�
}			// ~Example: 3��������ݣ�,��������ptr5�ͷ��ڲ�����
			// ~Example : -572662307��������ݣ�,��������ptr6�ͷ��ڲ����󣬳������

void test6_inner1(shared_ptr<Example> ptr6_1)
{
	ptr6_1->test_print();		// in test print: number = 6��������ݣ�
	cout << "ptr6_1 use count : " << ptr6_1.use_count() << endl;// ptr6 use count : 2��������ݣ�
}

shared_ptr<Example> test6_inner2()
{
	shared_ptr<Example> ptr6_2(new Example(62));	// Example:62��������ݣ�
	ptr6_2->test_print();			// in test print: number = 62��������ݣ�
	cout << "ptr6_2 use count : " << ptr6_2.use_count() << endl;// ptr6_2 use count : 1��������ݣ�
	return ptr6_2;
}

void test6()
{
	shared_ptr<Example> ptr6(new Example(6));	// Example:6��������ݣ�
	ptr6->test_print();			// in test print: number = 6��������ݣ�
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1��������ݣ�
	test6_inner1(ptr6);
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1��������ݣ�

	ptr6 = test6_inner2();		// ~Example: 6��������ݣ�,ptr6�ӹ��µĶ���ԭ����������
	cout << "ptr6 use count : " << ptr6.use_count() << endl;// ptr6 use count : 1��������ݣ�
}								// ~Example: 62��������ݣ�,��������ptr6�ͷ��ڲ�����

bool comp(shared_ptr<Example> a, shared_ptr<Example> b) // һ���д��ֻ���������ͣ�����Ϊ��˵���������������
{
	return a->get_number() > b->get_number();
}

void test7()
{
	vector<shared_ptr<Example>> v(10);
	for (int i = 0; i < 10; i++)
	{
		v[i] = shared_ptr<Example>(new Example(70+i));
	}// �������Example:70,Example:71,Example:72...Example:79

	// ѭ������
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// �������in test print: number = 70....in test print: number = 79

	sort(v.begin(), v.end(), comp); // ������������У�����ʹ��auto_ptr�����ĺ��ѿ�

	// ѭ������
	for (int i = 0; i < 10; i++)
	{
		v[i]->test_print();
	}// �������in test print: number = 79....in test print: number = 70
}// �������~Example: 79,~Example: 78...~Example: 70


void test8_inner1(shared_ptr<Example>* ptr8_1)
{
	(*ptr8_1)->test_print();	// in test print: number = 8��������ݣ�
	cout << "ptr8_1 use count : " << (*ptr8_1).use_count() << endl;// ptr8_1 use count : 1��������ݣ�
}

void test8_inner2(shared_ptr<Example>& ptr8_2)
{
	ptr8_2->test_print();	// in test print: number = 8��������ݣ�
	cout << "ptr8_2 use count : " << ptr8_2.use_count() << endl;// ptr8_2 use count : 1��������ݣ�
}

void  test8()
{
	shared_ptr<Example> ptr8(new Example(8));	// Example:8��������ݣ�
	ptr8->test_print();			// in test print: number = 8��������ݣ�
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1���������)
	test8_inner1(&ptr8);
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1���������)
	test8_inner2(ptr8);
	cout << "ptr8 use count : " << ptr8.use_count() << endl;// ptr8 use count : 1���������)
}											// ~Example: 8��������ݣ�,��������ptr8�ͷ��ڲ���

// һ��9������
// get reset swap unique use_count operator* operator-> operator=  operator bool
int main(int argc, char**argv)
{
	test1(); // ����get reset operator* operator->���� 

	test2(); // ����operator bool����

	test3(); // ����swap����

	test4(); // ���Ժ���unique use_count operator=

	//test5(); // ������ͬһ������ָ��������������

	test6(); // ������Ϊ���������ͷ���ֵ

	test7(); // ������Ϊ����Ԫ��

	test8(); // ����ʹ��ָ�����������Ϊ����

	getchar();
	return 0;
}