
#include "stdafx.h"
#include "AThread.h"

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
