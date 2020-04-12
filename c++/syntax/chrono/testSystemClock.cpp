#include <chrono>
#include <iostream>
int main()
{
    std::chrono::duration<int, std::ratio<60*60*24> > one_day(1);

    // 根据时钟得到现在时间
    std::chrono::system_clock::time_point today = std::chrono::system_clock::now();
    std::time_t time_t_today = std::chrono::system_clock::to_time_t(today);
    std::cout <<  "now time stamp is " << time_t_today << std::endl;
    std::cout <<  "now time is " << ctime(&time_t_today) << std::endl;


    // 看看明天的时间
    std::chrono::system_clock::time_point tomorrow = today + one_day;
    std::time_t time_t_tomorrow = std::chrono::system_clock::to_time_t(tomorrow);
    std::cout <<  "tomorrow time stamp is " << time_t_tomorrow << std::endl;
    std::cout <<  "tomorrow time is " << ctime(&time_t_tomorrow) << std::endl;


    // 计算下个小时时间
    std::chrono::system_clock::time_point next_hour = today + std::chrono::hours(1);
    std::time_t time_t_next_hour = std::chrono::system_clock::to_time_t(next_hour);
    std::chrono::system_clock::time_point next_hour2 = std::chrono::system_clock::from_time_t(time_t_next_hour);

    std::time_t time_t_next_hour2 = std::chrono::system_clock::to_time_t(next_hour2);
    std::cout <<  "tomorrow time stamp is " << time_t_next_hour2 << std::endl;
    std::cout <<  "tomorrow time is " << ctime(&time_t_next_hour2) << std::endl;

    return 0;
}