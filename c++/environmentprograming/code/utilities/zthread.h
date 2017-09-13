#ifndef __Z_THREAD_H__
#define __Z_THREAD_H__

#ifdef OS_WINDOWS
#include <Windows.h>
#else
#include <pthread.h>
#endif

class zthread
{
public:
	zthread();
	virtual ~zthread();

	int start();
	int stop();
	virtual void* action() = 0;

private:
	enum ethread_status {justcreated, running, stopped};
	ethread_status thread_status;
#ifdef OS_WINDOWS
	HANDLE		thread_id;
#else
	pthread_t	thread_id;
#endif
};

#endif//__Z_THREAD_H__