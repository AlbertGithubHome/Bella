// testAssignment.cpp : ╤╗рЕ©ьжфл╗с╕сцЁлпР╣дхК©з╣Ц║ё
//

#include "stdafx.h"


int main()
{
    char szParam1[32];
    char *szParam2 = "123";
    char szParam3[32] = { "456" };
    char szParam4[32] = "789";

    printf("szParam1 = %s\n", szParam1);
    printf("szParam2 = %s\n", szParam2);
    printf("szParam3 = %s\n", szParam3);
    printf("szParam4 = %s\n", szParam4);

    return 0;
}

//szParam1 = лллллллллллллллллллллллллллллллллллл┴┘ ? ─В@n 0
//szParam2 = 123
//szParam3 = 456
//szParam4 = 789