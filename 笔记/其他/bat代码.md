# 基础格式

`@echo off`可以在输出命令的时候不显示盘符路径

`echo` 可以输出语句

`pause`可以使屏幕在执行完之后不会退出

```shell
@echo off
echo "hello world" 
pause
```

# 命令查询

如果忘记了命令，可以使用`/?`来查询命令

```shell
color /?
```



# 变量与传参



## 使用变量

使用变量的时候使用两个`%`来把变量包裹起来。

```shell
@echo off
set /a num = 1+2
echo %num% 
pause
```

## 接收参数

如果想要使用外部的参数，就需要用`%`来表示，1表示第一个，2表示第二个

```shell
rem 加法函数
@echo off
set /a num = %1+%2 
echo %num%
pause 
```

在使用时，传进来的参数用空格来分隔

```sh
rem 调用方法，传入1和2，并执行加法语句
test.bat 1 2
```



# 运算符

- 算术运算

  ```shell
  set /a 1+1
  ```




- 将数据覆盖读入文件

  ```shell
  echo "hello world" > test.txt
  ```

- 将数据追加到文件

  ```shell
  echo "hello world2" >> test.txt
  ```

- 查看文件内容

  ```powershell
  type test.txt
  ```

- 与运算符

  如果第一个错了，那么逻辑短路。都不执行

  如果第一个对，第二个错，那么执行第一个。

  ```shell
  set /a 1+1 && set /a 1+1
  ```

- 或运算符

  如果两个命令有一个对，那么就执行那个

  都对的话，逻辑短路，只执行第一个。

  ```
  set /a 1+1 || set /a 1+1
  ```

- 查找当前目录所有文件

  ```shell
  dir
  ```

- 筛选文件

  查找文件名中包含txt的文件

  ```powershell
  dir find|"txt"
  ```

  

- 注释

  ```shell
  rem 注释内容
  
  ```

  

# 用户相关

## 创建用户

```powershell
@echo off
net user "用户名" "密码" /add
pause
```

## 删除用户

```sh
@echo off
net user "用户名" /delet
pause
```

# 终端的样式

```shell
rem 更改颜色
color 07

rem 更改窗口标题
title test
```

# 时间相关

```shell
rem 查询时间，格式是年月日 星期
date /T
rem 修改时间
date

rem 查询时间，格式是下午几点
time /T
rem 修改时间
time 
```



# 附录1——常用的命令

这些命令可以直接用<kbd>win</kbd>+<kbd>r</kbd>打开。

| 命令    | 效果       |
| ------- | ---------- |
| calc    | 打开计算器 |
| notepad | 打开记事本 |
| mstsc   | 远程桌面   |
|         |            |
|         |            |
|         |            |
|         |            |
|         |            |

# 附录2 ——常用的shell命令





| cmd命令  |              |
| -------- | ------------ |
| cls      | 清屏         |
| ipconfig | 查看网络信息 |
|          |              |
|          |              |
|          |              |
|          |              |
|          |              |
|          |              |
|          |              |

