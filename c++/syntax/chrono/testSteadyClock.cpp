#include <chrono>
#include <iostream>
int main()
{
    // 先记录程序运行时间
    std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();

    volatile int nDstVal, nSrcVal;
    for (int i = 0; i < 1000000000; ++i)
        nDstVal = nSrcVal;

    // 做差值计算耗时
    std::chrono::duration<double> duration_cost = std::chrono::duration_cast<
        std::chrono::duration<double> >(std::chrono::steady_clock::now() - start);
    std::cout <<  "total cost " << duration_cost.count() << " seconds." << std::endl;

    return 0;
}