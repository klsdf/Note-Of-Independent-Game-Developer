# unity特性（编辑器开发）

原文链接：https://blog.csdn.net/qq_35361471/article/details/84713382

## 编辑器相关文件夹介绍

Editor

- 该文件夹可以放在项目的任何文件夹下，可以有多个"Editor"文件夹。
- 编辑器扩展相关的脚本都要放在该文件夹内，该文件夹中的脚本只会对Unity编辑器起作用。
- 项目打包的时候，不会被打包到项目中。如果编辑器相关脚本不放在该文件夹中，打包项目可能会出错。比如Editor文件夹中的resource文件夹就不会被打包
- 如果非要有些编辑器相关脚本不放在该文件夹中，需要在该类的前后加上UNITY_EDITOR的宏定义



## Serializable和NonSerialized



system命名空间

Serializable可以序列化一个类或一个变量

NonSerialized可以反序列化一个变量

## SerializeField

展示私有变量

## HideInInspector

隐藏公有变量，不改变序列化属性

## Multiline

可以让string变量在监视板上多加几行。

## Space

用于在监视板上加空行

```c#
[Space(20)]
```



## RequireComponent



自动添加需要的组件。若已存在则不额外添加。这样脚本就可以安全的使用该组件。



```c#
[RequireComponent(typeof(TextAnimatorPlayer))]
public class TextController : MonoBehaviour{}
```

## Tooltip

给监视板的字段添加小贴士。及鼠标指向字段显示的提示。

## Range

## TextArea

让string在监视板上显示成带滚动条的文本域。

```c#
//默认显示3行，超出会有滚动条
[TextArea]

//最小2行，最多5行。超过会有滚动条
[TextArea(2,5)]
```



## AddComponentMenu

可以添加一个组件菜单项到编辑器里。

将一个类添加到Component菜单中

```c#
[AddComponentMenu("测试/test1")]
public class TextController : MonoBehaviour
{
    public int 第几篇;
    public int 第几章;
    public int 第几句;

    protected TextAnimatorPlayer animatorPlayer;
    protected TMP_Text tmp_text;
}

```



## ColorUsage

```c#
//是否开启alpha通道
//是否启用HDR，若为true则开启下面的
//最小，最大亮度
//最小，最大曝光
//
[ColorUsage(true, true, 0f, 8f, 0.125f, 3f)]
```



## Header

标题特性，给监视版加一个小标题。



## HelpURL



给类提供一个自定义文档URL。如图可以按Ctrl+鼠标左键跳转到目标。

## [Tooltip("")]




## CreateAssetMenu

可以在unity中右键，来创建一个自定义的assert

代码如下：
![](Pasted%20image%2020230207000906.png “而”)

```c#
[CreateAssetMenu(fileName = "DailogData", menuName = "Dialog/DailogData")]
```



## Delayed

用于float、int、或string变量，只有按了回车或焦点离开字段才会返回新值。





## DisallowMultipleComponent

用于MonoBehaviour或其子类，不能重复添加这个类的组件，重复添加会弹出对话框。

```c#
[DisallowMultipleComponent]
public class TextController : MonoBehaviour
{}
```



## [MenuItem]

[MenuItem(“MyTools/test1”,false,priority)]

- 第一个参数用来表示菜单的路径；

- 第二个参数用来判断是否是有效函数，是否需要显示；为false的话可以被显示，true的话，说明是有效函数，用来判断其他函数是否可以执行的

- 第三个参数priority是优先级，用来表示菜单按钮的先后顺序，默认值为1000。一般菜单中的**分栏**，数值相差大于10。也就是说一个分栏最多10个元素，若priority相差大于10，自动分栏。

- 注意需要是静态方法

  

例如:[MenuItem(“MyTools/test1”)]
也可以添加在Unity默认的菜单栏中，例如添加到Window菜单中，[MenuItem(“Window/test2”)]，添加到Assets下，[MenuItem(“Assets/Project中的按钮”)]



```c#
// [MenuItem("测试/test1")]，也可以直接省略后面的
//&s代表注册快捷键 alt+s
[MenuItem("测试/test1 &s", false, 1000)]
public static void Test1()
{
    Debug.Log("test1");
}

//因为1030和1000之间差了30，所以自动分栏了
[MenuItem("测试/test2", false, 1030)]
public static void Test2()
{

}
```



### 添加快捷键

| 符号               | 字符        |
| ------------------ | ----------- |
| %                  | Ctr/Command |
| #                  | Shift       |
| &                  | Alt         |
| LEFT/Right/UP/DOWN | 方向键      |
| F1-F2              | F功能键     |
| _g                 | 字母g       |

例如：[MenuItem(“MyTools/test1 %_q”)] 快捷键 Ctrl+Q



### 有效函数

```c#
   //DeleteValidate方法是MyToolDelete方法的有效函数，所以第二个参数为true。
    //该有效函数用来判断当前是否选择了对象，如果选择了，返回true，才可以执行MyToolDelete方法。
    [MenuItem("测试/删除选中物体", true)]
    private static bool DeleteValidate()
    {
        if (Selection.objects.Length > 0)
            return true;
        else
            Debug.Log("没有东西");
            return false;
    }

    [MenuItem("测试/删除选中物体", false)]
    private static void MyToolDelete()
    {
        //Selection.objects 返回场景或者Project中选择的多个对象
        foreach (Object item in Selection.objects)
        {
            //记录删除操作，允许撤销
            Undo.DestroyObjectImmediate(item);
        }
    }
```



### 修改组件的右键菜单



这样就可以为Transform组件添加额外的右键菜单

```c#
[MenuItem("CONTEXT/Transform/Test")]
private static void TransformTest()
{
    //TODO
    Debug.Log("我是额外的方法");
}
```



### 获取当前组件本身

通过这个方法可以直接执行某个脚本的方法，而不用运行游戏

```c#
[MenuItem("CONTEXT/SoundController/SoundTest")]
static void SoundTest(MenuCommand cmd)
{
    SoundController soundController = cmd.context as SoundController;
    soundController.PlayBGM_迷踪林();
}
```



## ContextMenu、ContextMenuItem

ContextMenu不需要放在Editor文件夹里面，同样也不需要using UnityEditor;

它可以放到普通的脚本中，为某个脚本添加**右键菜单**。

这个方法不能是静态方法

```c#
[ContextMenu("测试")]
public void Test()
{

}
```



ContextMenuItem可以为某个脚本的属性添加右键菜单。

```c#
[ContextMenuItem("菜单名称", "执行的函数")]
public float health;

private void 执行的函数()
{
       Debug.Log("执行！");
    //ToDo
}
```



```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
public class WindowTest : EditorWindow
{

    [MenuItem("Window/打开自定义窗口")]
    static void Init()
    {
        WindowTest window = (WindowTest)EditorWindow.GetWindow(typeof(WindowTest));
        window.Show();
    }

    private Texture m_MyTexture = null;
    private float m_MyFloat = 0.5f;
    void Awake()
    {
        Debug.LogFormat("窗口初始化时调用");
        m_MyTexture = AssetDatabase.LoadAssetAtPath<Texture>("Assets/unity1.png");
    }
    void OnGUI()
    {
        GUILayout.Label("Hello World!!", EditorStyles.boldLabel);
        m_MyFloat = EditorGUILayout.Slider("Slider", m_MyFloat, -5, 5);
        GUI.DrawTexture(new Rect(0, 30, 100, 100), m_MyTexture);
    }
    void OnDestroy()
    {
        Debug.LogFormat("窗口销毁时调用");
    }
    void OnFocus()
    {
        Debug.LogFormat("窗口拥有焦点时调用");
    }
    void OnHierarchyChange()
    {
        Debug.LogFormat("Hierarchy视图发生改变时调用");
    }
    void OnInspectorUpdate()
    {
        //Debug.LogFormat ("Inspector每帧更新");
    }
    void OnLostFocus()
    {
        Debug.LogFormat("失去焦点");
    }
    void OnProjectChange()
    {
        Debug.LogFormat("Project视图发生改变时调用");
    }
    void OnSelectionChange()
    {
        Debug.LogFormat("Hierarchy或者Project视图中选择一个对象时调用");
    }
    void Update()
    {
        //Debug.LogFormat ("每帧更新");
    }
}

```




如何判断越界

```c#
public class RoomController : MonoBehaviour
{
    public bool isActive=false;//房间是否被激活 

    private float speed = 50.0f;

    private Renderer renderer,parentRender;
    RectTransform rectTransform;
    RectTransform fatherRect;
    private void Awake()
    {
        renderer = GetComponent<Renderer>();
        parentRender = transform.parent.GetComponent<Renderer>();
        rectTransform = GetComponent<RectTransform>();
        fatherRect = transform.parent.GetComponent<RectTransform>();
    }

    void Start()
    {
        
    }


    void Update()
    {
        var x = Input.GetAxis("Horizontal");
       var y = Input.GetAxis("Vertical");
        transform.position += speed * Time.deltaTime * new Vector3(-x, -y, 0);

        //float left = renderer.bounds.min.x, parentLeft = parentRender.bounds.min.x;
        //float right = renderer.bounds.max.x ,parentRight = parentRender.bounds.max.x;
        //float up = renderer.bounds.max.y, parentUp  = parentRender.bounds.max.y;
        //float down = renderer.bounds.min.y, parentDown = parentRender.bounds.min.y;
        //Vector3[] corners = new Vector3[4];
        //rectTransform.GetWorldCorners(corners);


        //Vector3[] fathercorners = new Vector3[4];
        //fatherRect.GetWorldCorners(corners);

        //print(corners[0].x );


        //if (isActive == true && GameManager.Instance.storyMode == false)
        //{
        //    var x = Input.GetAxis("Horizontal");
        //    var y = Input.GetAxis("Vertical");

        //    if (left >= parentLeft && -x > 0   )
        //    {
        //        GameManager.Instance.PlayerMove(true);
        //        return;
        //    }

        //    if (up <= parentUp && -y < 0)
        //    {
        //        GameManager.Instance.PlayerMove(true);
        //        return;
        //    }
        //    if (right <= parentRight && -x < 0)
        //    {
        //        GameManager.Instance.PlayerMove(true);
        //        return;
        //    }
        //    if (down >= parentDown  && -y > 0)
        //    {
        //        GameManager.Instance.PlayerMove(true);
        //        return;
        //    }

        //    GameManager.Instance.PlayerMove(false);

        //    //if (right > parentRight && left < parentLeft && up > parentUp && down < parentDown)
        //    //{
        //    transform.position += speed * Time.deltaTime * new Vector3(-x, -y, 0);
        //    //}


        //    //print(right > parentRight);
        //}



    }
}

```



# 自定义inspector面板







# Gizmos可视化辅助

Gizmos能且只能在MonoBehaviour相关子类中，使用特定的函数调用，其中：

**OnDrawGizmos()** 在每帧调佣。所有在OnDrawGizmos中的渲染都是可见的。

**OnDrawGizmosSelected()** 仅在脚本附加的物体被选择时调用。

```c#
private void OnDrawGizmos()
{
    //Gizmos.color作为全局的静态变量，
    //为了防止这里的color修改会对其他地方的绘制造成影响，
    //所以在绘制完Gizmos的时候，将Gizmos.color修改为原先的值。
    var color = Gizmos.color;
    Gizmos.color = Color.red;
    Gizmos.DrawCube(transform.position, Vector3.one);
    Gizmos.color = color;
}

private void OnDrawGizmosSelected()
{
    Gizmos.color = Color.blue;
    Gizmos.DrawCube(transform.position, Vector3.one);
}
```



## 在Editor中单独控制





如果脚本过多，想要控制每个脚本的Gizmos就会很困难。

因此，可以用特性，将Gizmos单独控制。这个脚本需要放到Editor里面。



SoundController是指所有挂载了SoundController的脚本都会执行DrawGizmosTest。

```c#
    //表示物体被激活并且被选中时，激活Gizmos
    [DrawGizmo(GizmoType.Active|GizmoType.Selected)]
    private static void DrawGizmosTest(SoundController soundController,GizmoType gizmoType)
    {
        var color = Gizmos.color;
        Gizmos.color = Color.red;
        Gizmos.DrawCube(soundController.transform.position, Vector3.one);
        Gizmos.color = color;
    }
```

## Gizmos绘制种类

| GizmosType      | 描述                               |
| --------------- | ---------------------------------- |
| Active          | 如果激活，则绘制                   |
| SelectedOrChild | 如果被选择或者选择子物体时，则绘制 |
| NotSelected     | 如果全没选择，则绘制               |
| Selected        | 如果选择，则绘制                   |
| Pickable        | 在编辑器中gizmo可以被点选          |





## 常用Gizmos的方法

```c#
Gizmos.DrawCube() 绘制实体立方体
Gizmos.DrawWireCube() 绘制立方体边框
Gizmos.DrawRay() 绘制射线
Gizmos.DrawLine() 绘制直线
Gizmos.DrawIcon() 绘制Icon,Icon素材需要放在Gizmos文件夹中,填name的时候要加后缀名
Gizmos.DrawFrustum() 绘制摄像机视椎体的视野范围
```



## 在scene中一直保持摄像机视野



放到任意类下面即可

```c#
private Camera mainCamera;

    private void OnDrawGizmos()
    {
        if(mainCamera == null)
            mainCamera = Camera.main;
        Gizmos.color = Color.green;
        //设置gizmos的矩阵   
        Gizmos.matrix = Matrix4x4.TRS(mainCamera.transform.position, mainCamera.transform.rotation, Vector3.one);
        Gizmos.DrawFrustum(Vector3.zero, mainCamera.fieldOfView, mainCamera.farClipPlane, mainCamera.nearClipPlane, mainCamera.aspect);
    }

```

