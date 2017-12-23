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
    #define MAXBUF 1024

    int main(int argc, char **argv)  
    {  
        printf("this is a test server\n");
        int sockfd, new_fd;  
        socklen_t len;  

        struct sockaddr_in my_addr, their_addr;  // IPv4  
        unsigned int myport, lisnum;  

        if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {  // IPv4  
            perror("socket");
            printf("create socket error\n");
            exit(1);  
        } else  
            printf("socket created\n");

        bzero(&my_addr, sizeof(my_addr));  
        my_addr.sin_family = AF_INET;           // IPv4  
        my_addr.sin_port = htons(atoi(argv[1]));         // IPv4  
        my_addr.sin_addr.s_addr = INADDR_ANY;   // IPv4  

        if (bind(sockfd, (struct sockaddr *) &my_addr, sizeof(my_addr)) == -1) { // IPv4 
            perror("bind");
            exit(1);
        } else  
            printf("binded\n");
      
        if (listen(sockfd, 100) == -1) {
            perror("listen");
            exit(1);
        } else
            printf("begin listen %d, %d\n", atoi(argv[1]), 100);  
      
        while (1) {  
            len = sizeof(struct sockaddr);
            if ((new_fd =  accept(sockfd, (struct sockaddr *)&their_addr,  &len)) == -1)
            {  
                perror("accept");
                exit(errno);  
            }
            else
            {
                printf("server: got connection from %s, port %d, socket %d\n",  inet_ntoa(their_addr.sin_addr), ntohs(their_addr.sin_port), new_fd); // IPv4  
            }
        }  
      
        close(sockfd);  
        return 0;  
    }  