// quick_sort.cpp : k快速排序算法
//

#include <stdio.h>
#include <stdlib.h>

// 数组元素的个数
#define MAX_ELEMNT_COUNT 10

// 快速排序，从小到大
void quick_sort(int array[], int low, int high);

// 数组输出函数
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
	// 初始化原始数据
	int array_data[MAX_ELEMNT_COUNT] = {100, 34, 54, 65, 11, 0, 5, 12, 89, 42};


	// 排序前输出元素
	printf("before sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);


	// 调用排序函数
	printf("\nsort action...\n\n");
	quick_sort(array_data, 0, MAX_ELEMNT_COUNT - 1);


	// 排序后输出
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
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
功能：	快速排序，实现数组元素从小到大排列
参数：	array--表示待排序的数组，此处会退化成指针
		low  --待排序区间的起始索引
		high --待排序区间的结束索引
返回值：无
注意：	只用来表示思路，不考虑指针为空等特殊情况
*/
void quick_sort(int array[], int low, int high)
{
	if (low >= high)
		return;

	int front = low, back = high, key = array[low];	// 选取第一个元素作为中轴
	while (front < back)
	{
		while (front < back && array[back] >= key)
			--back;
		array[front] = array[back];		// 从后面找到第一个比中轴小的交换

		while (front < back && array[front] <= key)
			++front;
		array[back] = array[front];		// 从前面找到第一个比中轴大的交换
	}

	array[front] = key;
	quick_sort(array, low, front - 1);	// 递归快排前半段
	quick_sort(array, low, front + 1);	// 递归快排后半段
}
