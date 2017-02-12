#include "stdafx.h"
#include "GlobalData.h"
#include "Component.h"


CCComponent::CCComponent()
{
}


CCComponent::~CCComponent()
{
}


CRingBuffer::CRingBuffer()
{
}


CRingBuffer::~CRingBuffer()
{
}

int CRingBuffer::Init(char* pStart, const DWORD dwBufferLen, const DWORD dwMaxPackLen)
{
	if ( dwBufferLen < dwMaxPackLen * 2 + RB_SPACE )
		return INVALID_VALUE;

	pStart = new char[dwBufferLen];

	if ( pStart == NULL )
		return INVALID_VALUE;

	memset( pStart, 0, dwBufferLen );

	m_pStart = m_pLeft = m_pRight = m_pNext = pStart;
	m_pTemp = m_pStart + dwMaxPackLen + RB_SPACE;

	m_dwBufferLen = dwBufferLen - dwMaxPackLen - RB_SPACE;
	m_dwMaxPackLen = dwMaxPackLen;

	return SUCCESS_VALUE;
}

int CRingBuffer::ReInit()
{
	if ( m_pStart == NULL )
		return INVALID_VALUE;

	m_pLeft = m_pRight = m_pNext = m_pStart;
	m_pTemp = m_pStart + m_dwBufferLen + RB_SPACE;

	return SUCCESS_VALUE;
}

char* CRingBuffer::PutPack(const char* pData, const DWORD dwDataSize)
{
	if ( pData == NULL )
		return NULL;

	DWORD dwRemainEmptySize = 0;
	if ( m_pLeft <= m_pRight )
		dwRemainEmptySize = m_dwBufferLen - (m_pRight - m_pLeft) - 1;
	else
		dwRemainEmptySize = m_pRight - m_pLeft - 1;

	if ( dwRemainEmptySize < dwDataSize + PACK_HEADER_SIZE )
	{
		printf("The RingBuffer is overflow!\n");
		return NULL;
	}

	char *pLeft = m_pLeft, *pRight = m_pRight;

	// 写入数据长度
	pRight = PutData(pLeft, pRight, (const char*)&dwDataSize, PACK_HEADER_SIZE);

	if ( pRight == NULL ) 
		return NULL;

	// 写入原始数据
	pRight = PutData(pLeft, pRight, pData, dwDataSize);

	if (pRight == NULL)
		return NULL;

	m_pRight = pRight;

	return m_pRight;
}

void* CRingBuffer::GetPack(DWORD& dwDateSize)
{
	dwDateSize = 0;
	m_pLeft = m_pNext; 

	char* pLeft = m_pLeft;
	char* pRight = m_pRight;

	dwDateSize = GetPackLen(pLeft, pRight);
		 
	DWORD dwRemainDataLen = 0;

	if ( pLeft <= pRight )
		dwRemainDataLen = pRight - pLeft;
	else
		dwRemainDataLen = m_dwBufferLen - (pLeft - pRight);

	// 剩余数据的长度小于数据头所记录的长度
	if ( dwRemainDataLen < dwDateSize + PACK_HEADER_SIZE )
	{
		dwDateSize = 0;
		return NULL;
	}

	DWORD dwRemainLeft2End = m_dwBufferLen - (m_pLeft - m_pStart);

	// 数据环绕
	if ( pLeft > pRight && dwRemainLeft2End < dwDateSize + PACK_HEADER_SIZE )
	{
		memcpy(m_pTemp, pLeft, dwRemainLeft2End);
		memcpy(m_pTemp + dwRemainLeft2End, m_pStart, dwDateSize + PACK_HEADER_SIZE - dwRemainLeft2End);
		m_pNext = m_pStart + dwDateSize + PACK_HEADER_SIZE - dwRemainLeft2End;
		return m_pTemp + PACK_HEADER_SIZE;
	}

	m_pNext = pLeft + dwDateSize + PACK_HEADER_SIZE;
	return pLeft + PACK_HEADER_SIZE;
}

char* CRingBuffer::PutData(const char* pLeft, char* pRight, const char* pData, const DWORD dwDataSize)
{
	DWORD dwRemainRight2End = 0;

	if (pLeft < pRight)
		dwRemainRight2End = m_dwBufferLen - (pRight - m_pStart);
	else
		dwRemainRight2End = pRight - pLeft;

	if (dwDataSize <= dwRemainRight2End)
	{
		memcpy(pRight, pData, dwDataSize);
		pRight += dwDataSize;
	}		
	else
	{
		memcpy(pRight, pData, dwRemainRight2End);
		memcpy(m_pStart, pData + dwRemainRight2End, dwDataSize - dwRemainRight2End);
		pRight = m_pStart + dwDataSize - dwRemainRight2End;
	}
	
	return pRight;
}

DWORD CRingBuffer::GetPackLen(const char* pLeft, const char* pRight)
{
	DWORD dwRemainLeft2End = m_dwBufferLen - (pLeft - m_pStart);

	// 数据环绕且剩余字节不能完整读出数据长度
	if (pLeft > pRight && dwRemainLeft2End < SIZEOF_DWORD_SIZE)
	{
		DWORD dwDataSize = 0;
		char* pHeader = (char*)&dwDataSize;
		memcpy(pHeader, pLeft, dwRemainLeft2End);
		memcpy(pHeader + dwRemainLeft2End, m_pStart, SIZEOF_DWORD_SIZE - dwRemainLeft2End);
		return dwDataSize;
	}

	return *((DWORD*)pLeft);
}

CRingBuffer& CRingBuffer::Singleton()
{
	static CRingBuffer sInstance;
	return sInstance;
}


/*
*	to implement a thread seed
*/

DWORD WINAPI GThreadProc(LPVOID lpParam)
{
	CThreadSeed* pThread = (CThreadSeed *)lpParam;
	pThread->Action();

	return SUCCESS_VALUE;
}


CThreadSeed::CThreadSeed()
{
	m_hThreadId = NULL;
	m_eThreadState = ePrepareStart;
}

int CThreadSeed::Start()
{
	m_hThreadId = CreateThread(NULL, 0, GThreadProc, this, 0, NULL);

	if (m_hThreadId != NULL)
	{
		m_eThreadState = eRunning;
	}

	return SUCCESS_VALUE;
}

int CThreadSeed::Stop()
{
	if (m_eThreadState == eRunning)
		TerminateThread(m_hThreadId, 0);

	return SUCCESS_VALUE;
}

CCenterMgr::CCenterMgr()
{
	m_bRunning = false;
	m_dwCounter = 0;
}

CCenterMgr::~CCenterMgr()
{

}

CCenterMgr& CCenterMgr::Singleton()
{
	static CCenterMgr sInstance;
	return sInstance;
}

int CCenterMgr::Start()
{
	m_cLogic(this, &CCenterMgr::LogicThreadFuc);
	m_bRunning = true;

	m_pServer = new CNetServer();

	m_pServer->Init(2, 8888, 64 * KB, 4 * KB);
	m_pServer->Start();

	return SUCCESS_VALUE;
}

int CCenterMgr::Stop()
{
	m_bRunning = false;

	return SUCCESS_VALUE;
}

void CCenterMgr::Yeild(const DWORD dwInterval)
{
	Sleep(dwInterval);
}

int CCenterMgr::LogicThreadFuc()
{
	while (m_bRunning)
	{
		printf("the number is %d.\n", m_dwCounter++);

		Yeild(400);
	}

	return SUCCESS_VALUE;
}

ICenterManager* CreateCenterMgr()
{
	return &CCenterMgr::Singleton();
}


CNetServer::CNetServer()
{
	m_tSocketId = INVALID_VALUE;
	m_nListenPort = INVALID_VALUE;

	m_dwMaxRecvLen = 0;
	m_dwMaxSendLen = 0;
}

CNetServer::~CNetServer()
{

}


int CNetServer::Init(const int nMaxConnNum, const int nPort, const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen)
{
	m_nListenPort = nPort;
	m_nMaxConnNum = nMaxConnNum;

	m_dwMaxRecvLen = dwMaxRecvLen;
	m_dwMaxSendLen = dwMaxSendLen;

	m_pNetBufferList = new CNetBuffer[nMaxConnNum];

	for (int nIndex = 0; nIndex < nMaxConnNum; nIndex++)
	{
		m_pNetBufferList[nIndex].Init(0, m_dwMaxRecvLen, m_dwMaxSendLen, KB);
	}

	return SUCCESS_VALUE;
}

int CNetServer::Start()
{
	WSADATA sWsaData;

	WORD wVersionRequested = MAKEWORD(2, 2);
	int nError = WSAStartup(wVersionRequested, &sWsaData);

	if (nError != 0)
	{
		printf("WSAStartup Error! errno = %d\n", WSAGetLastError());
		return INVALID_VALUE;
	}

	m_tSocketId = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (m_tSocketId == INVALID_SOCKET)
	{
		printf("socket Error! errno = %d\n", WSAGetLastError());
		return INVALID_VALUE;
	}

	//int nMode = 1;	// 0-block,1-non block
	//ioctlsocket(m_tSocketId, FIONBIO, (u_long FAR*)&nMode);

	sockaddr_in sAddr;
	sAddr.sin_family = AF_INET;
	sAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
	sAddr.sin_port = htons(m_nListenPort);

	if (bind(m_tSocketId, (SOCKADDR*)&sAddr, sizeof(sAddr)) == SOCKET_ERROR)
	{
		printf("bind Error! errno = %d\n", WSAGetLastError());
		return INVALID_VALUE;
	}

	if (listen(m_tSocketId, 1024) == SOCKET_ERROR)
	{
		printf("listen Error! errno = %d\n", WSAGetLastError());
		return INVALID_VALUE;
	}

	// start up three network threads
	m_cNetServerListen(this, &CNetServer::ListenThreadFunc);
	m_cNetServerRead(this, &CNetServer::ReadThreadFunc);
	m_cNetServerWrite(this, &CNetServer::WriteThreadFunc);
	
	return SUCCESS_VALUE;
}

int CNetServer::Stop()
{

	return SUCCESS_VALUE;
}


int CNetServer::Release()
{

	return SUCCESS_VALUE;
}

void CNetServer::Yeild(const DWORD dwInterval)
{
	Sleep(dwInterval);
}

int CNetServer::ListenThreadFunc()
{
	while (true)
	{
		SOCKET tSocket;
		if ((tSocket = accept(m_tSocketId, NULL, NULL)) == INVALID_SOCKET)
		{
			printf("accept Error! errno = %d\n", WSAGetLastError());		
			
		}
		else
		{
			AddConnection(tSocket);
		}

		Yeild(1000);

	}

	return SUCCESS_VALUE;
}

int CNetServer::ReadThreadFunc()
{
	while (true)
	{
		fd_set fdReadset;
		FD_ZERO(&fdReadset);
		

		for (int nIndex = 0; nIndex < m_nMaxConnNum; nIndex++)
		{
			if (m_pNetBufferList[nIndex].GetUseState() == 0)
			{
				FD_SET(m_pNetBufferList[nIndex].GetSocketId(), &fdReadset);
			}
		}


		int nfdnum = select(m_tSocketId, &fdReadset, NULL, NULL, NULL);

		if (nfdnum > 0)
		{
			if (FD_ISSET(m_tSocketId, &fdReadset) != 0)
			{
				for (int nIndex = 0; nIndex < m_nMaxConnNum; nIndex++)
				{
					if (m_pNetBufferList[nIndex].GetUseState() == 0)
					{
						m_pNetBufferList[nIndex].m_cRecvBuffer.RecvData();
					}
				}
			}
		}

		Yeild(100);
	}
	return SUCCESS_VALUE;
}

int CNetServer::WriteThreadFunc()
{
	while (true)
	{
		for (int nIndex = 0; nIndex < m_nMaxConnNum; nIndex++)
		{
			if (m_pNetBufferList[nIndex].GetUseState() == 0)
			{
				m_pNetBufferList[nIndex].m_cSendBuffer.SendData();
			}
		}
		Yeild(100);
	}
	return SUCCESS_VALUE;
}

int CNetServer::AddConnection(SOCKET tSocketId)
{
	int nIndex = 0;
	for (; nIndex < m_nMaxConnNum; nIndex++)
	{
		if (m_pNetBufferList[nIndex].GetUseState() == -1)
			break;
	}
	
	if (nIndex < m_nMaxConnNum)
	{
		m_pNetBufferList[nIndex].SetUseState(0);
		m_pNetBufferList[nIndex].SetSocketId(tSocketId);
	}

	return SUCCESS_VALUE;
}

int CNetServer::DelConnection(const int nConnectIndex)
{
	if (m_pNetBufferList[nConnectIndex].GetUseState() == 0)
	{
		m_pNetBufferList[nConnectIndex].Close();
	}

	return SUCCESS_VALUE;
}


CNetBuffer::CNetBuffer()
{

}

CNetBuffer::~CNetBuffer()
{

}

int CNetBuffer::Init(const SOCKET tSocket,const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen, const DWORD dwMaxPackLen)
{
	m_cRecvBuffer.Init(tSocket, NULL, dwMaxRecvLen, dwMaxPackLen);
	m_cSendBuffer.Init(tSocket, NULL, dwMaxSendLen, dwMaxPackLen);

	m_nUseState = -1;

	return SUCCESS_VALUE;
}

int CNetBuffer::ReInit(const SOCKET tSocket)
{
	m_cRecvBuffer.ReInit(tSocket);
	m_cSendBuffer.ReInit(tSocket);

	m_nUseState = -1;

	return SUCCESS_VALUE;
}

int CNetBuffer::Close()
{
	if ( m_nUseState == 0 )
	{
		closesocket(m_tSocketId);
		m_nUseState = -1;
	}

	return SUCCESS_VALUE;
}

int CNetBufferBase::Init(const SOCKET tSocket, char* pStart, const DWORD dwBufferLen /*= 4 * MB*/, const DWORD dwMaxPackLen /*= 16 * KB*/)
{
	CRingBuffer::Init(pStart, dwBufferLen, dwMaxPackLen);
	m_tSocket = tSocket;

	return SUCCESS_VALUE;
}

int CNetBufferBase::ReInit(const SOCKET tSocket)
{
	CRingBuffer::ReInit();
	m_tSocket = tSocket;

	return SUCCESS_VALUE;
}


int CNetBufferBase::RecvData()
{
	char* pLeft = m_pLeft;
	char* pRight = m_pRight;

	if (pRight < pLeft)
	{
		int nEmptySize = pLeft - pRight - 1;
		int nReadedSize = recv(m_tSocket, pRight, nEmptySize, 0);

		if (nReadedSize == 0)
		{
			return INVALID_VALUE;
		}
		else if (nReadedSize < nEmptySize)
		{
			m_pRight += nReadedSize;
			return SUCCESS_VALUE;
		}
		else if (nReadedSize == nEmptySize)
		{
			m_pRight += nReadedSize;
			printf("receive buffer is overflow!\n");
			return SUCCESS_VALUE;
		}
	}
	else
	{
		int nEmptySize = (int)m_dwBufferLen - (pRight - pLeft) - 1;
		int nRemainRight2End = (int)m_dwBufferLen - (pRight - m_pStart);
		int nReadedSize = recv(m_tSocket, pRight, nRemainRight2End, 0);

		nRemainRight2End = nRemainRight2End < nEmptySize ? nRemainRight2End : nEmptySize;

		if (nReadedSize == 0)
		{
			return INVALID_VALUE;
		}
		else if (nReadedSize < nRemainRight2End)
		{
			m_pRight += nReadedSize;
			return SUCCESS_VALUE;
		}
		else if (nReadedSize == nRemainRight2End)
		{
			m_pRight += nReadedSize;
		}

		if (m_pRight - m_pStart == m_dwBufferLen)
		{
			m_pRight = m_pStart;
		}

		int nNextReadSize = nEmptySize - nRemainRight2End;

		if (nNextReadSize > 0)
		{
			nReadedSize = recv(m_tSocket, pRight, nNextReadSize, 0);

			if (nReadedSize == 0)
			{
				return INVALID_VALUE;
			}
			else if (nReadedSize < nNextReadSize)
			{
				m_pRight += nReadedSize;
				return SUCCESS_VALUE;
			}
			else if (nReadedSize == nNextReadSize)
			{
				m_pRight += nReadedSize;
				printf("receive buffer is overflow!\n");
				return SUCCESS_VALUE;
			}
		}
		else
		{
			printf("receive buffer is overflow!\n");
		}
	}

	return SUCCESS_VALUE;
}

int CNetBufferBase::SendData()
{
	char* pLeft = m_pLeft;
	char* pRight = m_pRight;

	// no data
	if (pLeft == pRight)
		return SUCCESS_VALUE;

	// no wrap
	if (pLeft < pRight)
	{
		int nContentSize = pRight - pLeft;
		int nSendedSize = ::send(m_tSocket, pLeft, nContentSize, 0);

		m_pLeft += nSendedSize;
	}
	else
	{
		int nContentSize = (int)m_dwBufferLen - (pLeft - pRight);
		int nRemainLeft2End = (int)m_dwBufferLen - (pLeft - m_pStart);

		if (nContentSize > (int)m_dwMaxPackLen)
		{
			printf("temp buffer is overflow!\n");
			return INVALID_VALUE;
		}

		memcpy(m_pTemp + RB_SPACE, pLeft, nRemainLeft2End);
		memcpy(m_pTemp + RB_SPACE + nRemainLeft2End, m_pStart, nContentSize - nRemainLeft2End);
		m_pLeft = m_pLeft + nContentSize - nRemainLeft2End;

		int nSendedSize = ::send(m_tSocket, pLeft, nContentSize, 0);
		return SUCCESS_VALUE;
	}

	return SUCCESS_VALUE;
}
