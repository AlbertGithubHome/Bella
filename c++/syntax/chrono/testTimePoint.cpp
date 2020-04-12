#include <chrono>
#include <iostream>
int main()
{
    // 获得epoch 和 now 的时间点
    std::chrono::time_point<std::chrono::system_clock> epoch =
        std::chrono::time_point<std::chrono::system_clock>{};
    std::chrono::time_point<std::chrono::system_clock> now =
        std::chrono::system_clock::now();

    // 显示时间点对应的日期和时间
    time_t epoch_time = std::chrono::system_clock::to_time_t(epoch);
    std::cout << "epoch: " << std::ctime(&epoch_time);
    time_t today_time = std::chrono::system_clock::to_time_t(now);
    std::cout << "today: " << std::ctime(&today_time);

    // 显示duration的值
    std::cout << "seconds since epoch: "
        << std::chrono::duration_cast<std::chrono::seconds>(epoch.time_since_epoch()).count()
        << std::endl;

    std::cout << "today, ticks since epoch: "
        << now.time_since_epoch().count()
        << std::endl;

    std::cout << "today, hours since epoch: "
        << std::chrono::duration_cast<std::chrono::hours>(now.time_since_epoch()).count()
        << std::endl;

    return 0;
}