#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <signal.h>


void SignalKill( int signo )
{
	printf( "main crush, signo = %d \n", signo );
}

int main()
{

	signal( SIGURG, SignalKill );
	signal( SIGTERM, SignalKill );
	signal( SIGUSR1, SignalKill );	//<signal.h>

	printf("before while...\n");
	while(true)
	{
		sleep(1); // <unistd.h>
	}
	printf("after while...\n");

}

int main2()
{

	pid_t pid;

	if( ( pid = fork( ) ) < 0 ) //<sys/types.h> <unistd.h> 
		return 0;
	else
	{
		if( pid )
			exit( 0 );

		for(int i=0; i< 20; ++i)
			close(i);

		setsid( );
		umask( 0 );	//<sys/types.h> <sys/stat.h>

		//signal( SIGURG, SignalKill );
		//signal( SIGTERM, SignalKill );
		signal( SIGUSR1, SignalKill );	//<signal.h>
	}

	while(true)
	{
		sleep(1); // <unistd.h>
	}

}