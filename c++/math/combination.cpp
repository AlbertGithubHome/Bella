#include <iostream>
#include <vector>
#include <map>
using namespace std;

int C1(int a, int b)
{
    int ans = 1;
    for (int i = a; i > a - b; i--) ans *= i;
    for (int i = b; i > 1; i--) ans /= i;
    return ans;
}

int C2(int n, int m)
{
    int a = 1, b = 1, c = 1;
    for (int i = n; i >= 1; --i) a *= i;
    for (int i = m; i >= 1; --i) b *= i;
    for (int i = n-m; i >= 1; --i) c *= i;
    return a/(b*c);
}

int C3(int n, int m)
{
    int a = 1, b = 1;
    for (int i = n; i > n - m; --i) a *= i;
    for (int i = m; i >= 1; i--) b *= i;
    return a/b;
}

int C4(int n, int m)
{
    if (n == m || m == 0) return 1;
    return C4(n-1, m) + C4(n-1, m-1);
}

int C5(int n, int m, map<int, int>& memo)
{
    if (n == m || m == 0) return 1;

    auto itora = memo.find((n-1)*10000+m);
    int a = itora != memo.end() ? itora->second : C4(n-1, m);
    if (itora == memo.end()) memo[(n-1)*10000+m] = a;

    auto itorb = memo.find((n-1)*10000+m-1);
    int b = itorb != memo.end() ? itorb->second : C4(n-1, m-1);
    if (itorb == memo.end()) memo[(n-1)*10000+m-1] = b;

    return a + b;
}

int C6(int n, int m)
{
    if (n == m || m == 0) return 1;

    vector<vector<int>> dp(n+1, vector<int>(m+1));
    for (int i = 0; i <= n; i++)
        for (int j = 0; j <= i && j <= m; j++)
            if (i == j || j == 0) dp[i][j] = 1;
            else dp[i][j] = dp[i-1][j] + dp[i-1][j-1];

    return dp[n][m];
}

int C7(int n, int m)
{
    if (n == m || m == 0) return 1;

    vector<int> dp(m+1);
    for (int i = 0; i <= n; i++)
        for (int j = min(i, m); j >= 0; j--)
            if (i == j || j == 0) dp[j] = 1;
            else dp[j] = dp[j] + dp[j-1];

    return dp[m];
}

int C8(int n, int m)
{
    if (n == m || m == 0) return 1;
    return C8(n, m-1) * (n-m+1) / m;
}

int C9(int n, int m)
{
    if (n == m || m == 0) return 1;

    int ans = 1;
    m = min(m, n-m);

    for (int i = 1; i <= m; i++) ans = ans * (n-i+1) / i;
    return ans;
}


int main()
{
    int n = 5, m = 2;
    cout << "C1 = " << C1(n, m) << endl;
    cout << "C2 = " << C2(n, m) << endl;
    cout << "C3 = " << C3(n, m) << endl;
    cout << "C4 = " << C4(n, m) << endl;

    map<int, int> memo;
    cout << "C5 = " << C5(n, m, memo) << endl;
    cout << "C6 = " << C6(n, m) << endl;
    cout << "C7 = " << C7(n, m) << endl;
    cout << "C8 = " << C8(n, m) << endl;
    cout << "C9 = " << C9(n, m) << endl;

    return 0;
}

