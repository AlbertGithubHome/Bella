*本文主要总结一些用到的linux命令，做这个总结主要是为了便于后续查找，因为自己在工作过程中也用过不少的命令，一般在反复使用的那段时间，命令记得特别熟，但是稍微搁置几天就有些记不清了，所以萌生了总结到一起的想法，初步的思路就是用到哪些就记录哪些，没有什么先后顺序和层次关系，只要方便查找就好，一切为了进步！*

# 系统命令
1. 查询内核版本

- **uname -r**
- **uname -a**
- **cat /proc/version**
- **cat /etc/issue**  =>>查询发布版本
- **lsb_release -a**  =>>有些系统没有

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

2. 查看硬盘剩余情况

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

- **du -h --max-depth=1**

```shell
[shihengzhen@localhost#14:57:40#/home/shihengzhen]$sudo du -h --max-depth=1
5.0M    ./encoding
4.0K    ./.gnome2
332K    ./link_test
8.0K    ./externtest
191M    ./badoop
36K ./maptest
853M    ./svn_test
188K    ./ip_test
24K ./var_test
506M    ./hadoop
56K ./.subversion
32K ./intel
2.0M    ./r002hs
1.1G    ./software
80K ./r000hs-bad
16K ./testfriend
32K ./.intel
76K ./r001hs-bad
40K ./tmp
2.3M    ./gdbtest
34M ./logs
8.0K    ./.ssh
8.0K    ./.pki
168M    ./libtest
136K    ./ziptest
7.0G    .
```

查看当前目录下最占用硬盘的是哪个文件或者目录

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

```shell
[shihengzhen@localhost#14:01:25#/home/shihengzhen]$sudo fdisk /dev/sda1
Device contains neither a valid DOS partition table, nor Sun, SGI or OSF disklabel
Building a new DOS disklabel with disk identifier 0xb9c2964d.
Changes will remain in memory only, until you decide to write them.
After that, of course, the previous content won't be recoverable.

Warning: invalid flag 0x0000 of partition table 4 will be corrected by w(rite)

WARNING: DOS-compatible mode is deprecated. It's strongly recommended to
         switch off the mode (command 'c') and change display units to
         sectors (command 'u').

Command (m for help): i
i: unknown command

 0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris
 1  FAT12           39  Plan 9          82  Linux swap / So c1  DRDOS/sec (FAT-
 2  XENIX root      3c  PartitionMagic  83  Linux           c4  DRDOS/sec (FAT-
 3  XENIX usr       40  Venix 80286     84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
 4  FAT16 <32M      41  PPC PReP Boot   85  Linux extended  c7  Syrinx
 5  Extended        42  SFS             86  NTFS volume set da  Non-FS data
 6  FAT16           4d  QNX4.x          87  NTFS volume set db  CP/M / CTOS / .
 7  HPFS/NTFS       4e  QNX4.x 2nd part 88  Linux plaintext de  Dell Utility
 8  AIX             4f  QNX4.x 3rd part 8e  Linux LVM       df  BootIt
 9  AIX bootable    50  OnTrack DM      93  Amoeba          e1  DOS access
 a  OS/2 Boot Manag 51  OnTrack DM6 Aux 94  Amoeba BBT      e3  DOS R/O
 b  W95 FAT32       52  CP/M            9f  BSD/OS          e4  SpeedStor
 c  W95 FAT32 (LBA) 53  OnTrack DM6 Aux a0  IBM Thinkpad hi eb  BeOS fs
 e  W95 FAT16 (LBA) 54  OnTrackDM6      a5  FreeBSD         ee  GPT
 f  W95 Ext'd (LBA) 55  EZ-Drive        a6  OpenBSD         ef  EFI (FAT-12/16/
10  OPUS            56  Golden Bow      a7  NeXTSTEP        f0  Linux/PA-RISC b
11  Hidden FAT12    5c  Priam Edisk     a8  Darwin UFS      f1  SpeedStor
12  Compaq diagnost 61  SpeedStor       a9  NetBSD          f4  SpeedStor
14  Hidden FAT16 <3 63  GNU HURD or Sys ab  Darwin boot     f2  DOS secondary
16  Hidden FAT16    64  Novell Netware  af  HFS / HFS+      fb  VMware VMFS
17  Hidden HPFS/NTF 65  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE
18  AST SmartSleep  70  DiskSecure Mult b8  BSDI swap       fd  Linux raid auto
1b  Hidden W95 FAT3 75  PC/IX           bb  Boot Wizard hid fe  LANstep
1c  Hidden W95 FAT3 80  Old Minix       be  Solaris boot    ff  BBT
1e  Hidden W95 FAT1
```

5. 查看指定端口连接及数据堆积情况

- **netstat | grep 'Recv-Q\|8876'**

```shell
[shihengzhen@localhost#17:54:57#/home/shihengzhen]$netstat | grep 'Recv-Q\|8876'
Proto Recv-Q Send-Q Local Address               Foreign Address             State
tcp        0      0 192.168.1.214:8876          192.168.1.108:64711         ESTABLISHED
tcp        0    228 192.168.1.214:8876          192.168.1.151:31064         ESTABLISHED
```

本质上是netstat命令，然后通过grep过滤出标题和指定端口的行
其中"Recv-Q"和"Send-Q"指的是接收队列和发送队列。这些数字一般都应该是0。
如果不是则表示软件包正在队列中堆积。这种情况只能在非常少的情况见到。

6. 查看文件类型

- **file xxx**


```shell
[shihengzhen@localhost#20:02:20#/home/shihengzhen/test/gdbtest]$ll
总用量 76
-rwxrwxr-x 1 shihengzhen shihengzhen 47049 8月  16 19:44 a.out
-rwxr-xr-x 1 shihengzhen shihengzhen   221 8月  16 18:08 cc.sh
-rw-rw-r-- 1 shihengzhen shihengzhen 18595 8月  16 19:39 gdbhelp.txt
-rw-rw-r-- 1 shihengzhen shihengzhen   306 8月  16 19:44 main.cpp
[shihengzhen@localhost#20:03:23#/home/shihengzhen/test/gdbtest]$file a.out
a.out: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.18, not stripped
[shihengzhen@localhost#20:03:34#/home/shihengzhen/test/gdbtest]$file cc.sh
cc.sh: ASCII text
[shihengzhen@localhost#20:03:39#/home/shihengzhen/test/gdbtest]$file gdbhelp.txt
gdbhelp.txt: ASCII English text, with CRLF line terminators
[shihengzhen@localhost#20:03:51#/home/shihengzhen/test/gdbtest]$file main.cpp
main.cpp: ISO-8859 C program text
[shihengzhen@localhost#20:04:02#/home/shihengzhen/test/gdbtest]$
```
file xxx就可以查看文件的类型，只要把xxx替换成要查看的文件就可以了。


7. 建立软链接

- **ln -s source newlink**

```shell
[shihengzhen@localhost#17:28:54#/home/shihengzhen]$ll | grep git
drwxrwxr-x  3 shihengzhen shihengzhen      4096 3月  17 2017 gitproject
[shihengzhen@localhost#17:29:06#/home/shihengzhen]$ln -s gitproject gittest
[shihengzhen@localhost#17:29:37#/home/shihengzhen]$ll | grep git
drwxrwxr-x  3 shihengzhen shihengzhen      4096 3月  17 2017 gitproject
lrwxrwxrwx  1 shihengzhen shihengzhen        10 12月 18 17:29 gittest -> gitproject
```
使用的时候要注意源文件与新的链接文件的顺序，不要搞反了，个人理解硬链接类似于引用计数，软连接是一个特殊的
文本文件，其中包含指向源文件的信息'


8. 服务器之间复制文件

- **scp test.zip root@120.55.85.123:/tmp/**

如果IP正确就会提示你输入秘密，输入成功后文件被拷贝到指定位置，和本地拷贝一样不会有返回值，如果想
省略输入密码这一步可以建立公私钥或者使用sshpass来完成自动输入密码，查考[几种方法来实现scp拷贝时无需输入密码](https://blog.csdn.net/nfer_zhuang/article/details/42646849)

9. 服务器远程执行命令

- **ssh root@120.55.85.123 "cd /tmp; touch t.txt"**

上述命令执行了两条语句，用双引号包裹着，否则只会在远程机器上执行第一条，回车执行后会提示输入密码，输入成功后
便可以执行填写的命令


10. zip文件的压缩与解压

- **zip -r xxx.zip ./\***
- **unzip -r xxx.zip -d ./tmp\***

命令很简单，就是有时候参数不记得，容易把参数弄反，不清楚的时候看一下就行了，解压的时候如果是解压到指定目录
添加参数-d即可，否则就是解压到当前目录

11. 定时任务的查看与编辑

- **crontab -l**
- **crontab -e**

```shell
# 查看定时任务
[shihengzhen@localhost#13:48:51#/home/shihengzhen]$crontab -l
*/10 * * * * /bin/sh /home/shihengzhen/checkmemforlord.sh
*/1 * * * * /bin/sh /home/shihengzhen/trun.sh
*/1 * * * * /bin/sh /home/shihengzhen/t.sh

# 编辑定时任务
[shihengzhen@localhost#13:58:13#/home/shihengzhen]$crontab -e
crontab: no changes made to crontab

      1 */10 * * * * /bin/sh /home/shihengzhen/checkmemforlord.sh
      2 */1 * * * * /bin/sh /home/shihengzhen/trun.sh
      3 */1 * * * * /bin/sh /home/shihengzhen/t.sh

# 直接编辑定时任务文件
[shihengzhen@localhost#13:56:54#/home/shihengzhen]$sudo vi /var/spool/cron/shihengzhen
Error detected while processing /root/.vimrc:
line    1:
E484: Can't open file ${save}/.vimrc
Press ENTER or type command to continue

*/10 * * * * /bin/sh /home/shihengzhen/checkmemforlord.sh
*/1 * * * * /bin/sh /home/shihengzhen/trun.sh
*/1 * * * * /bin/sh /home/shihengzhen/t.sh

```

最主要的还是查看和编辑，我曾遇到过使用`crontab -e`编辑不了的情况，改成直接编辑`/var/spool/cron/xxx`文件即可
参考[Linux 定时任务](https://www.cnblogs.com/mingforyou/p/3930636.html)

11. 查看服务存在并启动

- **service xxxd status**
- **service xxxd start**

```shell
[shihengzhen@localhost#14:04:02#/home/shihengzhen]$service crond status
crond (pid  1181) 正在运行...
[shihengzhen@localhost#14:04:05#/home/shihengzhen]$service mysqld status
mysqld 已停

[shihengzhen@localhost#14:04:13#/home/shihengzhen]$service mysqld start
正在启动 mysqld：                                          [失败]
```

服务其实就是一个特定的程序，只不过用来提供某种服务，比如说mysqld就是用来提供mysql的使用服务器的，
可以直接使用`service`命令查询，并且可以启动某项服务

# 工具命令