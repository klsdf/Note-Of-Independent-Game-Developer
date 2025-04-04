
# SOLID设计原则

## 单一职责原则（Single Responsibility Principle, SRP）


一个类应该**只有一个原因可以引起它的变化**。

**❌ 违反 SRP 的例子**（一个 `Report` 类负责**数据处理和文件写入**）：

```c#
public class Report
{
    public void GenerateReport() { Console.WriteLine("生成报告"); }
    public void SaveToFile() { Console.WriteLine("保存到文件"); }
}
```


```c#
public class ReportGenerator
{
    public void Generate() { Console.WriteLine("生成报告"); }
}

public class ReportSaver
{
    public void Save(string filePath) { Console.WriteLine($"保存到 {filePath}"); }
}

```





## 开放封闭原则（Open/Closed Principle, OCP）

**原则**：**对扩展开放，对修改封闭**。即**可以扩展功能，但不要修改已有代码**。


❌ 违反 OCP（每次增加新形状，都要修改 `AreaCalculator`）
```c#
public class AreaCalculator
{
    public double CalculateArea(object shape)
    {
        if (shape is Circle circle) return Math.PI * circle.Radius * circle.Radius;
        if (shape is Rectangle rect) return rect.Width * rect.Height;
        return 0;
    }
}

```



👉 **新形状只需实现 `IShape`，无需修改 `AreaCalculator`，符合 OCP**。
```c#
public interface IShape { double GetArea(); }

public class Circle : IShape
{
    public double Radius { get; set; }
    public double GetArea() => Math.PI * Radius * Radius;
}

public class Rectangle : IShape
{
    public double Width { get; set; }
    public double Height { get; set; }
    public double GetArea() => Width * Height;
}

public class AreaCalculator
{
    public double CalculateArea(IShape shape) => shape.GetArea();
}

```





## 里氏替换原则（Liskov Substitution Principle, LSP）

**原则**：子类必须**完全和安全**替换父类，而不发生意料之外的情况。


❌ 违反 LSP（`Penguin` 不能飞，但继承 `Bird`，导致 `Fly()` 方法无意义）

```c#
public class Bird
{
    public virtual void Fly() { Console.WriteLine("鸟在飞翔"); }
}

public class Sparrow : Bird { } // 可以飞

public class Penguin : Bird
{
    public override void Fly() { throw new Exception("企鹅不会飞"); } // ❌ 违背 LSP
}

```


✅ 遵守 LSP（抽象出 `IFlyingBird` 和 `INonFlyingBird`）
```c#
public interface IFlyingBird { void Fly(); }
public interface INonFlyingBird { }

public class Sparrow : IFlyingBird
{
    public void Fly() { Console.WriteLine("麻雀在飞翔"); }
}

public class Penguin : INonFlyingBird { } // 企鹅不实现 `Fly`

```




## 接口隔离原则（Interface Segregation Principle, ISP）

**原则**：**不强迫类实现它不需要的接口**，即避免**大而全的接口**。


❌ 违反 ISP（所有动物都必须实现 `Swim`，但狗不会游泳）

```c#
public interface IAnimal
{
    void Run();
    void Swim(); // ❌ 狗不会游泳，但被强制实现
}

public class Dog : IAnimal
{
    public void Run() { Console.WriteLine("狗在跑"); }
    public void Swim() { throw new Exception("狗不会游泳"); } // ❌ 违背 ISP
}

```

✅ 遵守 ISP（拆分 `IAnimal` 为多个小接口）

```c#
public interface IRunnable { void Run(); }
public interface ISwimmable { void Swim(); }

public class Dog : IRunnable
{
    public void Run() { Console.WriteLine("狗在跑"); }
}
public class Fish : ISwimmable
{
    public void Swim() { Console.WriteLine("鱼在游泳"); }
}

```
👉 **接口拆分，使得类**只需实现**自己需要的功能，避免冗余代码。**





C# 官方的 `IList<T>` 就是一个**违反 ISP 的典型例子**，因为它继承自 `ICollection<T>` 和 `IEnumerable<T>`，但其中的方法**并不适用于所有情况**，导致一些数据结构必须实现不必要的方法。



```c#
using System;
using System.Collections.Generic;

class Program
{
    private static void AddToList(IList<int> list)
    {
        list.Add(1);  // 这里假设 list 能够添加元素
    }

    static void Main(string[] args)
    {
        var list = new List<int>();
        AddToList(list);  // ✅ List<int> 可以作为 IList<int> 传递

        var array = new int[5]; 
        AddToList(array); // ❌ 抛出异常

        Console.ReadKey();
    }
}

```

因为数组是一个不可以变长度的数据结构，所以虽然它实现了IList接口，但是内部在Add中抛出异常了。

```c#
int IList.Add(object value)
{
throw new NotsupportedException(Environment,GetResourcestring("Notsupported Fixedsizecollection")):
}
```


在 C# 中，`数组（int[]）` **确实实现了** `IList<int>`，但它**不支持添加和删除操作**，因为数组长度是固定的。所以c#官方强迫数组实现了它不应该实现的接口，违反了接口隔离原则（ISP）



## 依赖倒置原则（Dependency Inversion Principle, DIP）


**原则**：

1. **高层模块（如 `Game` 类）不应该依赖低层模块（如 `Bow`、`Sword`），两者都应该依赖抽象**。
2. **细节（具体实现）应该依赖抽象（接口），而不是相反**。


依赖倒置原则（DIP）说白了就是不建议让类去自己生成其它类的对象，导致了高耦合。而是应该传进来其它类的实现了所需接口的对象。

- 依赖注入就是指直接由外部传入一个对象到构造函数里面，避免类内部创建所需的对象。
- 依赖注入是实现依赖倒置原则的一种方法。



❌ 反例：违反 DIP
游戏角色依赖具体武器类

```c#
public class Sword
{
    public void Attack() { Console.WriteLine("挥舞剑攻击！"); }
}

public class Archer
{
    private Sword _sword = new Sword(); // ❌ 直接依赖具体实现

    public void Attack()
    {
        _sword.Attack();
    }
}

```



```c#
public interface IWeapon
{
    void Attack();
}

public class Sword : IWeapon
{
    public void Attack() { Console.WriteLine("挥舞剑攻击！"); }
}

public class Bow : IWeapon
{
    public void Attack() { Console.WriteLine("射箭攻击！"); }
}

public class Archer
{
    private IWeapon _weapon; // ✅ 依赖抽象，不依赖具体实现

    public Archer(IWeapon weapon) // ✅ 通过构造函数注入依赖
    {
        _weapon = weapon;
    }

    public void Attack()
    {
        _weapon.Attack();
    }
}

```



# 其它设计原则


## DRY原则

DRY（Don't Repeat Yourself）原则是一种软件开发原则，旨在减少代码重复，提高可维护性和可读性。它的核心思想是：**同一部分的知识或逻辑在代码中不应该重复，而应该被抽象成一个单一的、可复用的模块**。


违反 DRY 原则

```c#
Console.WriteLine("User 1: John Doe, Age: 30");
Console.WriteLine("User 2: Jane Doe, Age: 25");
Console.WriteLine("User 3: Alice, Age: 28");
```

遵循 DRY 原则
```c#

void PrintUser(string name, int age)
{
    Console.WriteLine($"User: {name}, Age: {age}");
}
PrintUser("John Doe", 30);
PrintUser("Jane Doe", 25);
PrintUser("Alice", 28);
```



 **DRY vs WET**

- **DRY（Don't Repeat Yourself）**：避免重复，提倡抽象和封装。
- **WET（Write Everything Twice 或 We Enjoy Typing）**：代码中存在大量重复逻辑，导致维护困难。

## 魔法数字（Magic Number）反模式


**魔法数字（Magic Number）反模式** 指的是在代码中直接使用**没有明确意义的数值常量**，而不是使用具有描述性的变量或常量名称。这种做法会降低代码的可读性、可维护性，并可能导致难以理解的逻辑错误。

❌ 违反魔法数字反模式的例子

```c#
double CalculateCircleArea(double radius)
{
    return 3.14159 * radius * radius;  // 这里的 3.14159 是魔法数字
}

```


✅ 遵循最佳实践

```c#
const double PI = 3.14159;

double CalculateCircleArea(double radius)
{
    return PI * radius * radius;  // 现在代码可读性更高
}

```



## 什么是意大利面代码？（Spaghetti Code）

**Spaghetti Code（面条代码）** 是用来形容**混乱、无结构的代码**，因为这种代码的逻辑像意大利面条一样纠缠在一起，难以理解和维护。因此，程序员用 **"Spaghetti Code"** 来比喻“杂乱无章的代码结构”。

### ** 面条代码的典型特征**

1. **没有结构化设计**
    - 代码缺乏清晰的层次结构，没有遵循良好的设计模式。
2. **大量全局变量**
    - 依赖多个全局变量，导致不同函数之间相互影响，难以跟踪数据变化。
3. **过长的方法和类**
    - 一个方法可能包含数百行代码，没有合理拆分成更小的函数，使得代码难以阅读和调试。
4. **缺乏注释和文档**
    - 代码逻辑复杂且没有注释，即使是原作者，过一段时间后也可能无法理解代码的意图。
5. **过多的 if/else 和嵌套循环**
    - 逻辑控制混乱，深层嵌套导致代码可读性极差。
6. **重复代码**
    - 没有遵循 **DRY（Don't Repeat Yourself）** 原则，导致同样的逻辑在多个地方重复出现，维护时需要修改多个地方。


❌ 违反最佳实践的面条代码示例
```c#
void ProcessOrder(string orderType, int quantity)
{
    if (orderType == "A")
    {
        if (quantity > 10)
        {
            Console.WriteLine("Large order for type A");
        }
        else
        {
            Console.WriteLine("Small order for type A");
        }
    }
    else if (orderType == "B")
    {
        if (quantity > 10)
        {
            Console.WriteLine("Large order for type B");
        }
        else
        {
            Console.WriteLine("Small order for type B");
        }
    }
    else if (orderType == "C")
    {
        if (quantity > 10)
        {
            Console.WriteLine("Large order for type C");
        }
        else
        {
            Console.WriteLine("Small order for type C");
        }
    }
}

```


✅ 采用良好实践优化面条代码

```c#
void ProcessOrder(string orderType, int quantity)
{
    string size = quantity > 10 ? "Large" : "Small";
    Console.WriteLine($"{size} order for type {orderType}");
}
```








# 创建型模式（Creational Patterns）

创建型模式的主要目的是**控制对象创建的过程**，让系统能够更加灵活、可扩展，避免直接使用 `new` 关键字实例化对象。它将对象的创建过程抽象化，并将其与客户端代码分离。


## 工厂模式（Factory Pattern）

### 简单工厂模式 （Simple Factory）

一个工厂负责生成所有产品

- **违反开闭原则（OCP）**：每次新增产品，都要修改工厂的 `switch` 或 `if-else` 语句。
- **单一工厂类可能变得臃肿**，如果产品越来越多，维护困难。

```c#
public interface IEnemy { void Attack(); }

public class Goblin : IEnemy { public void Attack() => Debug.Log("Goblin Attack!"); }
public class Orc : IEnemy { public void Attack() => Debug.Log("Orc Attack!"); }

public class SimpleEnemyFactory
{
    public static IEnemy CreateEnemy(string type)
    {
        switch (type)
        {
            case "Goblin": return new Goblin();
            case "Orc": return new Orc();
            default: throw new ArgumentException("Invalid type");
        }
    }
}

// 客户端调用：
IEnemy enemy = SimpleEnemyFactory.CreateEnemy("Goblin");
enemy.Attack();

```

### 工厂模式（Factory Method）

每个工厂生产自己的产品

- 每个产品有**自己的工厂**，避免了 `switch` 语句。
- **适用于对象类型较多的情况**，符合**开闭原则（OCP）**。
- **但类的数量增加**，每新增一个产品，都需要创建一个新的工厂类。


```c#
// 产品接口
public interface IEnemy { void Attack(); }

// 具体产品
public class Goblin : IEnemy { public void Attack() => Debug.Log("Goblin Attack!"); }
public class Orc : IEnemy { public void Attack() => Debug.Log("Orc Attack!"); }

// 抽象工厂
public abstract class EnemyFactory { public abstract IEnemy CreateEnemy(); }

// 具体工厂（每个工厂创建一种敌人）
public class GoblinFactory : EnemyFactory { public override IEnemy CreateEnemy() => new Goblin(); }
public class OrcFactory : EnemyFactory { public override IEnemy CreateEnemy() => new Orc(); }

// 客户端代码：
EnemyFactory factory = new GoblinFactory();
IEnemy enemy = factory.CreateEnemy();
enemy.Attack();
```



## 抽象工厂（Abstract Factory）

一个工厂可以生产多个产品，这些产品也有一定的联系，也就是产品族。


```c#
// 产品接口
public interface IWeapon { void Attack(); }
public interface IArmor { void Defend(); }

// 具体产品（精灵族装备）
public class ElfWeapon : IWeapon { public void Attack() => Debug.Log("Elf Weapon Attack!"); }
public class ElfArmor : IArmor { public void Defend() => Debug.Log("Elf Armor Defense!"); }

// 具体产品（兽人族装备）
public class OrcWeapon : IWeapon { public void Attack() => Debug.Log("Orc Weapon Attack!"); }
public class OrcArmor : IArmor { public void Defend() => Debug.Log("Orc Armor Defense!"); }

// 抽象工厂（定义产品族）
public abstract class EquipmentFactory
{
    public abstract IWeapon CreateWeapon();
    public abstract IArmor CreateArmor();
}

// 具体工厂（精灵族工厂）
public class ElfEquipmentFactory : EquipmentFactory
{
    public override IWeapon CreateWeapon() => new ElfWeapon();
    public override IArmor CreateArmor() => new ElfArmor();
}

// 具体工厂（兽人族工厂）
public class OrcEquipmentFactory : EquipmentFactory
{
    public override IWeapon CreateWeapon() => new OrcWeapon();
    public override IArmor CreateArmor() => new OrcArmor();
}

// 客户端代码
EquipmentFactory factory = new ElfEquipmentFactory();
IWeapon weapon = factory.CreateWeapon();
IArmor armor = factory.CreateArmor();
weapon.Attack();
armor.Defend();

```


## 建造者（Builder）

允许**分步骤创建复杂对象**，并允许我们使用相同的构建过程生产不同的对象。这个在node draw中用的很多，主要为了让构造函数过于复杂。有些对象的某些属性可以缺省，有些不可以。若用构造函数重载可能会复杂度爆炸。

```c#

//传统模式
public class Character
{
    public string Name;
    public int Health;
    public int Attack;
    public int Defense;

    public Character(string name, int health, int attack, int defense)
    {
        Name = name;
        Health = health;
        Attack = attack;
        Defense = defense;
    }
}

// 创建角色
Character hero = new Character("Warrior", 100, 50, 30);

```



```c#
public class Character
{
    public string Name;
    public int Health;
    public int Attack;
    public int Defense;

    public Character SetName(string name) { this.Name = name; return this; }
    public Character SetHealth(int health) { this.Health = health; return this; }
    public Character SetAttack(int attack) { this.Attack = attack; return this; }
    public Character SetDefense(int defense) { this.Defense = defense; return this; }

    public void ShowInfo()
    {
        Debug.Log($"角色：{Name} | 生命：{Health} | 攻击：{Attack} | 防御：{Defense}");
    }
}

// 这样创建角色更加直观：
Character warrior = new Character()
    .SetName("Warrior")
    .SetHealth(100)
    .SetAttack(50)
    .SetDefense(30);
    
warrior.ShowInfo();
```



## 单例模式（Singleton）




用来处理DontDestroyOnLoad

```c#
public class GameManager : MonoBehaviour
{
	private static GameManager _instance;   // 单例
	public GameManager GameManagerInstance
    {
        get { return _instance; }
    }
    void Awake()
    {
        if (_instance != null)
        {
        	//这里一定要是销毁this.gameObject
            Destroy(this.gameObject);
            return;
        }
        //这句话只执行一次，第二次上面return了
        _instance = this;
    }
}

```



不继承mono的

```c#
public class Test 
{


    private static Test _instance;
    //单例模式
    public static Test Instance
    {
        get
         {
            if (_instance == null) {
                _instance = new Test();
            }
            return _instance;

        }
    }
}
```



继承mono的

```c#
public class UIController:MonoBehaviour
{

    public static UIController Instance;
 

    private void Awake()
    {
        Instance = this;
    }

    public void changeRestBalls()
    {

    }
}
```

虽然直接在awake中写很方便，但是存在一个问题。那就是awake的调用顺序是不一定的，在脚本中，如果awake时出现了单例互相调用的情况，那么有可能其他的单例还没有初始化，因此可以用下面的方法进行改进。



```c#
static Test instance;
public static Test Instance
{
    get
    {
        if(instance == null)
        {
            instance = FindObjectOfType<Test>();
           
        }
         return instance;
    }
}
```




## 原型模式（Prototype）

**原型模式** 是一种**创建型设计模式**，用于**克隆（复制）对象**，而不需要每次都 `new` 一个新的实例。  
当对象的创建成本较高，或者需要大量相似的对象时，原型模式能提高性能并减少重复代码。

Unity 提供的 **`Instantiate`** 方法本质上就是**原型模式**的实现：
 

```c#
using System;
using UnityEngine;

// 1. 定义原型接口
public interface IPrototype<T>
{
    T Clone(); // 克隆方法
}

// 2. 具体原型类
[Serializable] // 让 Unity 能序列化
public class Enemy : IPrototype<Enemy>
{
    public string Name;
    public int Health;
    public float Speed;

    public Enemy(string name, int health, float speed)
    {
        Name = name;
        Health = health;
        Speed = speed;
    }

    // 3. 实现克隆方法（浅拷贝）
    public Enemy Clone()
    {
        return (Enemy)this.MemberwiseClone();
    }

    public void ShowInfo()
    {
        Debug.Log($"Enemy: {Name}, HP: {Health}, Speed: {Speed}");
    }
}

// 4. 客户端代码
public class GameManager : MonoBehaviour
{
    void Start()
    {
        // 创建原型对象
        Enemy originalEnemy = new Enemy("Orc", 100, 2.5f);
        originalEnemy.ShowInfo();

        // 克隆敌人
        Enemy clonedEnemy = originalEnemy.Clone();
        clonedEnemy.Name = "Goblin"; // 修改克隆体的属性
        clonedEnemy.Health = 50;
        clonedEnemy.ShowInfo();
    }
}
```



# 结构型模式（Structural Patterns）

结构型模式主要解决**类或对象之间的关系**，如何通过组合和继承来构建更大的结构。其核心思想是通过将小的模块组合成更复杂的结构，从而让系统更加灵活且易于维护。






## 适配器模式（Adapter）

假设你正在制作一款游戏，老版本的敌人 `OldEnemy` 使用 `AttackOld()`，但新版系统要求所有敌人都使用 `IAttack.Attack()`。

**🛑 问题：** 不能修改 `OldEnemy`，但你仍然希望它能在新系统中使用。

或者单纯适配各个api

- 本质上就是搞一个新通用的接口，让一个装饰器类实现这个接口。然后，把其它需要适配的对象传到装饰器类的构造函数里面就完事了。
- ai中用的很多

注意，在你自己写代码的时候，不要使用适配器！不要使用适配器！
没必要自己给自己上难度。只有在迫不得已去统一一个接口的时候才需要这个模式。就比如koishi框架，为了兼容qq和飞书等平台的机器人就用了适配器。不同平台的机器人api和调用肯定不一样，但是对外的表现都是一样的。所以需要做装饰器。


```c#

// 定义通用的 AI 接口
public interface IAIAdapter
{
    string GetResponse(string input);
}


// 假设 OpenAI 的 API 只能通过 SendToOpenAI(string prompt) 发送请求
public class OpenAI
{
    public string SendToOpenAI(string prompt)
    {
        return $"[OpenAI]: {prompt} 的回复";
    }
}

// OpenAI 适配器，实现 IAIAdapter 接口
public class OpenAIAdapter : IAIAdapter
{
    private OpenAI openAI;

    public OpenAIAdapter(OpenAI openAI)
    {
        this.openAI = openAI;
    }

    public string GetResponse(string input)
    {
        return openAI.SendToOpenAI(input);
    }
}






// Google AI 需要调用 GoogleRequest(string query)
public class GoogleAI
{
    public string GoogleRequest(string query)
    {
        return $"[Google AI]: {query} 的回复";
    }
}

// Google AI 适配器
public class GoogleAIAdapter : IAIAdapter
{
    private GoogleAI googleAI;

    public GoogleAIAdapter(GoogleAI googleAI)
    {
        this.googleAI = googleAI;
    }

    public string GetResponse(string input)
    {
        return googleAI.GoogleRequest(input);
    }
}


```


客户端代码

```c#
public class AIManager
{
    private IAIAdapter aiAdapter;

    public AIManager(IAIAdapter aiAdapter)
    {
        this.aiAdapter = aiAdapter;
    }

    public void Chat(string input)
    {
        string response = aiAdapter.GetResponse(input);
        Debug.Log(response);
    }
}

// 测试代码
public class Program
{
    public static void Main()
    {
        // 使用 OpenAI
        IAIAdapter openAI = new OpenAIAdapter(new OpenAI());
        AIManager aiManager1 = new AIManager(openAI);
        aiManager1.Chat("你好");

        // 使用 Google AI
        IAIAdapter googleAI = new GoogleAIAdapter(new GoogleAI());
        AIManager aiManager2 = new AIManager(googleAI);
        aiManager2.Chat("你好");
    }
}


```




## 桥接模式（Bridge）


- **将不同维度的变化分离**，避免类的层级爆炸。
- **用组合代替继承**，降低耦合度，提高灵活性。
- **适用于多个维度扩展的对象模型**。
- 本质上就是在构造函数里面可以new一些组件过来，在创造时来动态构成这个对象。





还是经典的《合成放置大乱斗》，先开始搞一个士兵抽象类，然后有了剑士，魔法师和牧师。剑士派生了骑士，但是现在再出一个医院骑士就麻烦了。因为不能多继承，只能多写一个医院骑士的类。而骑士不过是让士兵的速度变化。魔法师和牧师本质上是远程攻击敌人或自己人（只不过牧师的攻击伤害是负数）



```c#
// 士兵基类，桥接"移动方式"和"攻击方式"
public abstract class Soldier
{
    protected IMovement movement;  // 移动方式（步行、骑马）
    protected IAttack attack;      // 攻击方式（近战、远程、治疗）

    public Soldier(IMovement movement, IAttack attack)
    {
        this.movement = movement;
        this.attack = attack;
    }

    public void Move() => movement.Move();
    public void Attack() => attack.Execute();
}


// 移动方式接口（Implementor 1）
public interface IMovement
{
    void Move();
}

// 步行
public class Walk : IMovement
{
    public void Move() => Debug.Log("步行前进");
}

// 骑马
public class HorseRide : IMovement
{
    public void Move() => Debug.Log("骑马冲锋");
}




// 攻击方式接口（Implementor 2）
public interface IAttack
{
    void Execute();
}

// 近战攻击
public class MeleeAttack : IAttack
{
    public void Execute() => Debug.Log("进行近战攻击！");
}

// 远程魔法攻击
public class MagicAttack : IAttack
{
    public void Execute() => Debug.Log("施放远程魔法！");
}

// 治疗（远程攻击己方，伤害是负数）
public class HealAttack : IAttack
{
    public void Execute() => Debug.Log("释放治疗术！（攻击自己人，伤害是负数）");
}



// 剑士（可以选择任意攻击方式）
public class Swordsman : Soldier
{
    public Swordsman(IMovement movement, IAttack attack) 
        : base(movement, attack) { }
}


```



```c#
public class Game
{
    public static void Main()
    {
        // 剑士（步行 + 近战）
        Soldier swordsman = new Swordsman(new Walk(), new MeleeAttack());
        swordsman.Move();
        swordsman.Attack();

        // 骑士（剑士 + 骑马 + 近战）
        Soldier knight = new Swordsman(new HorseRide(), new MeleeAttack());
        knight.Move();
        knight.Attack();

        // 魔法剑士（剑士 + 骑马 + 远程魔法攻击）
        Soldier magicKnight = new Swordsman(new HorseRide(), new MagicAttack());
        magicKnight.Move();
        magicKnight.Attack();
    }
}
```





## 组合模式（Composite）


- 当逻辑的结构是树形结构的时候很适合用组合模式。比如人口普查，首先需要调用各个乡镇的统计接口，然后把乡镇组合成省市，调用省市的接口。而这些乡镇和省市都是可以理解为一个树的。每个枝干的接口都是一样的。
- 可以让单个对象和容器（一堆对象）使用相同的接口，让“整体”和“部分”可以用相同的方式操作。


在这里，一个普通敌人和军队，都拥有相同的attack接口。在设计战斗的时候，我只用考虑军队的attack即可。军队负责处理下级叶子节点的attack逻辑。
```c#
// 组件基类（组合模式的核心）
public abstract class Enemy
{
    public abstract void Attack();
}

// 叶子节点（单个敌人）
public class Soldier : Enemy
{
    public override void Attack()
    {
        Debug.Log("士兵发起攻击！");
    }
}

// 组合节点（多个敌人组成的队伍）
public class Army : Enemy
{
    private List<Enemy> enemies = new List<Enemy>();

    public void Add(Enemy enemy)
    {
        enemies.Add(enemy);
    }

    public void Remove(Enemy enemy)
    {
        enemies.Remove(enemy);
    }

    public override void Attack()
    {
        Debug.Log("军队开始攻击！");
        foreach (var enemy in enemies)
        {
            enemy.Attack();
        }
    }
}

```



```c#
public static void Main()
{
    Soldier soldier1 = new Soldier();
    Soldier soldier2 = new Soldier();
    
    Army smallArmy = new Army();
    smallArmy.Add(soldier1);
    smallArmy.Add(soldier2);

    Army bigArmy = new Army();
    bigArmy.Add(smallArmy);
    bigArmy.Add(new Soldier());

    Debug.Log("单个士兵攻击：");
    soldier1.Attack();

    Debug.Log("小型军队攻击：");
    smallArmy.Attack();

    Debug.Log("大型军团攻击：");
    bigArmy.Attack();
}

/*
单个士兵攻击：
士兵发起攻击！
小型军队攻击：
军队开始攻击！
士兵发起攻击！
士兵发起攻击！
大型军团攻击：
军队开始攻击！
军队开始攻击！
士兵发起攻击！
士兵发起攻击！
士兵发起攻击！
*/
```







## 装饰器模式（Decorator）


- 和适配器模式有点相似，都是对接口进行了包装
- 但是**组合多个装饰器**来为对象增加更多的功能。一个适配器是不可以再叠一个一样的适配器的


```c#
// 角色接口
public interface ICharacter
{
    void Attack();
    int GetAttackPower();
}

// 基本角色类：攻击力为 10
public class BasicCharacter : ICharacter
{
    private int attackPower = 10;

    public void Attack()
    {
        Debug.Log("角色发动攻击！");
    }

    public int GetAttackPower()
    {
        return attackPower;
    }
}

```


装饰器基类，装饰器一定是和装饰的物体实现同一套接口，才能保证相同的api。要不然调用的api不一样就算不上装饰器了。


**需要装饰谁就把谁搞成接口，然后实现谁，装饰器里面传入谁！！！**


而且装饰器的构造函数里面一定要传入一个装饰的物体的接口，这样才能去装饰它。
当然了，js的话直接用函数指针来赋值就完事了。




```c#
// 装饰器基类，继承自 ICharacter，所有装饰器都从这个类派生
public abstract class CharacterDecorator : ICharacter
{
    protected ICharacter _character;

    public CharacterDecorator(ICharacter character)
    {
        _character = character;
    }

    public virtual void Attack()
    {
        _character.Attack();
    }

    public virtual int GetAttackPower()
    {
        return _character.GetAttackPower();
    }
}

```


装饰器首先用了传进来的值，然后先调用了一波，之后加点自己的东西。装饰器加基类，主要是为了一致性。也可以直接实现ICharacter。
虽然**装饰器模式不强制要求有基类**，但在实际应用中，**引入一个基类或接口能够带来更好的扩展性、可维护性和一致性**，这就是为什么**大多数装饰器模式的实现都会有一个基类**。

```c#
// 武器装饰器：增加攻击力
public class WeaponDecorator : CharacterDecorator
{
    private int additionalAttackPower;

    public WeaponDecorator(ICharacter character, int additionalAttackPower)
        : base(character)
    {
        this.additionalAttackPower = additionalAttackPower;
    }

    public override void Attack()
    {
        base.Attack();
        Debug.Log("使用武器攻击！");
    }

    public override int GetAttackPower()
    {
        return base.GetAttackPower() + additionalAttackPower;
    }
}
```



```c#
public class Game
{
    public static void Main()
    {
        // 创建一个基本角色
        ICharacter character = new BasicCharacter();
        Debug.Log("基础角色攻击力：" + character.GetAttackPower());
        character.Attack();

        // 给角色装备武器
        character = new WeaponDecorator(character, 20); // 增加 20 攻击力
        Debug.Log("装备武器后的攻击力：" + character.GetAttackPower());
        character.Attack();
    }

//Weapon armoredWarrior = new Weapon(new Weapon(new BasicCharacter()));
}

```

装饰器模式可以无限嵌套，因为所有装饰器都会返回实现的接口，而它自己有需要传入这个接口。


## 外观模式（Facade）


**外观模式（Facade Pattern）** 是 **结构型设计模式**，它的主要目的是**对复杂的子系统提供一个统一的简化接口**，让客户端可以更方便地访问系统，而无需关心内部的复杂逻辑。

> **简单来说：**
> 
> - **隐藏系统的复杂性**，提供一个**简化的 API** 供外部使用。
> - **降低耦合度**，客户端不需要直接操作复杂的子系统，而是通过外观类进行交互。


违反了开闭原则，因为子系统变更会导致外观类也发生变化。



如果不使用外观模式，客户端代码可能如下：


```c#
public class Game
{
    public void Start()
    {
        AudioManager audio = new AudioManager();
        audio.LoadSounds();
        audio.PlayBackgroundMusic();

        GraphicsManager graphics = new GraphicsManager();
        graphics.LoadTextures();
        graphics.RenderScene();

        InputManager input = new InputManager();
        input.Initialize();
    }
}

```



如果使用了外观模式的话（
```c#
// 子系统1：音频管理
public class AudioManager
{
    public void LoadSounds() { Console.WriteLine("加载音效..."); }
    public void PlayBackgroundMusic() { Console.WriteLine("播放背景音乐..."); }
}

// 子系统2：图形管理
public class GraphicsManager
{
    public void LoadTextures() { Console.WriteLine("加载纹理..."); }
    public void RenderScene() { Console.WriteLine("渲染场景..."); }
}

// 子系统3：输入管理
public class InputManager
{
    public void Initialize() { Console.WriteLine("初始化输入设备..."); }
}

// 外观类：提供简单的接口
public class GameFacade
{
    private AudioManager _audio;
    private GraphicsManager _graphics;
    private InputManager _input;

    public GameFacade()
    {
        _audio = new AudioManager();
        _graphics = new GraphicsManager();
        _input = new InputManager();
    }

    public void InitializeGame()
    {
        Console.WriteLine("初始化游戏...");
        _audio.LoadSounds();
        _audio.PlayBackgroundMusic();
        _graphics.LoadTextures();
        _graphics.RenderScene();
        _input.Initialize();
        Console.WriteLine("游戏启动成功！");
    }
}

// 客户端代码
public class Game
{
    public void Start()
    {
        GameFacade gameFacade = new GameFacade();
        gameFacade.InitializeGame();  // 只需调用一个方法，简化了逻辑
    }
}

```



## 享元模式（Flyweight）


**享元模式（Flyweight Pattern）** 是一种**结构型设计模式**，它的核心思想是**通过共享数据来减少对象的数量，从而降低内存消耗**。


**！！！！注意，享元模式和对象池模式是两个概念！！！！！！！！！**

- 享元模式是为了解决内存问题，通过不同对象共享同一个数据减少内存占用！
- 而对象池模式是为了减少反复生成和销毁对象带来的算力开销。
- 享元模式还是需要创建一个新对象的，只不过对象中的一部分数据是共享的（例如贴图，模型等），而对象池是完完全全复用一个对象。


享元模式一般包含：

1. **Flyweight（享元类）**：表示**可共享的部分**，通常是**不可变数据**。
2. **ConcreteFlyweight（使用享元对象的具体类）**：实现共享逻辑，存储不可变数据。
3. **FlyweightFactory（享元工厂类）**：用于**管理和复用享元对象**，保证相同数据的对象不会重复创建。
4. **Client（客户端）**：使用享元对象，存储可变数据。



享元类，定义可以被享元的数据
```c#
using System;

public class EnemyFlyweight
{
    public string Name { get; private set; }  // 通过职级确定名字
    public string ImagePath { get; private set; }  // 通过职级确定图片路径
    public string[] SoundEffects { get; private set; }  // 统一的音效
    public string Color { get; private set; }  // 统一的颜色
    public int MaxHealth { get; private set; }  // 通过职级确定血量上限
    public double Speed { get; private set; }  // 通过职级确定速度

    public EnemyFlyweight(string name, string imagePath, string[] soundEffects, string color, int maxHealth, double speed)
    {
        Name = name;
        ImagePath = imagePath;
        SoundEffects = soundEffects;
        Color = color;
        MaxHealth = maxHealth;
        Speed = speed;
    }
}

```


正常的敌人类，并且持有EnemyFlyweight这个引用，并包含不可共享的属性：hp和height。


```c#
public class Enemy
{
    private EnemyFlyweight _flyweight;  // 享元对象
    public int CurrentHealth { get; set; }  // 当前血量
    public double Height { get; set; }  // 身高

    public Enemy(string rank, int currentHealth, double height)
    {
        _flyweight = FlyweightFactory.Instance.GetFlyweight(rank);
        CurrentHealth = currentHealth;
        Height = height;
    }

    public void DisplayEnemyInfo()
    {
        Console.WriteLine($"Name: {_flyweight.Name}");
        Console.WriteLine($"Health: {CurrentHealth}/{_flyweight.MaxHealth}");
        Console.WriteLine($"Height: {Height}m");
        Console.WriteLine($"Image: {_flyweight.ImagePath}");
        Console.WriteLine($"Sound Effects: {string.Join(", ", _flyweight.SoundEffects)}");
        Console.WriteLine($"Color: {_flyweight.Color}");
        Console.WriteLine($"Speed: {_flyweight.Speed}m/s");
    }
}

```


享元工厂，创建享元类，并且缓存享元对象
```c#
using System.Collections.Generic;

public class FlyweightFactory
{
    private Dictionary<string, EnemyFlyweight> _flyweights = new Dictionary<string, EnemyFlyweight>();

    public EnemyFlyweight GetFlyweight(string rank)
    {
        if (!_flyweights.ContainsKey(rank))
        {
            EnemyFlyweight flyweight;
            switch (rank)
            {
                case "新兵":
                    flyweight = new EnemyFlyweight("新兵", "b.png", new string[] { "death.wav", "attack.wav", "hit.wav" }, "Color(128,0,128,255)", 100, 1.0);
                    break;
                case "中士":
                    flyweight = new EnemyFlyweight("中士", "b.png", new string[] { "death.wav", "attack.wav", "hit.wav" }, "Color(128,0,128,255)", 200, 2.0);
                    break;
                case "上士":
                    flyweight = new EnemyFlyweight("上士", "b.png", new string[] { "death.wav", "attack.wav", "hit.wav" }, "Color(128,0,128,255)", 500, 3.0);
                    break;
                case "上尉":
                    flyweight = new EnemyFlyweight("上尉", "a.png", new string[] { "death.wav", "attack.wav", "hit.wav" }, "Color(128,0,128,255)", 1000, 4.0);
                    break;
                default:
                    throw new ArgumentException("未知职级");
            }
            _flyweights[rank] = flyweight;
        }
        return _flyweights[rank];
    }
}

```

客户端代码
```c#
public class Game
{
    public static void Main()
    {
        FlyweightFactory factory = new FlyweightFactory();

        // 创建10000个敌人（模拟）
        var enemies = new List<Enemy>();
        for (int i = 0; i < 10000; i++)
        {
            // 假设敌人职级随机
            string rank = i % 4 == 0 ? "新兵" :
                          i % 4 == 1 ? "中士" :
                          i % 4 == 2 ? "上士" : "上尉";
            
            var enemy = new Enemy(rank, 100, 1.75);  // 每个敌人有独立的血量和身高
            enemies.Add(enemy);
        }

        // 显示第一个敌人的信息（仅演示）
        enemies[0].DisplayEnemyInfo();
    }
}

```







## 代理模式（Proxy）


代理模式（Proxy Pattern）为某个对象提供一个代理，以**控制对该对象的访问**。代理通常用于**延迟加载、权限控制、日志记录、远程访问等**场景。

代理模式 = **给对象加一层“中介”**


**什么时候用代理模式？**

✅ **使用代理模式**

- 你需要**控制某个对象的访问**（如权限、远程调用）。
- 你需要**延迟加载**（如 `GameMapProxy` 先不加载数据）。
- 你想在访问对象前**增加额外行为**（如日志、缓存）。

✅ **不要使用代理模式**

- 如果不需要**拦截/控制**访问，直接使用对象即可。
- 如果只是**增强功能**，可以用**装饰器模式**。


在 RPG 游戏中，角色拥有普通技能和特殊技能。特殊技能通常需要满足一定的条件（比如达到特定等级、拥有特定道具等）才能使用。我们可以使用代理模式来实现这种权限控制，确保只有满足条件的角色才能使用特殊技能。

**也就是说为了保证单一职责原则，SpecialSkill类不应该负责验证技能的释放条件。而是由一个代理类来控制技能的释放条件。**

```c#
using UnityEngine;

// 抽象主题：定义技能使用的接口
public interface ISkill
{
    void UseSkill();
}

// 真实主题：代表角色的特殊技能
public class SpecialSkill : ISkill
{
    public void UseSkill()
    {
        Debug.Log("使用特殊技能，释放强大的魔法攻击！");
    }
}

// 代理：保护代理，用于控制特殊技能的使用权限
public class SkillProxy : ISkill
{
    private SpecialSkill specialSkill;
    private int requiredLevel;
    private int currentLevel;

    public SkillProxy(int requiredLevel, int currentLevel)
    {
        this.requiredLevel = requiredLevel;
        this.currentLevel = currentLevel;
        specialSkill = new SpecialSkill();
    }

    public void UseSkill()
    {
        if (currentLevel >= requiredLevel)
        {
            // 满足等级要求，调用真实技能的使用方法
            specialSkill.UseSkill();
        }
        else
        {
            Debug.Log("等级不足，无法使用特殊技能。");
        }
    }
}

// 角色类，包含技能使用的逻辑
public class Character : MonoBehaviour
{
    public int characterLevel;
    private ISkill skillProxy;

    private void Start()
    {
        // 创建技能代理，要求等级为 10
        skillProxy = new SkillProxy(10, characterLevel);
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.S))
        {
            // 尝试使用技能
            skillProxy.UseSkill();
        }
    }
}

```



# 行为型模式（Behavioral Patterns）

行为型模式主要关注**对象之间的通信**和**职责分配**，以及如何让系统中的对象进行有效的协作。这类模式通常用于定义**对象之间如何互相配合**，从而实现某一功能。



## 责任链模式（Chain of Responsibility）

**责任链模式**是一种**行为型设计模式**，它允许多个对象**按顺序处理一个请求**，直到其中一个对象能够处理它为止。这样可以避免请求的发送者与接收者之间的紧耦合，提高系统的可扩展性和灵活性。

- 请求沿着一条**链**传递，链上的每个对象都有**处理请求的机会**。
- **如果一个对象无法处理请求，它会将请求传递给下一个对象**，直到链的末端。
- 责任链模式使**请求的发送者**和**处理者**解耦，**发送者不需要知道最终由谁处理请求**。


- 当链条较长的时候，性能可能比较差


```c#
using System;

// 抽象处理者
public abstract class Logger
{
    protected Logger nextLogger; // 下一个处理者

    public void SetNext(Logger nextLogger)
    {
        this.nextLogger = nextLogger;
    }

    public void Log(string message, LogLevel level)
    {
        if (CanHandle(level))
        {
            WriteLog(message);
        }
        else if (nextLogger != null)
        {
            nextLogger.Log(message, level);
        }
    }

    protected abstract bool CanHandle(LogLevel level);
    protected abstract void WriteLog(string message);
}

// 日志级别
public enum LogLevel
{
    Debug,
    Warning,
    Error
}

// 具体处理者：调试日志处理器
public class DebugLogger : Logger
{
    protected override bool CanHandle(LogLevel level) => level == LogLevel.Debug;

    protected override void WriteLog(string message)
    {
        Console.WriteLine("[DEBUG]: " + message);
    }
}

// 具体处理者：警告日志处理器
public class WarningLogger : Logger
{
    protected override bool CanHandle(LogLevel level) => level == LogLevel.Warning;

    protected override void WriteLog(string message)
    {
        Console.WriteLine("[WARNING]: " + message);
    }
}

// 具体处理者：错误日志处理器
public class ErrorLogger : Logger
{
    protected override bool CanHandle(LogLevel level) => level == LogLevel.Error;

    protected override void WriteLog(string message)
    {
        Console.WriteLine("[ERROR]: " + message);
    }
}

// 测试代码
class Program
{
    static void Main()
    {
        Logger debugLogger = new DebugLogger();
        Logger warningLogger = new WarningLogger();
        Logger errorLogger = new ErrorLogger();

        // 设置责任链：Debug -> Warning -> Error
        debugLogger.SetNext(warningLogger);
        warningLogger.SetNext(errorLogger);

        // 发送不同级别的日志
        debugLogger.Log("This is a debug message.", LogLevel.Debug);
        debugLogger.Log("This is a warning!", LogLevel.Warning);
        debugLogger.Log("Critical error occurred!", LogLevel.Error);
    }
}

```



## 命令模式（Command）

**命令模式**是一种**行为型设计模式**，它将**请求（动作）封装为一个对象**，从而使得请求的发送者和执行者**解耦**，并且可以方便地**存储、撤销或扩展命令**。


和MVC用的一套东西，将业务逻辑和表现层分开，用command管理具体表现。


外观模式是为了方便使用，命令模式是为了方便复用Command


- 本质上就是把一个命令包装为一个对象，方便命令的内容变化时快速替换逻辑，而不是替换其它部分。
- 命令模式很重要一个特点就是可以撤销。
- 需要什么命令就new一个这个命令，然后用命令管理器加入history就完事了。



❌假设不使用命令模式
```c#
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public Image backgroundImage;

    public Button redButton;
    public Button blueButton;
    public Button greenButton;
    public Button undoButton;

    private Color previousColor;

    void Start()
    {
        redButton.onClick.AddListener(() => ChangeColor(Color.red));
        blueButton.onClick.AddListener(() => ChangeColor(Color.blue));
        greenButton.onClick.AddListener(() => ChangeColor(Color.green));
        undoButton.onClick.AddListener(UndoLastChange);
    }

    void ChangeColor(Color color)
    {
        previousColor = backgroundImage.color; // 记录上一个颜色
        backgroundImage.color = color;
    }

    void UndoLastChange()
    {
        backgroundImage.color = previousColor;
    }
}

```


1. **UIManager 直接操作 UI**：
    
    - `ChangeColor(Color color)` 直接操作 `backgroundImage.color`，**强依赖 UI 组件**。
    - 如果 UI 逻辑需要修改，比如新增一个 **动画效果** 或 **日志记录**，需要改 `UIManager` 代码。
2. **按钮的点击事件直接耦合到 `UIManager`**：
    
    - `onClick.AddListener()` 直接绑定 `ChangeColor()` 方法，使得 **UI 逻辑与颜色变化逻辑紧密绑定**。
    - 未来如果需要**支持撤销多个步骤**，现有代码不支持，需要**大改** `UIManager`。
3. **无法扩展新功能**：
    - 不能轻松添加 **日志系统、网络请求、动画**，如果需要的话，必须修改 `UIManager` 的 `ChangeColor()` 方法。






命令接口

```c#
// 命令接口，所有命令都要实现 Execute() 和 Undo()
public interface ICommand
{
    void Execute();  // 执行操作
    void Undo();     // 撤销操作
}
```


具体命令（ConcreteCommand）：改变 UI 颜色
```c#
using UnityEngine;
using UnityEngine.UI;

public class ChangeColorCommand : ICommand
{
    private Image targetImage; // 目标UI
    private Color newColor;    // 要更改的颜色
    private Color previousColor; // 记录上一个颜色（用于撤销）

    public ChangeColorCommand(Image image, Color color)
    {
        targetImage = image;
        newColor = color;
        previousColor = image.color; // 记录执行前的颜色
    }

    public void Execute()
    {
        targetImage.color = newColor;
    }

    public void Undo()
    {
        targetImage.color = previousColor;
    }
}

```


命令控制器（CommandController）：管理命令历史
```c#
using System.Collections.Generic;
using UnityEngine;

public class CommandController : MonoBehaviour
{
    private Stack<ICommand> commandHistory = new Stack<ICommand>(); // 存储命令历史

    public void ExecuteCommand(ICommand command)
    {
        command.Execute();
        commandHistory.Push(command); // 记录执行的命令
    }

    public void UndoLastCommand()
    {
        if (commandHistory.Count > 0)
        {
            ICommand lastCommand = commandHistory.Pop();
            lastCommand.Undo();
        }
    }
}

```


客户端
```c#
using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public Image backgroundImage; // 需要改变颜色的 UI
    public CommandController commandController; // 命令控制器

    public Button redButton;
    public Button blueButton;
    public Button greenButton;
    public Button undoButton;

    void Start()
    {
        redButton.onClick.AddListener(() => ExecuteCommand(Color.red));
        blueButton.onClick.AddListener(() => ExecuteCommand(Color.blue));
        greenButton.onClick.AddListener(() => ExecuteCommand(Color.green));
        undoButton.onClick.AddListener(() => commandController.UndoLastCommand());
    }

    void ExecuteCommand(Color color)
    {
        ICommand command = new ChangeColorCommand(backgroundImage, color);
        commandController.ExecuteCommand(command);
    }
}

```



- 最好把数据结构改为双向队列，这样可以方便固定长度。
- 不要用stack，因为如果需要redo的话，需要两个stack，额外保存弹出的命令。


**代码如何解耦？**
代码角色	作用	变化影响

| 代码角色                   | 作用        | 变化影响                       |
| ---------------------- | --------- | -------------------------- |
| **UIManager**          | 只负责执行命令   | UI 逻辑变化不会影响颜色变更逻辑          |
| **CommandController**  | 负责执行和撤销命令 | 不影响 UI 逻辑或命令逻辑             |
| **ChangeColorCommand** | 处理具体的颜色变化 | UI 变化不影响 CommandController |


✅ 结论：UIManager、CommandController、ChangeColorCommand 三者互不依赖，修改其中之一不会影响其他代码！




## 解释器模式（Interpreter）

主要是为了解释自己的DSL

比如可以实现rpg中的富文本效果。





定义解释器接口
```c#
public interface IExpression
{
    int Interpret();  // 解释方法，返回计算结果
}


```


定义上下文的对象，`Context` 负责存储变量的值，并提供获取方法
```c#
// 上下文类，用于存储变量的值
public class Context
{
    private Dictionary<string, int> variables = new Dictionary<string, int>();

    // 设置变量值
    public void SetVariable(string name, int value)
    {
        variables[name] = value;
    }

    // 获取变量值
    public int GetVariable(string name)
    {
        return variables.TryGetValue(name, out int value) ? value : 0; // 未定义变量默认返回 0
    }
}

```



终结符表达式 (数字)
```c#
// 数字类
public class NumberExpression : Expression
{
    private int _number;

    public NumberExpression(int number)
    {
        _number = number;
    }

    public override int Interpret()
    {
        return _number;
    }
}

```


操作符表达式 (加法和减法)
```c#
// 加法类
public class AddExpression : Expression
{
    private Expression _left;
    private Expression _right;

    public AddExpression(Expression left, Expression right)
    {
        _left = left;
        _right = right;
    }

    public override int Interpret()
    {
        return _left.Interpret() + _right.Interpret(); // 返回左边表达式与右边表达式之和
    }
}

// 减法类
public class SubtractExpression : Expression
{
    private Expression _left;
    private Expression _right;

    public SubtractExpression(Expression left, Expression right)
    {
        _left = left;
        _right = right;
    }

    public override int Interpret()
    {
        return _left.Interpret() - _right.Interpret(); // 返回左边表达式与右边表达式之差
    }
}

```


解析表达式的parser，用于真正处理表达式的逻辑

```c#
// 解析器，解析表达式并生成解释器树
public class ExpressionParser
{
    public static Expression Parse(string expression)
    {
        var tokens = expression.Split(' ');
        Expression currentExpression = null;
        string currentOperator = null;

        foreach (var token in tokens)
        {
            Debug.Log($"处理token：{token}");
            
            // 如果是运算符，保存起来等待下一个操作数
            if (token == "+" || token == "-")
            {
                currentOperator = token;
                continue;
            }

  
            Expression newExpression;
            // 是数字
            if (int.TryParse(token, out int number))
            {
                newExpression = new NumberExpression(number);
            }
            else//是变量
            {
                newExpression = new VariableExpression(token);
            }

            // 如果是第一个操作数
            if (currentExpression == null)
            {
                currentExpression = newExpression;
            }
            // 如果有之前的操作数和运算符，进行运算
            else if (currentOperator != null)
            {
                currentExpression = currentOperator == "+" 
                    ? new AddExpression(currentExpression, newExpression)
                    : new SubtractExpression(currentExpression, newExpression);
                currentOperator = null;
            }
        }

        if (currentExpression == null)
        {
            throw new System.ArgumentException("Invalid expression");
        }

        return currentExpression;
    }
}


```



客户端

```c#
public class Calculator
{
    public static void Main(string[] args)
    {
        string expression = "3 + 5 - 2 + 8"; // 计算这个表达式

        // 解析表达式
        Expression parsedExpression = ExpressionParser.Parse(expression);

        // 计算并输出结果
        int result = parsedExpression.Interpret();
        Console.WriteLine($"结果是：{result}"); // 输出结果：14
    }
}


///也可以使用变量

public class Calculator
{
    public static void Main(string[] args)
    {
        // 创建上下文并设置变量
        Context context = new Context();
        context.SetVariable("x", 10);
        context.SetVariable("y", 3);

        // 表达式
        string expression = "x + 5 - y"; // x=10, y=3，计算 10 + 5 - 3

        // 解析并计算
        Expression parsedExpression = ExpressionParser.Parse(expression);
        int result = parsedExpression.Interpret(context);

        Console.WriteLine($"结果是：{result}"); // 结果是：12
    }
}


```







## 迭代器模式（Iterator）


**迭代器模式** 是一种 **行为型设计模式**，用于**提供一种方法来顺序访问集合对象中的元素，而不暴露其内部表示**。


简单来说，它的作用是：
- **封装遍历逻辑**，让你可以像使用 `foreach` 一样遍历集合，而不必关心底层数据结构。
- **解耦遍历与集合本身**，使得可以为不同的集合提供不同的遍历方式。


对于迭代器模式来说，只要实现了迭代器接口就可以了
迭代器接口主要包括以下的方法：

    bool HasNext();
    Loli Next();//获取数据
    void Reset();

调用迭代器可以用下面的方式：

```c#
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

// 迭代器接口
public interface ILoliIterator
{
    bool HasNext();
    Loli Next();
    void Reset();
}

// 萝莉类
public class Loli
{
    public string Name { get; set; }
    public string Personality { get; set; }

    public Loli(string name, string personality)
    {
        Name = name;
        Personality = personality;
    }
}

// 萝莉集合类
public class LoliCollection
{
    private List<Loli> lolis = new List<Loli>();

    public void AddLoli(Loli loli)
    {
        lolis.Add(loli);
    }

    public ILoliIterator CreateIterator()
    {
        return new LoliIterator(lolis);
    }
}

// 具体迭代器实现
public class LoliIterator : ILoliIterator
{
    private List<Loli> lolis;
    private int currentPosition = 0;

    public LoliIterator(List<Loli> lolis)
    {
        this.lolis = lolis;
    }

    public bool HasNext()
    {
        return currentPosition < lolis.Count;
    }

    public Loli Next()
    {
        if (HasNext())
        {
            return lolis[currentPosition++];
        }
        return null;
    }

    public void Reset()
    {
        currentPosition = 0;
    }
}

public class Test : MonoBehaviour
{
    void Start()
    {
        // 创建萝莉集合
        LoliCollection loliCollection = new LoliCollection();
        loliCollection.AddLoli(new Loli("小樱", "活泼可爱"));
        loliCollection.AddLoli(new Loli("小圆", "温柔善良"));
        loliCollection.AddLoli(new Loli("小爱", "傲娇可爱"));

        // 使用迭代器遍历萝莉
        ILoliIterator iterator = loliCollection.CreateIterator();
        while (iterator.HasNext())
        {
            Loli loli = iterator.Next();
            Debug.Log($"萝莉姓名: {loli.Name}, 性格: {loli.Personality}");
        }
    }
}

```





- 因为这个东西非常常用，所以c#原生提供了迭代器模式的实现。**一个collection要支持Foreach进行遍历，就必须实现IEnumerable,并以某种方式返回迭代器象:IEnumerator。**
- foreach实际上是while的一种语法糖



```c#
using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

// 萝莉类
public class Loli
{
    public string Name { get; set; }
    public string Personality { get; set; }

    public Loli(string name, string personality)
    {
        Name = name;
        Personality = personality;
    }
}

// 方式1：手动实现IEnumerator的迭代器
public class LoliEnumerator : IEnumerator<Loli>
{
    private List<Loli> lolis;
    private int currentIndex = -1;

    public LoliEnumerator(List<Loli> lolis)
    {
        this.lolis = lolis;
    }

    public Loli Current => lolis[currentIndex];

    object IEnumerator.Current => Current;

    public bool MoveNext()
    {
        currentIndex++;
        return currentIndex < lolis.Count;
    }

    public void Reset()
    {
        currentIndex = -1;
    }

    public void Dispose()
    {
        // 清理资源
    }
}

// 萝莉集合类 - 实现IEnumerable接口
public class LoliCollection : IEnumerable<Loli>
{
    private List<Loli> lolis = new List<Loli>();

    public void AddLoli(Loli loli)
    {
        lolis.Add(loli);
    }

    public IEnumerator<Loli> GetEnumerator()
    {
        return new LoliEnumerator(lolis);
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    

    // 方式2：使用yield return实现迭代器，可以更加直观的做一些逻辑的定制
    public IEnumerable<Loli> GetCuteLolis()
    {
        foreach (var loli in lolis)
        {
            if (loli.Personality.Contains("可爱"))
            {
                //yield会自动生成一个迭代器
                yield return loli;
            }
        }
    }

}

public class Test : MonoBehaviour
{
    void Start()
    {
        // 创建萝莉集合
        LoliCollection loliCollection = new LoliCollection();
        loliCollection.AddLoli(new Loli("小樱", "活泼可爱"));
        loliCollection.AddLoli(new Loli("小圆", "温柔善良"));
        loliCollection.AddLoli(new Loli("小爱", "傲娇可爱"));

        // 方式1：使用手动实现的迭代器
        Debug.Log("=== 使用手动实现的迭代器 ===");
        foreach (var loli in loliCollection)
        {
            Debug.Log($"萝莉姓名: {loli.Name}, 性格: {loli.Personality}");
        }

        // 方式2：使用yield return实现的迭代器
        Debug.Log("\n=== 使用yield return实现的迭代器 ===");
        foreach (var loli in loliCollection.GetCuteLolis())
        {
            Debug.Log($"可爱的萝莉: {loli.Name}");
        }
    }
}

```




我们要遍历 RPG 游戏中的任务列表，但不希望直接暴露 `List<Task>` 结构。



## 中介者模式（Mediator）



**中介者模式（Mediator）** 是一种**行为设计模式**，用于**减少对象之间的直接依赖关系**，让多个对象通过一个中介者（Mediator）来进行交互，而不是相互直接调用。





- 当一个对象和其它的对象需要互相沟通时，会呈现网状的关系。为了避免这种关系需要中介者。例如飞机的塔楼，飞机降落的时候不会和彼此之间通信要降落，而是全部都通过塔楼沟通。


📌 **中介者模式的核心：** ✔ **去中心化**的点对点通信 → **集中式协调**


广播室的例子
虽然这玩意适合用广播模式做，但是我一时半会想不到其它的例子，所以可以先用中介者模式去做。

```c#
using System;
using System.Collections.Generic;

// **1️⃣ 定义中介者接口**
interface IChatMediator
{
    void SendMessage(string message, Player sender);
    void AddPlayer(Player player);
}

// **2️⃣ 具体中介者：聊天服务器**
class ChatMediator : IChatMediator
{
    private List<Player> players = new List<Player>();

    public void AddPlayer(Player player)
    {
        players.Add(player);
    }

    public void SendMessage(string message, Player sender)
    {
        foreach (var player in players)
        {
            if (player != sender)  // 不给自己发消息
            {
                player.ReceiveMessage(message, sender);
            }
        }
    }
}

// **3️⃣ 定义同事类（玩家）**
class Player
{
    public string Name { get; private set; }
    private IChatMediator chatMediator;

    public Player(string name, IChatMediator mediator)
    {
        Name = name;
        chatMediator = mediator;
        chatMediator.AddPlayer(this);
    }

    public void Send(string message)
    {
        Console.WriteLine($"📤 {Name} 发送消息：{message}");
        chatMediator.SendMessage(message, this);
    }

    public void ReceiveMessage(string message, Player sender)
    {
        Console.WriteLine($"📩 {Name} 收到 {sender.Name} 的消息：{message}");
    }
}

// **4️⃣ 测试代码**
class Program
{
    static void Main()
    {
        IChatMediator chatRoom = new ChatMediator();

        Player alice = new Player("Alice", chatRoom);
        Player bob = new Player("Bob", chatRoom);
        Player charlie = new Player("Charlie", chatRoom);

        alice.Send("你好，大家！");
        bob.Send("Hi Alice!");
    }
}


/*
📤 Alice 发送消息：你好，大家！
📩 Bob 收到 Alice 的消息：你好，大家！
📩 Charlie 收到 Alice 的消息：你好，大家！

📤 Bob 发送消息：Hi Alice!
📩 Alice 收到 Bob 的消息：Hi Alice!
📩 Charlie 收到 Bob 的消息：Hi Alice!

*/

```


虽然广播模式更加的松耦合，但是对单个对象的控制能力也会降低很多。而中介者模式会正儿八经拿到所有对象的引用。所以在复杂的情景下，还是中介者模式吧。








## 备忘录模式（Memento）


**备忘录模式（Memento Pattern）** 是一种 **行为型设计模式**，用于 **捕获对象的状态，并在需要时恢复到之前的状态**，而不破坏对象的封装性。

**适用于**：

- 需要支持**撤销（Undo）**和**恢复（Redo）**功能的系统（如文本编辑器、游戏存档）。
- 需要**存储和回溯对象的状态**，但不想暴露对象的内部细节。


 **备忘录模式的角色**

1. **`Memento（备忘录）`**：
    - 存储对象的**快照（状态数据）**，但不提供修改功能。
2. **`Originator（原发器）`**：
    - 负责创建 `Memento` 备忘录对象，并可以根据 `Memento` 恢复自身状态。
3. **`Caretaker（管理者）`**：
    - 负责**保存和管理**多个 `Memento`，但不直接操作其内容（防止破坏封装）。



在 RPG 游戏中，角色有 `血量（HP）` 和 `魔法（MP）`。我们希望在战斗前**保存角色状态**，如果战斗失败，则**恢复之前的存档**。


备忘录类（Memento）

保存玩家的存档快照。实际上就是存档的结构体，正常游戏里面就存所有的玩家数据了（
**只读（`readonly`）属性**，确保备忘录是不可变的。

```c#
public class PlayerMemento
{
    public int HP { get; }
    public int MP { get; }

    public PlayerMemento(int hp, int mp)
    {
        HP = hp;
        MP = mp;
    }
}
```


玩家原发器(Originator)
来调用保存的数据。
谁是原发器(Originator)，谁来CreateMemento和Restore备忘录
```c#
using System;

public class Player
{
    public int HP { get; private set; }
    public int MP { get; private set; }

    public Player(int hp, int mp)
    {
        HP = hp;
        MP = mp;
    }

    // 生成存档（创建备忘录）
    public PlayerMemento SaveState()
    {
        return new PlayerMemento(HP, MP);
    }

    // 读取存档（从备忘录恢复状态）
    public void RestoreState(PlayerMemento memento)
    {
        HP = memento.HP;
        MP = memento.MP;
    }

    public void ShowStatus()
    {
        Console.WriteLine($"[角色状态] HP: {HP}, MP: {MP}");
    }

    // 模拟战斗，消耗 HP 和 MP
    public void Fight()
    {
        HP -= 30;
        MP -= 10;
        Console.WriteLine("⚔️ 角色进行战斗...");
    }
}

```


存档管理器
用于增加和一条备忘录，以及读取一个备忘录
```c#
using System.Collections.Generic;

public class SaveManager
{
    private Stack<PlayerMemento> _history = new Stack<PlayerMemento>();

    public void Save(PlayerMemento memento)
    {
        _history.Push(memento);
    }

    public PlayerMemento Load()
    {
        return _history.Count > 0 ? _history.Pop() : null;
    }
}

```



客户端
```c#
class Program
{
    static void Main()
    {
        Player player = new Player(100, 50);
        SaveManager saveManager = new SaveManager();

        // 角色初始状态
        player.ShowStatus();

        // 保存存档
        saveManager.Save(player.SaveState());

        // 角色战斗
        player.Fight();
        player.ShowStatus();

        // 恢复存档
        Console.WriteLine("\n🔄 读取存档...");
        player.RestoreState(saveManager.Load());
        player.ShowStatus();
    }
}

```



**备忘录模式（Memento）** 和 **命令模式（Command）** 在**实现撤销（Undo）功能**时确实有相似之处，但它们的 **核心思想** 和 **使用场景** **不同**。🚀

对于同样恢复之前角色的状态

**备忘录模式的做法：**
- 直接存储 **角色的血量（HP）**。
- 需要撤销时，只需恢复之前的快照。
- 
**命令模式的做法：**
- 记录 **“上次执行了什么操作”**（比如 **受到 30 伤害**）。
- 需要撤销时，执行 **“反向操作”**（恢复 30 HP）。

而这种战斗的命令一局中有非常多，一局失败的时候，不应该撤销这些操作回到战斗前，非常不优雅。而是应该使用备忘录模式，直接恢复到战斗前。因为我不需要关注战斗中发生的各种指令，我只在乎战斗之前的状态。

重新开始当前关卡也很适合用备忘录模式

|          | **备忘录模式（Memento）**                  | **命令模式（Command）**                |
| -------- | ----------------------------------- | -------------------------------- |
| **核心思想** | 直接**存储对象状态（快照）**，并在需要时恢复            | **存储操作（Command），并提供撤销逻辑**        |
| **存储内容** | 仅存**对象的状态数据**（`Memento`）            | 存储**操作（Command）+ 可选的状态数据**       |
| **适用于**  | 需要**完整恢复对象状态**（如游戏存档）               | 需要**撤销/重做操作**（如文本编辑器）            |
| **实现方式** | `Memento` 负责保存状态，`Caretaker` 维护存档历史 | `Command` 封装操作，`Invoker` 负责执行和撤销 |
|          |                                     |                                  |


## 观察者模式（Observer）


当对象之间存在一对多的依赖关系时，其中一个对象的状态发生改变，所有依赖它的对象都会收到通知，这就是观察者模式。

在观察者模式中，只有两种主体：目标对象 (**Object**) 和 观察者 (**Observer**)。



```c#
using System.Collections;
using System.Collections.Generic; 
using UnityEngine;
using System;

public class ObserveMode : MonoBehaviour
{
    //玩家死亡之后的事件，需要被观察
    public static event Action playerDeadEvent;

    private void OnDestroy()
    {
        playerDeadEvent?.Invoke();
    }
}

```


```c#
//敌人
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Enemy : MonoBehaviour
{

    //在开始就观察玩家的死亡事件
    void Start()
    {
        ObserveMode.playerDeadEvent += () =>
        {
            print("玩家死了！！");
        };
    }

}

```




## 状态模式（State）



状态模式（State Pattern）是一种行为设计模式，它允许对象在其内部状态改变时改变其行为。状态模式将与状态相关的行为封装在独立的状态类中，并通过在这些状态类之间切换来改变对象的行为。

在Unity中，状态模式可以用于管理游戏对象的不同状态，比如角色的行走、跳跃、攻击等状态。

这种东西可以大量减少if else的嵌套


传统写法（错误示范：if-else 太多）

```c#
public class Character
{
    private string state = "Idle";

    public void Move()
    {
        if (state == "Idle" || state == "Combat")
            Console.WriteLine("角色移动");
        else
            Console.WriteLine("无法移动！");
    }

    public void Attack()
    {
        if (state == "Combat")
            Console.WriteLine("进行攻击！");
        else
            Console.WriteLine("无法攻击！");
    }

    public void Die()
    {
        state = "Dead";
        Console.WriteLine("角色死亡！");
    }
}

```


✅ 使用状态模式（State Pattern）
```c#
using System;

// **状态接口**
public interface ICharacterState
{
    void Move();
    void Attack();
    void Die();
}

// **具体状态：普通状态（Idle）**
public class IdleState : ICharacterState
{
    public void Move() => Console.WriteLine("🚶 角色正在移动...");
    public void Attack() => Console.WriteLine("⚠ 无法攻击，当前处于普通状态！");
    public void Die() => Console.WriteLine("💀 角色死亡！");
}

// **具体状态：战斗状态（Combat）**
public class CombatState : ICharacterState
{
    public void Move() => Console.WriteLine("🏃 战斗中移动...");
    public void Attack() => Console.WriteLine("⚔ 进行攻击！");
    public void Die() => Console.WriteLine("💀 角色死亡！");
}

// **具体状态：死亡状态（Dead）**
public class DeadState : ICharacterState
{
    public void Move() => Console.WriteLine("❌ 无法移动，角色已死亡！");
    public void Attack() => Console.WriteLine("❌ 无法攻击，角色已死亡！");
    public void Die() => Console.WriteLine("❌ 角色已经死亡！");
}

// **角色类**
public class Character
{
    private ICharacterState currentState;

    public Character() => currentState = new IdleState(); // 默认是 Idle

    public void SetState(ICharacterState newState) => currentState = newState;
    public void Move() => currentState.Move();
    public void Attack() => currentState.Attack();
    public void Die()
    {
        currentState.Die();
        SetState(new DeadState()); // 角色死亡后切换到死亡状态
    }
}

// **测试**
class Program
{
    static void Main()
    {
        Character player = new Character();
        
        player.Move();   // 🚶 角色正在移动...
        player.Attack(); // ⚠ 无法攻击，当前处于普通状态！
        
        Console.WriteLine("\n⚔ 切换到战斗状态！");
        player.SetState(new CombatState());

        player.Move();   // 🏃 战斗中移动...
        player.Attack(); // ⚔ 进行攻击！
        
        Console.WriteLine("\n💀 角色死亡！");
        player.Die();    // 💀 角色死亡！
        
        player.Move();   // ❌ 无法移动，角色已死亡！
    }
}
```









## 策略模式（Strategy）

策略模式是一种行为型设计模式，它的核心思想是：
1. 定义算法族：将一系列的算法分别封装成独立的类
2. 使它们可以互相替换：这些算法都实现同一个接口，可以互相替换
3. 算法的变化独立于使用算法的客户：客户端代码不需要因为算法的变化而改变



```c#
// 策略接口
public interface IAttackStrategy
{
    void Attack();
}

// 具体策略类
public class SwordAttack : IAttackStrategy
{
    public void Attack()
    {
        Debug.Log("使用剑攻击");
    }
}

public class MagicAttack : IAttackStrategy
{
    public void Attack()
    {
        Debug.Log("使用魔法攻击");
    }
}

public class BowAttack : IAttackStrategy
{
    public void Attack()
    {
        Debug.Log("使用弓箭攻击");
    }
}

// 上下文类
public class Character
{
    private IAttackStrategy attackStrategy;

    public void SetAttackStrategy(IAttackStrategy strategy)
    {
        this.attackStrategy = strategy;
    }

    public void PerformAttack()
    {
        attackStrategy.Attack();
    }
}
```





## 模板方法模式（Template Method）
 

**模板方法模式（Template Method）** 是一种**行为设计模式**，用于在**父类中定义算法的结构**，而**让子类来实现具体步骤**。  
它**固定了算法的整体框架**，但允许子类**对其中的某些步骤进行自定义**。

**场景：**  
我们要设计一个 RPG 游戏中的角色**攻击流程**：

1. **准备攻击**（固定步骤）
2. **执行攻击**（每个角色不同）
3. **收尾动作**（固定步骤）

🔹 **不同角色（战士 / 法师）攻击方式不同**，但整体流程相同。  
🔹 **可以用模板方法模式，统一流程，让子类决定细节**。

```c#
using System;

abstract class Character
{
    // **模板方法**：定义攻击流程，不允许子类修改结构
    public void Attack()
    {
        PrepareAttack();
        ExecuteAttack();
        FinishAttack();
    }

    // **固定的步骤**
    private void PrepareAttack()
    {
        Console.WriteLine("🛡️ 角色准备攻击...");
    }

    // **抽象方法，子类必须实现**
    protected abstract void ExecuteAttack();

    // **固定的步骤**
    private void FinishAttack()
    {
        Console.WriteLine("✅ 攻击完成！\n");
    }
}

// **具体子类：战士**
class Warrior : Character
{
    protected override void ExecuteAttack()
    {
        Console.WriteLine("⚔️ 战士挥舞大剑进行重击！");
    }
}

// **具体子类：法师**
class Mage : Character
{
    protected override void ExecuteAttack()
    {
        Console.WriteLine("🔥 法师释放火球术！");
    }
}

// **测试代码**
class Program
{
    static void Main()
    {
        Character warrior = new Warrior();
        warrior.Attack();

        Character mage = new Mage();
        mage.Attack();
    }
}



//🛡️ 角色准备攻击... ⚔️ 战士挥舞大剑进行重击！ ✅ 攻击完成！ 🛡️ 角色准备攻击... 🔥 法师释放火球术！ ✅ 攻击完成！
```





**模板方法模式（Template Method）** **一定会规定执行顺序**！它的核心思想就是**在基类中定义算法的整体流程**，并且**不允许子类更改这个顺序**，但允许子类**实现或覆盖某些步骤**。




## 访问者模式（Visitor）


访问者模式是一种**行为型设计模式**，它的核心思想是：  
**将作用于对象的数据操作从对象本身分离出来**，这样可以在不修改类的前提下，新增对这些对象的操作。

你可以理解为：**访问者模式让你可以在“不改动原始类”的情况下，给它们添加新功能**。


- 说白了，访问者模式就是在只定义了一个类的情况下，不修改原来的类，给它添加新的方法。
- 但是这根本没办法遵守开闭原则，我有一个新的element的话，还得再修改IVisitor
	- 访问者模式确实存在一个悖论：
	- 它在"添加新操作"方面支持开闭原则（只需添加新的Visitor类）
	- 但在"添加新元素"方面违反开闭原则（需要修改所有Visitor接口和实现）
	- 这个问题在设计模式中被称为"表达式问题"（Expression Problem）：




- 核心的结构只有两个
- 所有可以被修改的类都应该实现IElement接口，这个玩意里面有一个Accept，Accept里面有一个visit，可以让类把自身的数据传进去。
- 所有的操作都需要实现IVisitor，而IVisitor里面需要手动对每一种IElement进行访问。Visit的方法实际上没有具体含义，真正的含义在类名定义的。比如SaveGameVisitor，其实就是给普通的游戏对象添加了保存的方法。

```c#
// 基础接口
public interface IGameElement
{
    void Accept(IVisitor visitor);
}

public interface IVisitor
{
    void Visit(Player player);
    void Visit(Enemy enemy);
}

// 具体元素
public class Player : IGameElement
{
    public string Name { get; set; }
    public int Health { get; set; }

    public Player(string name, int health)
    {
        Name = name;
        Health = health;
    }

    public void Accept(IVisitor visitor)
    {
        visitor.Visit(this);
    }
}

public class Enemy : IGameElement
{
    public string Type { get; set; }
    public int Damage { get; set; }

    public Enemy(string type, int damage)
    {
        Type = type;
        Damage = damage;
    }

    public void Accept(IVisitor visitor)
    {
        visitor.Visit(this);
    }
}

// 访问者实现
public class StatisticsVisitor : IVisitor
{
    public void Visit(Player player)
    {
        Debug.Log($"统计访问者：收集玩家 {player.Name} 的数据");
        Debug.Log($"- 记录生命值：{player.Health}");
    }

    public void Visit(Enemy enemy)
    {
        Debug.Log($"统计访问者：收集敌人 {enemy.Type} 的数据");
        Debug.Log($"- 记录伤害值：{enemy.Damage}");
    }
}

public class SaveGameVisitor : IVisitor
{
    public void Visit(Player player)
    {
        Debug.Log($"存档访问者：保存玩家 {player.Name} 的数据");
        Debug.Log($"- 保存生命值：{player.Health}");
    }

    public void Visit(Enemy enemy)
    {
        Debug.Log($"存档访问者：保存敌人 {enemy.Type} 的数据");
        Debug.Log($"- 保存伤害值：{enemy.Damage}");
    }
}

// 使用示例
public class GameManager : MonoBehaviour
{
    void Start()
    {
        // 创建游戏元素
        List<IGameElement> gameElements = new List<IGameElement>
        {
            new Player("勇者", 100),
            new Enemy("史莱姆", 10),
            new Enemy("龙", 50)
        };

        // 创建访问者
        var statsVisitor = new StatisticsVisitor();
        var saveVisitor = new SaveGameVisitor();

        Debug.Log("=== 开始收集统计信息 ===");
        foreach (var element in gameElements)
        {
            element.Accept(statsVisitor);
        }

        Debug.Log("\n=== 开始保存游戏 ===");
        foreach (var element in gameElements)
        {
            element.Accept(saveVisitor);
        }
    }
}

```







# 其它常见的设计模式


## 发布者订阅者模式（广播模式）

和观察者模式很像，但是要注意！！！

观察者模式实际上是**松耦合(loosely coupled)**。也就是说，玩家死亡之后会直接通知所有的敌人。这个实际上还是有很强的耦合性的。

但是发布者订阅者模式中，发布者和订阅者并不会直接通信！而是通过一个中间商进行通信。

发布者只需告诉中间商，我要发的消息，topic是AAA；

订阅者只需告诉中间商，我要订阅topic是AAA的消息；即可。





```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public enum 事件类型
{
    玩家死亡,
    敌人死亡
}


public class 订阅者发布者模式 : MonoBehaviour
{
    //用来维护所有的事件
    private static Dictionary<事件类型, Delegate> 发布事件字典 = new Dictionary<事件类型, Delegate>();

    private static void  订阅前的检查(事件类型 事件, Delegate 回调函数)
    {
        if (!发布事件字典.ContainsKey(事件))
        {
            发布事件字典.Add(事件, null);
        }
        Delegate 已经存储的回调函数 = 发布事件字典[事件];
        if (已经存储的回调函数 != null && 已经存储的回调函数.GetType() != 回调函数.GetType())
        {
            throw new Exception(string.Format("尝试为事件{0}添加不同类型的委托，当前事件所对应的委托是{1}，要添加的委托类型为{2}", 事件, 已经存储的回调函数.GetType(), 回调函数.GetType()));
        }
    }

    //无参数的订阅与发布
    public static void 订阅(事件类型 事件, Action 回调函数)
    {
        订阅前的检查(事件, 回调函数);
        发布事件字典[事件] = (Action)发布事件字典[事件] + 回调函数;//用多播直接存储回调函数
    }

    public static void 发布(事件类型 事件)
    {

        Delegate 回调函数;
        if (发布事件字典.TryGetValue(事件, out 回调函数))
        {
            ((Action)回调函数)();
        }
    }



    //一个参数的订阅与发布

    public static void 订阅<T>(事件类型 事件, Action<T> 回调函数)
    {
        订阅前的检查( 事件,  回调函数);
        发布事件字典[事件] = (Action<T>)发布事件字典[事件] + 回调函数;//用多播直接存储回调函数
    }

    public static void 发布<T>(事件类型 事件,T 参数)
    {

        Delegate 回调函数;
        if (发布事件字典.TryGetValue(事件, out 回调函数))
        {
            ((Action<T>)回调函数)(参数);
        }
    }

}

```



```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class 订阅者 : MonoBehaviour
{

    void Start()
    {
        订阅者发布者模式.订阅<string>(事件类型.玩家死亡, (msg) =>{
            print("收到事件通知！"+msg);
        });
    }

}

```





```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class 发布者 : MonoBehaviour
{

    private void OnDisable()
    {
        订阅者发布者模式.发布(事件类型.玩家死亡,"GGGG");

    }
}

```



## MVC


虽然model用了事件，但是本质上还是model发送数据给了view


```c#
// 1. Model：管理数据
public class HealthModel {
    private int _currentHealth;
    public int CurrentHealth => _currentHealth;

    // 数据变化事件
    public event Action<int> OnHealthChanged;

    public HealthModel(int maxHealth) {
        _currentHealth = maxHealth;
    }

    public void TakeDamage(int damage) {
        _currentHealth -= damage;
        OnHealthChanged?.Invoke(_currentHealth); // 通知数据变化
    }
}

// 2. View：负责显示
public class HealthView : MonoBehaviour {
    [SerializeField] private Slider healthSlider;

    // 外部调用此方法更新显示
    public void UpdateHealthDisplay(int health) {
        healthSlider.value = health;
    }
}

// 3. Controller：处理输入和协调
public class HealthController : MonoBehaviour {
    private HealthModel _model;
    private HealthView _view;

    private void Start() {
        _model = new HealthModel(100);
        _view = GetComponent<HealthView>();
        _model.OnHealthChanged += _view.UpdateHealthDisplay; // 绑定事件
    }

    private void Update() {
        if (Input.GetKeyDown(KeyCode.Space)) {
            _model.TakeDamage(10); // 输入触发 Model 修改
        }
    }
}
```



## MVP

这玩意彻底断了model和view的联系，所以说OnPlayerTakeDamage的时候，要手动更新model和view的更新，而mvc只用改model

```c#
// 1. Model：管理数据
public class HealthModel {
    private int _currentHealth;
    public int CurrentHealth => _currentHealth;

    public HealthModel(int maxHealth) {
        _currentHealth = maxHealth;
    }

    public void TakeDamage(int damage) {
        _currentHealth -= damage;
    }
}

// 2. View：负责显示
public class HealthView : MonoBehaviour {
    [SerializeField] private Slider healthSlider;

    // 外部调用此方法更新显示
    public void UpdateHealthDisplay(int health) {
        healthSlider.value = health;
    }
}

// 3. Presenter：核心逻辑协调者
public class HealthPresenter {
    private HealthModel _model;
    private HealthView _view;

    public HealthPresenter(HealthModel model, HealthView view) {
        _model = model;
        _view = view;
    }

    // 处理逻辑并更新 View
    public void OnPlayerTakeDamage(int damage) {
        _model.TakeDamage(damage);
        _view.UpdateHealthDisplay(_model.CurrentHealth); // 主动更新 View
    }
}

// 4. MonoBehaviour 驱动输入（如 Unity 的脚本）
public class PlayerInputHandler : MonoBehaviour {
    [SerializeField] private HealthView healthView; // 通过 Inspector 绑定
    private HealthPresenter _presenter;

    private void Start() {
        var model = new HealthModel(100);
        _presenter = new HealthPresenter(model, healthView);
    }

    private void Update() {
        if (Input.GetKeyDown(KeyCode.Space)) {
            _presenter.OnPlayerTakeDamage(10); // 输入触发 Presenter
        }
    }
}
```





## MVVC


说白了是双向绑定的需求所衍生的。

以角色血量系统为例，结合 Unity 的 `UniRx`（响应式编程库）实现数据绑定：


```c#
// 1. Model（与 MVC/MVP 相同）
public class HealthModel {
    public ReactiveProperty<int> CurrentHealth { get; } = new ReactiveProperty<int>(100);

    public void TakeDamage(int damage) {
        CurrentHealth.Value -= damage;
    }
}

// 2. ViewModel：暴露可绑定属性
public class HealthViewModel {
    public ReactiveProperty<float> HealthNormalized { get; } = new ReactiveProperty<float>(1f);

    public HealthViewModel(HealthModel model) {
        // 将 Model 的 CurrentHealth 转换为进度条比例（0~1）
        model.CurrentHealth
            .Subscribe(health => HealthNormalized.Value = health / 100f)
            .AddTo(disposables);
    }

    private CompositeDisposable disposables = new CompositeDisposable();
}

// 3. View：绑定到 ViewModel
public class HealthView : MonoBehaviour {
    [SerializeField] private Slider healthSlider;
    private HealthViewModel _viewModel;

    public void Initialize(HealthViewModel viewModel) {
        _viewModel = viewModel;
        // 绑定 ViewModel 的 HealthNormalized 到 Slider
        _viewModel.HealthNormalized
            .Subscribe(value => healthSlider.value = value)
            .AddTo(this);
    }
}

// 4. 初始化及驱动
public class GameManager : MonoBehaviour {
    private void Start() {
        var model = new HealthModel();
        var viewModel = new HealthViewModel(model);
        var view = GetComponent<HealthView>();
        view.Initialize(viewModel);
    }

    private void Update() {
        if (Input.GetKeyDown(KeyCode.Space)) {
            model.TakeDamage(10); // 修改 Model，View 自动更新
        }
    }
}
```


## 领域驱动设计（DDD）



# Actor模型
