#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

#define PI  3.141592653
#define NAIL_COUNT  100
double arNailPos[NAIL_COUNT][NAIL_COUNT] = {0};

double GetLenByPos(double x1, double y1, double x2, double y2)
{
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

int main()
{
    int N;                  // 钉子数
    double dR;              // 钉子半径
    double dRopeLength = 0; // 绳子长度
    cin >> N >> dR;
    cin >> arNailPos[0][0] >> arNailPos[0][1];

    for (int nIndex = 1; nIndex < N; ++nIndex)
    {
        cin >> arNailPos[nIndex][0] >> arNailPos[nIndex][1];
        dRopeLength += GetLenByPos(arNailPos[nIndex - 1][0], arNailPos[nIndex - 1][1], arNailPos[nIndex][0], arNailPos[nIndex][1]);
    }

    dRopeLength += GetLenByPos(arNailPos[N - 1][0], arNailPos[N - 1][1], arNailPos[0][0], arNailPos[0][1]);
    dRopeLength += 2 * PI * dR;

    cout.setf(ios::fixed);  
    cout << fixed << setprecision(2) << dRopeLength << endl; // 输出绳子长度保留2位小数，不足两位填充0

    return 0;
}