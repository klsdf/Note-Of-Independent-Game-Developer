# 基础语法




```matlab
clear all %清除工作区
clc %清除命令行
```

## 函数

```matlab
function [new_image]  = my_imadjust(image,a,b,c,d)
L = 256;
[row,column]=size(image);
-----------------------------------   

for i = 1:row
    for j = 1:column
        if image(i,j)>=0 && image(i,j)<a
            new_image(i,j)= (c/a)*image(i,j);
        elseif image(i,j)>=a && image(i,j)<b
            new_image(i,j)= ((d-c)/(b-a))*(image(i,j)-a)+b;
        elseif image(i,j)>=b && image(i,j)<L
            new_image(i,j)= ((L-1-d)/(L-1-b))*(image(i,j)-b)+d;
        end
       
    end
end
```



# 数据类型

## 字符串与字符数组

在matlab中，双引号是字符串，单引号是字符数组。

```matlab
a="hello world" %字符串
size(a)

b= 'hello world' %字符数组
size(b)


%输出
a = 
    "hello world"

ans =
     1     1

b =
    'hello world'

ans =
     1    11

```

可以看到字符串是一行一列的，但是字符数组的每一个字符都需要占一列。





```matlab
%从左侧删除所有填充字符
substr = strip(str,'left','S');
str2num
```



## 元胞数组

实际上是一种广义矩阵，元胞数组可以存储任何一种常量。









```matlab
A= {...
    [1,2,3;4,5,6;7,8,9;],...
    "hello world",...
    123}
%访问某一个单元
A(3)

%访问某一个单元的数据
A{3}

```



## 结构体

```matlab
test = struct("key","value2","key2","value2","key3",[1,2,3;4,5,6])
```

结构体直接按照一个key一个value的顺序来构造就可以了。

对结构体的访问直接用点运算符就行。

```matlab
test.key
```



# 运算符

## 冒号运算符

## 比较运算符

### 向量比较

对于一个行向量使用比较运算符，也会返回行向量

```matlab
x = [1,2,3,4,5];
x>=3
```

 0   0   1   1   1



如果对行向量自己使用这个结果，那么可以输出其子集。

```matlab
% 输出x大于三的子集
x = [1,2,3,4,5]
x(x>=3)
```



### 矩阵比较

对于矩阵使用比较运算符，会返回列向量

```matlab
A = [1,2;3,4]
B = [33,11;53,42]
A(A>=2)
B(A>=2)

%输出
A =
     1     2
     3     4

B =
    33    11
    53    42

ans =
     3
     2
     4

ans =
    53
    11
    42
```







# 数组与字符串的切割

一个字符串可以直接用圆括号进行切割，

```

```



# 矩阵

## 矩阵的构造

```matlab
A = [1,2,3,4,5]
B = 1:3 
C = ones(2,4) %用1来填充指定大小的矩阵
```





## 矩阵的运算

```matlab
A = [1,2,3;
	4,5,6;
	7,8,9]
B= [1,2,3;
	4,5,6;
	7,8,9]
A = A+3 %每个元素+3
A = A' %求转置
[D,V] = eig(A) %特征值和特征向量
E = inv(A) %逆矩阵

A = A*A %矩阵叉乘
A = A.*A %矩阵点乘

X=A\B %A的逆矩阵乘以B

```



## find

```matlab
[m,n] = find(A>20) %找到大于20的数据，并把坐标存到mn里面
```

## 最大值与最小值

```matlab
y =max(A) %返回A的最大值
[y,k]=max(A) %b
```



# 画图

也可以同时绘制多张图

- 线型图

```matlab
x = 0:0.05:100;
y1 = sin(x);
y2 = cos(x);
plot(x,y1,x,y2,"linewidth",2)  %绘制两幅图，linewidth控制线条粗细，可以省略
axis([0,5,-1,1]) %设置横坐标范围[0,5]，纵坐标范围[-1,1]
xlabel("横坐标标题")
ylabel("纵坐标标题")
grid on
```



## 条形图

```matlab
y = [75 91 105 123.5 131 150 179 203 226 249 281.5];
bar(y)
```



```matlab
x = 0:0.1:100;
y = x*2;
bar(x,y,"linewidth",2)  %barh可以把图像旋转过来
grid on
```



- 散点图

```matlab
height = randn(1000,1);
width = randn(1000,1);
scatter(height,width);
```





清理缺失数据

实时编辑器-任务

# 常用函数

```matlab
sqrt() %根号
exp()  %自然指数
log()  %自然对数
```

# 常用命令

```matlab
who  %显示变量名
whos %显示变量名和数据类型等信息
```

# 图像处理

## 转为灰度图

```matlab
image = imread('peppers.png');%读取指定位置的图像
image = rgb2gray(image);%将原图转化为灰度图
```







```matlab

image = imread('peppers.png');%读取指定位置的图像
image = rgb2gray(image);%将原图转化为灰度图
figure,imshow(image);%显示图片

[row,col] = size(image);%将矩阵image的行赋值为row,列赋值为col
 
grayNum = zeros(1,256); %声明1行256列的数组用于存放[0;255]的像素个数
  
% 记录灰度值为image(i,j)像素个数
for i=1:row
    for j=1:col
    		%数组的列是从1到256。而image(i,j)的范围是0到255，故要+1
            grayNum(image(i,j)+1) = grayNum(image(i,j)+1)+1;
    end
end
 
%画灰度直方图，将列下标[1,256]即灰度值，映射到[0,255]
figure,
bar(0:255,grayNum,'grouped');%第一个参数为横轴（即灰度值），第二个参数为纵轴（个数），第三个为直方图类型

```

## 直方图均衡化

```matlab
G=imread('peppers.png');
I=rgb2gray(G);
J=histeq(I);  %直方图均衡化，这一个函数就可以做到均衡化的效果
figure,
subplot(121),imshow(uint8(I));
title('原图')
subplot(122),imshow(uint8(J));
title('均衡化后')
figure,
subplot(121),imhist(I,64);
title('原图像直方图');
subplot(122),imhist(J,64);
title('均衡化后的直方图');
```

## 灰度变换

```matlab
g=imread('rice.png')
figure,imshow(g)
g1=imadjust(g,[0 1],[1 0])
figure,imshow(g1)
```

