
#include "stdafx.h"
#include "AServer.h"


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