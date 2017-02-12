#include "StdAfx.h"
#include <direct.h>  
#include <windows.h>
#include <wininet.h>
#include "MessageHandler.h"

void ZMessageHandler::Release()
{
	memset(m_szInBuffer, 0, sizeof(m_szInBuffer));
	memset(m_szOutBuffer, 0, sizeof(m_szOutBuffer));
}

ZMessageHandler& ZMessageHandler::GetInstance()
{
	static ZMessageHandler sMsgHandlerInstance;
	return sMsgHandlerInstance;
}

bool ZMessageHandler::InitInOutFile( char *pInFileName, char *pOutFileName )
{
	if (NULL == pInFileName || NULL == pOutFileName)
		return false;

	//char   buffer[260];   
	//getcwd(buffer, 260);

	// ��ʼ�������ļ�
	m_cInFile.open(pInFileName, ios::in);
	if (m_cInFile.fail()) 
		return false;

	// ��ʼ������ļ�
	m_cOutFile.open(pOutFileName, ios::out);
	if (m_cOutFile.fail()) 
		return false;

	return true;
}

char* ZMessageHandler::GetLineFromFile()
{
	if (m_cInFile.eof())
		return NULL;

	m_cInFile.getline(m_szInBuffer, MAX_INOUT_BUFFER_LENGTH);
	return m_szInBuffer;
}

void ZMessageHandler::OutPutLineToFile( char *pOutContent )
{
	if (NULL == pOutContent)
		return;

	m_cOutFile << pOutContent;
}

char* ZMessageHandler::SendMessage( char *pszDomain, char *pszUrl, char *pszData, const int nSendMsgType /*= 0*/ )
{
	if(NULL == pszDomain || NULL == pszUrl || NULL == pszData)
		return NULL;

	char szHeader[] =
	{
		// �ύ��
		"Content-Type: application/x-www-form-urlencoded"
	};

	if ( nSendMsgType == 0)
	{
		strcat(pszUrl, "?");
		strcat(pszUrl, pszData);
		pszData[0] = '\0';
	}

	// ��ʼ��
	HINTERNET hOpen = InternetOpen("Mozilla/4.0 (Compatible; MSIE 6.0;)", INTERNET_OPEN_TYPE_DIRECT, NULL, INTERNET_INVALID_PORT_NUMBER, 0);
	if(NULL == hOpen)
		return NULL;

	int nTimeOut = 10000;
	//�������ӳ�ʱʱ�䡢��������ʱʱ�䣬�����ݳ�ʱʱ�䣬Ĭ����20��
	InternetSetOption(hOpen, INTERNET_OPTION_CONNECT_TIMEOUT, &nTimeOut, sizeof(nTimeOut));
	InternetSetOption(hOpen, INTERNET_OPTION_SEND_TIMEOUT, &nTimeOut, sizeof(nTimeOut));
	InternetSetOption(hOpen, INTERNET_OPTION_RECEIVE_TIMEOUT, &nTimeOut, sizeof(nTimeOut));
	int nRetries = 1;
	InternetSetOption(hOpen, INTERNET_OPTION_CONNECT_RETRIES, &nRetries, sizeof(nRetries));

	// ���ӵ�����
	HINTERNET hConn = InternetConnect(hOpen, pszDomain, INTERNET_DEFAULT_HTTP_PORT, "", "", INTERNET_SERVICE_HTTP, 0, 1);
	if(NULL == hConn)
	{
		InternetCloseHandle(hOpen);
		return NULL;
	}

	// ����������
	HINTERNET hReq = HttpOpenRequest(hConn, (nSendMsgType == 0 ? "GET" : "POST"), pszUrl, HTTP_VERSION, NULL, NULL/*lpszAccept*/, INTERNET_FLAG_DONT_CACHE, 1);
	if(NULL == hReq)
	{
		InternetCloseHandle(hConn);
		InternetCloseHandle(hOpen);
		return NULL;
	}

	// ��������
	if(HttpSendRequest(hReq, szHeader, lstrlen(szHeader), pszData, lstrlen(pszData)))
	{
		DWORD dwByteRead = 0;
		ZeroMemory(m_szReturnText, sizeof(m_szReturnText));

		// ѭ����ȡ����������ֱ������
		while (InternetReadFile(hReq, m_szReturnText, sizeof(m_szReturnText), &dwByteRead) && dwByteRead > 0)
		{
			// ����������
			m_szReturnText[dwByteRead] = '\0';
			InternetCloseHandle(hReq);
			return m_szReturnText;
		}

	}		

	InternetCloseHandle(hReq);
	InternetCloseHandle(hConn);
	InternetCloseHandle(hOpen);

	return NULL;
}

