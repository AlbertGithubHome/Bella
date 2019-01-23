本文件主要是对当前目录中其他文件的简单说明，用来记录sublime Text的使用过程和配置备份

# Sublime Text Build 3176 x64 Setup.exe

这个是sublime text软件的稳定版本，下载时间2019-1-12 21:08:29，软件的强大功能和常用快捷键参考[Sublime Text3使用指南](https://www.cnblogs.com/ma-dongdong/p/7653231.html)

# channel_v3.json

这个是安装Package Control以后sublime需要访问的一个文件，其中记录了可以安装的插件，但是常常因为网络问题无法访问这个文件，所以可以下载为本地文件，改为本地访问
来解决的`There are no packages available for installation`问题，具体做法参考[Sublime Text 安装插件时出现There are no packages available for installation解决步骤](https://blog.csdn.net/weixin_41762173/article/details/79382132)

# lua.exe

配置lua环境所需的软件，当前可执行文件为自己编译，使用的Lua5.3版本源代码，并且加入了Lua File System，加入lfs库主要为了使用lua-check插件，这时官网的要求，参考[lua5.3中加入lfs(luafilesystem)库](https://blog.csdn.net/qq_20363225/article/details/80806070)

# luacheck.zip

lua check 插件所需要调用的环境，参考[github源码及说明](https://github.com/mpeterv/luacheck)，配置参考[Lua在Sublime中的配置及插件推荐](https://www.onlyzyx.com/00025.html)和[sublime使用sublimelint-luacheck屏蔽指定警告](http://www.cnblogs.com/cheerupforyou/p/6592357.html)

# ctags58.zip

ctags 插件所需要调用的环境，但是生成的很多都无法跳转，需要进一步配置生成，配置方法参考[如何在sublime text中实现函数跟踪跳转(ctags)](https://blog.csdn.net/menglongfc/article/details/51141084)，改进方法参考[增强ctags对lua的支持](https://www.xuebuyuan.com/952070.html)

# zRebuildCTags.bat

配合ctags插件，手动生成tags文件，可以使ctags发挥更大的作用，调用了ctags58改进方法

# fonts

一些可以尝试的字体，可以根据自己的喜好替换

- DejaVu Sans Mono : 常用等宽字体

# Installed Packages

已经安装的插件，这些插件与以往认识的插件有些不同，他们仅仅是对已有环境的调用插件，并不会安装所以来的内容，比如SublimeLinter-luacheck插件，需要lua解释器和lua check环境，但是插件中并不包含这些内容，这些都需要提前安装好，lua和lua-check的可执行文件所在目录都要添加到环境变量Path中，才可以被 sublime text 的SublimeLinter-luacheck插件调用，其他的插件也大概如此。

- Alignment
- All Autocomplete
- ChineseLocalizations
- ColorPicker
- ConvertToUTF8
- CTags
- GMod Lua
- IMESupport
- Insert Nums
- LuaExtended
- LuaJumpDefinition
- LuaSmartTips
- MarkdownPreview
- OpenResty lua snippets
- Package Control
- PackageSync
- Starbound Lua
- SublimeLinter
- SublimeLinter-lua
- SublimeLinter-luacheck
- SublimeREPL
- Sublimerge Pro
- Sync Settings
- Theme - Windows 10
- TortoiseSVN
- Vue Syntax Highlight

# User

用户自己的配置文件，sublime的配置文件分为两部分，程序以及插件自带的默认配置和用户自己的配置，前者为只读文件，无法修改，所以要添加自定义内容只能修改用户自己的配置，并且用户自己的配置可以覆盖默认配置

配置文件目前发现3类：

1. 基础配置，以sublime-settings结尾
 - Base File.sublime-settings
 - CTags.sublime-settings
 - Localization.sublime-settings
 - Package Control.sublime-settings
 - PackageSync.sublime-settings
 - Preferences.sublime-settings
 - SublimeLinter.sublime-settings
 - Sublimerge.sublime-settings
-  SyncSettings.sublime-settings
 - TortoiseSVN.sublime-settings

2. 快捷键配置，以sublime-keymap结尾
 - Default (Windows).sublime-keymap

3. 编译系统配置，以sublime-build结尾
 - selfC.sublime-build
 - selfLua.sublime-build
 - selfPHP.sublime-build
 - selfPython.sublime-build

# User/old version sublime

这个目录保存了之前使用的sublime text版本的配置信息，用来查找对比

# User/Default (Windows).sublime-keymap

这里面是用户自己添加的所有快捷键，与默认不可修改的Default/Default (Windows).sublime-keymap文件对应，可以进行覆盖，一些重要的添加列举在此：

- [SublimeText 快速添加注释](https://blog.csdn.net/tianshan2008/article/details/48397741)，可以快速插入python文件头部说明

# User/Preferences.sublime-settings

这里面是用户自己添加的sublime text基础配置，与默认不可修改的Default/Preferences.sublime-settings文件对应，可以进行覆盖，一些重要的添加列举在此：

- 解决中文上下错位的问题参考[sublime 3143新版本中文字体上下不齐的问题](https://blog.csdn.net/qq_21108581/article/details/80357855)

# appdata_roaming_st3.zip

这个文件是一次暴力的结果，将目录`C:\Users\Administrator\AppData\Roaming\Sublime Text 3`直接打包上传，理论上新安装后的sublime text3 使用这个压缩包替换对应目录就可以直接使用、配置都是完整的

# 目前已通过Sync Settings插件同步到gist上

具体方法参考[使用 Sync Settings 同步 Sublime Text 3 设置(转)](https://www.jianshu.com/p/e27e2453d499)

