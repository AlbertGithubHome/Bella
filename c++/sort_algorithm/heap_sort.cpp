// heap_sort.cpp : 堆排序算法
//

#include <stdio.h>
#include <stdlib.h>

// 数组元素的个数
#define MAX_ELEMNT_COUNT 10

// 从start到end构成最大堆，前提是start之后的部分已满足最大堆
void max_heapify(int arr[], int start, int end);

// 插入排序，从小到大
void heap_sort(int array[], int count);

// 数组输出函数
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
    // 初始化原始数据
    int array_data[MAX_ELEMNT_COUNT] = { 100, 34, 54, 65, 11, 0, 5, 12, 89, 42 };


    // 排序前输出元素
    printf("before sort:\n");
    print_array(array_data, MAX_ELEMNT_COUNT);


    // 调用排序函数
    printf("\nsort action...\n\n");
    heap_sort(array_data, MAX_ELEMNT_COUNT);


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
注意：	只用来表示思路，不考虑指针为空等特殊情况
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
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void swap_data(int* element1, int* element2)
{
    int middle_value = *element1;
    *element1 = *element2;
    *element2 = middle_value;
}

/*
功能：  从start到end构成最大堆，前提是start之后的部分已满足最大堆，
       也就是说start存在左右子树的情况下，子树已经是最大堆
参数：  array--表示待排序的数组，此处会退化成指针
       start--需要调整的父节点索引
       end  --最后一个可以被调整的节点索引，当形成最大堆后，第一个节点与当前最后节点交换后，那么这个当前最后节点下一轮就不能被调整了
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void max_heapify(int array[], int start, int end)
{
    int parent_index = start;
    int child_index = start * 2 + 1;
    while (child_index <= end)
    {
        if (child_index + 1 <= end && array[child_index] < array[child_index + 1])
            ++child_index; // 如果右边的孩子更大，选择右边的

        if (array[parent_index] > array[child_index])
            break;

        swap_data(&array[parent_index], &array[child_index]);
        parent_index = child_index;
        child_index = parent_index * 2 + 1;
    }
}

/*
功能：  堆排序，实现数组元素从小到大排列
参数：  array--表示待排序的数组，此处会退化成指针
       count--数组元素的个数
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
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