// select_sort.cpp : 选择排序算法。
//

#include <stdio.h>
#include <stdlib.h>

// 数组元素的个数
#define MAX_ELEMNT_COUNT 10

// 选择排序，从小到大
void select_sort(int array[], int count);

// 选择排序，从小到大，并提供必要解释
void select_sort_for_explain(int array[], int count);

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
	select_sort_for_explain(array_data, MAX_ELEMNT_COUNT);


	// 排序后输出
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
}

/*
功能：	选择排序，实现数组元素从小到大排列
参数：	array--表示待排序的数组，此处会退化成指针
		count--数组元素的个数
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void select_sort(int array[], int count)
{
	for (int target_index = 0; target_index < count - 1; ++target_index)
	{
		int min_value_index = target_index;
		for (int scope_index = target_index + 1; scope_index < count; ++scope_index)
		{
			if (array[scope_index] < array[min_value_index])
			{
				min_value_index = scope_index;
			}
		}

		if (min_value_index != target_index)
		{
			swap_data(&array[target_index], &array[min_value_index]);	// 交换数据
		}
	}
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

/*
功能：	选择排序，实现数组元素从小到大排列
参数：	array--表示待排序的数组，此处会退化成指针
		count--数组元素的个数
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void select_sort_for_explain(int array[], int count)
{
	for (int target_index = 0; target_index < count - 1; ++target_index)
	{
		int min_value_index = target_index;
		printf("查找第%d个索引位置该放的元素\n", target_index);
		for (int scope_index = target_index + 1; scope_index < count; ++scope_index)
		{
			if (array[scope_index] < array[min_value_index])
			{
				min_value_index = scope_index;
			}
		}
		printf("在索引范围[%d-%d]内找到最小元素的索引是%d\n", target_index, count - 1, min_value_index);

		if (min_value_index != target_index)
		{
			printf("需要交换array[%d] = %d 和 array[%d] = %d\n", target_index, array[target_index], min_value_index, array[min_value_index]);
			swap_data(&array[target_index], &array[min_value_index]);
		}
		else
		{
			printf("最小元素的索引正好为目标位置的索引，不用交换\n");
		}

		printf("第%d次选择查找并尝试交换后的结果为：\n", target_index + 1);
		print_array(array, count);
		printf("\n");
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