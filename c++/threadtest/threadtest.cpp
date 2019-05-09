#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

static void* thread_proc(void* arg)
{
	unsigned int sum = 3;
	while(true)
	{
		for (int idx = 0; idx < 1000000000; ++idx)
			sum += idx;

		printf("thread sum = %u\n", sum);
		sleep(2);
	}

	return 0;
}

int main()
{
	pthread_t thread_id;
	pthread_create(&thread_id, NULL, thread_proc, NULL);
	unsigned int sum = 0;

	while(true)
	{
		for (int idx = 0; idx < 1000000000; ++idx)
			sum += idx;

		printf("main sum = %u\n", sum);
		sleep(1);
	}

	return 0;
}
