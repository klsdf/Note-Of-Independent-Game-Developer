## 鼠标中键控制画面（2D）

直接拖到摄像机上即可

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// 用于2D游戏中鼠标中键控制画面移动和缩放
/// </summary>
public class ViewController : MonoBehaviour
{
    Vector3 lastMousePosition;
    Vector3 nowMousePosition;
    bool isMouseDown;

    private Camera camera;

    void Start()
    {
        isMouseDown = false;
        camera = GetComponent<Camera>();
    }

    void Update()
    {
        if (Input.GetMouseButtonDown(2))
        {
            isMouseDown = true;
        }
        if (Input.GetMouseButtonUp(2))
        {
            isMouseDown = false;
            lastMousePosition = Vector3.zero;
        }
        if (isMouseDown)
        {
            nowMousePosition = Input.mousePosition;

            if (lastMousePosition != Vector3.zero)
            {
                Vector3 offset = nowMousePosition - lastMousePosition;
                transform.position = transform.position - offset * 0.05f;


            }
            lastMousePosition = nowMousePosition;
          
        }
        float m = Input.GetAxis("Mouse ScrollWheel");
        camera.orthographicSize += -m;

    }
}

```



## 鼠标中键拖动画面（3D）

直接挂载到摄像机上面即可

```c#
        if (Input.GetMouseButtonDown(2))
        {
            isMouseDown = true;
        }
        if (Input.GetMouseButtonUp(2))
        {
            isMouseDown = false;
            lastMousePosition = Vector3.zero;
        }
        if (isMouseDown)
        {
            nowMousePosition = Input.mousePosition;
      
            if (lastMousePosition != Vector3.zero)
            {
                Vector3 offset = nowMousePosition - lastMousePosition;
                //  print("offset:  " + offset);
                float temp;
                temp = offset.y;
                offset.y = offset.z;
                offset.z = temp;
                transform.position = transform.position - offset * 0.05f;

                // print("相机位置:  "+transform.position);

            }
            lastMousePosition = nowMousePosition;
            //lastMousePosition = Camera.main.ScreenToWorldPoint(Input.mousePosition);   //世界坐标系转换为屏幕坐标系
        }
    
```











# 物体的移动

Space.Self是指沿着自己的坐标系运动

```c#
 transform.Translate(0, 0.01f, 0,Space.Self);//自身坐标系
 transform.Translate(0, 0.01f, 0,Space.World);//世界坐标系
//或者
this.transform.Translate(0, 0.01f, 0);
```



## 匀速运动 

如果执行时间短，那么走得近，时间长走得远 

```c#
float step = 0.01f * Time.deltaTime;
transform.Translate(0, step, 0,Space.Self);
```

## 掉头运动

```c#
if (transform.position.y > 5) 
{
    transform.localEulerAngles = new Vector3(0, 0, 180);
}
if (transform.position.y < -5)
{
    transform.localEulerAngles = new Vector3(0, 0, 0);
}
float step = 10.0f * Time.deltaTime;
transform.Translate(0, step, 0, Space.Self);
```

## 转向某个物体 

```c#
//获取自身到目标对象的方向向量
Vector3 direction = GameObject.Find("target").transform.position-this.transform.position;

//计算自身方向转到这个方向需要多少角度
float degree = Vector3.SignedAngle(this.transform.up, direction,Vector3.forward);

//将自身角度转过去
this.transform.Rotate(0, 0, degree);
```









# 人物的移动

使用刚体移动

```c#
 void Update()
    {
     
     //其中，`transform.position`是玩家自身的位置，targetPosition是目标位置，后面那个是插值，也就是每次移动多少。moveSmooth可以设置为100


        rigid.MovePosition(Vector2.Lerp(transform.position, targetPosition, moveSmooth * Time.deltaTime));


        float x=  Input.GetAxisRaw("Horizontal");
        float y = Input.GetAxisRaw("Vertical");

        if (x != 0 || y != 0) {

            //射线检测
            collider.enabled = false;
            RaycastHit2D hitTest = Physics2D.Linecast(targetPosition,targetPosition+new Vector2(x,y));
            collider.enabled = true;

            if (hitTest.transform == null)
            {
                targetPosition += new Vector2(x, y);
            }
            else {
                switch (hitTest.collider.tag)
                {
                    case "fence":
                        hitTest.collider.SendMessage("getDamage");
                        animator.SetTrigger("attack");
                        break;
                    case "wall":

                        break;
                    case "food":
                        targetPosition += new Vector2(x, y);
                        break;
                }
            }
            freezingTime = 0;



            //敌人行动
            //GameObject.Find("Enemy1(Clone)").SendMessage("Action");
            GameObject[] enemys = GameObject.FindGameObjectsWithTag("enemy");
            foreach (GameObject enemy in enemys) { 
                enemy.SendMessage("Action");
            }
        }
    }
```











# 2D横板跳跃

1. 给底下木板设置刚体和碰撞器

2. 人物设置刚体和碰撞器

3. 代码

   ```c#
   public float jumpForce;
   private void Update()
   {
       if(Input.GetMouseButtonDown(0))
       {
           GetConent<Rigidbody2D>().velocity = Vector2.up * jumpForce;
       }
   }
   ```

   





# 2D ARPG人物控制器

```c#
 void FixedUpdate() {
        float horizontal = Input.GetAxis("Horizontal");//水平方向
        float vertical = Input.GetAxis("Vertical");//垂直方向
        //print(horizontal);

        Animator animator = GetComponent<Animator>();
        move = new Vector2(horizontal,vertical);
        if (!Mathf.Approximately(move.x, 0) || !Mathf.Approximately(move.y, 0)) 
        {
            animator.SetFloat("Speed", move.magnitude);
            //print(move.magnitude);
        }


        move.Normalize();
        animator.SetFloat("Look X", move.x);
        animator.SetFloat("Look Y", move.y);

        float speed = 5.0f;

        Vector2 position = transform.position;
        //position += speed * move * Time.deltaTime;
        position.x += Time.deltaTime * horizontal * speed;
        position.y += Time.deltaTime * vertical * speed;
        //transform.position = position;
        rigidbody2D.MovePosition(position);//防止抖动


  
 }
```



# 人物一步一步移动

创建一个子对象，用子对象移动，每次人物靠近子对象即可

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterController : MonoBehaviour
{
   private  Vector3 targetPosition;

    [Range(1,20)]
    public float speed;
    

    void Start()
    {
        targetPosition = transform.position;
    }
    void Update()
    {
        float x =  Input.GetAxisRaw("Horizontal");
        float y = Input.GetAxisRaw("Vertical");

        if (Vector3.Distance(transform.position, targetPosition) < 0.01f)
        {
            if (x != 0 || y != 0)
            {
                targetPosition += new Vector3(x, y, 0);
            }
        }

       
           

       transform.position  =  Vector3.MoveTowards(transform.position,targetPosition,speed*Time.deltaTime);
    }
}

```





# 物体的查找与获取



- 通过游戏物体的名字查找

  ```c#
  GameObject mainCameraGo= GameObject.Find("Main Camera");
  ```

- 通过游戏标签查找

  ```c#
  GameObject mainCameraGo = GameObject.FindGameObjectWithTag("MainCamera");
  ```

- 通过**组件类型**进行查找

  ```c#
  No2_EventFunction no2_EventFunction= GameObject.FindObjectOfType<No2_EventFunction>();
  ```

- 通过标签查找多个

  ```c#
  GameObject[] enemyGos= GameObject.FindGameObjectsWithTag("Enemy");
  for (int i = 0; i < enemyGos.Length; i++)
  {
      Debug.Log("查找到的敌人游戏物体名称是："+enemyGos[i].name);
  }
  ```

- 通过组件类型查找多个

  ```c#
  BoxCollider[] colliders= GameObject.FindObjectsOfType<BoxCollider>();
  for (int i = 0; i < colliders.Length; i++)
  {
      Debug.Log("查找到的敌人碰撞器名称是：" + colliders[i].name);
  }
  ```

  





# 2D世界屏幕坐标转世界坐标

```c#
Vector3 mouseWorldPosition = Camera.main.ScreenToWorldPoint(Input.mousePosition);
mouseWorldPosition.z = 0f;
```





# 2D俯视角射击

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterController : MonoBehaviour
{

    public GameObject bullet;

    private float speed = 10.0f;

    void Start()
    {
        
    }


    void Update()
    {
        float x = Input.GetAxis("Horizontal");
        float y = Input.GetAxis("Vertical");
        transform.Translate(new Vector3(x,y)*Time.deltaTime* speed);

        if (Input.GetMouseButtonDown(0))
        {
            Shoot();
        }
    }


    //开枪
    void Shoot() 
    {
        GameObject tempBullet = Instantiate(bullet, transform.position, Quaternion.identity);
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        tempBullet.GetComponent<BulletController>().SetMoveDirecion(mousePos - transform.position);
    }
}

```





```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletController : MonoBehaviour
{
    private float speed=10f;

    public Vector2 moveDirection;

    void Start()
    {
        Destroy(gameObject, 3f);

    }


    void Update()
    {
        transform.Translate(moveDirection*Time.deltaTime*speed);
    }

    public void SetMoveDirecion(Vector2 direction)
    {
     
        moveDirection = direction.normalized;
  
    }
}

```



# 物体移动的7种方法

- 匀速直线运动

  ```c#
  public class test : MonoBehaviour
  {
      public float speed;
      void Update()
      {
          gameObject.transform.Translate(Vector3.right*speed*Time.deltaTime);
      }
  }
  
  ```

- 变速运动，lerp插值法

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          gameObject.transform.position = 	Vector3.Lerp(transform.position,targetPosition,0.1f);
      }
  }
  
  ```

- 匀速运动，lerp插值法

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          var t = 1 /( (transform.position - targetPosition).magnitude);
          gameObject.transform.position = Vector3.Lerp(transform.position,targetPosition, t*0.001f);
      }
  }
  
  ```

  

- 变速运动，SmoothDamp

  ```c#
  public class test : MonoBehaviour
  {
      private Vector3 refSpeed;//用来接受传出的速度
      private Vector3 targetPosition = new Vector3(3,0,0);
  
      void Update()
      {
          gameObject.transform.position = Vector3.SmoothDamp(transform.position, targetPosition, ref refSpeed, 1);
         }
  }
  ```

- 刚体运动，匀速直线运动

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
          rigidbody2D.velocity = new Vector2(1,0);
      }
  }
  ```

- 匀加速直线运动，刚体一直受力

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
        
      }
  
      private void FixedUpdate()
      {
          rigidbody2D.AddForce(new Vector2(0.01f*Time.deltaTime, 0));
      }
  
  }
  
  ```

- 匀速运动，刚体的MovePosition

  ```c#
  public class test : MonoBehaviour
  {
      Rigidbody2D rigidbody2D;
  
      private void Start()
      {
          rigidbody2D = GetComponent<Rigidbody2D>();
        
      }
  
      private void FixedUpdate()
      {
          rigidbody2D.MovePosition(transform.position+ Vector3.right*Time.deltaTime);
      }
  
  }
  
  ```

  









# 2D俯视角射击模板

```c#

public class MonsterController : MonoBehaviour
{

    public GameObject player;




    private float speed = 2f;

    // Start is called before the first frame update
    void Start()
    {
        player = GameObject.Find("主角");
    }

    // Update is called once per frame
    void Update()
    {
        Vector2 direction = (player.transform.position - transform.position).normalized;
        transform.Translate(direction * Time.deltaTime * speed);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        Destroy(gameObject);
        Destroy(collision.gameObject);
        print("ok");
    }
}

```

# 存储系统

```c#
using UnityEngine;

//二进制头文件
using System.Runtime.Serialization.Formatters.Binary;
using System.IO;



//XML头文件
using System.Xml;

//JSON头文件
using LitJson;

/// <summary>
/// 存储类，具体需要存储的数据需要玩家来自定义
/// </summary>

[System.Serializable]
public class SaveData
{
    public int testData;
}



public class SaveSystem : MonoBehaviour
{
    //存储文件的位置
    private string saveFilePath;

    private void Start()
    {
        saveFilePath = Application.dataPath + "/Save" + "/save.txt";
    }

    public int testData = 0;

    /// <summary>
    /// 从游戏中获得存储信息，并创建存储对象
    /// </summary>
    /// <returns>存储对象</returns>
    private SaveData GetGameData()
    {
        SaveData saveData = new SaveData();
        saveData.testData = testData;

        return saveData;
    }


    /// <summary>
    /// 将某个存储对象的数据加载到游戏中
    /// </summary>
    private void SetGameData(SaveData saveData)
    {
        testData = saveData.testData;
        print("获得数据！"+saveData.testData);
    }



    /// <summary>
    /// 使用二进制方式来存储游戏
    /// </summary>
    public void SaveByBin()
    {
        //获得游戏数据
        SaveData saveData = GetGameData();


        //创建一个二进制格式化程序
        BinaryFormatter bf = new BinaryFormatter();

        //创建一个文件流
        FileStream fileStream = File.Create(saveFilePath);

        //用二进制格式化程序的序列化方法来序列化Save对象,参数：创建的文件流和需要序列化的对象
        bf.Serialize(fileStream, saveData);
        //关闭流
        fileStream.Close();

        //如果文件存在，则显示保存成功
        if (File.Exists(saveFilePath))
        {
           print("保存成功");
        }
    }
    public void LoadByBin()
    {
        if (File.Exists(saveFilePath))
        {
            //反序列化过程
            //创建一个二进制格式化程序
            BinaryFormatter bf = new BinaryFormatter();
            //打开一个文件流
            FileStream fileStream = File.Open(saveFilePath, FileMode.Open);
            //调用格式化程序的反序列化方法，将文件流转换为一个Save对象
            SaveData save = (SaveData)bf.Deserialize(fileStream);
            //关闭文件流
            fileStream.Close();

            SetGameData(save);//重置存档

        }
        else
        {
            print("存档文件不存在");
        }

    }




    /// <summary>
    /// 使用XML的方式来保存游戏
    /// </summary>
    public void SaveByXML()
    {
        SaveData saveData = GetGameData();

        XmlDocument xmlDoc = new XmlDocument();//创建XML文档
        XmlElement root = xmlDoc.CreateElement("save");//创建根节点
        root.SetAttribute("name", "saveFile1");//设置根节点中的属性


        //创建具体的存储数据
        XmlElement testData = xmlDoc.CreateElement("testData");
        testData.InnerText = saveData.testData.ToString();

        root.AppendChild(testData);
        xmlDoc.AppendChild(root);

        xmlDoc.Save(saveFilePath);//保存

        if (File.Exists(saveFilePath))
        {
            print("保存成功");
        }

    }


    public void LoadByXml()
    {
        if (File.Exists(saveFilePath))
        {
            SaveData save = new SaveData();
            //加载XML文档
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load(saveFilePath);
            XmlNodeList testData = xmlDoc.GetElementsByTagName("testData");
            //save.testData= testData
            save.testData  = int.Parse( testData[0].InnerText);
            SetGameData(save);
        }
        else
        {
            print("存档文件不存在");
        }

    }


    public void SaveByJson()
    {
        SaveData save = GetGameData();
      
        //利用JsonMapper将save对象转换为Json格式的字符串
        string saveJsonStr = JsonMapper.ToJson(save);
        //将这个字符串写入到文件中
        //创建一个StreamWriter，并将字符串写入文件中
        StreamWriter sw = new StreamWriter(saveFilePath);
        sw.Write(saveJsonStr);
        //关闭StreamWriter
        sw.Close();

       print("保存成功");
    }

    public void LoadByJson()
    {
       
        if (File.Exists(saveFilePath))
        {
            //创建一个StreamReader，用来读取流
            StreamReader sr = new StreamReader(saveFilePath);
            //将读取到的流赋值给jsonStr
            string jsonStr = sr.ReadToEnd();
            //关闭
            sr.Close();

            //将字符串jsonStr转换为Save对象
            SaveData save = JsonMapper.ToObject<SaveData>(jsonStr);
            SetGameData(save);
            print("保存成功");
        }
        else
        {
            print("存档文件不存在");
        }
    }

}


```



# 视角晃动

```c#
using UnityEngine;
using System.Collections;

public class ShakeView : MonoBehaviour
{
    // 震动标志位
    private bool isshakeCamera = false;

    // 震动幅度
    public float shakeLevel = 3f;
    // 震动时间
    public float setShakeTime = 0.2f;
    // 震动的FPS
    public float shakeFps = 45f;

    private float fps;
    private float shakeTime = 0.0f;
    private float frameTime = 0.0f;
    private float shakeDelta = 0.005f;
    private Camera selfCamera;

    private Rect changeRect;

    void Awake()
    {
        selfCamera = GetComponent<Camera>();
        changeRect = new Rect(0.0f, 0.0f, 1.0f, 1.0f);
    }

    // Use this for initialization
    void Start()
    {
        shakeTime = setShakeTime;
        fps = shakeFps;
        frameTime = 0.03f;
        shakeDelta = 0.005f;
    }

    // Update is called once per frame
    void Update()
    {
        if (isshakeCamera)
        {
            if (shakeTime > 0)
            {
                shakeTime -= Time.deltaTime;
                if (shakeTime <= 0)
                {
                    changeRect.xMin = 0.0f;
                    changeRect.yMin = 0.0f;
                    selfCamera.rect = changeRect;
                    isshakeCamera = false;
                    shakeTime = setShakeTime;
                    fps = shakeFps;
                    frameTime = 0.03f;
                    shakeDelta = 0.005f;
                }
                else
                {
                    frameTime += Time.deltaTime;

                    if (frameTime > 1.0 / fps)
                    {
                        frameTime = 0;
                        changeRect.xMin = shakeDelta * (-1.0f + shakeLevel * Random.value);
                        changeRect.yMin = shakeDelta * (-1.0f + shakeLevel * Random.value);
                        selfCamera.rect = changeRect;
                    }
                }
            }
        }
    }

    public void shake()
    {
        isshakeCamera = true;
    }
}
}

```





# 设计模式

## 单例模式



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

## 状态模式



```

```



## 观察者模式

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





接下来来设计一个更加同样的





## 组合模式

## 发布者订阅者模式

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



## 享元模式





# MVC架构





# UI框架



BasePanel，所有面板的基类

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


abstract public class BasePanel : MonoBehaviour
{
    public abstract void OnEnter();
    public abstract void OnExit();

    public abstract void OnPause();


    public abstract void OnContinue();
}
```



UISystem，用来控制面板的pop，push等

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public enum PanelType
{
    ItemPanel
}



public class UISystem
{

    private static UISystem instance;
    public static UISystem Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new UISystem();
            }
            return instance;
        }
    }

    private Stack<BasePanel> panels = new Stack<BasePanel>() { };



    public void PopPanel()
    {
        BasePanel temp = PeekPanel();
        temp.OnExit();
        panels.Pop();


    }
    public void PushPanel(BasePanel panel)
    {
        BasePanel tempPanel = PeekPanel();
         tempPanel?.OnPause();
 


        panels.Push(panel);
        panel.OnEnter();
    }

    public BasePanel PeekPanel()
    {
        if (panels.Count == 0)
        {
            return null;
        }
        return panels.Peek();
    }

    public void PauseGame()
    {
        Time.timeScale = 0;
    }
}

```





普通的面板

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class WinPanel : BasePanel
{
    public override void OnExit()
    {

    }

    public override void OnEnter()
    {
        gameObject.SetActive(true);
        

    }

    public override void OnPause()
    {

    }

    public override void OnContinue()
    {

    }


    public void NextLevel()
    {

    



    }
    public void GoBackToTitle()
    {
        SceneManager.LoadScene(0);
    }

}

```



# 流星滑落

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.EventSystems;


public class StartGame : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{


    private RectTransform rectTransform;
    private TMP_Text tmpText;

    private Vector2 direction;
    private float speed;


    private bool isPointerIn;


    private void Awake()
    {
        tmpText = GetComponent<TMP_Text>();

        rectTransform = GetComponent<RectTransform>();
    }
    void Start()
    {

        
        switch (Random.Range(0, 1))
        {
            case 0:
                //流星
                //direction = Random.insideUnitCircle.normalized;
                direction =new Vector2(-1,-1).normalized;
                speed = Random.Range(30, 100);
                tmpText.fontSize = 40-speed/10;
                break;
        }
     


    }






    // Update is called once per frame
    void Update()
    {
        if (isPointerIn == true)
        {
            return;
        }

        Vector3 worldPos = rectTransform.transform.position;
        float leftX = worldPos.x - rectTransform.sizeDelta.x / 2;
        float rightX = worldPos.x + rectTransform.sizeDelta.x / 2;
        float upY = worldPos.y + rectTransform.sizeDelta.y / 2;
        float downY = worldPos.y - rectTransform.sizeDelta.y / 2;

        //超出了屏幕范围的时候
        if (leftX < 0|| downY<0)
        {
            transform.position = new Vector3(Screen.width, Screen.height, 0);

        }
        transform.Translate(direction * Time.deltaTime* speed, Space.World);
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        print("ok");


    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        isPointerIn = true;
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        isPointerIn = false;
    }
}

```

