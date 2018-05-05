// RebulidTree.cpp : 定义控制台应用程序的入口点。
//

#include <stdlib.h>
#include <stdio.h>
#define MAX_LEN  6



struct node
{
	node* left;
	node* right;
	char value;
};

void rebulid(char* preOrder, char* inOrder, int length, node** root)
{
	node *curNode = new node;
	curNode->left = NULL;
	curNode->right = NULL;
	curNode->value = *preOrder;

	*root = curNode;


	if (length <= 1)
		return;

	char* leftEnd = inOrder;
	int nLeftLength = 0;

	while(*leftEnd != *preOrder && nLeftLength < length)
	{
		nLeftLength++;
		leftEnd++;
	}


	if (nLeftLength > 0)
	{
		rebulid(preOrder + 1, inOrder, nLeftLength, &curNode->left);
	}

	int rightLenght = length - nLeftLength - 1;
	if (rightLenght > 0)
	{
		rebulid(preOrder + 1 + nLeftLength, inOrder + nLeftLength + 1, rightLenght, &curNode->right);
	}

}


int main(int argc, char* argv[])
{
	char preOrder[MAX_LEN + 1] = "abdcef";
	char inOrder[MAX_LEN + 1] = "dbaecf";

	node* root = NULL;
	rebulid(preOrder, inOrder, MAX_LEN, &root);

	return 0;
}

