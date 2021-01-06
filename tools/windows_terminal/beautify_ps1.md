# 美化PowerShell

## 下载字体

1. 在 GitHub 下载开源 Powerline 字体，[powerline/fonts](https://github.com/powerline/fonts)
2. 在 GitHub 下载 Sarasa[更纱黑体] 字体，[Sarasa](https://github.com/be5invis/Sarasa-Gothic)，只安装其中 Sarasa Term SC 即可测试使用
3. 个人地址下载，[安装其中的Sarasa Term 系列](http://yy2.gxkjbg.com:8080/font/2020/gshtwzb_jb51.rar)

## 权限设置

以管理员权限运行PowerShell，执行下面命令

```ps1
set-executionpolicy remotesigned
```

如果不授权可能会遇到下面的错误

>. : 无法加载文件 C:\Users\Albert\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1，因为在此系统上禁止运行脚
本。有关详细信息，请参阅 https:/go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。

## 安装必要模块

```sp1
Install-Module posh-git   # 必须
Install-Module oh-my-posh # 必须

Install-Module git-aliases -AllowClobber # 可选，是安装 DirColors 的前提
Install-Module DirColors                 # 可选，让 ls 命令像 Linux 系终端一样具有多彩色
```

## 修改配置文件

```sp1
# 如果之前没有配置文件，就新建一个 PowerShell 配置文件
if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }

# 用记事本打开配置文件
notepad $PROFILE
```

在打开的文件中添加下面内容保存

```sp1
Import-Module posh-git
Import-Module oh-my-posh

Import-Module git-aliases -DisableNameChecking
Import-Module DirColors

Set-Theme PowerLine
```

至此就可以看到配置美化后的PowerShell了

[Beautiful PowerShell](https://cdn.jsdelivr.net/gh/albertgithubhome/cdn/img/powershell.png)

## 可选主题

`Agnoster`, `Avit`, `Darkblood`, `Fish`, `Honukai`, `Paradox`, `PowerLine`, `robbyrussell`, `Sorin`, `tehrob`

以上主题由 `oh my posh` 默认提供，使用 `Set-Theme Agnoster` 命令就可以切换
