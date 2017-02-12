#pragma once

#include "GlobalData.h"

// A thread seed
class CThreadSeed
{
private:
	enum E_TSTATE{ ePrepareStart, eRunning, eStopped };
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
