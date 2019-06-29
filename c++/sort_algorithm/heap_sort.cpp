// heap_sort.cpp : �������㷨
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// ��start��end�������ѣ�ǰ����start֮��Ĳ�������������
void max_heapify(int arr[], int start, int end);

// �������򣬴�С����
void heap_sort(int array[], int count);

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
    heap_sort(array_data, MAX_ELEMNT_COUNT);


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
���ܣ�  ��start��end�������ѣ�ǰ����start֮��Ĳ������������ѣ�
       Ҳ����˵start������������������£������Ѿ�������
������  array--��ʾ����������飬�˴����˻���ָ��
       start--��Ҫ�����ĸ��ڵ�����
       end  --���һ�����Ա������Ľڵ����������γ����Ѻ󣬵�һ���ڵ��뵱ǰ���ڵ㽻������ô�����ǰ���ڵ���һ�־Ͳ��ܱ�������
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void max_heapify(int array[], int start, int end)
{
    int parent_index = start;
    int child_index = start * 2 + 1;
    while (child_index <= end)
    {
        if (child_index + 1 <= end && array[child_index] < array[child_index + 1])
            ++child_index; // ����ұߵĺ��Ӹ���ѡ���ұߵ�

        if (array[parent_index] > array[child_index])
            break;

        swap_data(&array[parent_index], &array[child_index]);
        parent_index = child_index;
        child_index = parent_index * 2 + 1;
    }
}

/*
���ܣ�  ������ʵ������Ԫ�ش�С��������
������  array--��ʾ����������飬�˴����˻���ָ��
       count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void heap_sort(int array[], int count)
{
    for (int pos = count / 2 - 1; pos >= 0; --pos)
        max_heapify(array, pos, count - 1);

    for (int target_pos = count - 1; target_pos > 0; --target_pos)
    {
        swap_data(&array[0], &array[target_pos]);
        max_heapify(array, 0, target_pos - 1);
    }
}

/*
before sort:
100 34 54 65 11 0 5 12 89 42

sort action...

after sort:
0 5 11 12 34 42 54 65 89 100
*/