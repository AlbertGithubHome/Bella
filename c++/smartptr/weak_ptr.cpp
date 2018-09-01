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

// ����weak_ptr�÷�
void test1()
{
	// ������� // error C2665: ��std::weak_ptr<CA>::weak_ptr��: 3 ��������û��һ������ת�����в�������
	// weak_ptr<CA> ptr_1(new CA());

	shared_ptr<CA> ptr_1(new CA());

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // �����ptr_1 use count : 1

	shared_ptr<CA> ptr_2 = ptr_1;

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // �����ptr_1 use count : 2
	cout << "ptr_2 use count : " << ptr_2.use_count() << endl; // �����ptr_1 use count : 2

	weak_ptr<CA> wk_ptr = ptr_1;

	cout << "ptr_1 use count : " << ptr_1.use_count() << endl; // �����ptr_1 use count : 2
	cout << "ptr_2 use count : " << ptr_2.use_count() << endl; // �����ptr_1 use count : 2

	// �������
	// error C2440 : ����ʼ����: �޷��ӡ�std::weak_ptr<CA>��ת��Ϊ��std::shared_ptr<CA>��
	// shared_ptr<CA> ptr_3 = wk_ptr;
}

// 
// ����weak_ptr���ú����÷�
void test2()
{
	shared_ptr<CA> ptr_a(new CA());		// �����CA() called!
	shared_ptr<CB> ptr_b(new CB());		// �����CB() called!

	cout << "ptr_a use count : " << ptr_a.use_count() << endl; // �����ptr_a use count : 1
	cout << "ptr_b use count : " << ptr_b.use_count() << endl; // �����ptr_b use count : 1
	
	weak_ptr<CA> wk_ptr_a = ptr_a;
	weak_ptr<CB> wk_ptr_b = ptr_b;

	if (!wk_ptr_a.expired())
	{
		wk_ptr_a.lock()->show();		// �����this is class CA!
	}

	if (!wk_ptr_b.expired())
	{
		wk_ptr_b.lock()->show();		// �����this is class CB!
	}

	// �������
	// ���������������ͬ��ָ������֮��
	// wk_ptr_a.swap(wk_ptr_b);			// ���ý�������

	wk_ptr_b.reset();					// ��wk_ptr_b��ָ�����
	if (wk_ptr_b.expired())
	{
		cout << "wk_ptr_b is invalid" << endl;	// �����wk_ptr_b is invalid ˵����ָ���Ѿ���Ч
	}

	wk_ptr_b = ptr_b;
	if (!wk_ptr_b.expired())
	{
		wk_ptr_b.lock()->show();		// �����this is class CB! ���ø�ֵ������wk_ptr_b�ָ���Ч
	}

	// �������
	// ���������������ͬ��ָ������֮��
	// wk_ptr_b = wk_ptr_a;


	// �����������ü�������1��˵��֮ǰʹ��weak_ptr���͸�ֵ������Ӱ�����ü���
	cout << "ptr_a use count : " << ptr_a.use_count() << endl; // �����ptr_a use count : 1
	cout << "ptr_b use count : " << ptr_b.use_count() << endl; // �����ptr_b use count : 1
}

int main(int argc, char* argv[])
{

	test_refer_to_each_other();

	test1();

	test2();

	getchar();
	return 0;
}
