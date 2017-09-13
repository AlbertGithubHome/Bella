#include "zthread.h"

#ifdef OS_WINDOWS
static DWORD WINAPI thread_process(void* param)
{
	zthread* thread = (zthread*)param;
	thread->action();
	return 0;
}
#endif


zthread::zthread()
{
	thread_status = justcreated;
}

zthread::~zthread()
{
#ifdef OS_WINDOWS
	if (thread_status == running)
	{
		TerminateThread(thread_id, 0);
	}
#endif
}

int zthread::start()
{
#ifdef OS_WINDOWS
	if (thread_status == justcreated)
	{
		thread_id = CreateThread(NULL, 0, thread_process, this, 0, NULL);
		if (thread_id){
			thread_status = running;
			return 0;
		}
	}
#endif
	return -1;
}

int zthread::stop()
{
#ifdef OS_WINDOWS
	if (thread_status == running)
	{
		TerminateThread(thread_id, 0);
		thread_status = stopped;
		return 0;
	}
#endif
	return 0;
}
