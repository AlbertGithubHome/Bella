// linuxtraceback.cpp : 定义控制台应用程序的入口点。
//

#include <execinfo.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>

#define STACK_INFO_LEN  1024

void ShowTraceStack(const char* szBriefInfo)
{
    static const int MAX_STACK_FRAMES = 12;
    void *pStack[MAX_STACK_FRAMES];
    static char szStackInfo[STACK_INFO_LEN * MAX_STACK_FRAMES];

    char ** pStackList = NULL;
    int frames = backtrace(pStack, MAX_STACK_FRAMES);
    pStackList = backtrace_symbols(pStack, frames);
    if (NULL == pStackList)
        return;

    strcpy(szStackInfo, szBriefInfo == NULL ? "stack traceback:\n" : szBriefInfo);
    for (int i = 0; i < frames; ++i)
    {
        if (NULL == pStackList[i])
            break;

        strncat(szStackInfo, pStackList[i], STACK_INFO_LEN);
        strcat(szStackInfo, "\n");
    }

    printf("%s", szStackInfo); // 输出到控制台，也可以打印到日志文件中
}

void func2()
{
    bool isError = true;
    if (isError)
    {
        ShowTraceStack("error in func2\n");
    }
    else
    {
        printf("this is func2\n");
    }
}

void func1()
{
    int sum = 0;
    for (int i = 0; i < 100; ++i)
        sum += i;

    func2();
}


int main(int argc, char* argv[])
{
    printf("hello world\n");
    func1();

    return 0;
}
