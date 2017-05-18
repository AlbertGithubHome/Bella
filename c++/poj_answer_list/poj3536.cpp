#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int n;          // 冰箱的容积
    cin >> n;
    const int nLoopLimit = (int)sqrt((double)n);
    int nValueA = 1, nValueB = 1, nValueC = 1, nSurface = 2147483647;

    for (int nA = 1; nA <= nLoopLimit; ++nA)
    {
        if (n % nA != 0)
            continue;

        const int nArea = n / nA;
        const int nLengthLimit = (int)sqrt((double)nArea);
        for(int nB = 1; nB <= nLengthLimit; ++nB)
        {
            if (nArea % nB != 0)
                continue;

            const int nC = nArea / nB;
            const int nCurSurface = nA * nB + nB * nC + nC* nA;
            if (nCurSurface >= nSurface)
                continue;

            nSurface = nCurSurface;
            nValueA = nA;
            nValueB = nB;
            nValueC = nC;
        }
    }

    cout << nValueA << " " << nValueB << " "<< nValueC << endl;
    return 0;
}