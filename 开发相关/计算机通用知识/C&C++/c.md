# 1. 与C语言的出会

## 第一个C语言程序

```c
int main()
{ 
	return 0;
}
```

看到这个程序，想必会有人惊讶和诧异。

> 咦！我记得我们课本上明明写的是stdio.h然后hello world什么的啊？你这个什么都没有能运行的了嘛？  
>
> ​																																							——不愿意透露姓名的小明同学

这时候有疑问是很正常的，因为大部分课本，甚至包括一些课外书的第一个程序都是打印一个hello world，而且必定会有一个头文件`<stdio.h>`，所以很多同志就会错以为C语言什么的，没有这个头文件就无法运行的说。其实这个是不对的，最简单的C语言就是我写的这个，从中也可以发现，**C语言什么都能没有，唯独main函数，有且只有一个**。而且，main函数必须有返回值，返回值一般为0。

## main函数，

### main函数的返回值

> main函数为什么要有返回值？？？而且为什么是0？不是0可以吗？		——女装班花小红同学如是说

看到小红同学说话，班里默默无闻的小强同学张红了脸，鼓起勇气也提了一个问题。

> あ、あの，我记得main函数的返回值不是void吗？怎末变成int了？	——内向的小强同学罕见地提问

问得好啊，实际上main函数的返回值的问题已经非常深了，我们在此呢也仅仅是略作探讨不去深究。

1. main函数的返回值到底是void还是int？

**毫无疑问是int**。理由很简单，因为C++ 之父 Bjarne Stroustrup 在他的博客说了

> The definition void main( ) { /* … */ } is not and never has been C++, nor has it even been C.	—— Bjarne Stroustrup 

为什么现在很多书还是用的void呢？这，就是另一个故事了。。。。。。（谭浩强老师的C语言课本有很大的责任）

2. 可以不写吗？

可以，但是编译器会默认给函数加一个`return 0;`

实际上最早c语言是默认不用写返回值的，然后编译器会自动给你加一个`return 0;`，后来随着C语言的发展，在C99中明确要求了不允许缺省返回值，必须写int。

3. 必须是`int main(){}`吗？

这个看情况，在不同编译器会有不同的处理方法。在VS中，代码可以正常运行；但是在DEV C++中，代码会报错`[Error] invalid conversion from 'const char*' to 'int' `

一般来说，如果编译器允许，你甚至可以返回一个字符串。

```c
const char* main()
{ 
	return "hello wrold";
}
```

### 死宅也是人，main也是函数

> なるほど，main函数连返回值都这么讲究，那main函数到底是什么啊？和普通函数有什么区别啊？ ——学霸小明同学的眼神犀利了起来

俗话说的好啊，阿宅也是人，所以没必要带着有色眼镜去看他们，main函数也一样，它本身也只是一个函数而已，可以像普通函数那样运行。没有必要特别去在意它。

```c
//打印0到9的数字
#include <stdio.h>

int i = 0;

int main()
{
	if (i == 10) return 0;
	else
	{
		printf("%d",i++);
		main();
	}
	return 0;
}
```

但是main作为入口函数，还是有一些特殊之处的。

1. main函数的返回值被确定了，不建议随意修改
2. main函数的参数要么是`void `，要么是`int argc, char* argv[]`
3. main函数必须有，而且只能有一个。p

## Hello 头文件！

接下来，我们就来按照传统规矩，打印一个hello world吧！

```c
#include <stdio.h>

int main()
{
	printf("hello world!");
	return 0;
}
```

这个想必就是各位所熟悉的hello world程序吧，各位应该敏锐地发现了，这个程序相较于最开始的程序，新增了两条语句。

`#include <stdio.h>`和`printf("hello world!");` 

真奇怪，printf那句姑且能看明白是打印语句，但是include那个又是什么意思啊？

原来啊，C语言中输入输出有关的函数都放在了`<stdio.h>`中，这个头文件的名字就叫做`standard input output.headfile`，C语言中，很多头文件都是用的这种缩写。比如说`standard library.headfile`就是`<stdlib.h>`的缩写。

这里面包含了C语言自带的很多函数和宏定义，可以直接来用。



## 指针，做好脱发的准备了吗？

接下来，我们就会进入一个奇妙的世界，也是C语言最重要的部分——指针，学好指针可以让你在转型其他语言的时候，获得其为强大的buff，拳打java的引用类型，脚踢JavaScript的this指针。你准备好了吗？

## dereferencing运算符

### 指针与const

首先看以下几个例子

```c
//a和b表示的含义有什么区别？
int const a = 1;
const int b = 2;

//这两个有什么区别？分别代表什么意思？
const int* p_a = &a;
int const* p_b = &b;

int c = 1;
int d = 2;

//这两个有什么区别？分别代表什么意思？
int* const p_c = &c;
int const* p_d = &d;
```



### 数组与指针

数组应该是各位用的最多的一种数据结构了，但是C语言的数组是真的不好使，真心顶不住。

C语言中，数组名就是指向这个数组的指针（实际上其他语言也是如此）

```c
int a[] = { 1,2,3 };
```

a等价于`int* const a`

a[0]等价于 *(a + 0)



### 形参与指针

```c
void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}
```



### 函数与指针

```c

int add(int a,int b) {
	return a + b;
}



int main()
{
	int(*fun_p)(int a, int b);
	fun_p = add;
	printf("%d", fun_p(1, 23));
	return 0;
}
```



## <del>时间</del>内存管理大师

在C语言中，数据的存储可以简单理解为堆区和栈区。

```c
	//栈的地址
	printf("栈的地址：\n");

	int a = 1;
	printf("a的地址：%p\n", &a);

	int b = 1;
	printf("b的地址：%p\n", &b);

	static int const Pi = 3.1415926;
	printf("Pi的地址：%p\n", &Pi);//静态区和全局区，今天不做讨论

	int arr[] = { 1,2,3 };
	printf("arr的地址：%p\n",arr);
	printf("arr[0]元素的地址：%p\n", &arr[0]);
	printf("arr[1]元素的地址：%p\n", &arr[1]);

	//堆的地址
	printf("堆的地址：\n");

	int* new_arr = new int[3];
	printf("new_arr的地址：%p\n", new_arr);
	printf("new_arr[0]元素的地址：%p\n", &new_arr[0]);
```



## 你以为我是结构体，其实我是类哒！

结构体实际上就是一类数据的集合，比如一个学生有姓名学号等多个数据，如果单独写的话过于繁琐，这时候就可以用结构体来封装数据。

```c
struct Student {
	int age;
	int id;
	const char* name;
};
//实例化结构体对象
struct Student xiaoMing;
```

等等！这个概念怎末这么熟悉？仔细一想，这玩意不就是类的概念嘛！类就是对某一类事物进行了抽象封装的结果，那你跟结构体岂不是概念冲突了？

实际上的却如此，struct和class没有本质的区别。也就是说你class能干的事情我struct都能干。包括构造函数，初始化列表等待操作。但是要注意的是，结构体的访问级别默认是public。

```c
//真正意义上的结构体
struct Student {
private:
	int age;
	int id;
	const char* name;
public:
	Student(int age,int id,const char* name = "小明"):age(age),id(id) {

	}
	Student(){}
};

int main()
{
  //创建结构体的实例对象
	Student* xiaoMing = new Student(14,201807071008);
	return 0;
}

```


> 啊这，你这就把我整迷了，我记得书上的结构体明明不是这个样子的啊？不是有一个typedef什么什么的，不是在那个student后面还有一个的吗？？？ ——开始懵逼的斌斌同学如是说

这个斌斌就是逊呐，我想各位学到的结构体也大都是这个样子吧！

```c
typedef struct Student {
	int age;
	int id;
	const char* name;
}Stu;

int main()
{
	Stu xiaoMing;
	printf("%d", xiaoMing.age=14);
	return 0;
}
```

哦哦哦！我想有人此时一定会眼前一亮，“这才是我熟悉的结构体嘛！ ”实际上这个东西换汤不换药，首先看看我们一般创立一个结构体对象的写法：

```c
struct Student xiaoMing;

//注意在C++中，struct可以省略
Student xiaoMing;//C++的写法
```

有没有觉得这个struct很扎眼，所以C++把这个语法给取消掉了。但是C语言没有取消掉啊！你该写还得写。所以一些有强迫症的大佬就不愿意了，他们就用了一个技巧`typedef`，把后面整个结构体都定义为一个Stu，每次写Stu的时候，都相当于写了一遍这个结构体。

```c
Stu xiaoMing;
//等价于
struct Student {
	int age;
	int id;
	const char* name;
}xiaoMing;
```

同样的，类也是有这样的语法，但是类默认不需要写class，所以一般来说没有人会typedef一个类的。





# 2. 卷王之路

## 读代码



## 写代码

### 鸡兔同笼

有若干只鸡和兔在同个笼子里，从上面数，有三十五个头；从下面数，有九十四只脚。求笼中各有几只鸡和兔？



设有x个鸡，y个兔子。

首先分析$y=35-x$

### 打印水仙花数

水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。

## 冒泡排序



# 输入/输出

## printf的输出顺序

printf在打印参数的时候是**从右往左**的，要特别注意。

```c
int main()
{
    int i = 1;
    printf_s("%d,%d",i,++i);
    return 0;
}
//2，2
```

## printf的格式输出

- 在%后面写数字代表**至少**占多少字符宽度。

  ```c
  printf("%10d",a); //至少保留10字符的长度
  ```

- 小数点后面加数字代表保留几位小数

  ```c
  printf("%10.5f",a); //保留5位小数
  ```
  
- 除了%d之外还有很多格式

  %d：十进制整数

  %o：八进制整数

  %x：十六进制整数

  %u：十进制无符号整数

  %c：字符

  %s：字符串

  %f：实数

  %e：以指数形式表现

## 字符的输入/输出

标准库所提供的函数是`getchar`和`putchar`。

```c
char c;
c = getchar();
putchar(c);
```

如果想要连续输入字符，我们可以利用`EOF`这个特殊常量来设计。EOF是（end of file）的简称，值为-1。

此时想要退出的话可以按`ctrl+Z`。

```c
while ((c = getchar()) !=EOF)
  putchar(c);
```



## 输入缓冲区

在进行cin的时候，如果数据过多的话，输入缓冲区就会多出来很多完全没有用的数据，而且会对之后的数据造成干扰。这时候就可以把输入缓冲区进行清除。

```c++
char c;
while ((c = getchar()) != '\n');
```



# 数组

## 动态二维数组

```c++
	int maxNum, polyNum;
	cout << "请输入最高次数" << endl;
	cin >> maxNum;
	cout << "请输入多项式个数" << endl;
	cin >> polyNum;

	vector<vector<int> >polys(polyNum);
	for (int i = 0; i < maxNum; i++)
		polys[i].resize(maxNum);
```



## 数组的指针

数组名是指向该数组的指针。同时，数组名也指向数组的第一个元素。

```c
int a[10][10];
printf("%x\n",a);
printf("%x\n",&a);
printf("%x\n",&a[0]);
```



## 数组越界

首先看下面的代码。

```c++
#include<stdio.h>
int main()
{
	int i = 0;
	int a[10];
	for (i = 0; i <= 20; i++)
	{
		a[i] = 0;
		printf("i的地址是%p,a[i]的地址是%p\n",&i, &a[i]);
	}
	return 0;
}
```

这是一个平平无奇的越界。功能是把数组每一项都设为0。其实这个是有可能出现死循环的（其实就是一定，我试过了4个编译器都死循环了）**因为编译器可能会把i放在a数组的后面。**这就意味着，如果数组长度10，那么i的地址就在a[10]，或者a[11]之类的。具体的位置要根据编译器来决定。

这样的结构就导致了一个致命的问题。假如`&i=&a[10]`，**那么循环执行到a[10]的时候，就会把i的值重新置为0**。这就导致了i此时又变成了0，而再次运行到a[10]的时候，再次置为0。这样for循环将永远执行下去。

但是如果用c++的语法，在for循环内使用i，将不会导致循环，因为这样时，i的地址默认在数组之前，不会存在越界问题。

```c++
#include<stdio.h>
int main()
{
	int a[10];
	for (int i = 0; i <= 20; i++)
	{
		a[i] = 0;
		printf("i的地址是%p,a[i]的地址是%p\n",&i, &a[i]);
	}
	return 0;
}
```



## 指定初始器

c++允许在数组初始化时，用自身变量名来指定赋值。

```c++
int days[5] = {1,2,3,days[0]=4,5};
for (int i = 0; i < 5; i++)
{
  printf_s("days[%d]=%d\n",i,days[i]);
}
/*输出结果为
days[0]=4
days[1]=2
days[2]=3
days[3]=4
days[4]=5
*/
```

但是要注意，c++的执行顺序是顺序的，这就意味着，首先会把数组初始化为[1,2,3]，执行到`days[0]=4`之后，修改0的位置为4，然后再把自身的数据赋值为4，此时数组为[4,2,3,4]。

如果这个数字大于了自身下标，那么修改不会起效。如下

```c++
int days[5] = {1,2,3,days[4]=4,5};
for (int i = 0; i < 5; i++)
{
  printf_s("days[%d]=%d\n",i,days[i]);
}
/*输出结果为
days[0]=1
days[1]=2
days[2]=3
days[3]=4
days[4]=5
*/
```

此时，虽然在执行`day[4]=4`的时候把4号下标的数据改为了4，但是接下来又被5的数据重新覆盖了。

# 变量作用域

先看下面的代码

```c
int i = 1;

int main()
{
    int i = i;
    return 0;
}
```

main里面i的值将是多少？

答案是编译器会报错，或者打印一个野指针的值，外面的i作用域虽然是全局的，但是在函数作用域里面，会优先使用自己已经定义过的变量。

首先编译器会发现main中已经定义了i，然后初始化为i。之后编译器会去作用域链查找i的值，发现刚刚定义过了这个变量，之后就把刚刚那个定义的值（undefined）赋值给i。导致i的结果最后还是未定义。

# 函数

函数是C语言的核心，**C语言程序就是由函数和变量所组成的**。函数包含着所要执行的语句，而变量则储存着所需要使用的数据。

## 参数的值传递

C语言在进行参数传递的时候，全都是值传递，也就是说传递的时候，并不是把主调函数中的实参直接传递过来，而是拿到其副本，更加安全。

```c
int wrongSwap(int a ,int b)
{
  int temp = a;
  a = b;
  b= temp;
}
```

上面这个例子虽然确实交换了a和b的值，但是实际上只是交换了其副本的值，并没有修改实参的值。

## 参数的指针传递

C语言在进行参数传递的时候，全都是值传递，但是如果传递的值是指针的话，就叫指针传递了。

## 参数引用传递

尽量传引用，而不要直接值传递，因为引用传递的是指针，只有4字节，而值传递传递的数据可能会很多，影响速率。如果不希望修改原数据，只需要加const就行了。

## 函数返回值

void类型的函数，可以不写return，默认执行`return;`。

# 字符串



# 指针

> 指针就是地址，地址就是指针。	——书上说的

## 指针与常量

**在C语言中，const修饰左边的东西，若左边没东西则修饰右边的东西。**所以说` int const a `和`const int a`是完全等价的东西。

加了指针之后，也是同样的道理。`int const *`修饰的是int，所以int的值不能被修改；`int * const `修饰的是*，所以指针不能被修改。

```c++
int a = 1;
int b = 2;

int const  *p_a = &a; //int为常量，指针可以改变，但是指向的int数据不能被修改

int * const p_b = &b; //const修饰*，p_b的指针无法被修改。但是*p_b可以被修改。

int const * const p = &a; //*p和p都不能被改变
```

## 指针与数组

首先来看看这个东西：

```c
int* p1[10]; //这是一个数组，一个拥有10个指针的数组
int(*p2)[10]; //这是一个指针，指向拥有10个int元素的数组的指针
```

在C语言中，`[]`的优先级比`*`高，这就导致了如果你写`int *p1[10]`，`[]`会首先来修饰p1，这样就先构成了一个数组，然后再看到数组的数据类型的`int*`；同样的，如果用了小括号，那么指针就会就先修饰p2，然后再描述指针指向的空间有10个int。



然后说一下数组传参的写法：

```c
//一维数组传参
void fun(int* temp) {
	for (int i = 0; i < 10; i++)
	{
		cout << temp[i] << " ";
	}
}

int main()
{ 
	int a[10] = { 0,1,2,3,4,5,6,7,8,9 };
	fun(a);
}

//二维数组传参
void fun(int (*temp)[3]) {
	for (int i = 0; i < 10; i++)
	{
		cout << temp[i] << " ";
	}
}

int main()
{ 
	int a[3][3] = { {1,2,3},{4,5,6},{7,8,9} };
	fun(a);
}
```



## 指针与引用

- 引用不可以为空，就是说初始化的时候就必须赋值，但是指针可以初始化为NULL
- 指针可以更改指向的对象，但是引用不可以指向新的变量。看来引用真的是老实人啊，指针太花心了。

# 宏命令

## #include

自己写的头文件可以用“”来导入

```C++
#include "complex.h"
```

系统自带的头文件可以用<>来导入

```cpp
#include <iostream>
```



## #define

#define 会把文本直接进行替换

```c
#define PAI 3.14
```

比如上例中，将程序中所有的PAI都替换为3.14。但是要注意，宏替换是文本替换，也就是无脑把文本进行复制粘贴，容易造成一些不必要的bug。

```c
#define square(x) x*x 
square(3,3) //将会变为 3*3，这个是正确的。
square(a+1) //将会变为 a+1*a+1 ，此时就有问题了。
```

可以看到，宏命令是简单的文本替换，所以会在运算符优先级上面出现bug，解决方法就是多用括号。

```c
#define square(x) ((x)*(x))
```

因为这样子真的很麻烦，所以对于常量的替换可以使用const，对于函数可以使用inline内联函数。

## #ifdef

这个常用于头文件的防卫式声明。

头文件名一般用  \__头文件名__ 的格式来定义。

```c
#ifndef __COMPLEX__
#define __COMPLEX__
//代码
#endif 
```



# 枚举

## 使用与定义

```c++
enum class PROCESS_STATE {
    ready
};


STATE = PROCESS_STATE::ready;
```

# 命名空间

## 定义

程序设计里面经常就有变量名重复的问题，你跟其他人合作开发，你有一个a变量，人家说不定也有一个a变量，到时候一联合编译是不是就出错了，那怎么办？大佬们就想到一个方法，那就是把每个人的代码都放到自己的一个作用域里面，互不影响，这个作用域就叫做**命名空间**。

命名空间就是用`namespace`修饰的带名字的一个代码块，里面的数据不会影响到外界，这样子每个人的代码就独立开了。

```c++
namespace Loli {
	const char* name = "小丛雨";
	void show() {
		cout << "我叫" << name << endl;
	}
}
```



## 三种使用方式

- 使用`::`运算符

命名空间使用`::`运算符，可以直接访问到里面的数据，对于一些不常用的数据可以这样写，避免导入太多污染全局环境。

```c++
namespace Loli {
	const char* name = "小丛雨";
	void show() {
		cout << "我叫" << name << endl;
	}
}

int main()
{
	Loli::show();
	return 0;
}
```



- 使用`using`关键字

可以直接导入某个变量或函数，以后在全局空间可以直接使用，前面不用再写那一串东西了，比较方便。

```c++
namespace Loli {
	const char* name = "小丛雨";
	void show() {
		cout << "我叫" << name << endl;
	}
}
using Loli::show;

int main()
{
	show();
	return 0;
}
```

- `using namespace`命令

这个命令可以直接把命名空间所有数据都导出，虽然很方便，但是实际上已经起不到封装数据的作用了。我们常用的`using namespace std;`就是把std这个命名空间全部导入了，因为这个命名空间的数据使用频率非常高，所以可以直接导出，一般来说不建议这样写。

```c++
namespace Loli {
	const char* name = "小丛雨";
	void show() {
		cout << "我叫" << name << endl;
	}
}
using namespace Loli;

int main()
{
	show();
	return 0;
}
```




# STL

STL就是Standard Template Library的缩写，STL里面封装了贼多数据结构和算法，可以说是轮子大全了。再也不用重复造轮子了。

## vector

### 创建

```c++
#include <vector>
vector<数据类型> 变量名;
```

### 插入数据

```c++
vector<PCB*> pcb;
pcb.push_back(new PCB(0, 9, 0, 3));
```

### 删除数据

```c++
vec1.pop_back();//删除末尾元素
```

### 遍历

- for区间遍历

```c++
for (auto val : valList)
{
    cout << val << endl;
}
```

-  迭代器

```c++
				vector<int>::iterator iter = path.begin();
					for (; iter != path.end(); iter++) {
						cout << *iter;//利用取指针的操作读出迭代器指向的值
					}
```

### 排序

首先必须自定义一个排序方法

```c++
static bool sortRules(const PCB* p1, const PCB* p2) {
	return p1->PRIORITY > p2->PRIORITY;
}
```

之后在需要的地方直接调用sort方法，并把排序方法传进去

```c++
sort(PCBList.begin(), PCBList.end(), PCB::sortRules);
```



# 常用函数/语句



```c++
#define _CRT_SECURE_NO_WARNINGS
 system("cls");

​ fflush(stdin);
```



# VS密钥

2019专业版：NYWVH-HT4XC-R2WYW-9Y3CM-X4V3Y
