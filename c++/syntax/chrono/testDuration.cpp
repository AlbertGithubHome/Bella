#include <chrono>
#include <iostream>
int main()
{
    // 以下为5分钟表达
    std::chrono::minutes minute1{5}; // 5个1分钟
    std::chrono::duration<int, std::ratio<5*60, 1>> minute2{1}; // 1个5分钟
    std::chrono::duration<double, std::ratio<2*60, 1>> minute3{2.5}; // 2.5个2分钟

    std::cout <<  "minutes1 duration has " << minute1.count() << " ticks\n"
              <<  "minutes2 duration has " << minute2.count() << " ticks\n"
              <<  "minutes3 duration has " << minute3.count() << " ticks\n";

    // 一下为12小时表达
    std::chrono::hours hours1{12}; // 12个1小时
    std::chrono::duration<double, std::ratio<60*60*24, 1>> hours2{0.5}; // 0.5个1天

    std::cout <<  "hours1 duration has " << hours1.count() << " ticks\n"
              <<  "hours2 duration has " << hours2.count() << " ticks\n";

    // 使用 std::chrono::duration_cast<T> 将分钟间隔转化成标准秒间隔
    std::cout <<  "minutes1 duration has " <<
        std::chrono::duration_cast<std::chrono::seconds>(minute1).count() << " ticks\n";
}