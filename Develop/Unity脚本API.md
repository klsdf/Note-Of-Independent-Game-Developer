

# 读取Excel

```c#
public static class CSVTools
{
    public static void LoadFile(string path, Action<List<string[]>> action)
    {
        if (!File.Exists(path))
        {
            Debug.LogError("路径不存在");
            return;
        }
        StreamReader streamReader =null;
        try
        {
            streamReader = File.OpenText(path);
            List<string[]> content = new List<string[]>();
            string line;
            while ((line = streamReader.ReadLine() )!= null)
            {
                content.Add(line.Split(","));
            }
            streamReader.Close();
            streamReader.Dispose();
            action?.Invoke(content);
        }
        catch(Exception ex)
        {
            Debug.LogError(ex.Message);
        }
    }

}
```





使用读取的数据

```c#
CSVTools.LoadFile(Application.streamingAssetsPath+ "/数据测试.csv", (content) =>{

    var row = content[0];
    foreach (var i in row)
    {
        print(i);
    }

});
```



# 坐标与单位

## 单位

unity中有很多网格，网格的尺寸为1 unit，对应屏幕上的100px。

unity中，长度单位就是unit，1unit显示为100px。场景的高度为10unit。

在真实世界中1unit多大，可以自己约定。

## 坐标系

x朝向右，y轴向上

unit中，z轴的方向采用左手系，也就是朝里面的。

![坐标系](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQ4ODE4Mg==,size_16,color_FFFFFF,t_70%23pic_center.jpeg)









# Mathf数学函数类

```c#
 private float endTime = 10;

    void Start()
    {
        // 静态变量
        print(Mathf.Deg2Rad+",度到弧度换算常量");
        print(Mathf.Rad2Deg+ ",弧度到度换算常量");
        print(Mathf.Infinity+"正无穷大的表示形式");
        print(Mathf.NegativeInfinity + "负无穷大的表示形式");
        print(Mathf.PI);
        // 静态函数
        print(Mathf.Abs(-1.2f)+ ",-1.2的绝对值");
        print(Mathf.Acos(1)+",1（以弧度为单位）的反余弦");
        print(Mathf.Floor(2.74f)+",小于或等于2.74的最大整数");
        print(Mathf.FloorToInt(2.74f)+",小于或等于2.74的最大整数");
        a+(b-a)*t
        print(Mathf.Lerp(1,2,0.5f)+",a和b按参数t进行线性插值");        
        print(Mathf.LerpUnclamped(1, 2, -0.5f) + ",a和b按参数t进行线性插值");
    }

    void Update()
    {
        print("游戏倒计时：" + endTime);
        endTime = Mathf.MoveTowards(endTime,0,0.1f);      
    } 
```

## bug

功能：1.占位 2.检错（可以每一步进行检测，可以很明显的知道哪一步错了）

```c#
Debug.Log("UnityAPI常用方法类与组件");
Debug.LogWarning("这是一个警告！");
Debug.LogError("这里有报错！");
```





# Transform

## 查找预制体中的某个子对象

```c#
 对话框文本 = 对话面板.transform.GetChild(0).GetChild(0).GetComponent<TMP_Text>();
```



## 移动缩放和旋转

根据坐标系的来移动

```c#
//1.第一个参数按世界坐标系移动，第二个参数指定世界坐标系（实际情况按世界坐标系移动）
grisGo.transform.Translate(Vector2.left*moveSpeed,Space.World);

//2.第一个参数按世界坐标系移动，第二个参数指定自身坐标系（实际情况按自身坐标系移动）
grisGo.transform.Translate(Vector2.left * moveSpeed, Space.Self);

//3.第一个参数按自身坐标系移动，第二个参数指定世界坐标系（实际情况按自身坐标系移动）
grisGo.transform.Translate(-grisGo.transform.right * moveSpeed, Space.World);

//4.第一个参数按自身坐标系移动，第二个参数指定自身坐标系（实际情况按世界坐标系移动）(一般不使用)
grisGo.transform.Translate(-grisGo.transform.right * moveSpeed, Space.Self);

//旋转
grisGo.transform.Rotate(new Vector3(0,0,1));
grisGo.transform.Rotate(Vector3.forward,1);
```



## 成员变量

```c#
Debug.Log("Gris变换组件所挂载的游戏物体名字是："+grisTrans.name);
Debug.Log("Gris变换组件所挂载的游戏物体引用是："+grisTrans.gameObject); 
Debug.Log("Gris下的子对象（指Transform）的个数是："+grisTrans.childCount);
Debug.Log("Gris世界空间中的坐标位置是："+grisTrans.position);
Debug.Log("Gris以四元数形式表示的旋转是："+grisTrans.rotation);
Debug.Log("Gris以欧拉角形式表示的旋转（以度数为单位）是"+grisTrans.eulerAngles);
Debug.Log("Gris的父级Transform是："+grisTrans.parent);
Debug.Log("Gris相对于父对象的位置坐标是："+grisTrans.localPosition);
Debug.Log("Gris相对于父对象以四元数形式表示的旋转是：" + grisTrans.localRotation);
Debug.Log("Gris相对于父对象以欧拉角形式表示的旋转（以度数为单位）是：" + grisTrans.localEulerAngles);
Debug.Log("Gris相对于父对象的变换缩放是："+grisTrans.localScale);
Debug.Log("Gris的自身坐标正前方（Z轴正方向）是："+grisTrans.forward);
Debug.Log("Gris的自身坐标正右方（X轴正方向）是：" + grisTrans.right);
Debug.Log("Gris的自身坐标正上方（Y轴正方向）是：" + grisTrans.up);
```



## 查找相关的成员方法

```c#
Debug.Log("当前脚本挂载的游戏对象下的叫Gris的子对象身上的Transform组件是："+transform.Find("Gris"));
Debug.Log("当前脚本挂载的游戏对象下的第一个（0号索引）子对象的Transform引用是："+transform.GetChild(0));
Debug.Log("Gris当前在此父对象同级里所在的索引位置："+ grisTrans.GetSiblingIndex());
```



## 静态方法

```c#
Transform.Destroy(grisTrans);
Transform.Destroy(grisTrans.gameObject);
Transform.FindObjectOfType();
Transform.Instantiate();
```



## 获取父节点

```c#
GameObject parent = this.transform.parent.gameObject;
Debug.Log(parent.name);
```

## 遍历所有子节点

 

```c#
Transform[] myTransforms = GetComponentsInChildren<Transform>();
foreach (var child in myTransforms)
{
    Debug.Log(child.name);
}
```

## 查找二级子物体

需要标注路径

```c#
Debug.Log(transform.Find("Child0/Child00"));//二级子物体
```



## 设置父子节点关系

注意，决定父子节点关系的是由`transform`组件控制的，所以说，在设置父子节点的时候，需要设置的是transform。

```c#
GameObject obj1 =  GameObject.Find("女主抱胸_1");
GameObject obj2 = GameObject.Find("Circle");
obj1.transform.SetParent(obj2.transform);
```

## 把节点设置为顶级节点

如果把SetParent设置为null，就会挂载到当前场景上去。



# Color

Color接收的是一个[0,1]的值，需要用R，G，B，A四个值各自除以255

```c#
image.color = new Color(1, 1, 1, 1);
```



Color32接收的是一个[0,255]的值，直接用R，G，B，A四个值来表示

```
image.color = new Color(255, 255, 255, 255);
```



ColorUtility.TryParseHtmlString 可以将十六进制的颜色值转换为Color类型的变量

```c#
Color tempColor; 
ColorUtility.TryParseHtmlString("#CCEEFFFF", out tempColor); 
image.color = tempColor;
```





# Random

```c#
 void Start()
    {
        // 静态变量
        print(Random.rotation+",随机出的旋转数是(以四元数形式表示)");
        print(Random.rotation.eulerAngles+",四元数转换成欧拉角");
        print(Quaternion.Euler(Random.rotation.eulerAngles)+",欧拉角转四元数");
        print(Random.value+",随机出[0,1]之间的浮点数");
        print(Random.insideUnitCircle+",在（-1，-1）~（1,1）范围内随机生成的一个vector2");
        print(Random.state+",当前随机数生成器的状态");
        // 静态函数
        print(Random.Range(0,4)+",在区间[0,4）（整形重载包含左Min,不包含右Max）产生的随机数");
        print(Random.Range(0, 4f) + ",在区间[0,4）（浮点形重载包含左Min,包含右Max）产生的随机数");
        Random.InitState(1);
        print(Random.Range(0,4f)+",设置完随机数状态之后在[0,4]区间内生成的随机数");
    }
```



# MonoBehaviour基类

**Behaviour与MonoBehaviour的关系：Mono继承自Behaviour,Behaviour继承自Compontent，Compontent继承自Object**





```c#
Debug.Log("No4_MonoBehaviour组件的激活状态是："+this.enabled);
Debug.Log("No4_MonoBehaviour组件挂载的对象名称是：" + this.name);
Debug.Log("No4_MonoBehaviour组件挂载的标签名称是：" + this.tag);
Debug.Log("No4_MonoBehaviour组件是否已激活并启用Behaviour：" + this.isActiveAndEnabled);
```



# Input

### 1.连续检测（移动）

```c#
连续检测（移动）
    // (-1到1)
        print("当前玩家输入的水平方向的轴值是："+Input.GetAxis("Horizontal"));
        print("当前玩家输入的垂直方向的轴值是：" + Input.GetAxis("Vertical"));
   // (-1,0,1三个值)
        print("当前玩家输入的水平方向的边界轴值是：" + Input.GetAxisRaw("Horizontal"));
        print("当前玩家输入的垂直方向的边界轴值是：" + Input.GetAxisRaw("Vertical"));
        print("当前玩家鼠标水平移动增量是："+Input.GetAxis("Mouse X"));
        print("当前玩家鼠标垂直移动增量是：" + Input.GetAxis("Mouse Y"));
```

### 2.连续检测（事件）

```c#
    //连续检测（事件）
     // bool类型
    if (Input.GetButton("Fire1"))
    {
        print("当前玩家正在使用武器1进行攻击！");
    }
    if (Input.GetButton("Fire2"))
    {
        print("当前玩家正在使用武器2进行攻击！");
    }
    if (Input.GetButton("RecoverSkill"))
    {
        print("当前玩家使用了恢复技能回血！");
    }
    
} 
```

### 3.间隔检测（事件）

```c#
   // 间隔检测（事件）
    if (Input.GetButtonDown("Jump"))
    {
        print("当前玩家按下跳跃键");
    }
    if (Input.GetButtonUp("Squat"))
    {
        print("当前玩家松开蹲下建");
    }
    if (Input.GetKeyDown(KeyCode.Q))
    {
        print("当前玩家按下Q键");
    }
    if (Input.anyKeyDown)
    {
        print("当前玩家按下了任意一个按键，游戏开始");
    }
    if (Input.GetMouseButton(0))
    {
        print("当前玩家按住鼠标左键");
    }
    if (Input.GetMouseButtonDown(1))
    {
        print("当前玩家按下鼠标右键");
    }
    if (Input.GetMouseButtonUp(2))
    {
        print("当前玩家抬起鼠标中键（从按下状态松开滚轮）");
    }
```



















# 画线系统







# 地形系统

1. 在Hierarchy面板中，右键3D object，选择Terrain
2. 在Terrain组件中选择Paint Terrain，可以来绘制地形
3. 其中有一个下拉框，可以绘制很多不同的东西

# TileMap

## 创建与绘制

用于绘制像素画

1. 在hierarchy中右键——2D Object——TileMap——rectanglar

   这个是创建画布的，画板上的内容可以直接画到这个上面

2. window——2D——palette

   创建画板，这个就是RPGMV左边那个画板。

3. 把sprite拖入到platee中去，此时会出现一个保存文件夹，建议把tile的资源单独保存

4. 要是画布上的图片有空白，就去sprite中，看看pixels per unit和图片大小是否一样





可以添加TileMap collider 2d来进行图块碰撞器的添加

还可以添加composite collider 2D来进行碰撞器的合并，这样可以提高性能，同时也可以防止多个碰撞器之间的缝隙，以免玩家卡进去.

如果不想被碰撞，那么需要去**tile保存的那个文件夹**，把对应的tile设置为none



## 碰撞器与合并

1. 在Hierarchy中创建Tilemap-Rectangle
2. 在生成的TileMap挂载TileMap Collider 2D组件
3. 勾选组件中的Used By Composite
4. 挂载Composite Collider 2D组件

## 代码管理

Tilemap 组件：用于管理瓦片地图

 TileBase 组件：瓦片资源对象基类

 Grid 组件：用于坐标转换

 使用它们需要引用命名空间：`using UnityEngine.Tilemaps;`

```c#
// 瓦片地图信息 可以通过它得到瓦片格子
public Tilemap map;

// 格子位置相关控制 可以通过它 进行坐标转换
public Grid grid;

// 瓦片资源基类通过它可以得到瓦片资源
public TileBase tileBase;

// Start is called before the first frame update
void Start()
{
    // 1.清空瓦片地图
    map.ClearAllTiles();

    // 2.获取指定坐标格子
    TileBase tmp = map.GetTile(Vector3Int.zero);

    // 3.设置删除瓦片
    map.SetTile(new Vector3Int(0, 2, 0), tileBase); // 设置
    map.SetTile(new Vector3Int(1, 0, 0), null);     // 删除

    // 4.替换瓦片
    map.SwapTile(tmp, tileBase); // tmp 的所有瓦片将变成 tileBase

    // 5.世界坐标转格子坐标

    //   屏幕坐标转世界坐标
    //   世界坐标转格子坐标
    // 传入的参数是世界坐标
    grid.WorldToCell();
}






```





```c#
using UnityEngine;
using UnityEngine.Tilemaps;

public class CreateTileMap : MonoBehaviour
{
    public Tilemap targetTileMap;
    public TileBase oldTile;
    public TileBase newTile;

    private void Start()
    {
        //只填充一个Grid，可覆盖
        //targetTileMap.SetTile(new Vector3Int(-2, 2, 0), tile);

        //动态清除一个Grid
        //targetTileMap.SetTile(new Vector3Int(-2, 2, 0), null);

        //动态填充一块矩形区域，参数分别是：起笔位置，需要绘制的Tile，矩形参数
        //注意：起笔位置必须在矩形的参数范围内，不能通过此方法批量清除Grid，不可覆盖
        //targetTileMap.BoxFill(Vector3Int.zero, null, -2, -2, 2, 2);

        //使用BoxFill来达到只填充一个Grid的目的
        //targetTileMap.BoxFill(new Vector3Int(1, 2, 0), tile, 1, 2, 1, 2);

        //将指定TileMap中的oldTile替换成newTile
        //targetTileMap.SwapTile(oldTile, newTile);

        //根据给定边界批量获得Grid中的Tile
        //TileBase[] tileBase = targetTileMap.GetTilesBlock(new BoundsInt(-3, -3, 0, 3, 3, 1));
        //foreach (var item in tileBase)
        //{
        //    Debug.Log(item);
        //}

        //根据给定边界和Tile数组批量填充Grid
        //targetTileMap.SetTilesBlock(new BoundsInt(0, 0, 0, 3, 3, 1), tileBase);

        //动态填充一块区域，采用油漆桶模式，参数分别是：起笔位置，需要绘制的Tile，填充范围自动识别
        //注意：可以通过此方法批量清除Grid，清空的范围自动识别
        //targetTileMap.FloodFill(new Vector3Int(-1, -1, 0), null);
    }
}

```



# 自动寻路

1. 选择window——AI——navigation

2. 在Hierarchy中选择想要寻路的地图，在navigation中选择bake

3. 如果某一个物体不想被烘焙，可以点击在navigation中的Object的navigation area选择not walkable

4. 3D自动寻路的代码

   agent把玩家自身拖过来就行

   ```c#
   using System.Collections;
   using System.Collections.Generic;
   using UnityEngine;
   using UnityEngine.AI;
   
   public class Character : MonoBehaviour
   {
       public NavMeshAgent agent;
   
   
       void Start()
       {
           
       }
   
       // Update is called once per frame
       void Update()
       {
   
           if (Input.GetMouseButtonDown(0))
           {
               Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
               RaycastHit raycastHit;
               if (Physics.Raycast(ray, out raycastHit))
               {
                   print(raycastHit.point);
                   agent.SetDestination(raycastHit.point);
               }
           }
   
       }
   }
   
   ```

   



1. 对需要寻路的物体添加static

2. 在window-ai下面找到navigation面板

3. 在bake下面进行烘焙

4. 如果是普通的gameobject，可能会出现可以通过的情况，此时选中物体，在navigation面板中的object中，可以选择Navigation Area是否通过。

5. 代码

   ```c#
   using UnityEngine;
   using UnityEngine.AI;
   
   public class Character : MonoBehaviour
   {
       public NavMeshAgent agent;
   
   
       void Start()
       {
           
       }
   
       // Update is called once per frame
       void Update()
       {
   
           if (Input.GetMouseButtonDown(0))
           {
               Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
               RaycastHit raycastHit;
               if (Physics.Raycast(ray, out raycastHit))
               {
                   print(raycastHit.point);
                   agent.SetDestination(raycastHit.point);
               }
           }
   
       }
   }
   ```

   











# 动画系统

# Timeline

# Cinemachine

## 2D相机

1. 在Hierarchy中创建Vitural Cinema
2. 把主角挂载到 CM vcam中
3. Body 选择Framing Transposer



- Dead zoom：当不为0时，会出现一个死区，玩家在其中运动的时候，镜头不会跟随，进入蓝色区域后才会跟随。
- Damping：阻尼，也就是镜头跟随玩家的速度



- 白区：跟随对象在白区内，摄像机不跟随。白区大小受Dead zoom影响。

- 蓝区： 跟随对象移动至蓝区中，摄像机就会跟随。速度会受Damping影响。

- 红区： 跟随对象高速移动时，会由于摄像机没有及时跟随上目标而丢失目标不在跟随。此时红区的作用就是，当跟随目标触及红线时，摄像机会立即跟随目标而不是缓慢跟随。

  红区的大小受到Soft Zone影响。

  



增加镜头移动边缘：

1. 在add Extension中选择confiner 2D，
2. 创建一个多边形碰撞器
3. 将碰撞器拖入到confiner 2D中
4. 要注意碰撞器的大小要比镜头大才有效果









# 灯光系统

## 2D光照

1. 安装Scriptable Build Pipeline
2. 安装Universal RP

## 四种灯光



## 制作天空盒

1. 在网上找一个天空盒的素材
2. 拖到unity中
3. texture type改成cube
4. 拖到画面上
5. 此时会自动生成一个material
6. 可以在material的inspector面板修改相关属性



## 影响光照的因素

- 天空盒

  在lighting界面中，可以设置

- Directional Light

  这个是模拟平行光的光影

- Environment Light

  在lighting界面设置

## Gamma空间和Linear空间

## 全局光照

全局光照由直接光照和间接光照组成。

全局光照可以使暗面没有那么暗



如果想要开启实时全局光照，需要在lighting中的scene开启realtime Global illumination

## 灯光烘焙

选择烘焙的时候，只有baked模式下的物体会有灯光





# UGUI系统

## 自动排列，滚动框

Scroll Rect组件：





## Text Mesh Pro

### 获取

```c#
using TMPro;
dialogText = GameObject.Find("对话框").GetComponent<TMP_Text>();
```



### 解决无中文问题

1. 将一个字体拖入unity
2. 右键-creat-text mesh pro-for asset



### 支持的转义字符

```text
表情<sprite=1>

字体大小<size=30>大小

字体颜色<color=#FFFFFF>白色

超链接<link=123>显示的文本
```



## 动态创建按钮

```c#
private void OnGUI()
{
    if (GUI.Button(new Rect(10, 20, 100, 40), "这是一个按钮"))
    {
        print("点击");
    }
}
```



## 单选框

1. 给父组件添加`Toggle Group`组件
2. 创建ui-toggle的子组件
3. 把父组件拖到Group里面就行了

## 组件

Outline：描边

Shadow：阴影



## 创建滚动条



## 富文本



| 代码                                 | 类型     |      |
| ------------------------------------ | -------- | ---- |
| `<b>不</b>`                          | 粗体     |      |
| `<color=green>羡慕</color>`          | 颜色     |      |
| `<size=50>大部分</size>都未受到影响` | 字体大小 |      |



## Canvas

Canvas组件自带有三个组件，分别是Canvas、Canvas Scaler、Graphic Raycaster组件



### Canvas组件

#### Screen Space-Overlay —— 屏幕空间覆盖模式

表示不管有没有相机去渲染场景，Canvas下的所有UI永远位于屏幕的前面，覆盖掉渲染场景显示的元素。



| 属性                      | 功能                                                         |
| ------------------------- | ------------------------------------------------------------ |
| Pixel Perfect             | 使UI元素像素对应，效果就是边缘清晰不模糊                     |
| Sort Order                | 多个Canvas时，数值越大越后渲染。值大的 画布，会挡住值小的    |
| Target Display            | 目标显示器，如果有多个屏幕的话可以选择                       |
| Addtional Shader Channels | 附加着色通道，决定Shader可以读取哪些相关数据，比如 法线、 切线 等数据。 |





#### Screen Space-Camera —— 相机模式

这种渲染模式 适用于场景模型太多太大，在调整UI的时候挡住UI，让UI和渲染的相机移动到比较远的位置，就可以避免遮挡。并且Canvas 和 摄像机之间有一定的距离 , 可以在摄像机和 Canvas之间放置一些模型或粒子特效。

| 属性           | 功能                                     |
| -------------- | ---------------------------------------- |
| Pixel Perfect  | 使UI元素像素对应，效果就是边缘清晰不模糊 |
| Render Camera  | 渲染的相机                               |
| Plane Distance | Canvas与相机之间的距离                   |
| Sorting Layer  | 画布的深度,指定了相机的渲染顺序          |
| Order In Layer | 值越大，该UI越显示在前面                 |



#### World Space —— 世界模式

| 属性                      | 功能                                                         |
| ------------------------- | ------------------------------------------------------------ |
| Event Camera              | 响应事件的相机                                               |
| Sorting Layer             | 画布的深度,指定了相机的渲染顺序                              |
| Order in Layer            | 值越大，该UI越显示在前面                                     |
| Addtional Shader Channels | 附加着色通道，决定Shader可以读取哪些相关数据，比如 法线、 切线 等数据 |





### Canvas Scaler组件

控制UI画布的放大缩放的比例



#### Constant Pixer Size —— 恒定像素

这种模式下 UI以像素为大小，同样的像素在不同的分辨率下尺寸不一样

| 属性                     | 功能             |
| ------------------------ | ---------------- |
| Scale Factor             | 缩放因子         |
| Reference Pixels Per Uit | 单位面积像素数量 |



#### Scale With Screen Size —— 屏幕尺寸比例

这种缩放模式下的UI位置是根据屏幕的分辨率和设置的宽高比来调整UI的位置的，通常做屏幕UI自适应的时候都需要调整到这个缩放模式下。

| 属性                  | 功能         |
| --------------------- | ------------ |
| Referencee Resolution | 预设屏幕大小 |
| Screen Match Mode     | 缩放模式     |
| Match                 | 宽高比       |

#### Constant Physical Size —— 恒定尺寸

| 属性                     | 功能             |
| ------------------------ | ---------------- |
| Physical Unit            | 使用单位         |
| Fallback Screen DPI      | 备用屏幕的DPI    |
| Default Sprite DPI       | 默认图片的DPI    |
| Reference Pixels Per Uit | 单位面积像素数量 |



### Graphic Raycaster组件

控制是否让UI响应射线点击

| 属性                    | 功能                                                         |
| ----------------------- | ------------------------------------------------------------ |
| Ignore Reversed Graphic | 忽略反转的UI，UI反转后点击无效。                             |
| Blocking Objects        | 阻挡点击物体，当UI前有物体时，点击前面的物体射线会被阻挡。   |
| Blocking Mask           | 阻挡层级，当UI前有设置的层级时，点击前面的物体射线会被阻挡。 |





## EventSystem

Canvas一同创建的还有一个EventSystem，这是一个基于Input的事件系统，可以对键盘、触摸、鼠标、自定义输入进行处理。



### Event System组件

Event System负责处理输入、射线投射以及发送事件。一个场景中只能有一个Event System组件。

| 属性                   | 介绍         |
| ---------------------- | ------------ |
| First Selected         | 首选对象     |
| Send Navigation Events | 发送导航事件 |
| Drag Threshold         | 拖动阈值     |







### Standalone Input Module组件

处理输入的鼠标或触摸事件，进行事件的分发。

| 属性                     | 介绍         |
| ------------------------ | ------------ |
| Horizontal Axis          | 横轴         |
| Vertical Axis            | 纵轴         |
| Submit Button            | 提交按钮     |
| Canvel Button            | 取消按钮     |
| Input Actions Per Second | 每秒输入动作 |
| Repeat Delay             | 重复延迟     |
| Force Module Active      | 力模块激活   |





## Button组件

### Transition 过渡

点击按钮时候的变化

#### Color Tint —— 颜色过渡



| 属性              | 介绍                                                         |
| ----------------- | ------------------------------------------------------------ |
| Interactable      | 是否启动按钮的响应                                           |
| Transition        | 按钮的过渡动画类型，有Color Tint颜色过渡、Sprite Swap图片过渡、Animation动画过渡 |
| Target Graphic    | 目标图形                                                     |
| Normal Color      | 普通状态下的颜色                                             |
| Highlighted Color | 鼠标悬停时状态下的颜色                                       |
| Pressed Color     | 点击状态的颜色                                               |
| Disabled Color    | 禁用状态的颜色                                               |
| Color Multiplier  | 颜色乘数                                                     |
| Fade Duration     | 效果消失的时间                                               |
| Navigation        | 导航类型                                                     |
| OnClick           | 点击事件列表                                                 |

### 事件绑定

1. 直接在inspector面板绑定

2. 监听器绑定

   ```c#
   using UnityEngine;
   using UnityEngine.UI;
   
   public class ButtonTest : MonoBehaviour
   {
       public Button m_Button;
       public Text m_Text;
       void Start()
       {
           m_Button.onClick.AddListener(ButtonOnClickEvent);
       }
       public void ButtonOnClickEvent()
       {
           m_Text.text = "鼠标点击";
       }
   }
   
   ```

3. 射线检测监听

   ```c#
   using System.Collections.Generic;
   using UnityEngine;
   using UnityEngine.EventSystems;
   using UnityEngine.UI;
   
   public class ButtonTest : MonoBehaviour
   {
       public Text m_Text;
   
       void Update()
       {
           if (Input.GetMouseButtonDown(0))
           {
               if (OnePointColliderObject() != null)
               {
                   if (OnePointColliderObject().name == "Button" || OnePointColliderObject().name == "Text")
                   {
                       ButtonOnClickEvent();
                   }
               }
           }
       }
   
       //点击对象获取到对象的名字
       public GameObject OnePointColliderObject()
       {
           //存有鼠标或者触摸数据的对象
           PointerEventData eventDataCurrentPosition = new PointerEventData(EventSystem.current);
           //当前指针位置
           eventDataCurrentPosition.position = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
           //射线命中之后的反馈数据
           List<RaycastResult> results = new List<RaycastResult>();
           //投射一条光线并返回所有碰撞
           EventSystem.current.RaycastAll(eventDataCurrentPosition, results);
           //返回点击到的物体
           if (results.Count > 0)
               return results[0].gameObject;
           else
               return null;
       }
   
       public void ButtonOnClickEvent()
       {
           m_Text.text = "鼠标点击";
       }
   }
   ```

4. 通过 EventTrigger 实现按钮点击事件

   ```c#
   using UnityEngine;
   using UnityEngine.EventSystems;
   using UnityEngine.UI;
   
   [RequireComponent(typeof(EventTrigger))]
   public class ButtonTest : MonoBehaviour
   {
       public Text m_Text;
   
       void Start()
       {
           Button btn = transform.GetComponent<Button>();
           EventTrigger trigger = btn.gameObject.GetComponent<EventTrigger>();
           EventTrigger.Entry entry = new EventTrigger.Entry
           {
               // 鼠标点击事件
               eventID = EventTriggerType.PointerClick,
               // 鼠标进入事件 entry.eventID = EventTriggerType.PointerEnter;
               // 鼠标滑出事件 entry.eventID = EventTriggerType.PointerExit;
               callback = new EventTrigger.TriggerEvent()
           };
           entry.callback.AddListener(ButtonOnClickEvent);
           // entry.callback.AddListener (OnMouseEnter);
           trigger.triggers.Add(entry);
       }
   
       public void ButtonOnClickEvent(BaseEventData pointData)
       {
           m_Text.text = "鼠标点击";
       }
   }
   
   ```

5. 通过通用类 UIEventListener 来处理Button响应事件

   ```c#
   using UnityEngine;
   using UnityEngine.EventSystems;
   
   public class UIEventListener : MonoBehaviour, IPointerClickHandler
   {
       // 定义事件代理
       public delegate void UIEventProxy();
       // 鼠标点击事件
       public event UIEventProxy OnClick;
   
       public void OnPointerClick(PointerEventData eventData)
       {
           if (OnClick != null)
               OnClick();
       }
   }
   
   ```

   从

   ```c#
   using UnityEngine;
   using UnityEngine.EventSystems;
   using UnityEngine.UI;
   
   [RequireComponent(typeof(EventTrigger))]
   public class ButtonTest : MonoBehaviour
   {
       public Text m_Text;
   
       void Start()
       {
           Button btn = this.GetComponent<Button>();
           UIEventListener btnListener = btn.gameObject.AddComponent<UIEventListener>();
   
           btnListener.OnClick += delegate () {
               ButtonOnClickEvent();
           };
       }
   
       public void ButtonOnClickEvent()
       {
           m_Text.text = "鼠标点击";
       }
   }
   
   ```

   

​	
​	
​	




## Text组件



<table><thead><tr><th>属性</th><th>说明</th></tr></thead><tbody><tr><td>Text</td><td>用于显示的文本</td></tr><tr><td>Font</td><td>文本的字体</td></tr><tr><td>Font Style</td><td>文本的样式（正常、加粗、斜线）</td></tr><tr><td>Font Size</td><td>字体的大小</td></tr><tr><td>Line Spacing</td><td>文本行之间的间距</td></tr><tr><td>Rich Text</td><td>是否支持富文本，富文本是带有标记标签的文本，增强文本的显示效果</td></tr><tr><td>Alignment</td><td>文本的水平和垂直对齐方式</td></tr><tr><td>Align By Geometry</td><td>是否以当前所显示的文字中获得的最大长宽（而不是字体的长宽）进行对齐。</td></tr><tr><td>Horizontal Overflow</td><td>文字横向溢出处理方式，可以选择Warp隐藏或者Overflow溢出</td></tr><tr><td>Vertical Overflow</td><td>文本纵向溢出的处理方式，可以选择Truncate截断或者Overflow溢出</td></tr><tr><td>Best Fit</td><td>忽略Font Size设置的文字大小，自适应改变文字大小以适应文本框的大小</td></tr><tr><td>Color</td><td>文本的颜色</td></tr><tr><td>Material</td><td>用来渲染文本的材质，可以通过设置材质，让文本拥有更加炫酷的效果。</td></tr><tr><td>Raycast Target</td><td>是否可以被射线检测，通常情况下可以关闭，因为文本最好只用来显示。</td></tr></tbody></table>



## Toggle



## 接口

<table><thead><tr><th>接口</th><th>说明</th></tr></thead><tbody><tr><td>IPointerEnterHandler - OnPointerEnter</td><td>当指针进入对象时调用</td></tr><tr><td>IPointerExitHandler - OnPointerExit</td><td>当指针退出对象时调用</td></tr><tr><td>IPointerDownHandler - OnPointerDown</td><td>当指针压在对象上时调用</td></tr><tr><td>IPointerUpHandler - OnPointerUp</td><td>当指针被释放时调用(在原始按下的对象上调用)</td></tr><tr><td>IPointerClickHandler - OnPointerClick</td><td>当在同一对象上按下和释放指针时调用</td></tr><tr><td>IInitializePotentialDragHandler - OnInitializePotentialDrag</td><td>在找到拖动目标时调用，可用于初始化值</td></tr><tr><td>IBeginDragHandler - OnBeginDrag</td><td>当拖动即将开始时，在拖动对象上调用</td></tr><tr><td>IDragHandler - OnDrag</td><td>当发生拖动时在拖动对象上调用</td></tr><tr><td>IEndDragHandler - OnEndDrag</td><td>当拖动完成时在拖动对象上调用</td></tr><tr><td>IDropHandler - OnDrop</td><td>在拖动完成时对对象调用</td></tr><tr><td>IScrollHandler - OnScroll</td><td>当鼠标滚轮滚动时调用</td></tr><tr><td>IUpdateSelectedHandler - OnUpdateSelected</td><td>在选定的对象上调用</td></tr><tr><td>ISelectHandler - OnSelect</td><td>当对象变成选定对象时调用</td></tr><tr><td>IDeselectHandler - OnDeselect</td><td>被选中的对象被取消选中</td></tr><tr><td>IMoveHandler - OnMove</td><td>当移动事件发生时调用(左、右、上、下等)</td></tr><tr><td>ISubmitHandler - OnSubmit</td><td>在按下提交按钮时调用</td></tr><tr><td>ICancelHandler - OnCancel</td><td>按下取消按钮时调用</td></tr></tbody></table>





# 粒子系统



| 属性           | 说明                                         |
| -------------- | -------------------------------------------- |
| Duration       | 粒子运行时间，若勾起Looping则没有效果        |
| Looping        | 是否循环播放                                 |
| Prewarm        | 是否立即播放。选了这个就不能选Start Delay    |
| Start Delay    | 粒子的播放延迟时间                           |
| Start Lifetime | 粒子的生命周期，可以理解为单个粒子的存在时间 |
| Start Speed    | 粒子的速度，就是单个粒子发射速度             |
| 3D Start Size  | 可以从xyz来调整粒子大小                      |
| Start Size     | 等比例缩放粒子大小                           |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |
|                |                                              |





3D Start Rotation:3D旋转，勾选后可以用XYZ调节粒子的旋转
Start Rotation：开始的旋转，勾选后可从整体调整粒子旋转。
Flip Rotation:镜像翻转。
Start Color:开始时的颜色，可以调节
Gravity Modifier:受重力影响的大小，越大粒子下落越快，负数则粒子上升越快。可以用做喷泉等。
Simulation Space：粒子系统在自身坐标系还是世界坐标系。如果是粒子之间的互动，用局部空间。如果是物体来影响粒子，用世界空间。
Simulation Speed:模拟速度，根据Update模拟的速度。
Delta Time:主要用于暂停菜单的粒子系统。
Scaling Mode:缩放比例，三个选项：Hierarachy:当前粒子大小会受到上一级对象的缩放影响、Local:只跟自身大小有关、Shape:跟发射器有关系。
Play On Awake:点击Play时是否运行。
Emitter Velocity:发射器速度
Max Particles:最大粒子数，就是游戏内存在的最大粒子数量
Auto Random Seed:粒子随机，启用后每次播放都会有不同。
Stop Action:当属于系统的所有粒子都已完成时，可使系统执行某种操作。当一个系统的所有粒子都已死亡，并且系统存活时间已超过 Duration 设定的值时，判定该系统已停止。对于循环系统，只有在通过脚本停止系统时才会发生这种情况。
Disable:禁用游戏对象
Destory：销毁游戏对象
Callback：将 OnParticleSystemStopped 回调发送给附加到游戏对象的任何脚本。





# 场景系统

## 同步加载场景

## 异步加载场景





```c#
 private AsyncOperation ao;
    void Start()
    {
        SceneManager.LoadScene(1);
        SceneManager.LoadScene("TriggerTest");
        SceneManager.LoadScene(2);
        SceneManager.LoadSceneAsync(2);
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            SceneManager.LoadSceneAsync(2);
            StartCoroutine(LoadNextAsyncScene());
        }
        if (Input.anyKeyDown&&ao.progress>=0.9f)
        {
            ao.allowSceneActivation = true;
        }
    }

    IEnumerator LoadNextAsyncScene()
    {
        ao= SceneManager.LoadSceneAsync(2);
        ao.allowSceneActivation = false;
        while (ao.progress<0.9f)
        {
         // 当前场景加载进度小于0.9
         // 当前场景挂起，一直加载，直到加载基本完成
            yield return null;
        }
        Debug.Log("按下任意键继续游戏");
    }
```





# 物理系统

Player settings：Queries Hit Triggers，取消鼠标和触发器的碰撞



## 射线检测

```c#
 private Collider2D collider;
void Start()
{
    collider = GetComponent<Collider2D>();
}
void Update()
{

            collider.enabled = false;
            RaycastHit2D hitTest = Physics2D.Linecast(start位置,end位置);
            collider.enabled = true;
}
```



```c#
  RaycastHit2D hit = Physics2D.Raycast(rigidbody2d.position+
                Vector2.up*0.2f,lookDirection,1.5f,LayerMask.GetMask("NPC"));
```







## 2D碰撞器

box collider 2D



**产生碰撞的条件：**

**双方都挂载碰撞器，运动的一方挂载刚体**



旋转与抖动问题

使用默认的组件只会会发生抖动与旋转的问题

1. 在rigidbody 2d中把constrain的z轴冻结

2. 会发生抖动是因为自己写的代码直接控制了  transform.position

   但是这个位置会直接移动进入刚体内部，因此会被引擎拉出去。

   因此为了防止这个bug，可以直接操纵刚体的位置

   ```c#
    rigidbody2D.position = position;
   ```

   







## 触发器和碰撞器的区别

触发器只会进行触发而不会进行物理碰撞

1. 双方挂载collider

2. 一方挂载刚体

3. 一方把is Trigger打开

4. 写代码

   ```c#
       private void OnTriggerEnter2D(Collider2D collision)
       {
            if (collision.GetComponent<RubyController>()!=null)
            collision.GetComponent<RubyController>().changeHP(-1);
       }
   ```



碰撞器会进行物理碰撞

1. **两物都有Collider**

2. ​    **至少有一个带有RigidBody**

3. 写代码

   ```c#
    void OnCollisionEnter2D(Collision2D collision)
       {
           Debug.Log("OnCollisionEnter2D:" + collision.transform.name);
       }
   ```

   

   

   防止人物和子弹之间碰撞

   1. 在右边设置层级
   2. 自定义一个层级，子弹和人物分别占据不同的层级
   3. 在设置中找到physics 2d，拉到最下面，把对应的勾取消就行

**注意**，碰撞器是Collision2D而触发器是Collider2D



**Unity 3D 中的碰撞体和触发器的区别在于：碰撞体是触发器的载体，而触发器只是碰撞体的一个属性**。



## 碰撞和触发检测

```c#
  private void OnCollisionEnter2D(Collision2D collision)
    {
        // 碰撞到的游戏物体名字
        Debug.Log(collision.gameObject.name);
    }

    private void OnCollisionStay2D(Collision2D collision)
    {
        Debug.Log("在碰撞器里");
    }

    private void OnCollisionExit2D(Collision2D collision)
    {
        Debug.Log("从碰撞器里移出");
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        // 碰撞到的游戏物体名字
       Debug.Log(collision.gameObject.name);
    }

    rivate void OnTriggerStay2D(Collider2D collision)
    {
        Debug.Log("在触发器里");
    }

    private void OnTriggerExit2D(Collider2D collision)
    {
        Debug.Log("从触发器里移出");
    }
```





# 时间系统

暂停游戏

Time.timescale = 0

Time.timescale = 1



# 

# unity脚本的生命周期

## 生命周期图

unity脚本是挂在在游戏物体上的，物体有生命周期，脚本当然也有了。

unity脚本的生命周期是unity开发中必须掌握的重要内容。

![](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/生命周期函数.jpg)





## 生命周期函数



| 函数名            | 调用时机                                                     |
| ----------------- | ------------------------------------------------------------ |
| Reset             | 当Scripts第一次绑定 到物体上或者点击Reset按钮的时候会触发，<br/>且只在Editor的模式下触发，游戏打包的时候并不会触发 |
| Awake             | 当脚本实例在游戏运行被载入的时候运行，一般为<br/>了初始化游戏变量和游戏状态，注意，无论函数是<br/>否被激活，Awake都会执行! ! |
| OnEnable          | 每当启用脚本时调用                                           |
| Start             | 游戏对象调用脚本时执行                                       |
| FixedUpdate       | 它是物理循环中最先执行的函数，它每隔固定时间执行一次。我们通常与把物理模拟有关的代码，写在 FixedUpdate 函数中，比如给游戏对象添加力。默认0.02s执行一次。 |
| OnTrigger         |                                                              |
| OnCollision       |                                                              |
| OnMouseXXX        | 有关鼠标的函数就在此刻执行。                                 |
| Update            | 它在每帧执行一次，该函数主要处理游戏对象在游戏世界的行为逻辑，例如游戏角色的控制和游戏状态的控制. |
| LateUpdate        | 它也是每帧执行一次，在 Update 函数后执行。 在实际开发过程中 Update 函数与 LateUpdate 函数通常共同使用。一般我们在 Update 函数中处理玩家角色的移动，在 LateUpdate 函数中处理摄像机跟随玩家，这样能防止摄像机出现抖动现象。因为，如果我们把这两个都写在Update中，有可能造成摄像机先跟随，玩家后移动的逻辑bug。 |
| OnBecameVisible   |                                                              |
| OnBecameInvisible | 当物体在任何相机中可见/不可见时调用。注意：Scene视图的相机也需要考虑进去。 |
| OnGUI             | 一帧会调用多次来响应GUI事件。                                |
| OnDestroy         | 脚本或者脚本挂载的游戏对象销毁时，在对象存在的最后一帧调用。 |
| OnApplicationQuit | 应用退出时所有的游戏物体将会调用此函数                       |





## Awake和Start区别

各个脚本的awake乱序执行，而start



## 变量初始化的顺序问题

顺序如下，首先是初始化时赋值，然后再外部编辑器，之后以此类推

```c#
public int a = 0;

//外部编辑器赋值，也就是inspector面板

private void Awake()
{
    a = 1;
}

private void OnEnable()
{
    a = 2;
}

void Start()
{
    a = 3;
}

```





# OnMouseEventFunction鼠标回调事件

```c#
 private void OnMouseDown()
    {
        print("在Gris身上按下了鼠标");
    }

    private void OnMouseUp()
    {
        print("在Gris身上按下的鼠标抬起了");
    }

    private void OnMouseDrag()
    {
        print("在Gris身上用鼠标进行了拖拽操作");
    }

    private void OnMouseEnter()
    {
        print("鼠标移入了Gris");
    }

    private void OnMouseExit()
    {
        print("鼠标移出了Gris");
    }

    private void OnMouseOver()
    {
        print("鼠标悬停在了Gris上方");
    }

    private void OnMouseUpAsButton()
    {
        print("鼠标在Gris身上松开了");
    }
```





# Utility



- JsonUtility

  负责Json文件的序列化和反序列化

  ```c#
  //从object序列化为json字符串
  JsonUtility.ToJson(_class1);
  //从json字符串反序列化为object
  JsonUtility.FromJson<TestClass1>(_jsonStr);
  //此方法与JsonUtility.FromJson非常相似，不同之处在于，
  //它不是创建新对象并将JSON数据加载到其中，而是将JSON数据加载到现有对象中。
  //这使您无需任何分配即可更新存储在类或对象中的值
  JsonUtility.FromJsonOverwrite(_jsonStr,this);
  ```

- EditorUtility

  ```c#
  //显示进度条
   EditorUtility.DisplayProgressBar("标题", "进度条内容", progress / secs); 
   //关闭进度条
   EditorUtility.ClearProgressBar();
   //标准对话框
   EditorUtility.DisplayDialog("标题","询问？", "确定", "取消"));
  ```

  



# Unity特性

## 修改inspector

### Header

```c#
[Header("与物体交互时的信息")]
public string[] text;
```


## 修改editor



| 代码                                                         | 代码 | 特性描述                                                     |
| ------------------------------------------------------------ | ---- | ------------------------------------------------------------ |
| [SerializeField]                                             |      | 序列化一个类，实际用处是把数据存储到硬盘上，表面用处可以把私有的在检视面上显示出来 |
| [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)] |      | 无需创建空物体就能执行代码                                   |
| [HideInInspector]                                            |      | 隐藏公有变量                                                 |
|                                                              |      | 在Inspector中重命名一个变量                                  |
| [Range(minnum,maxNum)]                                       |      | 给一个数值变量添加滑块                                       |
| [TextArea（最小行数，最大行数）]                             |      | 文本框扩大， 超过最大行数会出现滚动条                        |
|                                                              |      |                                                              |
| [ContextMenu("执行函数")]                                    |      | 为挂载脚本的物体的Inspector界面脚本添加一个脚本右键选项,点击执行方法内的逻辑 |



## 增加标题

```
 [Header("xxxxx")]
```







# 人工智能

## 群组行为

模拟鸟群飞行或者人群行走过程称之为群组行为



分离 队列 聚集









# 小技巧



## scriptableobject类

浅拷贝来避免开销

## 使用TryGetComponent

对于



## 使用本地函数localFunction

对于一些只在函数内部调用的函数，可以写成本地函数。

```c#
public void Test()
{
    var attack = RandamNum();
    var defense = RandamNum();
    int RandamNum()
    {
       return Mathf.Rnage(10,20);
    }
}
```







## 多个Awake之间的顺序

方法一：手动调整Scripts的执行顺序

在Unity菜单中，选择Edit>Project Settings>Script Execution Order,可以添加并且调整Scripts的手动顺序。可以参考官方文档。 

方法二：使用 [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]





## 建立程序集

 Create Assembly Defintion，然后跟他同一个文件夹的脚本都会成为该程序集。





多用try

- 对齐摄像机到视口

  选中摄像机，GameObject选择algin with view

- 







············································································································································································································  



# unity原生



## 按照世界坐标移动

常用于摄像机移动

```c#
   void Update()
    {
        float h =  Input.GetAxis("Horizontal");
        float v =  Input.GetAxis("Vertical");
        transform.Translate(new Vector3(h,0,v)*Time.deltaTime*speed,Space.World);
    }
```



## 加载下一个场景

1. 新建一个UI组件，或是别的什么的

2. 给ui组件添加button组件，然后挂载下面的脚本

   ```c#
   using System.Collections;
   using System.Collections.Generic;
   using UnityEngine;
   using UnityEngine.UI;
   using UnityEngine.SceneManagement;
   
   public class StartGame : MonoBehaviour
   {
      
       void Start()
       {
           GetComponent<Button>().onClick.AddListener(LoadNextScene);
       }
   
       // Update is called once per frame
       void Update()
       {
           
       }
   
       void LoadNextScene() 
       {
           SceneManager.LoadScene(1);
       }
   }
   
   ```

3. 打开build settings，在上面添加需要加载的场景

## 替换默认的鼠标样式

1. 找到中意的图片，并在unity中修改texture type为cursor
2. 在Edit->Project Setting->Player->Default Cursor，将图片拖进去

## 图片切割

1. 导入图片
2. 在project里面点击图片
3. 右边属性里面把Sprite mode设置为mutiple
4. 点击sprite editor
5. 进去，点击slice
6. apply保存

## 读取JSON的信息

1. 建立一个JSON

   最好建在Resources中

   要注意，unity中，JSON不能单纯用list。每一个list都必须有一个对象包裹。

   ```json
   {
     "infoList": [
       {
         "panelType": "主面板",
         "panelPath": "UIPanels/主面板"
       },
       {
         "panelType": "任务面板",
         "panelPath": "UIPanels/任务面板"
       }
     ]
   }
   ```

2. 建立JSON对应的类

   类中的属性名和JSON要一一对应

   ```c#
   //可序列化的
   [Serializable]
   public class UIInfo
   {
       public string panelType;
       public string panelPath;
   }
   class UIPanelTypeJson
   {
       public List<UIInfo> infoList;
   }
   ```

3. 读取

   ```c#
   //用于存储UI面板路径
   private Dictionary<string,string> UIPathdictionary;
   private void loadUIInfo() {
       //将UI的信息存入字典
       UIPathdictionary = new Dictionary<string, string>();
   
       
       TextAsset textAsset = Resources.Load<TextAsset>("UIInfoJSON");
   
       UIPanelTypeJson jsonObject = JsonUtility.FromJson<UIPanelTypeJson>(textAsset.text);
   
       foreach (UIInfo info in jsonObject.infoList)
       {
           UIPathdictionary.Add(info.panelType, info.panelPath);
       }
   
   }
   ```

4. 使用

   ```c#
   public void Test() 
   {
       string path;
       UIPathdictionary.TryGetValue("主面板", out path);
       Debug.Log(path);
   }
   ```

   





## 帧率

unity中帧率是不固定的，引擎会尽可能快的刷新游戏

下面的代码会要求引擎尽可能按照这个帧率去更新

```c#
Application.targetFrameRate = 60;
```



## 神秘的2019.3

用unity2019.3之前打包游戏，玩的时候会弹出一个选择框







## 延迟调用



```c#
 Invoke("closeDialog", 2f);  //两秒后调用demo()函数
```



```c#
InvokeRepeating("方法名",多长时间之后开始调用,每几秒调用一次)
```



## 动画


      1. 把多张精灵图拖进场景可以创建逐帧动画
      2. 对动画按ctrl+6，可以进行编辑

   



















































   1. 对想要加载动画的对象挂载Animator

   2. 在资源管理器创建一个animator controller

   3. 把这个controller挂载到组件上面

   4. 打开window-animation的animation和animator两个面板

   5. 在animation中创建动画

   6. 在animator中创建混合树，把参数设置为xy

   7. 分别把四个状态挂载上去。

   8. 写代码控制状态

      ```c#
      Animator animator = GetComponent<Animator>();
      animator.SetFloat("x", direction.x);
      animator.SetFloat("y", direction.y);
      ```

      



## 如何对2D精灵图的渲染进行排序

1. 在edit—project settings—Graphics中，修改Transparency Sort Mode的值为Custom Axis
2. 将y设为1，剩下的为0
3. 设置精灵图的pivot为custom。如果精灵图的显示模式为Multiple，那么需要Sprite Edit里面调整
4. 将Sprite制作成Prefab之后，Sprite Sort Point设置成pivot
5. 要注意sorting layers和order in layers是否一样，否则无法正常排序







## sorting layer和order in layer的区别

- sorting是处理**碰撞**的，也就是需要互相碰撞的放到一个sorting layer中
- sorting layer越下面，渲染越晚。也就是说越下面越显示
- order in layer是处理同一个sorting layer中的排序问题的。order in layer越大，渲染越晚。也就是数值越大越能看见。



Edit Project Seetings——graphic

Transparency Sort Mode改为custom axis

下面的Z改为0，Y改为1

两者的order in layer都为一个层级

可以实现人物在下面时和上面时被不同遮挡的效果



若不满意排序的锚点，可以把sprite sort point改成pivot，具体锚点可以去sprite中修改









## 相机跟随

1. Window-Package Manager
2. 选择安装cinema chine
3. 在follow里面把主角拖进去
4. 最下面选择add extension-confiner
5. 创建一个空对象挂载polygon collider 2d
6. 调整大小之后拖进Bound shape 2D
7. 对空对象新建一个层级
8. 在Edit-project setting-Physics 2d里面将人物与空对象的碰撞取消



## 键盘控制

```c#
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.E)) {
            dialog.SetActive(false);
        }
    }
```



## 开关一个游戏对象

这个是指控制一个游戏对象是否显示，我感觉很像前端的display:none;

```c#
dialog.SetActive(false);
```

## 鼠标点击

```c#
if (Input.GetMouseButtonDown(0))
    Debug.Log("Pressed left click.");

if (Input.GetMouseButtonDown(1))
    Debug.Log("Pressed right click.");

if (Input.GetMouseButtonDown(2))
    Debug.Log("Pressed middle click.");
```



## 音乐

- 背景音乐

  新建一个空对象，挂载audio source组件，直接把音频拖到组件里面

- 音效

  给需要音效的对象挂载audio source组件，

  ```c#
  private AudioSource audioSource;
  public AudioClip hurtClip;
  void Start()
  {
      audioSource = GetComponent<AudioSource>();
  }
  void 某函数(){
        audioSource.PlayOneShot(hurtClip);
  }
  
  ```





# UGUI

```c#
using UnityEngine.UI;
```



## 准备工作

### 建立必要的文件夹

1. 在Project下面建立**UIFramework**文件夹

2. 在文件夹中建立

   - Assets：用于存储UI的各种资源
   - Fonts：用于存储UI的字体
   - Scripts：用于存放UI框架的脚本
   - Resources：用于存放需要使用的游戏资源

   

### 建立UI的面板

1. 在unity中的Hierarchy中新建一个UI—Canvas

2. 在canvas下建立若干image组件

   按照自己的需求建立组件

   例如，起名为：

   - MainPanel
   - TaskPanel
   - EquipPanel

3. 为各个组件添加image组件，并加上button组件

4. 如果这个面板拥有二级菜单，也就是说不是最顶层的菜单，那么需要再添加**Canvas Group**组件

5. 修改其锚点

![image-20220812162135103](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812162135103.png)

5. 将其全部拉进Resources中的UIPanels，以便后期调用

6. 之后删掉屏幕上的UI即可，只需要保留Canvas

   ![image-20220812162528798](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812162528798.png)





## 编写JSON

![image-20220812165850237](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812165850237.png)

这个JSON是用来储存所有UI面板的信息用的。

为了方便后期的维护和拓展，所以采用了JSON存储

**JSON也是放在Resoures中的，这是为了方便读取！**

起名为`UIPanelsInfoJson.json`

```json
{
  "panelsInfo": [
    {
      "panelType": "EquipPanel",
      "panelPath": "UIPanels/EquipPanel"
    },
    {
      "panelType": "MainPanel",
      "panelPath": "UIPanels/MainPanel"
    },
    {
      "panelType": "TaskPanel",
      "panelPath": "UIPanels/TaskPanel"
    }
  ]
}
```

unity中的json比较特殊，必须用一个对象来包裹数组



## 编写BasePanel

![image-20220812165827465](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812165827465.png)

这个是用来控制所有面板的基类。

1. 编写BasePanel

   此时仅需要一个大框框即可

   ```c#
   public class BasePanel : MonoBehaviour
   {
       /// <summary>
       /// 界面被显示出来
       /// </summary>
       public virtual void OnEnter()
       {
   
       }
   
       /// <summary>
       /// 界面暂停
       /// </summary>
       public virtual void OnPause()
       {
   
       }
   
       /// <summary>
       /// 界面继续
       /// </summary>
       public virtual void OnResume()
       {
   
       }
   
       /// <summary>
       /// 界面不显示,退出这个界面，界面被关系
       /// </summary>
       public virtual void OnExit()
       {
   
       }
   
   }
   
   ```

   

2. 给每个面板都挂载自己的面板

   ![image-20220812170210167](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812170210167.png)

3. 让各自的面板继承BasePanel

   ```c#
   public class EquipPanelManager : BasePanel
   {
   
   }
   ```

   







## 编写UIManager

### 构造单例模式

接下来就是编写UI的管理器了

```c#
    /// <summary>
    /// 单例模式的设计
    /// </summary>

    private static UIManager _instance;

    public static UIManager Instance
    {
        get
        {
            if (_instance == null)
            {
                _instance = new UIManager();
            }
            return _instance;
        }
    }

    private UIManager()
    {
        //在构造函数中读取JSON的数据
        LoadJson();
    }
```

### 构造数据结构并读取JSON



```c#
using System;

    /// <summary>
    /// //////////////读取面板信息///////////////
    /// </summary>
    //用于存储UI面板路径
    private Dictionary<string, string> UIPathdictionary;

    //下面是数据结构
    //可序列化的
    [Serializable]
    public class UIInfo
    {
        public string panelType;
        public string panelPath;
    }
    class UIPanelTypeJson
    {
        //这个属性和JSON里面对应
        public List<UIInfo> panelsInfo;
    }

    private void LoadJson()
    {
        //将UI的信息存入字典
        UIPathdictionary = new Dictionary<string, string>();


        //注意这里要把JSON的名字读对了
        TextAsset textAsset = Resources.Load<TextAsset>("UIPanelsInfoJson");

        UIPanelTypeJson jsonObject = JsonUtility.FromJson<UIPanelTypeJson>(textAsset.text);

        foreach (UIInfo info in jsonObject.panelsInfo)
        {
            UIPathdictionary.Add(info.panelType, info.panelPath);
        }

    }

```

### 利用读取到的路径生成面板

```c#
    /// <summary>
    /// /////////////////////////////加载面板/////////////////////
    /// </summary>
    //用于存储真正的UI对象
    private Dictionary<string, BasePanel> UIPanelDictionary;
    private BasePanel getUIPanel(string UIType)
    {

        //如果存储字典不存在就实例化一个
        if (UIPanelDictionary == null)
        {
            UIPanelDictionary = new Dictionary<string, BasePanel>();
        }
        BasePanel panel;
        UIPanelDictionary.TryGetValue(UIType, out panel);

        if (panel == null)
        {
            //如果找不到，那么就找这个面板的prefab的路径，然后去根据prefab去实例化面板
            string UIPath;

            UIPathdictionary.TryGetValue(UIType, out UIPath);

            GameObject instPanel = GameObject.Instantiate(Resources.Load(UIPath)) as GameObject;

            //将获取到的面板放入Canvas下面
            Transform canvasTransform = GameObject.Find("Canvas").transform;
            instPanel.transform.SetParent(canvasTransform, false);

            //加入字典
            UIPanelDictionary.Add(UIType, instPanel.GetComponent<BasePanel>());
            return instPanel.GetComponent<BasePanel>();
        }
        else
        {
            return panel;
        }
    }

```

### 控制各个面板的栈

```c#
/// <summary>
    /// //////////////////控制面板的栈
    /// </summary>
    private Stack<BasePanel> panelStack;

    public void PushPanel(string panelType)
    {
        if (panelStack == null)
            panelStack = new Stack<BasePanel>();

        //判断一下栈里面是否有页面
        if (panelStack.Count > 0)
        {
            BasePanel topPanel = panelStack.Peek();
            topPanel.OnPause();
        }
        BasePanel panel = getUIPanel(panelType);
        panel.OnEnter();
        panelStack.Push(panel);
    }

    /// <summary>
    /// 出栈 ，把页面从界面上移除
    /// </summary>
    public void PopPanel()
    {
        if (panelStack == null)
            panelStack = new Stack<BasePanel>();

        if (panelStack.Count <= 0) return;

        //关闭栈顶页面的显示
        BasePanel topPanel = panelStack.Pop();
        topPanel.OnExit();

        //如果关闭之后，栈已经没有了就退出
        //如果还有，就继续执行之前的页面

        if (panelStack.Count <= 0) return;
        BasePanel topPanel2 = panelStack.Peek();
        topPanel2.OnResume();

    }

```





1. 建立各个面板，并加入prefab

2. 在Resources下建立**UIType**文件，这个是

   也就是说有什么面板就在这里面注册什么

   ```c#
   public enum UIType
   {
      主面板,
      任务面板
   }
   ```

   

3. 建立JSON来保存，各个面板的路径

   这个路径是从Resources开始作为根目录，这个是为了方便后续代码读取

   ```json
   {
       "msg":[
           {
               "panelType": "主面板",
               "panelPath": "UIPanels/主面板"
           },
           {
               "panelType": "任务面板",
               "panelPath": "UIPanels/任务面板"
           }
       ]
   }
   ```

4. 建立一个**UIINFO**，用来储存JSON里面的信息

   ```c#
   //可序列化的
   [Serializable]
   public class UIInfo
   {
       //UI信息的结构
       public UIType panelType;
       public string panelPath;
   }
   ```

5. 建立一个**UIController**的管理类

   ```c#
   public class UIController 
   {
       private Dictionary<UIType,string> UIdictionary;
   
       private static UIController _instance;
       //单例模式
       public static UIController Instance
       {
           get
            {
               if (_instance == null) {
                   _instance = new UIController();
               }
               return _instance;
   
           }
       }
   
       class UIInfoJSON 
       {
           public List<UIInfo> infoList;
       }
       [Serializable]
       class UIPanelTypeJson
       {
           public List<UIInfo> infoList;
       }
   
       private void loadUIInfo() {
           UIdictionary = new Dictionary<UIType, string>();
   
           TextAsset textAsset = Resources.Load<TextAsset>("UIType");
           UIPanelTypeJson jsonObject = JsonUtility.FromJson<UIPanelTypeJson>(textAsset.text);
   
           foreach (UIInfo info in jsonObject.infoList)
           {
               //Debug.Log(info.panelType);
               UIdictionary.Add(info.panelType, info.panelPath);
           }
   
       }
   }
   ```





## 编写各个面板的逻辑关系

### 主菜单打开各个子菜单

核心就是编写`onCilckPanel`

```c#
public class MainPanelManager : BasePanel
{
    private CanvasGroup canvasGroup;

    void Start()
    {
        canvasGroup = GetComponent<CanvasGroup>();
    }
    public override void OnPause()
    {
        canvasGroup.blocksRaycasts = false;//当弹出新的面板的时候，让主菜单面板 不再和鼠标交互
    }
    public override void OnResume()
    {
        canvasGroup.blocksRaycasts = true;
    }



    //当点击按钮的时候
    public void onCilckPanel(string panelType)
    {
        UIManager.Instance.PushPanel(panelType);
    }
}
```

然后在button组件中新增事件

<img src="J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812171308185.png" alt="image-20220812171308185" style="zoom:50%;" />

将MainPanel拖进来，因为MainPanel挂载了MainPanelManager脚本，因此可以直接调用这个脚本的onCilckPanel方法

![image-20220812171406270](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812171406270.png)





### 关闭按钮

以装备控制器为例：

需要CanvasGroup组件

```c#
public class EquipPanelManager : BasePanel
{
    private CanvasGroup canvasGroup;

    void Start()
    {
        canvasGroup = GetComponent<CanvasGroup>();
    }
    public void ColsePanel()
    {
        UIManager.Instance.PopPanel();
    }

    public override void OnExit()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        canvasGroup.alpha = 0;
        canvasGroup.blocksRaycasts = false;
    }

    public override void OnEnter()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        canvasGroup.alpha = 1;
        canvasGroup.blocksRaycasts = true;
    }
}

```

同样在关闭按钮上添加一个关闭组件，并且将EquipPanel拖进去，然后调用ColsePanel方法。

![image-20220812173648327](J:/0_我的项目备份/笔记/游戏开发/unity开发/img/unity脚本/image-20220812173648327.png)

## 编写总控制器

这个是用来开启UI框架的，需要游戏的总控制器来调用

```c#
public class GameManager : MonoBehaviour
{
    void Start()
    {
        UIManager.Instance.PushPanel("MainPanel");
    }

    void Update()
    {
        
    }
}

```

## UI组件的操作

对UI组件进行操作，需要用local

```c#
gameObject.transform.localPosition
```



## 酌情加入Do Tween

以EquipPanelManager为例

```c#
public class EquipPanelManager : BasePanel
{
    private CanvasGroup canvasGroup;

    void Start()
    {
        canvasGroup = GetComponent<CanvasGroup>();
    }
    public void ColsePanel()
    {
        UIManager.Instance.PopPanel();
    }

    public override void OnExit()
    {
        if (canvasGroup == null)
            canvasGroup = GetComponent<CanvasGroup>();
        //canvasGroup.alpha = 0;
        canvasGroup.blocksRaycasts = false;

        //退出后隐藏
        transform.DOLocalMoveX(600, .5f).OnComplete(() => canvasGroup.alpha = 0);
    }

    public override void OnEnter()
    {
        if (canvasGroup == null)
            canvasGroup = GetComponent<CanvasGroup>();
        canvasGroup.alpha = 1;
        canvasGroup.blocksRaycasts = true;

        //点击时平移
        Vector3 temp = transform.localPosition;
        temp.x = 600;
        transform.localPosition = temp;
        transform.DOLocalMoveX(0, .5f);
    }
}
```









15. 






# 代码模板（短）

## 判断2D物体的点击

物体需要挂载collider

```c#
    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            RaycastHit2D hit = Physics2D.Raycast(Camera.main.ScreenToWorldPoint(Input.mousePosition), Vector2.zero);

            if (hit.collider != null)
            {
                Debug.Log("点击");
            }
        }
    }
```



## 3D物体的点击

```c#
       if (Input.GetMouseButtonDown(0)) {
            //射线检测
            Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
            RaycastHit raycastHit;
            bool isCollider = Physics.Raycast(ray, out raycastHit, 100, LayerMask.GetMask("Cube"));
            if (isCollider)
            {
                raycastHit.collider.gameObject.SendMessage("BuildTurret", turret);
            }
        }
```





































# unity脚本运行的基本原理

unity脚本是创建一个类，但是并没有实例化，要想运行就必须实例化一个对象，这个对象的创建就是靠挂载到游戏对象完成的。把脚本拖到对象上时，系统自动创建一个对象，然后把引用返回给游戏对象，这时在inspector中就有了这个脚本。其实inspector中的那些组件和脚本都是对象的引用，Transform其实就是Transform类的对象，而挂载这些组件的游戏对象其实就是一个特殊的数组，里面存放着很多对象的引用，需要时会自动访问这些对象。

## 获取其他游戏对象

```C#
GameObject obj = GameObject.Find("女主抱胸_1");//Find方法需要传入一个url，可以找到场景下面的某个对象
SpriteRenderer renderer2  =  obj.GetComponent<SpriteRenderer>();
renderer2.flipY = true;
```









# 坐标与向量

```c#
transform.position = new Vector3(0, 1.0f, 0);//位置
transform.eulerAngles = new Vector3(0, 0, 45);//旋转，逆时针的
```

## 世界坐标和本地坐标

- 世界坐标：

  以世界坐标系计算

  ```c#
  transform.position = new Vector3(0, 1.0f, 0);
  transform.eulerAngles = new Vector3(0, 0, 45);//逆时针旋转45度
  ```

  

- 本地坐标：

  以父节点坐标系计算

  ```c#
  transform.localPosition = new Vector3(0, 1.0f, 0);
  transform.localEulerAngles = new Vector3(0, 0, 45);
  ```

## 向量长度

对向量使用.magnitude属性就可以了

```c#
.magnitude
```

## 向量单位化

把向量长度缩为1

（0，3）-》（0，1）

（2，2）-》（0.707，0.707）

```c#
var a = new Vector3(0, 0, 180);
var b = a.normalized;
Debug.Log("标准化：" + b.ToString("F3"));//转为字符串，保留三位小数  
```

## 标准向量

```c#
Vector3.up;//（0，1，0）
Vector3.right;//（1，0，0）
Vector3.left;//（-1，0，0）
Vector3.forward;//（0，0，1）
```

除此之外，在本地坐标系中，也有一些标准向量

```c#
transform.up;
transform.right;
```

等

## 向量点积和叉积

```c#
Vector3.Dot(a,b)
Vector3.Cross(a,b)
```

## 向量夹角

```c#
Vector3 a = new Vector3(2, 2, 0);
Vector3 b = new Vector3(-1, 3, 0);
float angle = Vector3.SignedAngle(b, a,Vector3.forward);//从a到b的角度，逆时针为正值，顺时针负值
float angle2 = Vector3.Angle(b, a);//只关心角度，不关心顺时针逆时针
Debug.Log(angle);
Debug.Log(angle2);

//-63
//63
```

## 屏幕坐标系

坐标原点在左下角



空间坐标：`Vector3 worldPos = transform.position`，指的是物体在世界空间中的坐标

屏幕坐标：`  Vector3 a = Camera.main.WorldToScreenPoint(worldPos);`，指的是物体在屏幕上的坐标

屏幕宽高，这个会根据实际屏幕动态变化 



```c#
Screen.width;
Screen.height;
```

 











# 组件



## Spring Joint 2D

弹簧关节

让一个刚体围绕另一个刚体作钟摆运动

## Ciecle Collider 2D

圆形2D碰撞



## LineRenderer

画线

```c#
lineRenderer = GetComponent<LineRenderer>();

//设置端点数
lineRenderer.SetVertexCount(LengthOfLineRenderer);


while (index < LengthOfLineRenderer)
{   
    //两点确定一条直线，所以我们依次绘制点就可以形成线段了
    lineRenderer.SetPosition(index, position);
    index++;
}

```



3. 





# 脚本执行优先级

点一个脚本，右上角有一个execution order

值越小，优先级越高





# 错误调试与输出

## print和Debug.Log()

print和Debug.Log()这两个是完全一样的，print不过是封装了一下而已。

```c#
print("hello world");
Debug.Log("hello world");
```

print实际上是MonoBehaviour内部封装的函数，在一般的函数里面无法调用。而Debug.Log则是unity的封装的模块。







# ctrl+k+f



# pivot的设置

1. 去sprite里面把pivot改成各自位置，也可以改成custom

# onmouse enter

这个东西可能会被其他游戏物体挡住。

这时候，可以在physics的设置里面把射线检测是否检测触发器给取消。

# 安卓操作

## 手指点击

```c#
void Update () {
		if (Input.GetMouseButtonDown(0))
		{
			Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
			RaycastHit hitinfo;
			if (Physics.Raycast(ray, out hitinfo))
			{
				//一根手指，并且刚刚开始按下
				if (Input.touchCount == 1 && Input.GetTouch(0).phase == TouchPhase.Began) 
				{
					//单击的代码

					if (Input.GetTouch(0).tapCount == 2) 
					{
						//双击的代码
					}
						
				}
			}
		}
	}
```









# 面试题

```c#
static int Test()
{
    int i=10;
    try
    {
        return i;
    }
    finally
    {
        i=11;
        Console.WriteLine($"i={i}")
    }
}
```

返回值是 10，因为返回了10.而打印的i是11.

这是因为要等finally执行完才能return















# 条件编译



```c#
#if XXX_XXX
#endif
```

在player settings——player中，找到scripting define symbols，然后输入宏即可





# 可视化调试

```
onDrawGizmos 
```



v键可以吸附顶点





# 旋转

Mathf.Clamp

```
transform.eulerAngle = new Vector(,,,,,)
```



















# 程序集

unity编译的时候

# PlayerPrefs存储

用注册表来存储

```c#
PlayerPrefs.SetInt("a",1);
PlayerPrefs.SetFloat("a",1);
PlayerPrefs.SetString("a",1);


PlayerPrefs.Save();
```



获取

```c#
PlayerPrefs.GetString("a",1);
```





# 创建游戏对象的三种方式

```c#
//1.使用构造函数
GameObject gameObject = new GameObject();

//2.根据预制体和游戏场景的对象实例化
public GameObject gameObject;

void Start()
{
    Instantiate(gameObject);
}


//3.创建基本物体
GameObject.CreatePrimitive(PrimitiveType.Capsule);
```







# 射线检测

[Raycast和Linecast都是Unity中用来进行碰撞检测的方法。它们的主要区别在于，Raycast需要设置起点、方向和距离来进行检测，而Linecast只需设置起点和终点，它会在这两个点之间进行检测](https://answers.unity.com/questions/848189/difference-between-linecast-and-raycast.html)[1](https://answers.unity.com/questions/848189/difference-between-linecast-and-raycast.html)。

例如，你可以使用Physics.Raycast方法从transform.position位置沿着transform.forward方向发射一条射线，并指定射线的长度为Mathf.Infinity：

```csharp
Ray ray = new Ray(transform.position, transform.forward);
RaycastHit hit;
if (Physics.Raycast(ray, out hit, Mathf.Infinity))
{
    // ...
}
```

你也可以使用Physics.Linecast方法在transform1.position和transform2.position之间进行碰撞检测：

```csharp
RaycastHit hit;
if (Physics.Linecast(transform1.position, transform2.position, out hit))
{
    // ...
}
```





[在Unity中，射线检测是用来检测碰撞体或触发器的。不带碰撞体的是检测不到的，不检测触发器要在物理设置里设置。可以使用Physics.Raycast方法进行射线检测](https://blog.csdn.net/qq_36251561/article/details/119174801)[1](https://blog.csdn.net/qq_36251561/article/details/119174801)。

例如，你可以创建一个射线并显示它：

```csharp
Ray ray = new Ray(transform.position, transform.forward);
RaycastHit hit;
if (Physics.Raycast(ray, out hit, Mathf.Infinity))
{
    if (hit.collider.gameObject.CompareTag("Obstacles"))
    {
        Debug.Log("检测到物体");
    }
}
```

[这段代码会创建一个从transform.position位置沿着transform.forward方向发射的射线，并使用Physics.Raycast方法进行碰撞检测。如果碰撞到了标签为"Obstacles"的物体，则输出"检测到物体"](https://blog.csdn.net/weixin_44809857/article/details/114364783)[2](https://blog.csdn.net/weixin_44809857/article/details/114364783)。

[你还可以使用多条射线组成扇形面来进行多个物体的检测](https://blog.csdn.net/weixin_44809857/article/details/114364783)[2](https://blog.csdn.net/weixin_44809857/article/details/114364783)。





# 多语言本地化

1. 在package manager中安装Localization

2. 来到project setting选择Localization，并创建一个

3. 点击Locale Generator ，选择创建的语言

4. 为了方便起见，可以创建一个文件夹Localization Settings放Localization，然后里面再一个文件夹放locale

5. 创建默认语言，选择Specific Locale Selector，然后选语言

6. Window—Asset Management—Localization Tables

7. 选择 new table collections，然后选String Table Collection，可以在Localization Settings文件夹里面新建一个文件夹Tables来存放这个

8. 为需要替换的文本挂载Localize String Event组件，或者也可以直接点TextMeshPro右上角小点，来选择Localize 

9. 确保update挂载了想要翻译的文本

   ![image-20230812143227889](img/Unity脚本/image-20230812143227889.png)

10. Table Collection选刚刚的table，String Reference里面查找一下刚才写的key
