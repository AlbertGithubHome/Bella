# git 常用配置说明

## 名字和邮件

git作为分布式版本控制系统，需要在你提交修改是时知道你是谁，每个机器都必须自报家门，提交之前首先配置你的name和email，如果你不配置，在提交时会受到下面的提醒：

```bash
$ git commit -m"update README file"

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'albert@homepc.(none)')
```

当然这个设置内容全凭自愿，你设置成什么都可以，可是如果你真的想参与开源项目或者维护团队项目，这个名字和邮箱最好是有意义，随便设置带来的问题就是没人知道修改代码的是谁，比如我把我的名字和邮箱都设置成`111`，得到了下面的记录：

```bash
$ git log -1
commit 220aee4d2ce810e2c65e9e095ecafc3f4526c5bf (HEAD -> feature)
Author: 111 <111>
Date:   Sun Mar 29 18:19:12 2020 +0800

    update README file
```

从日志上根本不知道是谁改的，所以我还是规规矩矩的修改成自己的信息吧，像下面这样：

```bash
$ git config --global user.name "albert"
$ git config --global user.email "alberts52190@gmail.com"
```

# 换行符

为什么换行符要单独拿来配置，主要的原因就是这个换行符在不同的系统上要求不一样，据说这来源于计算机出现之前的电传打字机，当时出现了“回车”和“换行”的概念，之后这两个概念被搬到了计算机上。但在那个存储器很贵的时代，有些人认为在每行结尾加两个字符太浪费了，决定使用一个，于是就产生了不同换行方式的分歧。

在计算机中，虽然换行方式有多种，但是涉及换行的字符只有两个：

- 回车符 CR (Carriage Return)，ASCII 码为 0x0D，转义字符为\r。
- 换行符 LF (NL line feed, new line)，ASCII 码为 0x0A，转义字符为\n。

换行方式的不同主要表现在不同的操作系统上，常见的换行方式有：

- CR + LF：DOS/Windows；
- LF：Unix/Linux、macOS；
- CR：Mac OS 9 以前。

介绍了这么多背景，终于要说到 git 中为什么要配置换行符了，其实了解了背景之后就明白其中的原因了，git 是一套分布式版本控制系统，这意味着会有很多人共同参与一个项目的开发，这种情况下就会出现不同的人使用不同的系统来编辑项目，而不同的系统中换行标准是不一样的，可能会造成代码样式的混乱，比如在 linux 上编辑的文件，在 windows 上会显示成一行，而在 windows 上编辑的文件到了 linux 上又会在结尾出现 `^M` 符号。

我们在 git 配置文件中提前配置换行参数就是为了避免这种情况，一般地，提交到代码库中的格式应保证是 `LF` 结尾，在本地开发时保持自己的换行格式就可以，这时可以通过参数配置达到这种目的。

如果是在Windows系统上，应该按照以下命令设置，这样在签出代码时把 `LF` 转换成 `CRLF`，在你提交时自动地把行结束符 `CRLF` 转换成 `LF`：
```bash
$ git config --global core.autocrlf true
```

如果在Linux或Mac系统上，应该将 `core.autocrlf` 的值设置成 `input` ，会在提交时把 `CRLF` 转换成 `LF`，而在签出时不做转换：

```bash
$ git config --global core.autocrlf input
```

如果就想保留原有的换行方式，或者你是Windows程序员，并且正在开发仅运行在Windows上的项目，可以将 `core.autocrlf` 的值设置成 `false`，或者干脆不设置这个值，这样允许把回车符记录在库中：

```bash
$ git config --global core.autocrlf false
```

# 别名

在 linux 系统中很多长长的命令总是会被人起一个别名，这样方便记忆和输入，而在 git 的使用中也常常需要设置别名，比如一个查看工作目录状态的 `git status` 每天要输入很多遍可以起一个别名，用 `git st` 来代替 `git status`，具体的设置方法如下：

```bash
$ git config --global alias.st "status"
```

### 查看日志

```bash
$ git config --global alias.adog "log --all --decorate --oneline --graph"
```

## 完整更新内容及子模块

```bash
$ git config --global alias.pullall "!f() { git pull "$@" && git submodule update --init --recursive; }; f"
```

# `.gitconfig` 文件

最新文件配置如下，持续更新中...

```bash
[user]
    name = albert
    email = alberts52190@gmail.com
[core]
    autocrlf = true
[alias]
    st = status
    adog = "log --all --decorate --oneline --graph"
    pullall = "!f() { git pull "$@" && git submodule update --init --recursive; }; f"
```