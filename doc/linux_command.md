*本文主要总结一些用到的linux命令，做这个总结主要是为了便于后续查找，因为自己在工作过程中也用过不少的命令，一般在反复使用的那段时间，命令记得特别熟，但是稍微搁置几天就有些记不清了，所以萌生了总结到一起的想法，初步的思路就是用到哪些就记录哪些，没有什么先后顺序和层次关系，只要方便查找就好，一切为了进步！*

# 系统命令
1.查询内核版本

**uname -r**
**uname -a**
**cat /proc/version**

```shell
[shihengzhen@localhost#19:55:24#/home/shihengzhen]$uname -a
Linux localhost.localdomain 2.6.32-279.el6.x86_64 #1 SMP Fri Jun 22 12:19:21 UTC 2012 x86_64 x86_64 x86_64 GNLinux
[shihengzhen@localhost#19:55:35#/home/shihengzhen]$uname -r
2.6.32-279.el6.x86_64
[shihengzhen@localhost#19:55:46#/home/shihengzhen]$cat /proc/version
Linux version 2.6.32-279.el6.x86_64 (mockbuild@c6b9.bsys.dev.centos.org) (gcc version 4.4.6 20120305 (Red Hat4.4.6-4) (GCC) ) #1 SMP Fri Jun 22 12:19:21 UTC 2012
```
其中2.6.32-279.el6.x86_64就是版本号，一般查询工具的使用环境时用到，也可根绝内核版本确定是否可以使用某个，这次查询（2018-06-18 20:10:30）查询内核就是因为学习epoll时提到“epoll是在2.6内核中提出的，是之前的select和poll的增强版本”，所以查了下开发环境的内核版本，经确定次内核可以使用epoll



# 工具命令