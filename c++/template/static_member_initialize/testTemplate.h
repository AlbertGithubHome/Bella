

template <typename T> class TestTemStatic  
{  
public:  
	static int knownTypeVar;  
	static T unKnownTypeVar;
	int n;
};  

// knownTypeVar���������ֳ�ʼ����ʽ

// ��һ��
//template <> int TestTemStatic<int>::knownTypeVar=2;

// �ڶ���
template <typename T> int TestTemStatic<T>::knownTypeVar=50;


// unKnownTypeVar��ʼ����ʽ
template <typename T> T TestTemStatic<T>::unKnownTypeVar=30;


class A
{
public:
	static int i;
	int m;
};

int A::i;