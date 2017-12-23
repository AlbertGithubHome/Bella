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
        //struct sockaddr_in6 my_addr, their_addr; // IPv6  
      
        unsigned int myport, lisnum;  
        char buf[MAXBUF + 1];  
      
        if (argv[1])  
            myport = atoi(argv[1]);  
        else  
            myport = 8876;  
      
       // if (argv[2])  
        //    lisnum = atoi(argv[2]);  
        //else  
        lisnum = 100;  
      
        if ((sockfd = socket(PF_INET, SOCK_STREAM, 0)) == -1) {  // IPv4  
        // if ((sockfd = socket(PF_INET6, SOCK_STREAM, 0)) == -1) { // IPv6  
            perror("socket");
            printf("create socket error\n");
            exit(1);  
        } else  
            printf("socket created\n");

        printf("create complete\n");
      
        bzero(&my_addr, sizeof(my_addr));  
        my_addr.sin_family = PF_INET;  // IPv4  
        //my_addr.sin6_family = PF_INET6;    // IPv6  
        my_addr.sin_port = htons(myport);    // IPv4  
        //my_addr.sin6_port = htons(myport);   // IPv6  
        if (argv[3])  
            my_addr.sin_addr.s_addr = inet_addr(argv[3]); // IPv4  
            //inet_pton(AF_INET6, argv[3], &my_addr.sin6_addr);  // IPv6  
        else  
            my_addr.sin_addr.s_addr = INADDR_ANY; // IPv4  
           // my_addr.sin6_addr = in6addr_any;            // IPv6  
      
        if (bind(sockfd, (struct sockaddr *) &my_addr, sizeof(struct sockaddr))  // IPv4  
        //if (bind(sockfd, (struct sockaddr *) &my_addr, sizeof(struct sockaddr_in6))  // IPv6  
            == -1) {  
            perror("bind");  
            exit(1);  
        } else  
            printf("binded\n");  
      
        if (listen(sockfd, lisnum) == -1) {  
            perror("listen");  
            exit(1);  
        } else  
            printf("begin listen %d, %d\n", myport, lisnum);  
      
        while (1) {  
            len = sizeof(struct sockaddr);  
            if ((new_fd =  
                 accept(sockfd, (struct sockaddr *) &their_addr,  
                        &len)) == -1) {  
                perror("accept");  
                exit(errno);  
            } else  
                printf("server: got connection from %s, port %d, socket %d\n",  
                        inet_ntoa(their_addr.sin_addr),  // IPv4  
                       //inet_ntop(AF_INET6, &their_addr.sin6_addr, buf, sizeof(buf)), // IPv6  
                        ntohs(their_addr.sin_port), new_fd); // IPv4  
                       //their_addr.sin6_port, new_fd); // IPv6  
                       //
            printf("accept connect\n");
      
            /* 开始处理每个新连接上的数据收发 */  
            bzero(buf, MAXBUF + 1);  
            strcpy(buf,  
                   "这是在连接建立成功后向客户端发送的第一个消息/n只能向new_fd这个用accept函数新建立的socket发消息，不能向sockfd这个监听socket发送消息，监听socket不能用来接收或发送消息/n");  
            /* 发消息给客户端 */  
            len = send(new_fd, buf, strlen(buf), 0);  
            if (len < 0) {  
                printf  
                    ("消息'%s'发送失败！错误代码是%d，错误信息是'%s'\n",  
                     buf, errno, strerror(errno));  
            } else  
                printf("消息'%s'发送成功，共发送了%d个字节！\n",  
                       buf, len);  
      
            bzero(buf, MAXBUF + 1);  
            /* 接收客户端的消息 */  
            len = recv(new_fd, buf, MAXBUF, 0);  
            if (len > 0)  
                printf("接收消息成功:'%s'，共%d个字节的数据\n",  
                       buf, len);  
            else  
                printf  
                    ("消息接收失败！错误代码是%d，错误信息是'%s'\n",  
                     errno, strerror(errno));  
            /* 处理每个新连接上的数据收发结束 */  
        }  
      
        close(sockfd);  
        return 0;  
    }  