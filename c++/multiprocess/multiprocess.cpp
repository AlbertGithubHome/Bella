#include <unistd.h>
#include <stdlib.h>

int main ()
{
    pid_t pid; //pid表示fork函数返回的值，会根据不同进程返回不同值
    pid = fork();
    if (pid < 0)
    {
        exit(-1);
    }
    else if (pid == 0) // 子进程返回pid为0
    {
        unsigned int u = 0;
        while(true)
        {
            ++u;
            sleep(1);
        }
    }
    else // 父进程返回pid为子进程的id，大于0
    {
        exit(1);
    }
    return 0;
}