#include <stdio.h>  
#include <stdlib.h>  
#include <errno.h>  
#include <string.h>  
#include <sys/types.h>  
#include <netinet/in.h>  
#include <sys/socket.h>  
#include <sys/wait.h>  
#include <unistd.h>  
#include <arpa/inet.h>
#include <netdb.h>
#define MAXBUF 1024

int main(int argc, char **argv)
{  
        //连接ip  
    char ip[128] = "www.baidu.com";
    void* svraddr = NULL;
    int error=-1, svraddr_len;
    struct sockaddr_in svraddr_4;
    struct sockaddr_in6 svraddr_6;

    printf("test target ip is %s\n", ip);
  
    //获取网络协议  
    struct addrinfo *result;
    error = getaddrinfo(ip, NULL, NULL, &result);
    socklen_t maxlen = 128;
    switch(result->ai_addr->sa_family) {
        case AF_INET://ipv4
            printf("current network is IPV4\n");
            break;
        case AF_INET6://ipv6
            printf("current network is IPV6\n");
            break;
        default:
            printf("Unknown AF\ns");
            break;
    }  
    freeaddrinfo(result);
}
