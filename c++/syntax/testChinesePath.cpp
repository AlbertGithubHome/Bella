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
		//判断是否有子目录
		if (FileInfo.attrib & _A_SUBDIR)
		{
			// 排除两个特殊目录
			if ((strcmp(FileInfo.name, ".") != 0) && (strcmp(FileInfo.name, "..") != 0))
			{
				string newPath = folderPath + "\\" + FileInfo.name;
				dfsFolder(newPath);
			}
		}
		else
		{
			EXPECT_TRUE(isFullAsciiChar(FileInfo.name)) << folderPath + "\\" + FileInfo.name << " 文件路径名中包含中文，请从服务器目录移除，不要上传到svn";
		}
	} while (_findnext(Handle, &FileInfo) == 0);

	_findclose(Handle);
}

TEST(ChineseTest, CheckPath)
{
	//要遍历的目录
	string path = "..";
	dfsFolder(path);
}