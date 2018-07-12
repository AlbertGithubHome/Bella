#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>

//struct addrinfo
//{
//    int ai_flags;             /* customize behavior */
//    int ai_family;            /* address family */
//    int ai_socktype;          /* socket type */
//    int ai_protocol;          /* protocol */
//    socklen_t ai_addrlen;     /* length in bytes of address */
//    struct sockaddr *ai_addr; /* address */
//    char *ai_canonname;       /* canonical name of host */
//    struct addrinfo *ai_next; /* next in list */
//};

int main(int argc, char *argv[])
{
    struct addrinfo hints;
    struct addrinfo *result, *rp;
    char buffer[512];
 
    if (argc < 2)
    {
        printf("Usage: %s host name or ip\n", argv[0]);
        exit(1);
    }
    printf("getaddrinfo('%s', NULL, ...);\n", argv[1]);

    memset(&hints, 0, sizeof(struct addrinfo));
    hints.ai_family = AF_UNSPEC;    /* Allow IPv4 or IPv6 */
    hints.ai_socktype = SOCK_STREAM;/* Stream socket */
    hints.ai_flags = AI_PASSIVE;    /* For wildcard IP address */
    hints.ai_protocol = 0;          /* Any protocol */
    hints.ai_canonname = NULL;
    hints.ai_addr = NULL;
    hints.ai_next = NULL;

    int ret = getaddrinfo(argv[1], NULL, &hints, &result);
    if (ret != 0)
    {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(ret));
        exit(1);
    }

    for (rp = result; rp != NULL; rp = rp->ai_next)
    {
        printf(">[%s] %s\n", rp->ai_family == AF_INET ? "IPv4" : "IPv6",
            inet_ntop(rp->ai_family, 
                rp->ai_family == AF_INET ? (const char *)(&(((struct sockaddr_in *)(rp->ai_addr))->sin_addr)) : \
                (const char *)(&(((struct sockaddr_in6 *)(rp->ai_addr))->sin6_addr)),
                buffer, sizeof(buffer)));
    }

    freeaddrinfo(result);           /* No longer needed */
    return 0;
}

/*
[xxx]$$./zgetaddrinfo www.zhihu.com
getaddrinfo('www.zhihu.com', NULL, ...);
>[IPv4] 118.89.204.190
>[IPv4] 118.89.204.100
>[IPv4] 118.89.204.109
*/