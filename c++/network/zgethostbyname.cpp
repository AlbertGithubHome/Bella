#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include <netdb.h>
#include <arpa/inet.h>
#include <sys/socket.h>

/* Description of data base entry for a single host.  */
//struct hostent
//{
//    char *h_name;         /* Official name of host.  */
//    char **h_aliases;     /* Alias list.  */
//    int  h_addrtype;      /* Host address type.  */
//    int  h_length;        /* Length of address.  */
//    char **h_addr_list;   /* List of addresses from name server.  */
//#if defined __USE_MISC || defined __USE_GNU
//# define    h_addr  h_addr_list[0] /* Address, for backward compatibility.*/
//#endif
//};

int main(int argc, char *argv[])
{
    char buffer[1024] = {0};
    struct hostent* hptr;

    if (argc <= 1 || (hptr = gethostbyname(argv[1])) == NULL)
    {
        printf("gethostbyname error for %s. error msg is '%s'\n", argc <= 1 ? "null" : argv[1], strerror(errno));
        exit(1);
    }

    printf("gethostbyname('%s');\n", argv[1]);
    printf(">official: %s\n", hptr->h_name);
    for(char** pptr = hptr->h_aliases; *pptr != NULL; pptr++)
        printf(">[alias] : %s\n",*pptr);

    switch(hptr->h_addrtype)
    {
    case AF_INET:
    case AF_INET6:
        {
            printf(">addrtype: %s\n", hptr->h_addrtype == AF_INET ? "IPv4" : "IPv6");
            printf(">length  : %d\n", hptr->h_length);
            for(char** pptr = hptr->h_addr_list; *pptr != NULL; ++pptr)
                printf(">address : %s\n", inet_ntop(hptr->h_addrtype, *pptr, buffer, sizeof(buffer)));
        }
        break;
    default:
        printf("=>>unknown address type\n");
    break;
    }
    return 0;
}