#include "common.h"

int main(int argc, char * argv[])
{
	int listen_fd = socket(AF_INET, SOCK_STREAM, 0);
	printf("fd = %d\n", listen_fd);
	
	listen_fd = socket(AF_INET, SOCK_STREAM, 0);
	printf("fd = %d\n", listen_fd);

	listen_fd = socket(AF_INET, SOCK_STREAM, 0);
	printf("fd = %d\n", listen_fd);

	listen_fd = socket(AF_INET, SOCK_STREAM, 0);
	printf("fd = %d\n", listen_fd);

	FILE* fp = fopen("in.txt", "w");
	fp = fopen("in.txt", "w");
	fp = fopen("in.txt", "w");

	listen_fd = socket(AF_INET, SOCK_STREAM, 0);
	printf("fd = %d\n", listen_fd);


	return 0;
}
