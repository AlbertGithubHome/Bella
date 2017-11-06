#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    printf("char size = %ld\n", (long)sizeof(char));
    printf("unsigned char size = %ld\n\n", (long)sizeof(unsigned char));

    printf("short size = %ld\n", (long)sizeof(short));
    printf("unsigned short size = %ld\n\n", (long)sizeof(unsigned short));

    printf("int size = %ld\n", (long)sizeof(int));
    printf("unsigned int size = %ld\n\n", (long)sizeof(unsigned int));

    printf("long size = %ld\n", (long)sizeof(long));
    printf("unsigned long size = %ld\n\n", (long)sizeof(unsigned long));

    printf("long long size = %ld\n", (long)sizeof(long long));
    printf("unsigned long long size = %ld\n\n", (long)sizeof(unsigned long long));

    printf("float size = %ld\n", (long)sizeof(float));
    //printf("long float size = %ld\n\n", sizeof(long float));

    printf("double size = %ld\n", (long)sizeof(double));
    //printf("long double size = %ld\n\n", sizeof(unsigned long double));

    printf("point size = %ld\n", (long)sizeof(&argc));

    return 0;
}