// testVarAddr.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

int global_var = 1;
static int global_static = 2;

int _main()
{
    int local_var = 3;
    static int local_static = 4;

    printf("%d, %p\n", global_var, &global_var);
    printf("%d, %p\n", global_static, &global_static);
    printf("%d, %p\n", local_var, &local_var);
    printf("%d, %p\n", local_static, &local_static);
    getchar();
    return 0;
}

// ÿ����������ֻ�оֲ��Ǿ�̬�����ĵ�ַ�ڱ�
//1, 001E9000
//2, 001E9004
//3, 0099FE74
//4, 001E9008
//
//1, 001E9000
//2, 001E9004
//3, 012FFCE0
//4, 001E9008
//
//1, 001E9000
//2, 001E9004
//3, 007AFC20
//4, 001E9008

// ���±����ȫ����ַ�����仯�����ٴ�������Ȼֻ�оֲ��Ǿ�̬�����ڱ�
//1, 00069000
//2, 00069004
//3, 00CFF868
//4, 00069008
//
//1, 00069000
//2, 00069004
//3, 004FFD00
//4, 00069008


int main(int argc)
{
    if (argc == 1)
    {
        static int static_var1 = 1;
        static int static_var2 = 2;
        printf("! %d, %p\n", static_var1, &static_var1);
        printf("! %d, %p\n", static_var2, &static_var2);
    }
    else
    {
        static int static_var2 = 2;
        //static int static_var1 = 1;
        //printf("@ %d, %p\n", static_var1, &static_var1);
        printf("@ %d, %p\n", static_var2, &static_var2);
    }

    static int static_var3 = 3;
    printf("# %d, %p\n", static_var3, &static_var3);
}

// ��̬�����ĵ�ַ�������������Ƿ����Ӱ��
//PS C : \Users\Administrator\Documents\Visual Studio 2015\Projects\testVarAddr\Debug > .\testVarAddr.exe
//!1, 00209050
//!2, 00209054
//# 3, 0020905C
//PS C : \Users\Administrator\Documents\Visual Studio 2015\Projects\testVarAddr\Debug > .\testVarAddr.exe 2
//@ 2, 00209058
//# 3, 0020905C
//PS C : \Users\Administrator\Documents\Visual Studio 2015\Projects\testVarAddr\Debug >