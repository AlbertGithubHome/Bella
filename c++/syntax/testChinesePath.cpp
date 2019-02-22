#include "unittest.h"
#include <io.h>
#include <fstream>
#include <string>
using namespace std;


bool isFullAsciiChar(char* pStr)
{
	while (*pStr)
		if (*pStr < 0)
			return false;
		else 
			pStr++;
	return true;
}

void dfsFolder(string folderPath)
{
	_finddata_t FileInfo;
	string strfind = folderPath + "\\*";
	long Handle = _findfirst(strfind.c_str(), &FileInfo);

	if (Handle == -1L)
	{
		cerr << "can not match the folder path" << endl;
		exit(-1);
		//_findclose(Handle);
		//return;
	}

	do{
		//�ж��Ƿ�����Ŀ¼
		if (FileInfo.attrib & _A_SUBDIR)
		{
			// �ų���������Ŀ¼
			if ((strcmp(FileInfo.name, ".") != 0) && (strcmp(FileInfo.name, "..") != 0))
			{
				string newPath = folderPath + "\\" + FileInfo.name;
				dfsFolder(newPath);
			}
		}
		else
		{
			EXPECT_TRUE(isFullAsciiChar(FileInfo.name)) << folderPath + "\\" + FileInfo.name << " �ļ�·�����а������ģ���ӷ�����Ŀ¼�Ƴ�����Ҫ�ϴ���svn";
		}
	} while (_findnext(Handle, &FileInfo) == 0);

	_findclose(Handle);
}

TEST(ChineseTest, CheckPath)
{
	//Ҫ������Ŀ¼
	string path = "..";
	dfsFolder(path);
}