// templateStaticInit.cpp : 定义控制台应用程序的入口点。
//
#include <stdio.h>
#include "templateStaticInit.h"


int main(int argc, char* argv[])
{
	TimerApp<CMsgHdl> test;
	printf("test.interval_ = %d\n", test.GetInterval());

	CMsgHdl msgHdl;

	TimerApp<CMsgHdl>::AddTimer(6, &msgHdl);
	msgHdl.handlemsg();
	
	
	TimerApp<CMsgHdl>::AddMethod(&CMsgHdl::handlemsg);

	test.execute();
	

	return 0;
}

