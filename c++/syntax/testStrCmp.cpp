// TestStr5.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <string.h>


int main()
{
    char szbuf1[32] = { 0 };
    char szbuf2[32] = "";
    char* p = "";

    if (szbuf1 == "")
        printf("1\n");

    if (szbuf2 == "")
        printf("2\n");

    if (p == "")
        printf("3\n");

    if (!strcmp(szbuf1,""))
        printf("4\n");

    if (!strcmp(szbuf2, ""))
        printf("5\n");

    return 0;
}

/*
3
4
5
*/

