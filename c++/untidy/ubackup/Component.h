#pragma once
#include "stdafx.h"
#include "GlobalData.h"

class CCComponent
{
public:
	CCComponent();
	~CCComponent();

private:
	char* m_pStart;
	char* m_pLeft;
	char* m_pRight;

};

// A ring buffer zone
class CRingBuffer
{
public:
	CRingBuffer();
	~CRingBuffer();

	static CRingBuffer& Singleton();
public:
	int Init(char* pStart, const DWORD dwBufferLen = 4 * MB, const DWORD dwMaxPackLen = 16 * KB);
	int ReInit();

	char* PutPack(const char* pData, const DWORD dwDataSize);
	void* GetPack(DWORD& dwDateSize);

private:
	char* PutData(const char* pLeft, char* pRight, const char* pData, const DWORD dwDataSize);
	DWORD GetPackLen(const char* pLeft, const char* pRight);

protected:
	char* m_pStart;
	char* m_pLeft;
	char* m_pRight;

	char* m_pTemp;
	char* m_pNext;

	DWORD m_dwBufferLen;
	DWORD m_dwMaxPackLen;
};

// net buffer
class CNetBufferBase : public CRingBuffer
{
public:
	CNetBufferBase() : CRingBuffer(){

};

//a network buffer
class CNetBuffer
{
public:
	CNetBuffer();
	~CNetBuffer();

	int Init(const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen, const DWORD dwMaxPackLen);
	int ReInit();

	int RedvData();
	int SendData();

	inline int GetUseState()
	{
		return m_nUseState;
	}

	inline void SetUseState(const int nState)
	{
		m_nUseState = nState;
	}

	inline SOCKET GetSocketId()
	{
		return m_nUseState;
	}

	inline void SetSocketId(const SOCKET tSocketId)
	{
		m_tSocketId = tSocketId;
	}

private:
	CRingBuffer m_cSendBuffer;
	CRingBuffer m_cRecvBuffer;

	SOCKET	m_tSocketId;
	int		m_nUseState;
};


// A thread seed
class CThreadSeed
{
private:
	enum E_TSTATE{ePrepareStart, eRunning, eStopped};
public:
	CThreadSeed();
	virtual ~CThreadSeed(){}

	// to start thread 
	int Start();
	
	// to stop thread
	int Stop();

	// to execute a global function
	virtual void* Action() = 0;
private:
	HANDLE		m_hThreadId;
	E_TSTATE	m_eThreadState;

};

template<class SourceObj>
class CThread : public CThreadSeed
{
private:
	typedef int(SourceObj::*CALLBACK_FUNC)();

	SourceObj*		m_pObj;
	CALLBACK_FUNC	m_pFunc;
	
public:
	CThread() : CThreadSeed(), m_pObj(NULL), m_pFunc(NULL){}

	void operator()(SourceObj* pObj, CALLBACK_FUNC pFunc)
	{
		m_pObj = pObj;
		m_pFunc = pFunc;
		Start();
	}

	void* Action()
	{
		if (m_pObj != NULL && m_pFunc != NULL)
		{
			(m_pObj->*m_pFunc)();
		}
		
		return NULL;
	}

	void Yeild(const DWORD dwInterval = 16)
	{
		Sleep(dwInterval);
	}

};

// center manager interface
class ICenterManager
{
public:
	ICenterManager(){}
	~ICenterManager(){}

	virtual int Start() = 0;
	virtual int Stop() = 0;

	virtual void Yeild(const DWORD dwInterval) = 0;
};

// server interface
class IServer
{
public:
	IServer(){}
	~IServer(){}

	virtual int Init(const int nMaxConnNum, const int nPort, const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen) = 0;
	virtual int Start() = 0;
	virtual int Stop() = 0;
	virtual int Release() = 0;

	virtual void Yeild(const DWORD dwInterval) = 0;
};

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
	int DelConnection();

private:

	SOCKET m_tSocketId;

	int	m_nListenPort;
	int m_nMaxConnNum;
	DWORD m_dwMaxRecvLen;
	DWORD m_dwMaxSendLen;

	CNetBuffer*	m_pNetBufferList;

};

// A single center manager class
class CCenterMgr : public ICenterManager
{
private:
	CThread<CCenterMgr> m_cLogic;

	bool	m_bRunning;
	DWORD	m_dwCounter;

	IServer* m_pServer;

public:
	CCenterMgr();
	~CCenterMgr();

	static CCenterMgr& Singleton();

	int Start();

	int Stop();

	void Yeild(const DWORD dwInterval);

private:
	// thread function
	int LogicThreadFuc();
};

ICenterManager* CreateCenterMgr();





