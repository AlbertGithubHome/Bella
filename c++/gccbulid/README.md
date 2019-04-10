# 分步编译

源文件main.c，分别使用gcc和g++分步编译，结果在c和c++两个目录下

## gcc

### 一步到位
```
gcc main.c -o main_direct
```

### 分步执行
```
gcc -E main.c -o main.i
gcc -S main.i -o main.s
gcc -c main.s -o main.o
gcc main.o -o main
```

### 文件大小

```bash
[/test/build]$ll
总用量 48
-rwxrwxr-x 1 shihengzhen shihengzhen  6550 4月  10 17:47 main
-rw-rw-r-- 1 shihengzhen shihengzhen   173 4月  10 17:46 main.c
-rwxrwxr-x 1 shihengzhen shihengzhen  6550 4月  10 17:48 main_direct
-rw-rw-r-- 1 shihengzhen shihengzhen 16802 4月  10 17:46 main.i
-rw-rw-r-- 1 shihengzhen shihengzhen  1664 4月  10 17:47 main.o
-rw-rw-r-- 1 shihengzhen shihengzhen   978 4月  10 17:47 main.s
```


## g++

### 一步到位
```
g++ main.c -o main_direct
```

### 分步执行
```
g++ -E main.c -o main.i
g++ -S main.i -o main.s
g++ -c main.s -o main.o
g++ main.o -o main
```

### 文件大小

```bash
[/test/build]$ll
总用量 48
-rwxrwxr-x 1 shihengzhen shihengzhen  6550 4月  10 17:47 main
-rw-rw-r-- 1 shihengzhen shihengzhen   173 4月  10 17:46 main.c
-rwxrwxr-x 1 shihengzhen shihengzhen  6550 4月  10 17:48 main_direct
-rw-rw-r-- 1 shihengzhen shihengzhen 16802 4月  10 17:46 main.i
-rw-rw-r-- 1 shihengzhen shihengzhen  1664 4月  10 17:47 main.o
-rw-rw-r-- 1 shihengzhen shihengzhen   978 4月  10 17:47 main.s
```