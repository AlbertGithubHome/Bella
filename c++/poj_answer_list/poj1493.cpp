#include <iostream>
#include <cstring>
using namespace std;

#define STRING_LEN 26
char szInputMsg[STRING_LEN] = {0};

int main()
{
    int N;
    while((cin >> N) && N)
    {
        cin.get();  // 去除'\n'
        int nTotalSapce = 0;
        int nMinLineSapce = STRING_LEN;
        for (int nLine = 0; nLine < N; ++nLine)
        {
            cin.getline(szInputMsg, STRING_LEN);
            int nLineSpaceCount = 0;
            for (int nIndex = 0; nIndex < STRING_LEN - 1; ++nIndex)
            {
                if (szInputMsg[nIndex] == ' ')
                    ++nLineSpaceCount;
                else if (nLineSpaceCount > 0)
                    break;
            }
            nTotalSapce += nLineSpaceCount;

            if (nLineSpaceCount < nMinLineSapce)
                nMinLineSapce = nLineSpaceCount;
        }
        cout << nTotalSapce - (N * nMinLineSapce) << endl;
    }

    return 0;
}