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
git config --global user.name "albert"
git config --global user.email "alberts52190@gmail.com"
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
    adog = "log --all --decorate --oneline --graph"
    pullall = "!f() { git pull "$@" && git submodule update --init --recursive; }; f"
```