#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <chrono>

using namespace std;

int main()
{

    chrono::system_clock::time_point start = chrono::system_clock::now();

    unsigned long long ul = 1234567890123456789;
    string base = "123456789012345678901234";
    map<string,int> mymap;

    int count = 0;
    for (int i = 10000000; i < 20000000; i+=50)
    {
        count++;
        stringstream ss;
        ss << i;
        string s = base + ss.str();
        //cout << s << endl;

        mymap.insert(make_pair(s, 1));
    }

    auto duration_cost = chrono::system_clock::now() - start;

    cout << chrono::duration_cast<chrono::microseconds>(duration_cost).count() << endl;
    //cout << ul << endl;
    //cout << count << endl;
    cout << mymap.size() << endl;

    map<string,int>::iterator itor = mymap.begin();
    cout << itor->first << endl;
    cout << itor->second << endl;

    cin >> count;

    return 0;
}