#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include <sys/epoll.h>
#include <unistd.h>
#include <sys/types.h>

/*

struct sockaddr_in: #include <netinet/in.h>
bzero:              #include <string.h>
inet_pton:          #include <netinet/in.h> <sys/socket.h> <arpa/inet.h>

*/

#define SERVER_IP       "192.168.1.214"
#define SERVER_PORT     8899
#define LISTEN_NUM      10

#define EPOLL_SIZE      128
#define WAIT_EVENT_NUM  EPOLL_SIZE / 2
#define COMMON_EP_EVENT EPOLLIN | EPOLLET | EPOLLHUP | EPOLLERR

#define BUFFER_SIZE     1024