#include <iostream>
#include <cstring>
using namespace std;

#define LEN 100
int flag[LEN] = {0};

int main()
{
    int N, Q, M, m;
    while((cin >> N >> Q) && (N || Q))
    {
        int nMax = -1;
        int index = 0;
        memset(flag, 0, sizeof(flag));

        while (N--)
        {
            cin >> M;
            while (M--)
            {
                cin >> m;
                flag[m]++;

                if (flag[m] > nMax || (flag[m] == nMax && m < index))
                {
                    nMax = flag[m];
                    index = m;
                }
            }
        }
        cout << (nMax >= Q ? index : 0) << endl;
    }
    return 0;
}