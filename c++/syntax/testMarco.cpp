// testMarco.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"

#define MAX_LEN 1
#define MAX_LEN 2
#define MAX_LEN 3


#define MAX_SIZE 1
#undef MAX_SIZE
#define MAX_SIZE 2


#define MAX_HEIGHT 1
#ifndef MAX_HEIGHT
#define MAX_HEIGHT 2
#endif // !MAX_HEIGHT



int main()
{
    printf("MAX_LEN = %d\n", MAX_LEN);
    printf("MAX_SIZE = %d\n", MAX_SIZE);
    printf("MAX_HEIGHT = %d\n", MAX_HEIGHT);
    return 0;
}

//MAX_LEN = 3
//MAX_SIZE = 2
//MAX_HEIGHT = 1

//1 > c:\users\administrator\documents\visual studio 2015\projects\testmarco\testmarco\testmarco.cpp(7) : warning C4005 : ��MAX_LEN��: ���ض���
//1 > c:\users\administrator\documents\visual studio 2015\projects\testmarco\testmarco\testmarco.cpp(6) : note: �μ���MAX_LEN����ǰһ������
//1 > c:\users\administrator\documents\visual studio 2015\projects\testmarco\testmarco\testmarco.cpp(8) : warning C4005 : ��MAX_LEN��: ���ض���
//1 > c:\users\administrator\documents\visual studio 2015\projects\testmarco\testmarco\testmarco.cpp(7) : note: �μ���MAX_LEN����ǰһ������