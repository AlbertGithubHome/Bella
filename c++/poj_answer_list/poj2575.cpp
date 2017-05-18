#include <iostream>
#include <cmath>
using namespace std;

#define SEQUENCE_COUNT  3000
char flag[SEQUENCE_COUNT] = {0};

int main()
{
    int N;                  // 序列中数字的个数
    int nNum, nNextNum;     // 连续的两个数字

    while ((cin >> N) && N)
    {
        cin >> nNum;
        if (N == 1)
        {
            cout << "Jolly" << endl;
            continue;
        }

        memset(flag, 0, sizeof(flag));
        for (int nIndex = 2; nIndex <= N; ++nIndex)
        {
            cin >> nNextNum;
            int nDiff = abs(nNextNum - nNum);
            if (nDiff < SEQUENCE_COUNT)
                flag[nDiff] = 1;

            nNum = nNextNum;
        }

        int nFlagIndex = 1;
        for (; nFlagIndex < N; ++nFlagIndex)
        {
            if (flag[nFlagIndex] <= 0)
            {
                cout << "Not jolly" << endl;
                break;
            }
        }

        if (nFlagIndex == N)
            cout << "Jolly" << endl;
    }

    return 0;
}

