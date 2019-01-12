本文件主要是对当前目录中其他文件的简单说明，用来记录sublime Text的使用过程和配置备份

# Sublime Text.exe

这个是sublime text软件的稳定版本，下载时间2019-1-12 21:08:29

# channel_v3.json

这个是安装Package Control以后sublime需要访问的一个文件，其中记录了可以安装的插件，但是常常因为网络问题无法访问这个文件，所以可以下载为本地文件，改为本地访问

# lua.exe

配置lua环境所需的软件，当前可执行文件为自己编译，使用的Lua5.3版本源代码，并且加入了Lua File System

# luacheck.zip

lua check 插件所需要调用的环境

# ctags58.zip

ctags 插件所需要调用的环境，但是生成的很多都无法跳转

# zRebuildCTags.bat

配合ctags插件，手动生成tags文件，可以使ctags发挥更大的作用

# Installed Packages

已经安装的插件，这些插件与以往认识的插件有些不同，他们仅仅是对已有环境的调用插件，并不会安装所以来的内容，比如SublimeLinter-luacheck插件，需要lua解释器和lua check环境，但是插件中并不包含这些内容，这些都需要提前安装好，lua和lua-check的可执行文件所在目录都要添加到环境变量Path中，才可以被sublime、的SublimeLinter-luacheck插件调用，其他的插件也大概如此。

- All Autocomplete
- CTags
- LuaJumpDefinition
- LuaSmartTips
- OpenResty lua snippets
- Package Control
- Starbound Lua
- SublimeLinter
- SublimeLinter-lua
- SublimeLinter-luacheck
- Theme - Windows 10
- TortoiseSVN

# User

用户自己的配置文件，sublime的配置文件分为两部分，程序以及插件自带的默认配置和用户自己的配置，前者为只读文件，无法修改，所以要添加自定义内容只能修改用户自己的配置，并且用户自己的配置可以覆盖默认配置

配置文件目前发现3类：

1. 基础配置，以sublime-settings结尾
 - CTags.sublime-settings
 - Package Control.sublime-settings
 - Preferences.sublime-settings
 - SublimeLinter.sublime-settings
 - TortoiseSVN.sublime-settings

2. 快捷键配置，以sublime-keymap结尾
 - Default (Windows).sublime-keymap

3. 编译系统配置，以sublime-build结尾
 - selfLua.sublime-build
