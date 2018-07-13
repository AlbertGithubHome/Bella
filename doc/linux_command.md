*本文主要总结一些用到的linux命令，做这个总结主要是为了便于后续查找，因为自己在工作过程中也用过不少的命令，一般在反复使用的那段时间，命令记得特别熟，但是稍微搁置几天就有些记不清了，所以萌生了总结到一起的想法，初步的思路就是用到哪些就记录哪些，没有什么先后顺序和层次关系，只要方便查找就好，一切为了进步！*

# 系统命令
1.查询内核版本

- **uname -r**
- **uname -a**
- **cat /proc/version**

```shell
[shihengzhen@localhost#20:16:15#/home/shihengzhen]$date
2018年 06月 28日 星期四 20:16:19 CST
[shihengzhen@localhost#20:16:19#/home/shihengzhen]$uname -r
2.6.32-279.el6.x86_64
[shihengzhen@localhost#20:16:23#/home/shihengzhen]$uname -a
Linux localhost.localdomain 2.6.32-279.el6.x86_64 #1 SMP Fri Jun 22 12:19:21 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux
[shihengzhen@localhost#20:16:25#/home/shihengzhen]$cat /proc/version
Linux version 2.6.32-279.el6.x86_64 (mockbuild@c6b9.bsys.dev.centos.org) (gcc version 4.4.6 20120305 (Red Hat 4.4.6-4) (GCC) ) #1 SMP Fri Jun 22 12:19:21 UTC 2012
[shihengzhen@localhost#20:16:28#/home/shihengzhen]$
```

其中 2.6.32-279.el6.x86_64 就是版本号，一般查询工具的使用环境时用到，也可根据内核版本确定是否可以使用某个工具，这次查询（2018-06-18 20:10:30）查询内核就是因为学习epoll时，有一句话提到“epoll是在2.6内核中提出的，是之前的select和poll的增强版本”，所以查了下开发环境的内核版本，经确定此内核可以使用epoll

2.查看硬盘剩余情况

- **df -TH**

```shell
[shihengzhen@localhost#12:20:24#/tmp]$df -TH
文件系统    类型      容量  已用  可用 已用%% 挂载点
/dev/mapper/VolGroup-lv_root
              ext4      53G    51G      0 100% /
tmpfs        tmpfs     4.2G      0   4.2G   0% /dev/shm
/dev/sda1     ext4     508M    33M   449M   7% /boot
/dev/mapper/VolGroup-lv_home
              ext4      83G    33G    47G  42% /home
```

3. 查看磁盘空间占用

- **du -m**

```shell
[shihengzhen@localhost#20:50:24#/home/shihengzhen/test]$du -m
1   ./epoll_cs_demo
1   ./mysql/include/mysql
1   ./mysql/include
1   ./mysql
1   ./network
1   ./linux_version
1026    ./so/withoutvoice
1027    ./so/withvoice
3970    ./so
1   ./logs
22915   .
```
与df命令不同的是Linux du命令是对文件和目录磁盘使用的空间的查看

4. 查看硬盘信息

- **fdisk -l**
- **sudo fdisk -l**

```shell
[shihengzhen@localhost#12:27:06#/home/shihengzhen]$sudo fdisk -l

Disk /dev/sda: 146.8 GB, 146815733760 bytes
255 heads, 63 sectors/track, 17849 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x7960ae01

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *           1          64      512000   83  Linux
Partition 1 does not end on cylinder boundary.
/dev/sda2              64       17850   142861312   8e  Linux LVM

Disk /dev/mapper/VolGroup-lv_root: 53.7 GB, 53687091200 bytes
255 heads, 63 sectors/track, 6527 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/mapper/VolGroup-lv_swap: 8388 MB, 8388608000 bytes
255 heads, 63 sectors/track, 1019 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000


Disk /dev/mapper/VolGroup-lv_home: 84.2 GB, 84213235712 bytes
255 heads, 63 sectors/track, 10238 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000
```
如果直接执行没有输出任何信息应该是没有权限，尝试用root用户执行

# 工具命令