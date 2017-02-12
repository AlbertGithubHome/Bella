#pragma once

#include "GlobalData.h"
// a network server
class CNetServer : public IServer
{
public:
	CNetServer();
	~CNetServer();

	int Init(const int nMaxConnNum, const int nPort, const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen);

	int Start();

	int Stop();

	int Release();

	void Yeild(const DWORD dwInterval);

private:

	CThread<CNetServer> m_cNetServerListen;
	CThread<CNetServer> m_cNetServerRead;
	CThread<CNetServer> m_cNetServerWrite;

	int ListenThreadFunc();
	int ReadThreadFunc();
	int WriteThreadFunc();

	int AddConnection(SOCKET tSocketId);
	int DelConnection(const int nConnectIndex);

private:

	SOCKET m_tSocketId;

	int	m_nListenPort;
	int m_nMaxConnNum;
	DWORD m_dwMaxRecvLen;
	DWORD m_dwMaxSendLen;

	CNetBuffer*	m_pNetBufferList;

};
