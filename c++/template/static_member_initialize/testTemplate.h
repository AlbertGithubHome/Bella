

template <typename T> class TestTemStatic  
{  
public:  
	static int knownTypeVar;  
	static T unKnownTypeVar;
	int n;
};  

// knownTypeVar变量有两种初始化方式

// 第一种
//template <> int TestTemStatic<int>::knownTypeVar=2;

// 第二种
template <typename T> int TestTemStatic<T>::knownTypeVar=50;


// unKnownTypeVar初始化方式
template <typename T> T TestTemStatic<T>::unKnownTypeVar=30;


class A
{
public:
	static int i;
	int m;
};

int A::i;