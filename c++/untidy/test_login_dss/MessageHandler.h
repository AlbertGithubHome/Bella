#pragma once
#include <fstream>

using namespace std;

#define	g_MsgHandler	ZMessageHandler::GetInstance()

#define MAX_INOUT_BUFFER_LENGTH		1204
#define MAX_RETURN_CONTENT_LENGTH	12040

class ZMessageHandler
{
private:
	ZMessageHandler(void){ Release(); };
	~ZMessageHandler(void){ Release(); };
	void Release();
public:
	static ZMessageHandler& GetInstance();

	// ��ʼ����������ļ�
	bool	InitInOutFile(char *pInFileName, char *pOutFileName);

	// ���ļ��еõ�һ��
	char*	GetLineFromFile();

	// ���ļ������һ��
	void	OutPutLineToFile(char *pOutContent);

	// ������Ϣ
	char*	SendMessage(char *pszDomain, char *pszUrl, char *pszData, const int nSendMsgType = 0);

private:
	ifstream m_cInFile;
	ofstream m_cOutFile;

	char m_szOutBuffer[MAX_INOUT_BUFFER_LENGTH];
	char m_szInBuffer[MAX_INOUT_BUFFER_LENGTH];

	// ������Ϣ
	char m_szReturnText[MAX_RETURN_CONTENT_LENGTH];
};
