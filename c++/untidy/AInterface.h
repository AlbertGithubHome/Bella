#pragma once

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