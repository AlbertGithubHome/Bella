// merge_sort.cpp : 归并排序算法
//

#include <stdio.h>
#include <stdlib.h>

// 数组元素的个数
#define MAX_ELEMNT_COUNT 10

// 将数组的两个有序段[left,mid]和[mid+1,right]合并成[left,right]区间完整有序
void merge(int array[], int left, int mid, int right);

// 归并排序，从小到大
void merge_sort(int array[], int left, int right);

// 数组输出函数
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
    // 初始化原始数据
    int array_data[MAX_ELEMNT_COUNT] = { 2, 3, 9, 4, 7, 12, 6, 1, 11, 5 };


    // 排序前输出元素
    printf("before sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);


    // 调用排序函数
    printf("\nsort action...\n\n");
    merge_sort(array_data, 0, MAX_ELEMNT_COUNT-1);


    // 排序后输出
    printf("after sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);

    return 0;
}

/*
功能：  按行输出数组元素，使用空格分隔
参数：  array--表示带输出的数组，此处会退化成指针
       count--数组元素的个数
返回值：无
注意： 只用来表示思路，不考虑指针为空等特殊情况
*/
void print_array(int array[], int count)
{
    for (int index = 0; index < count; ++index)
        printf("%d ", array[index]);

    printf("\n");
}

/*
功能：  交换两个变量
参数：  element1--被交换的第一个元素的地址
       element2--被交换的第二个元素的地址
返回值：无
注意： 只用来表示思路，不考虑指针为空等特殊情况
*/
void swap_data(int* element1, int* element2)
{
    int middle_value = *element1;
    *element1 = *element2;
    *element2 = middle_value;
}

/*
功能：  将数组的两个有序段[left,mid]和[mid+1,right]合并成[left,right]区间完整有序
参数：  array--表示待排序的数组，此处会退化成指针
        left--数组第一段开始的索引
        mid--数组第一段结束的索引
        right--数组第二段结束的索引
返回值：无
注意： 只用来表示思路，不考虑指针为空等特殊情况
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

    //第一段仍有元素没加到结果
    while (l <= mid) temp[i++] = array[l++];

    //第二段仍有元素没加到结果
    while (r <= right) temp[i++] = array[r++];

    //结果赋值回原数组
    for (int j = 0; j <= right - left; j++) array[left+j] = temp[j];

    free(temp);
}

/*
功能：  归并排序，实现数组元素从小到大排列
参数：  array--表示待排序的数组，此处会退化成指针
        left--数组第一个待排序元素索引
        right--数组最后一个待排序元素索引
返回值：无
注意： 只用来表示思路，不考虑指针为空等特殊情况
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