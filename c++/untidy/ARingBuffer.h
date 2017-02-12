#pragma once

#include "GlobalData.h"

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
	CNetBufferBase() : CRingBuffer(){}
	~CNetBufferBase(){}

	int Init(const SOCKET tSocket, char* pStart, const DWORD dwBufferLen = 4 * MB, const DWORD dwMaxPackLen = 16 * KB);
	int ReInit(const SOCKET tSocket);

	int RecvData();
	int SendData();


private:
	SOCKET m_tSocket;

};

//a network buffer
class CNetBuffer
{
public:
	CNetBuffer();
	~CNetBuffer();

	int Init(const SOCKET tSocket, const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen, const DWORD dwMaxPackLen);
	int ReInit(const SOCKET tSocket);

	int Close();

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
public:
	CNetBufferBase m_cSendBuffer;
	CNetBufferBase m_cRecvBuffer;

private:

	SOCKET	m_tSocketId;
	int		m_nUseState;
};