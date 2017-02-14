// select_sort.cpp : ѡ�������㷨��
//

#include <stdio.h>
#include <stdlib.h>

// ����Ԫ�صĸ���
#define MAX_ELEMNT_COUNT 10

// ѡ�����򣬴�С����
void select_sort(int array[], int count);

// ѡ�����򣬴�С���󣬲��ṩ��Ҫ����
void select_sort_for_explain(int array[], int count);

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
	select_sort_for_explain(array_data, MAX_ELEMNT_COUNT);


	// ��������
	printf("after sort:\n");
	print_array(array_data, MAX_ELEMNT_COUNT);

	return 0;
}

/*
���ܣ�	ѡ������ʵ������Ԫ�ش�С��������
������	array--��ʾ����������飬�˴����˻���ָ��
		count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
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
			swap_data(&array[target_index], &array[min_value_index]);	// ��������
		}
	}
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
���ܣ�	ѡ������ʵ������Ԫ�ش�С��������
������	array--��ʾ����������飬�˴����˻���ָ��
		count--����Ԫ�صĸ���
����ֵ����
ע�⣺	ֻ������ʾ˼·��������ָ��Ϊ�յ��������
*/
void select_sort_for_explain(int array[], int count)
{
	for (int target_index = 0; target_index < count - 1; ++target_index)
	{
		int min_value_index = target_index;
		printf("���ҵ�%d������λ�ø÷ŵ�Ԫ��\n", target_index);
		for (int scope_index = target_index + 1; scope_index < count; ++scope_index)
		{
			if (array[scope_index] < array[min_value_index])
			{
				min_value_index = scope_index;
			}
		}
		printf("��������Χ[%d-%d]���ҵ���СԪ�ص�������%d\n", target_index, count - 1, min_value_index);

		if (min_value_index != target_index)
		{
			printf("��Ҫ����array[%d] = %d �� array[%d] = %d\n", target_index, array[target_index], min_value_index, array[min_value_index]);
			swap_data(&array[target_index], &array[min_value_index]);
		}
		else
		{
			printf("��СԪ�ص���������ΪĿ��λ�õ����������ý���\n");
		}

		printf("��%d��ѡ����Ҳ����Խ�����Ľ��Ϊ��\n", target_index + 1);
		print_array(array, count);
		printf("\n");
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