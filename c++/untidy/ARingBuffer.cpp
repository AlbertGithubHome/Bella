
#include "stdafx.h"
#include "ARingBuffer.h"

CRingBuffer::CRingBuffer()
{
}


CRingBuffer::~CRingBuffer()
{
}

int CRingBuffer::Init(char* pStart, const DWORD dwBufferLen, const DWORD dwMaxPackLen)
{
	if (dwBufferLen < dwMaxPackLen * 2 + RB_SPACE)
		return INVALID_VALUE;

	pStart = new char[dwBufferLen];

	if (pStart == NULL)
		return INVALID_VALUE;

	memset(pStart, 0, dwBufferLen);

	m_pStart = m_pLeft = m_pRight = m_pNext = pStart;
	m_pTemp = m_pStart + dwMaxPackLen + RB_SPACE;

	m_dwBufferLen = dwBufferLen - dwMaxPackLen - RB_SPACE;
	m_dwMaxPackLen = dwMaxPackLen;

	return SUCCESS_VALUE;
}

int CRingBuffer::ReInit()
{
	if (m_pStart == NULL)
		return INVALID_VALUE;

	m_pLeft = m_pRight = m_pNext = m_pStart;
	m_pTemp = m_pStart + m_dwBufferLen + RB_SPACE;

	return SUCCESS_VALUE;
}

char* CRingBuffer::PutPack(const char* pData, const DWORD dwDataSize)
{
	if (pData == NULL)
		return NULL;

	DWORD dwRemainEmptySize = 0;
	if (m_pLeft <= m_pRight)
		dwRemainEmptySize = m_dwBufferLen - (m_pRight - m_pLeft) - 1;
	else
		dwRemainEmptySize = m_pRight - m_pLeft - 1;

	if (dwRemainEmptySize < dwDataSize + PACK_HEADER_SIZE)
	{
		printf("The RingBuffer is overflow!\n");
		return NULL;
	}

	char *pLeft = m_pLeft, *pRight = m_pRight;

	// 写入数据长度
	pRight = PutData(pLeft, pRight, (const char*)&dwDataSize, PACK_HEADER_SIZE);

	if (pRight == NULL)
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

	if (pLeft <= pRight)
		dwRemainDataLen = pRight - pLeft;
	else
		dwRemainDataLen = m_dwBufferLen - (pLeft - pRight);

	// 剩余数据的长度小于数据头所记录的长度
	if (dwRemainDataLen < dwDateSize + PACK_HEADER_SIZE)
	{
		dwDateSize = 0;
		return NULL;
	}

	DWORD dwRemainLeft2End = m_dwBufferLen - (m_pLeft - m_pStart);

	// 数据环绕
	if (pLeft > pRight && dwRemainLeft2End < dwDateSize + PACK_HEADER_SIZE)
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

CNetBuffer::CNetBuffer()
{

}

CNetBuffer::~CNetBuffer()
{

}

int CNetBuffer::Init(const SOCKET tSocket, const DWORD dwMaxRecvLen, const DWORD dwMaxSendLen, const DWORD dwMaxPackLen)
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
	if (m_nUseState == 0)
	{
		closesocket(m_tSocketId);
		m_nUseState = -1;
	}

	return SUCCESS_VALUE;
}
