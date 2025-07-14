

# bat语法



## 注释



```powershell
::注释

rem 注释
```



## 输出文字

```bash
echo "hello world"
```

## 防止窗体关闭

```powershell
pause
```



## 关闭回显



默认开启，可以手动关闭

```powershell
@echo off	#从本行开始关闭回显。一般批处理第一行都是这个
echo off    #从下一行开始关闭回显
echo        #显示当前是 echo off 状态还是 echo on 状态
```



## 设置变量

```powershell
set 变量名=变量值
```

## 调用变量

```powershell
%变量名%
```

## 显示文件夹的树状结构

```powershell
tree d:  #d盘的目录结构
```



## 进入文件夹

```shell
cd
```





## 设置cmd窗口的标题

```powershell
title 新标题          #可以看到cmd窗口的标题栏变了
```



## 显示系统版本

```powershell
ver
```





## 显示卷标

```powershell
vol  d:                 #显示D盘的名字
```



```powershell
label   d:              #显示卷标，同时提示输入新卷标
```

# 逻辑运算符

## &

顺序执行多条命令，而不管命令是否执行成功

```powershell
qjwheriuw & echo 虽然前面的命令有问题，但是我还是执行了
```



## &&

顺序执行多条命令，当碰到执行出错的命令后将不执行后面的命令

```powershell
qjwheriuw && echo 前面的命令有问题，我g了
```

## ||

顺序执行多条命令，当碰到执行正确的命令后将不执行后面的命令





# 变量控制

