#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
    cout << "PERFECTION OUTPUT" << endl;
    int nNum;
    while((cin >> nNum) && nNum)
    {
        cout << setw(5) << setfill(' ') << right << nNum << "  ";// 先输出数字
        const int nLoopLimit = (int)sqrt((double)nNum);
        int nSum = 0;

        if (nNum == 1)
        {
            cout << "DEFICIENT" << endl;
            continue;
        }

        for (int nDivisor = 1; nDivisor <= nLoopLimit; ++nDivisor)
        {
            if (nNum % nDivisor != 0)
                continue;

            nSum += nDivisor;

            if (nDivisor * nDivisor != nNum && nDivisor != 1)
                nSum += (nNum / nDivisor);

            if (nSum > nNum)
                break;
        }

        if (nSum == nNum)
            cout << "PERFECT" << endl;
        else if (nSum < nNum)
            cout << "DEFICIENT" << endl;
        else
            cout << "ABUNDANT" << endl;
    }
    cout << "END OF OUTPUT" << endl;

    return 0;
}