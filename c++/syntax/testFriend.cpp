// testFriend.cpp : 定义控制台应用程序的入口点。
//

#include<iostream>
using namespace std;
class M
{
private:
    int a[2][3];
public:
    M();
    M operator+(M &m2)
    {
        M m1;
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                m1.a[i][j] = a[i][j] + m2.a[i][j];
            }
        }
        return m1;
    }
    friend ostream & operator<<(ostream& cin, M& m);
    friend istream & operator >> (istream&, M& m);
};
M::M()
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            a[i][j] = 0;
        }
    }
}

istream & operator >> (istream& cin, M& m)
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> m.a[i][j];
        }
    }
    return cin;
}
ostream & operator<<(ostream& cout, M& m)
{
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << m.a[i][j] << " ";
        }
        cout << endl;
    }
    return cout;
}

int main()
{
    M a, b, c;
    cin >> a;
    cin >> b;
    c = a + b;
    cout << c << endl;
    system("pause");
    return 0;
}

