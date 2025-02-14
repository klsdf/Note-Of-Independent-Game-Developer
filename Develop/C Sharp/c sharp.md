# Hello World

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TEST
{
	class Program
	{
		static void Main(string[] args)
		{
     		Console.WriteLine("Hello World!");
      		Console.ReadKey();
		}
	}
}
```



## XML注释

 这是一个特殊的注释,跟java里面的一样,不仅仅可以用来为写源码的人提供提示,调用时也可以定制提示信息。

```c#
///<summary> 这是一个加法函数 </summary> 
///<param name="a"> 参数</param>     
///<param name="b"> 也是参数</param>  
///<returns>返回a+b</returns>
public int Add(int a,int b) 
{
	return a+b;
}
```





## 运算符

大部分运算符和别的语言都差不多,但是下面这些比较特殊,是需要强调的.

| 运算符   | 描述                                       | 示例 |
| :------- | :----------------------------------------- | ---- |
| typeof() | 返回是哪一种class                          |      |
| is       | 判断对象是否为某一个class的实例            |      |
| &        | 取地址，当然也有按位与的意思               |      |
| *        | 指针，接收地址,当然也有乘法的意思          |      |
| as       | 将左边的类型强制转换为右边，转不了返回null |      |

# 数据类型



| 类型      | 描述                      | 范围                                                     | 默认值   |
| :------ | :---------------------- | :----------------------------------------------------- | :---- |
| bool    | 布尔值                     | true或 false                                            | False |
| byte    | 8 位无符号整数                | 0 到 255                                                | 0     |
| char    | 16 位 Unicode 字符         | U +0000 到 U +ffff                                      | '\0'  |
| decimal | 128 位精确的十进制值，28-29 有效位数 | (-7.9 x 1028 到 7.9 x 1028) / 100 到 28                  | 0.0M  |
| double  | 64 位双精度浮点型              | (+/-)5.0 x 10-324 到 (+/-)1.7 x 10308                   | 0.0D  |
| float   | 32 位单精度浮点型              | -3.4 x 1038 到 + 3.4 x 1038                             | 0.0F  |
| int     | 32 位有符号整数类型             | -2,147,483,648 到 2,147,483,647                         | 0     |
| long    | 64 位有符号整数类型             | -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807 | 0L    |
| sbyte   | 8 位有符号整数类型              | -128 到 127                                             | 0     |
| short   | 16 位有符号整数类型             | -32,768 到 32,767                                       | 0     |
| uint    | 32 位无符号整数类型             | 0 到 4,294,967,295                                      | 0     |
| ulong   | 64 位无符号整数类型             | 0 到 18,446,744,073,709,551,615                         | 0     |
| ushort  | 16 位无符号整数类型             | 0 到 65,535                                             | 0     |



## 值类型

### 基本值类型

### 结构体

 看上去和c++的结构体一模一样，就是每个属性前面需要加一个访问权限,其实还是有很多不一样的地方

- 结构体不能有析构函数

- 不能为结构定义无参构造函数。无参构造函数(默认)是自动定义的，且不能被改变。

- 结构成员不能指定为 abstract、virtual 或 protected。

```C#
struct Loli
{
    public string name;
    public int age;
};  
```

### 枚举

通过enum来声明。

```c#
enum Loli{傲娇,妹系,呆萌};
```

可以强制转换为int

```c#
int a =(int)Loli.傲娇;
```





## 其他类型

### 指针类型

### 可空类型

# 数组



## 声明与初始化

```c#
	//用new初始化
	datatype[] arrayName = new datatype[num]{ };

	//直接初始化
	datatype[] arrayName = { 1,2,3 };
```



#### 多维数组

所谓多维数组其实就是维数相同的数组，比如二维数组，三维数组。

声明方法和一维数组一样，但是唯一的区别就是要用[,]来声明。

```c#
	//多维数组行列个数必须确定。
	int[,] a = {
		{1,2,3 },
		{4,5,6 },
	};
	//或者用new也可以声明
	int[,] a = new int[2,3]{{1,2,3}，{4,5,6}};
	//切记，不能写成int[2,3] a，不要被C语言迷惑了。
```

#### 交错数组

 第一个参数不能缺省，并且第二个不能加,因为这个玩意其实就是一个特殊的一维数组,只不过他每一个元素也是一个一维数组。

 所以你只能知道有多少个一维数组，但是不能指定每个一维数组里面有多少元素,所以每个元素都要初始化，并且只能用new

```c#
	int[][] a = new int[2][]{
		new int[]{1,2,3},
		new int[]{4,5} 
	};
```

#### foreach遍历

跟其他语言一样,foreach会遍历数组,i每次都会被赋值为数组的一个元素.

```c#
	int[] a=new int[3]{1,2,3}
	foreach (int i in a )
	{
		Console.WriteLine(i);
	}
```

结果会打印出1,2,3。这个i每次迭代会携带a[0],a[1],a[2]。并不是数组下标，而是元素本身。

当然了,在交错数组foreach的时候,要注意每次所携带的数据都是一个一维数组.

```c#
int[][] a = new int[2][] {
	new int[]{1,2,3},
	new int[]{4,5} 
};
foreach (int[] i in a)
	foreach (int j in i)
		Console.WriteLine(j);
```





# foreach循环



```c#
int[] a = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
foreach (int i in a) {
    Console.WriteLine(i);

}
```

# 面向对象

```c#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{

    class YuzuSoft : Loli
    {
        //默认有一个base作为基类的构造函数
        public YuzuSoft(int age =500 ,string name = "小丛雨") : base(age,name)
        { }

        public void show() {
            Console.WriteLine("我叫" + this.name+"的说");
        }
    }
    class Loli
    {
        private int age;
        protected string name;

        private string _sukiHito;

        public string sukihito
        {
            get {
                return this._sukiHito;
            }
            set //默认有一个value参数
            {
                this._sukiHito = value;
            }
            
        }

        public Loli() 
        {
            this.age = 14;
            this.name = "莲华";
        }
        public Loli(int age,string name)
        {
            this.age = age;
            this.name = name;
        }
        ~Loli() 
        {
            Console.WriteLine(this.name+"要离开啦~");
        }
        public void show() 
        {
            Console.WriteLine("我叫"+this.name);
        }

        
    }

    public class Program
    {
        
        public static void Main() {
            Loli loli = new Loli();
            loli.show();
            Console.WriteLine(loli.sukihito="我");

            YuzuSoft yuzu = new YuzuSoft();
            yuzu.show();

            Console.Read();

        }
       
    }
}

```



## 访问控制符

c#的访问控制有很多种

- public：所有对象都可以访问；
- private：对象本身在对象内部可以访问；
- protected：只有该类对象及其子类对象可以访问
- internal：同一个程序集的对象可以访问；
- protected internal：访问限于当前程序集或派生自包含类的类型。

![shadow-img](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/C%23/csharp-public.png)



## this和base关键字

如果想要父类的属性，可以使用base关键字。this则是访问本对象的属性。



## 虚函数与override

通过虚函数的方式实现多态

   virtual 关键字用于在基类中修饰方法。virtual的使用会有两种情况：

- 在基类中定义了virtual方法，但在派生类中没有重写该虚方法。那么在对派生类实例的调用中，该虚方法使用的是基类定义的方法。

- 在基类中定义了virtual方法，然后在派生类中使用override重写该方法。那么在对派生类实例的调用中，该虚方法使用的是派生重写的方法。

```c#
class Base 
{
    public virtual void show() 
    {
        Console.WriteLine("我是基类");
    }
}

class Derive:Base
{
    public override void show() 
    {
        Console.WriteLine("我是派生类");
    }
}

```



在调用的时候，需要全部用基类来定义，但是new的东西需要是子类的。

```c#
Base b = new Base();
Base d = new Derive();

b.show();
d.show();
                
```

## 抽象函数与override

```c#
abstract public class Father
{
    public abstract void show1();


}

public class Son:Father
{
    public override void show1() 
    {
        Console.WriteLine("派生类show1");
    }

}
```

测试

```c#
Father father = new Son();
father.show1();//派生类show1
```

抽象函数可以被重写

## new隐藏父类方法

需要在子类使用new关键字

```c#
   class Base 
    {
        public void show() 
        {
            Console.WriteLine("我是基类");
        }
    }

    class Derive:Base
    {
        public new void show() 
        {
            Console.WriteLine("我是派生类");
        }
    }
```



## new与override的区别

```c#
public class Father
{
    public virtual void show1()
    {
        Console.WriteLine("基类show1");
    }

    public virtual void show2()
    {
        Console.WriteLine("基类show2");
    }
}

public class Son:Father
{
    public new void show1() 
    {
        Console.WriteLine("派生类show1");
    }

    public override void show2()
    {
        Console.WriteLine("派生类show2");
    }
}


```



测试代码

```c#
Father father = new Son();
father.show1();//基类show1
father.show2();//派生类show2
```



new重写的方法，具体执行的内容是依照其声明的类型决定的。而override则是依照new的类型决定的。这也就是为什么override可以实现多态。声明时全部都按照基类来声明，只需要动态传入不同的对象，就可以实现不同的结果。

## 抽象类

抽象类不能实例化，**抽象类可以包括抽象函数和普通函数**。

abstract关键字只能用在抽象类中修饰方法，并且没有具体的实现。抽象方法的实现必须在派生类中使用override关键字来实现。

```c#
abstract class A 
{
    abstract public void show();
}
```

## 密封类与密封方法

- 密封类不可以被继承
- 在密封类中不能声明受保护成员或虚成员，因为受保护成员只能从派生类进行访问，而虚成员只能在派生类中重写。
- 由于密封类的不可继承性，因此密封类不能声明为抽象的，即sealed修饰符不能与abstract修饰符同时使用。

```c#
sealed class Test
{
    public int a = 1;
}
```



密封方法不可以单独声明，只能用于用于对基类的虚方法进行实现。所以，声明密封方法时，sealed修饰符总是和override修饰符同时使用。密封方法不可以再被重写。

```c#
public class BaseClass
{
    public virtual void Show() { }
}

public class InheritClass : BaseClass
{
    public override sealed void Show()
    {
        base.Show();
    }
}
```



## readonly

只读字段只可以在声明和构造函数中进行赋值

在其他地方不可以被修改

```c#
public class Test
{
    readonly int a = 1;
    Test(int a) 
    {
        this.a = a;
    }

}
```

## 接口

定义一个接口在语法上跟定义-一个抽象类完全相同，但不允许提供接口中任何成员的实现方式，-般情况下，接口只能包含方法，属性，索引器和事件的声明。

接口不能有构造函数，也不能有字段，接口也不允许运算符重载。

接口定义中不允许声明成员的修饰符，接口成员都是公有的

```c#
public interface InterfaceTest
{
    void show();
    void show2();
}

public class Test : InterfaceTest
{
    public void show()
    {

    }

    public void show2()
    {

    }
}

```



同样的，接口也可以实现多态





接口也可以进行继承



## 通过接口进行多继承

## 索引器

```c#
public class Week
{
    private string[] weeks = { "周天","周一","周二","周三","周四","周五","周六"};
    public string this[int day] 
    {
        get{
            return weeks[day];
        }
        set 
        {
            weeks[day] = value;
        }
    }
}
```



测试数据

```c#
Week week = new Week();
Console.WriteLine(week[1]);
week[1] = "萝莉";
Console.WriteLine(week[1]);

Console.Read();
```

## 运算符重载

运算符重载的参数个数和返回值有具体要求。+号必须返回自身对象的类型。

```c#
public class Loli
{
    public static Loli operator +(Loli loli1, Loli loli2)
    {
        Console.WriteLine("小萝莉进行了交配");
        Loli loli3 = new Loli();
        return loli3;
    }
}
```

## 类与结构体

- 结构体是值类型，new出来也是放在栈里面的
- 结构体不能继承
- 结构体不能拥有析构函数

## 静态类和静态方法

静态类里的变量和方法，都必须是静态的。静态方法里的变量，也必须是静态的。

普通类里有两个变量，一个是静态的，一个是普通的。Unity里有两个场景A和B，可以由场景A跳转到场景B，A和B中都有这个普通类脚本——普通变量，在跳转场景后，恢复初始值；静态变量，保留上个场景中的值。静态变量的这一特性，常和单例模式配合，用于**跨场景传值**。

# 泛型

```c#
class Complex<T>
{
    private T a;
    private T b;
    public Complex(T a, T b)
    {
        this.a = a;
        this.b = b;
    }
    public void add(Complex<T> complex) 
    {
        dynamic newa = complex.a;
        dynamic newb = complex.b;

        this.a = this.a + newa;
        this.b = this.b + newb;

    }

    public override string ToString()
    {
        return this.a+" "+this.b;
    }
}
```

测试

```c#
public static void Main() {
    Complex<int> complex1 = new Complex<int>(1,2);
    Complex<int> complex2 = new Complex<int>(3, 4);

    complex1.add(complex2);
    Console.WriteLine(complex1);

    Console.Read();

}
```

# 重写Equals方法

```c#
class Loli 
{
    private int age;
    private string name;
    public Loli(int age,string name) {
        this.age = age;
        this.name = name;
    }
    public override bool Equals(object obj)
    {
        Loli loli = obj as Loli;
        return this.age == loli.age && this.name == loli.name;
    }

}
```

测试

```
Loli loli1 = new Loli(14,"莲华");
Loli loli2 = new Loli(14, "莲华");

Console.WriteLine(loli1.Equals(loli2));//True
```



# 可空类型



# 实例

## 2048

```c#
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2048
{
    /*
     游戏规则：
    1，如果一行有三个一样的，那么合并方向上最远处的两个
    2，只有元素移动或者何并才会生成新元素
    3，生成的新元素为2，位置随机
    4，只有元素一样才能合并
    5，得到2048游戏结束
    6，一次可以合成多个。
     */

    /*
     设计思路：
    游戏核心就是合并，与移动。
    用伪代码来讲就是
    start:
    {
    init();

    while(!GameOver())
    {
        get input= Input();
        //第一次move先把没有接触的方块放到一起
        Move(input);

        //然后合并，那么中间就会少一个位置，需要再次移动
        Merge()
        
        //合并之后看看有没有2048
          GameOver();
        //没有结束就生成新的元素继续
        AddElement()
         
    
        //最终移动完
        Move();
    }
    } 
     
     */
    class Direction
    {
        //表示一个坐标点
        public int interval_x, interval_y;

        Direction()
        {

        }

        public Direction(int x, int y) : this()
        {
            interval_x = x;
            interval_y = y;
        }

        public static Direction UP
        {
            get
            {
                return new Direction(-1, 0);
            }
        }

        public static Direction DOWN
        {
            get
            {
                return new Direction(1, 0);
            }
        }

        public static Direction LEFT
        {
            get
            {
                return new Direction(0, -1);
            }
        }
        public static Direction RIGHT
        {
            get
            {
                return new Direction(0, 1);
            }
        }

    };





    class _2048
    {
        const int ROW = 4;
        const int COLUMN = 4;
        const int NUMS = 2;
        //得到了初始化的数组
        static int[,] array = init(ROW, COLUMN, NUMS);

        enum Over {win,lost };
        static Over over;

        /// <summary>
        /// 用于初始化
        /// </summary>
        /// <param name="row">生成行数</param>
        /// <param name="column">列数</param>
        /// <param name="nums">初始化几个块</param>
        /// <returns>把生成的二维数组返回</returns>
        static public int[,] init(int row,int column,int nums=2)
        {
            int[,] array = new int[row,column];
            Random random = new Random();
            for(int i=0;i<nums;i++ )
             array[random.Next(0, row), random.Next(0, column)] = 2;
            return array;
        }
        /// <summary>
        /// 把一个元素插入到某一个direction上不为target的第一个元素，
        /// 全为target就插到方向尽头。
        /// 插完之后原来的地方就为0
        /// </summary>
        /// <param name="data">插入的元素位置</param>
        /// <param name="direction">方向</param>
        /// <param name="target_data">说白了就是0</param>

        static bool Valid(int x,int y)
        {
            return (x >= 0 && x < array.GetLength(0) && y >= 0 && y < array.GetLength(1));
                 
        }
        static void Merge(Direction now_position, Direction direction)
        {
            if (0==array[now_position.interval_x, now_position.interval_y])
                return;
            
                    //这个就是你目标元素的位置，比如说往左移动
                    //就是左边那个元素的坐标
            int target_poi_x = now_position.interval_x + direction.interval_x;
            int target_poi_y = now_position.interval_y + direction.interval_y;
            if(Valid( target_poi_x,target_poi_y) && 
                array[now_position.interval_x,now_position.interval_y]== array[target_poi_x, target_poi_y])
            {
                array[target_poi_x, target_poi_y] *= 2;
                array[now_position.interval_x, now_position.interval_y] = 0;
            }
                
        }


        static void MoveElement(Direction now_position, Direction direction)
        {
            int array_data = array[now_position.interval_x, now_position.interval_y];
            //不管最后也没有移动，先清零
            array[now_position.interval_x, now_position.interval_y] = 0;
            while (Valid(now_position.interval_x,now_position.interval_y)
                && array[now_position.interval_x, now_position.interval_y] == 0)
            {
                now_position.interval_x += direction.interval_x;
                now_position.interval_y += direction.interval_y;
            }
            now_position.interval_x -= direction.interval_x;
            now_position.interval_y -= direction.interval_y;
            array[now_position.interval_x, now_position.interval_y] = array_data;
        }


        static void Move(Direction direction)
        {

            for(int i=0;i<array.GetLength(0);i++)
                for(int j=0;j<array.GetLength(1);j++)
                {
                    MoveElement(new Direction(i,j),direction);
                }
            for (int i = 0; i < array.GetLength(0); i++)
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Merge(new Direction(i, j), direction);
                }
           
            for (int i = 0; i < array.GetLength(0); i++)
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    MoveElement(new Direction(i, j), direction);
                }
        }

        static public void Show()
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    Console.Write("{0,-8}",array[i, j]);
                }
                Console.Write('\n');
            }
        }


        static char GetKeybord()
        {
            //读取字符，但是会有缓冲区的bug
            char key = (char)Console.Read();
            //清除输入缓冲区
            Console.ReadLine();
            return key;
        }

        static bool GameOver()
        {
            //没有0，或者有2048游戏结束
            bool has0=false;
            for (int i = 0; i < array.GetLength(0); i++)
            
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    if (2048 == array[i, j])
                    {
                        over = Over.win;
                        return true;
                    }
                       
                    if (0 == array[i, j])
                        has0 = true;
                }
            if (false == has0)
            {
                over = Over.lost;
                return true;
            }
              
            return false;
        }
        static void AddElement()
        {
            Random random = new Random();
            int row = random.Next(0, array.GetLength(0));
            int column = random.Next(0, array.GetLength(1));
            while (true)
            {
                if (0 == array[row, column])
                    break;
                row = random.Next(0, array.GetLength(0));
                column = random.Next(0, array.GetLength(1));
            }
            array[row, column] = 2;
        }


        static void Main(string[] args)
        {

           
            while(GameOver()!=true)
            {

                Show();      
                char key = GetKeybord();
                switch(key)
                {
                    case 'w': Move(Direction.UP);break;
                    case 's':Move(Direction.DOWN);break;
                    case 'a':Move(Direction.LEFT);break;
                    case 'd':Move(Direction.RIGHT);break;

                    default: break;

                }
                if (GameOver())
                    break;
                AddElement();
                Console.Clear();

            }

            if(over==Over.win)
            {
                Console.WriteLine("牛的一批，666666666666");
            }
            else
            {
                Console.WriteLine("废物，蛇人一个");
            }
                
        }
    }
}

```



# 字符串

一个字符串前面加@可以使其转义字符失效

```c#
@"123123\n\n\n\n"
```





```c#
string s = "hat-soft.top";

//比较字符串是否相等，相等为0，不相等为1
s.CompareTo("asdasdasd"));

//替换字符串 hat-soft-top
 s.Replace( ".","-" ));

//将字符串拆分为字符数组[hat-soft,top]
string[] vs = s.Split(".");
foreach(string v in vs)
{
    Console.WriteLine(v);
}

//获得子字符串
Console.WriteLine(s.Substring(4));//soft.top
Console.WriteLine(s.Substring(4,4));//soft

//大小写
Console.WriteLine(s.ToLower());
Console.WriteLine(s.ToUpper());

//去除前后的空格
Console.WriteLine(s.Trim()) ;

//字符串拼接
Console.WriteLine( string.Concat("www","sikiedu.com") );

//将字符数组拼接为字符串
char[] cA = { 'A', 'B', 'C', 'D' };
Console.WriteLine( string.Join( "、",cA ) );


//将字符串复制到一个字符数组中
char[] cA = new char[20];
s.CopyTo(4, cA, 1, 7);//将s从第4个字符开始，复制到cA。从cA的第一个位置开始，一共复制7个。
foreach(char c in cA)
{
    Console.WriteLine(c);
}



//下标
Console.WriteLine(s.IndexOf("."));

//字符串格式化
int x = 23;
int y = 545;
print(string.Format(" {0}+{1}={2}", x, y, x + y));

int money = 120000;
print(string.Format("{0:C}", money));

print(string.Format("{0:F2}", 23.12512));//保留两位小数，自动四舍五入

print(string.Format("{0:P1}", 0.25657));//转百分数

DateTime dt = System.DateTime.Now;
Console.WriteLine(string.Format("{0:yyyy-MM-dd hh:mm}", dt));
Console.WriteLine(dt.ToString("yyyy-MM-dd hh:mm"));//可以直接在toString中书写

//插入
print(s.Insert(3, "-----"));//hat------soft.top
```





# StringBuilder



**在操作StringBuilder的时候，所有的操作都会改变原数据，而String则不会改变。**

而且StringBuilder是存储在堆里面的，并不是静态区。可以理解为字符数组。



```c#
StringBuilder sb = new StringBuilder("hat-soft.top");

sb.Append("123111");//在字符串之后直接添加
sb.Insert(3, " ");//直接插入
sb.Remove(4, 2);
sb.Replace("i", "Love");




//动态扩容
StringBuilder sb = new StringBuilder(5);
sb.Append("http");
sb.Append("www.sikiedu.com");
Console.WriteLine(sb.Capacity);

StringBuilder sb = new StringBuilder("www.sikiedu.com",100);
```







# Array

sort

```c#
int[] a = { 9, 2, 3, 4, 5, 6, 7, 3, 3, 1, 123, 6, 889 };
Array.Sort(a);
foreach (int i in a) {
    Console.Write(i+" ");
}
```



<p id="test">123</p>

<input type="text"></input>









```

```

```
&copy;
```



# List

- List默认的存储容量为4

- 若容量被占满，则会翻倍地申请新的内存

  使⽤Array.Copy()⽅法将旧数组中的元素 复制到新数组中。

  

  

```c#
List<int> list = new List<int>(50) { 1,2,3,4,5,6,7,8,9};//申请空间为50的列表
list.Add(123);

//list.Count代表当前存储的元素个数
//list.Capacity代表当前的存储空间
for (int i = 0; i < list.Count; i++) {
    Console.WriteLine(list[i]);//按索引访问
}


foreach (int i in list)
{
    Console.WriteLine(i);//foreach访问
}
```

  

1,Capacity获取容量⼤⼩

2,Add()⽅法添加元素Unity 1143

3,Insert()⽅法插⼊元素

4,[index]访问元素

5,Count属性访问元素个数

6,RemoveAt()⽅法移除指定位置的元素

7,IndexOf()⽅法取得⼀个元素所在列表中的索引位置

LastIndexOf()上⾯的⽅法是从前往后搜索，这个是从后往前搜索，搜索到满⾜条件的 就停⽌ 上⾯的两个⽅法，如果没有找到指定元素就返回-1

8,Sort()对列表中是元素进⾏从⼩到⼤排序

# 委托



## 创建

委托实际上就是c++中的函数指针

- 传入委托的函数，返回值和参数类型要和委托函数一致
- 构造委托有两种方法，可以直接把函数指针赋值，也可以new一个实例出来

```c#
delegate void ShowMessage();
class Test
{
    static public void Hello()
    {
        Console.WriteLine("Hello World");
    }

    static public void GG()
    {
        Console.WriteLine("GG");
    }
}

ShowMessage showHello = Test.Hello;

ShowMessage showGG = new ShowMessage(Test.GG);
showHello();
showGG();

```





可以看到委托函数和传入的函数参数和返回值要一致

```c#
delegate int  ShowMessage(int a,int b);
class Test
{
    static public int Add(int a,int b)
    {
        return a + b;
    }

}


ShowMessage add = Test.Add;

Console.WriteLine(add(1,2));//3
```



## Action委托



Action可以接受一个无返回值的函数指针

```c#
using System;
void test()
{
    Console.WriteLine("test");
}

Action action = test;
action();

```

如果函数要传参，可以在模板里写入参数类型

```c#
void hello(string str)
{
    Console.WriteLine("hello "+str);
}

Action<string> action = hello;
action("world");

```



## Func委托



Func委托可以接受一个有返回值的函数指针。**最后一个参数是函数返回值**。

```c#
float add (int a,int b)
{
    return a + b;
}

Func<int,int,float> func = add;

Console.WriteLine(func(1, 2));
```



## 多播

一个委托可以同时保存多个函数指针，并一起执行

```c#
void Hello()
{
    Console.WriteLine("hello ");
}

void World()
{
    Console.WriteLine("world");
}

Say say = Hello;
say += World;
say();



delegate void Say();

```



多播实际上就是一个列表

```c#
void Hello()
{
    Console.WriteLine("hello ");
}

void World()
{
    Console.WriteLine("world");
}

Say say = Hello;
say += World;

//可以获取到委托指针的列表，手动执行
Delegate[] delegates = say.GetInvocationList();
foreach (Delegate d in delegates)
{
    d.DynamicInvoke();
}


delegate void Say();

```











## Delegate、delegate、 Action、 Func的联系与区别

`delegate`是一个关键字，被delegate修饰的函数，最终会被编译为Delegate类型。

Action和Func是官方定义的两套泛函委托类型，Action没有返回值，Func有返回值。

Delegate是Action和Func的基类。



# Lambda表达式

## 匿名方法

使用

```c#
Func<int, int, int> plus = delegate (int a, int b) 
{
    return a + b;
};
int res = plus(1, 2);
```



## lambda表达式

lambda表达式实际上就是匿名方法的简写形式

和JavaScript的箭头函数一模一样。

```c#
Func<int, int, int> plus = (a, b) => { return a + b; };
```

而且和JavaScript一样，当只有一条语句的时候，默认该语句就是返回值

```c#
Func<int, int, int> plus = (a, b) => a + b; 
```

只有一个参数的时候，参数的括号也可以省略

```c#
Func<double, double> square = x => x * x;
```



# 事件（Event）



# 迭代器





# 异步

```c#
using System;
using System.Threading.Tasks;
async void Test() 
{
    await Task.Delay(TimeSpan.FromSeconds(0.2f));
    print("测试");
}

```



# 协程



```c#
IEnumerator TestIEnumerator()
{
    //等待3s
    yield return new WaitForSeconds(3f);
    //执行下一帧
	yield return null;
    //
} 


 StartCoroutine(TestIEnumerator()); 
```





```c#
 // 用法和用途（1.延时调用，2.和其他逻辑一起协同执行
    // (比如一些很耗时的工作，在这个协程中执行异步操作，比如下载文件，加载文件等)

    public Animator animator;
    public int grisCount;
    private int grisNum;

    void Start()
    {
        // 协程的启动
        StartCoroutine("ChangeState");
        StartCoroutine(ChangeState());
        IEnumerator ie = ChangeState();
        StartCoroutine(ie);
        // 协程的停止
        StopCoroutine("ChangeState");
        // 无法停止协程
        StopCoroutine(ChangeState());
        StopCoroutine(ie);
        StopAllCoroutines();
        StartCoroutine("CreateGris");
    }

    void Update()
    {
        
    }

    IEnumerator ChangeState()
    {
        // 暂停几秒（协程挂起）
        yield return new WaitForSeconds(2);
        animator.Play("Walk");
        yield return new WaitForSeconds(3);
        animator.Play("Run");
        // 等待一帧 yield return n(n是任意数字)
        yield return null;
        yield return 100000;
        print("转换成Run状态了");
        // 本帧帧末执行以下逻辑
        yield return new WaitForEndOfFrame();
    }
    IEnumerator CreateGris()
    {
        StartCoroutine(SetCreateCount(5));
        while (true)
        {
            if (grisNum>=grisCount)
            {
                yield break;
            }
            Instantiate(animator.gameObject);
            grisNum++;
            yield return new WaitForSeconds(2);
        }
    }
    IEnumerator SetCreateCount(int num)
    {
        grisCount =num;
        yield return null;
    }
```





# 异常

```c#
try
{
    throw new Exception("自定义异常");
}
catch (Exception e)
{
    Console.WriteLine(e);
    Console.ReadLine();
}
finally { 
}

```





# Invoke延时调用

```c#
 public GameObject grisGo;
void Start()
{
    //调用
    //Invoke("CreateGris",3);
    InvokeRepeating("CreateGris",1,1);
    //停止
    CancelInvoke("CreateGris");
    //CancelInvoke();
    InvokeRepeating("Test",1,1);
}

void Update()
{
    print(IsInvoking("CreateGris"));
    print(IsInvoking());
}

private void CreateGris()
{
    Instantiate(grisGo);
}

private void Test()
{
    
}
```





# 多线程

## 创建

```c#
using System.Threading;
public static void show() 
{
    Console.WriteLine("hello world");
}

Thread childThread = new Thread(new ThreadStart(Program.show));
childThread.Start();
```

## 终止

```c#
 childThread.Abort();
```



# 类型转换



隐式转换

```c#
int a = 1;
double b = a;//可以小类型转到大类型
```





```c#
class Father 
{}

class Son:Father
{ }


```

测试

```c#
//子类可以隐式转换到父类 
Father father = new Son();

//父类只能强制转换，或者通过as转换


```

如果父类指向的对象确实是子类，那么可以用强制类型转换。

```c#
Father father = new Son();
Son son = (Son)father;
```



如果父类指向的不是子类，那么会在运行时报错

```c#
Father father = new Father();
Son son = (Son)father;
```

<img src="J:/0_我的项目备份/笔记/游戏开发/unity开发/img/C%23/image-20220516142537402.png" alt="image-20220516142537402" style="zoom:50%;" />



可以使用as语法，来转换，转换失败时不会报错，但是会赋值为null

```c#
Father father = new Father();
Son son = father as Son;
Console.WriteLine(son==null);//True
```



# 折叠代码

```c#
#region 左右两侧头发的摇摆
#endregion
```



# 正则表达式



# 字符串

string实际上是`System.String`的别名



- 比较

  如果相等则返回0

  ```c#
  var str = "test";
  Console.WriteLine(str.CompareTo("test"));//0
  ```

  



# 可变参数

使用 [params](https://so.csdn.net/so/search?q=params&spm=1001.2101.3001.7020) 关键字可以指定采用数目可变的参数的方法参数。 参数类型必须是一维数组。

在方法声明中的 params 关键字之后不允许有任何其他参数，并且在方法声明中只允许有一个 params 关键字。

```c#
public static void UseParams(params int[] list)
{
    for (int i = 0; i < list.Length; i++)
    {
        Console.Write(list[i] + " ");
    }
    Console.WriteLine();
}
```





# where

Where是一个C#的关键字，它有两种用法：

-   [一种是用在泛型类型约束中，表示类型参数必须满足某些条件，比如继承自某个类或实现某个接口](https://learn.microsoft.com/ja-jp/dotnet/csharp/language-reference/keywords/where-generic-type-constraint)[1](https://learn.microsoft.com/ja-jp/dotnet/csharp/language-reference/keywords/where-generic-type-constraint)。例如：

```csharp
// T必须是Animal的子类或本身
class Zoo<T> where T : Animal
{
    // ...
}
```

-   [另一种是用在LINQ查询中，表示对数据源中的元素进行过滤，只保留满足某个条件的元素](https://learn.microsoft.com/ja-jp/dotnet/csharp/language-reference/keywords/where-clause)[2](https://learn.microsoft.com/ja-jp/dotnet/csharp/language-reference/keywords/where-clause)[3](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.where?view=net-8.0)。例如：

```csharp
// 从numbers中筛选出偶数
var evenNumbers = from n in numbers
                  where n % 2 == 0
                  select n;
```

[在你的代码中，Where是一个扩展方法，它接受一个委托作为参数，返回一个IEnumerable，其中只包含满足委托条件的元素](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.where?view=net-8.0)[3](https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.where?view=net-8.0)。例如：

```csharp
// 从mrs中筛选出不等于transform的元素
mrs = mrs.Where(c => c.transform != transform);
```

你明白了吗？



你好，这是Bing。😊

[GetComponentInChildren是一个Unity的方法，它可以返回一个GameObject或它的任何子对象中的指定类型的组件](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)[1](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)[2](https://docs.unity3d.com/ja/current/ScriptReference/Component.GetComponentInChildren.html)[。它使用深度优先搜索，首先检查调用它的GameObject，然后递归地向下搜索，直到找到一个匹配的组件](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)[1](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)[。它只包括活动的子对象，除非另外指定](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)[1](https://docs.unity3d.com/ScriptReference/Component.GetComponentInChildren.html)。

GetComponentInChildren的使用方法是：

```csharp
// 获取当前对象或其子对象中的第一个Rigidbody组件
Rigidbody rb = GetComponentInChildren<Rigidbody>();

// 获取当前对象或其子对象中的所有MeshRenderer组件
MeshRenderer[] mrs = GetComponentsInChildren<MeshRenderer>();
```

[注意，GetComponentInChildren会包括自身的组件，如果只想获取子对象的组件，可以使用以下方法](https://bing.com/search?q=unity+GetComponentInChildren)[3](https://bing.com/search?q=unity+GetComponentInChildren)：

```csharp
// 获取子对象中的所有MeshRenderer组件
MeshRenderer[] mrs = transform.GetComponentsInChildren<MeshRenderer>().Where(c => c.transform != transform).ToArray();
```