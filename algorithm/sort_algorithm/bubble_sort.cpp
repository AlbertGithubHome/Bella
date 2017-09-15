// bubble_sort.cpp : 冒泡排序算法
//

#include <stdio.h>
#include <stdlib.h>

// 数组元素的个数
#define MAX_ELEMNT_COUNT 10

// 冒泡排序，从小到大
void bubble_sort(int array[], int count);

// 数组输出函数
void print_array(int array[], int count);

// 元素交换函数
void swap_data(int* element1, int* element2);

int main(int argc, char* argv[])
{
	// 初始化原始数据
	int array_data[MAX_ELEMNT_COUNT] = {100, 34, 54, 65, 11, 0, 5, 12, 89, 42};


	// 排序前输出元素
	printf("before sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	
	// 调用排序函数
	printf("\nsort action...\n\n");
	bubble_sort(array_data, MAX_ELEMNT_COUNT);


	// 排序后输出
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
}

/*
功能：	冒泡排序，实现数组元素从小到大排列
参数：	array--表示待排序的数组，此处会退化成指针
		count--数组元素的个数
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void bubble_sort(int array[], int count)
{
	for (int bubble_count = 0; bubble_count < count - 1; ++bubble_count)
	{
		for (int bubble_pos = 0; bubble_pos < count - 1 - bubble_count; ++bubble_pos)
		{
			if (array[bubble_pos] > array[bubble_pos + 1])
			{
				swap_data(&array[bubble_pos], &array[bubble_pos + 1]);	// 交换数据
			}
		}
	}
}

/*
功能：	交换两个变量
参数：	element1--被交换的第一个元素的地址
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
功能：	按行输出数组元素，使用空格分隔
参数：	array--表示带输出的数组，此处会退化成指针
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

