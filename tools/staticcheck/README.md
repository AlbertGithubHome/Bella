# 静态检查工具

## C++静态检查

- Visual Lint：是一个静态检查工具的集合，其中需要配置PC-lint、CppCheck、FxCop，个人理解这是一个工具的再封装，
 需要首先安装PC-lint、CppCheck、FxCop，然后这个VS插件会有一个配置向导将上述3个工具一次配置好，方便管理

- CppCheck：单独的这个工具也能配置成VS的插件，并且可以通过静态检查发现一些越界错误