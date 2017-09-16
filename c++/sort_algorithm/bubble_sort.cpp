// bubble_sort.cpp : ð�������㷨
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// ð�����򣬴�С����
void bubble_sort(int array[], int count);

// �����������
void print_array(int array[], int count);

// Ԫ�ؽ�������
void swap_data(int* element1, int* element2);

int main(int argc, char* argv[])
{
	// ��ʼ��ԭʼ����
	int array_data[MAX_ELEMNT_COUNT] = {100, 34, 54, 65, 11, 0, 5, 12, 89, 42};


	// ����ǰ���Ԫ��
	printf("before sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	
	// ����������
	printf("\nsort action...\n\n");
	bubble_sort(array_data, MAX_ELEMNT_COUNT);


	// ��������
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
}

/*
���ܣ�	ð������ʵ������Ԫ�ش�С��������
������	array--��ʾ����������飬�˴����˻���ָ��
		count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void bubble_sort(int array[], int count)
{
	for (int bubble_count = 0; bubble_count < count - 1; ++bubble_count)
	{
		for (int bubble_pos = 0; bubble_pos < count - 1 - bubble_count; ++bubble_pos)
		{
			if (array[bubble_pos] > array[bubble_pos + 1])
			{
				swap_data(&array[bubble_pos], &array[bubble_pos + 1]);	// ��������
			}
		}
	}
}

/*
���ܣ�	������������
������	element1--�������ĵ�һ��Ԫ�صĵ�ַ
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

