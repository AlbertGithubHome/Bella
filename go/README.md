# go 语言学习

> go go go go go go go go go
> go go go go go go go go
> go go go go go go go
> go go go go go go
> go go go go go
> go go go go
> go go go
> go go
> go

## 居然没有三目运算符

go语言居然没有三目运算符，这让人有点想不通，这么优秀的语法为啥要去掉呢？那我以后怎么用一行代码解决约瑟夫环来装X啊？

```c++
int joseph_ring(int n, int m) {
    return n == 1 ? 0 : (joseph_ring(n - 1, m) + m) % n
}
```

写成go版本居然要这么长，有些让人难以接受

```golang
func JosephRing(n int, m int) int {
    if n == 1 {
        return 0
    }

    return (JosephRing(n - 1, m) + m) % n
}
```
