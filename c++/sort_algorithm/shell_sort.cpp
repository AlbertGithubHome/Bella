// shell_sort.cpp : ϣ�������㷨
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// �������򣬴�С����
void insert_sort(int array[], int count);

// �����������
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
    // ��ʼ��ԭʼ����
    int array_data[MAX_ELEMNT_COUNT] = { 100, 34, 54, 65, 11, 0, 5, 12, 89, 42 };


    // ����ǰ���Ԫ��
    printf("before sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);


    // ����������
    printf("\nsort action...\n\n");
    insert_sort(array_data, MAX_ELEMNT_COUNT);


    // ��������
    printf("after sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);

    return 0;
}

/*
���ܣ�  �����������Ԫ�أ�ʹ�ÿո�ָ�
������  array--��ʾ����������飬�˴����˻���ָ��
count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void print_array(int array[], int count)
{
    for (int index = 0; index < count; ++index)
        printf("%d ", array[index]);

    printf("\n");
}

/*
���ܣ�  ������������
������  element1--�������ĵ�һ��Ԫ�صĵ�ַ
element2--�������ĵڶ���Ԫ�صĵ�ַ
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void swap_data(int* element1, int* element2)
{
    int middle_value = *element1;
    *element1 = *element2;
    *element2 = middle_value;
}


/*
���ܣ�  ϣ������ʵ������Ԫ�ش�С��������
������  array--��ʾ����������飬�˴����˻���ָ��
count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void insert_sort(int array[], int count)
{
    int step = count / 2;
    while (step > 0)
    {
        for (int pos = step; pos < count; ++pos)
        {
            for (int insert_index = pos; insert_index >= step; insert_index -= step)
            {
                if (array[insert_index] < array[insert_index - step])
                    swap_data(&array[insert_index], &array[insert_index - step]);
            }
        }
        step /= 2;
    }
}


