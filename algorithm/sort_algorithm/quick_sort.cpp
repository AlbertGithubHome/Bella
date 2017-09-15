// quick_sort.cpp : k���������㷨
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// �������򣬴�С����
void quick_sort(int array[], int low, int high);

// �����������
void print_array(int array[], int count);


int main(int argc, char* argv[])
{
	// ��ʼ��ԭʼ����
	int array_data[MAX_ELEMNT_COUNT] = {100, 34, 54, 65, 11, 0, 5, 12, 89, 42};


	// ����ǰ���Ԫ��
	printf("before sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);


	// ����������
	printf("\nsort action...\n\n");
	quick_sort(array_data, 0, MAX_ELEMNT_COUNT - 1);


	// ��������
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
}

/*
���ܣ�	�����������Ԫ�أ�ʹ�ÿո�ָ�
������	array--��ʾ����������飬�˴����˻���ָ��
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
���ܣ�	��������ʵ������Ԫ�ش�С��������
������	array--��ʾ����������飬�˴����˻���ָ��
		low  --�������������ʼ����
		high --����������Ľ�������
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void quick_sort(int array[], int low, int high)
{
	if (low >= high)
		return;

	int front = low, back = high, key = array[low];	// ѡȡ��һ��Ԫ����Ϊ����
	while (front < back)
	{
		while (front < back && array[back] >= key)
			--back;
		array[front] = array[back];		// �Ӻ����ҵ���һ��������С�Ľ���

		while (front < back && array[front] <= key)
			++front;
		array[back] = array[front];		// ��ǰ���ҵ���һ���������Ľ���
	}

	array[front] = key;
	quick_sort(array, low, front - 1);	// �ݹ����ǰ���
	quick_sort(array, low, front + 1);	// �ݹ���ź���
}
