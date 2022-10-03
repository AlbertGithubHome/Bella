// merge_sort.cpp : �鲢�����㷨
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// ����������������[left,mid]��[mid+1,right]�ϲ���[left,right]������������
void merge(int array[], int left, int mid, int right);

// �鲢���򣬴�С����
void merge_sort(int array[], int left, int right);

// �����������
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
    // ��ʼ��ԭʼ����
    int array_data[MAX_ELEMNT_COUNT] = { 2, 3, 9, 4, 7, 12, 6, 1, 11, 5 };


    // ����ǰ���Ԫ��
    printf("before sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);


    // ����������
    printf("\nsort action...\n\n");
    merge_sort(array_data, 0, MAX_ELEMNT_COUNT-1);


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
ע�⣺ ֻ������ʾ˼·��������ָ��Ϊ�յ��������
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
ע�⣺ ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void swap_data(int* element1, int* element2)
{
    int middle_value = *element1;
    *element1 = *element2;
    *element2 = middle_value;
}

/*
���ܣ�  ����������������[left,mid]��[mid+1,right]�ϲ���[left,right]������������
������  array--��ʾ����������飬�˴����˻���ָ��
        left--�����һ�ο�ʼ������
        mid--�����һ�ν���������
        right--����ڶ��ν���������
����ֵ����
ע�⣺ ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void merge(int array[], int left, int mid, int right)
{
    int* temp = (int*)malloc((right-left+1)*4);
    int i = 0, l = left, r = mid + 1;

    while (l <= mid && r <= right)
    {
        if (array[l] <= array[r])
            temp[i++] = array[l++];
        else
            temp[i++] = array[r++];
    }

    //��һ������Ԫ��û�ӵ����
    while (l <= mid) temp[i++] = array[l++];

    //�ڶ�������Ԫ��û�ӵ����
    while (r <= right) temp[i++] = array[r++];

    //�����ֵ��ԭ����
    for (int j = 0; j <= right - left; j++) array[left+j] = temp[j];

    free(temp);
}

/*
���ܣ�  �鲢����ʵ������Ԫ�ش�С��������
������  array--��ʾ����������飬�˴����˻���ָ��
        left--�����һ��������Ԫ������
        right--�������һ��������Ԫ������
����ֵ����
ע�⣺ ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void merge_sort(int array[], int left, int right)
{
    if (right > left)
    {
        int mid = (right + left) / 2;
        merge_sort(array, left, mid);
        merge_sort(array, mid+1, right);
        merge(array, left, mid, right);
    }
}

/*
before sort:
2 3 9 4 7 12 6 1 11 5

sort action...

after sort:
1 2 3 4 5 6 7 9 11 12
*/