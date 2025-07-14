# 编辑器

## 快捷键

|                   |                          |
| ----------------- | ------------------------ |
| F4                | 全屏                     |
| Ctrl+Enter        | 播放动画                 |
|                   |                          |
| v                 | 选择工具                 |
| Ctrl+b            | 把绘制对象变成形状，打散 |
| ctrl+g  / ctrl +b | 编组/取消编组            |
| Ctrl+Alt+Shift+r  | 打开标尺                 |
| Ctrl+F10          | 打开历史记录             |
|                   |                          |



## 基础知识



- 源文件格式：.fla
- 脚本语言：ActionScript



## 基本绘图

### 形状

如果两个图形属性都为形状，那么上面的图形会把下面的吞掉

如果两个图形颜色相同，那么会融合



## 原件

## 按钮

## 图形





## 引导层

1. 创建一个图层，右键点击引导层，将其转化为引导层
2. 在引导层中，用钢笔工具绘制路径，**注意不要转为原件，路径的属性必须是形状**。
3. 创建一个新的图层，在里面放入需要引导的东西。
4. 将这个图形的中心点在不同帧，分别放入到路径的首位
5. 给这个图形的图层创建传统补间。



## 遮罩层

1. 创建一个图层，里面绘制想要遮罩的图形。**注意如果有多个图形，那么必须保证其属性相同**。
2. 对这个图层右键，转化为遮罩层。
3. 之后把想要遮罩的图层拉到这个图层下面，就可以了

# ActionScript脚本

## 舞台的属性

| 属性                                    | 说明       |      |
| --------------------------------------- | ---------- | ---- |
| stage.stageWidth<br />stage.stageHeight | 舞台的长宽 |      |
|                                         |            |      |
|                                         |            |      |

是否还在舞台上面

```assembly
stage.contains($battleSystem.enemys[j])
```



## 元件的属性

| 属性               | 说明         |      |
| ------------------ | ------------ | ---- |
| x<br />y           | 在舞台的位置 |      |
| scaleX<br />scaleY | 缩放比例     |      |
|                    |              |      |

## 场景控制

| 方法                      | 参数         | 说明 |
| ------------------------- | ------------ | ---- |
| gotoAndStop(1 ,"场景 2"); | 帧数、场景数 |      |
|                           |              |      |
|                           |              |      |

## 文本



```typescript
var txt: TextField = new TextField();

// 位置
txt.x = 250;
txt.y = 250;

// 长宽
txt.width = 200;
txt.height = 50;

// 边框
txt.border = true;
txt.borderColor = 0xbbffcc;


// 文本内容
txt.text = "游戏规则：小猪吃到钱币就会长大"

//html本文
txt.htmlText = "AS3开发AS3开发AS3开发AS3开发AS3开发";

//在原基础上增加内容
txt.appendText("追加内容");

// 文字颜色
txt.textColor = 0x000000;

// 背景
txt.background = true;
txt.backgroundColor = 0xffffff;

// 可输入多行
txt.multiline = true;

// 是否自动换行
txt.wordWrap = true;

//透明
txt.alpha = 0.3;

stage.addChild(txt);
```





# 文本样式

```typescript
var style: TextFormat = new TextFormat();
//style.color = strColor;
//style.font = strFont; //设置字体啊

//是否加粗
style.bold  = true;

//字体
style.font = "黑体";

//文字排版样式
style.align = "center";

//字体大小
style.size = 20;

//行距
style.leading = 5;
//字间距
style.letterSpacing = 10; 

//首字缩进
style.indent = 50; 

//下划线
style.underline = true;

/**给文本设置   文本样式*/
txt.defaultTextFormat = style;
txt.setTextFormat(style);
```







## 元件之间互相访问

在元件内部写这个代码

```ts
var pig = this["parent"].pig;
pig.scaleX = 2;
pig.scaleY = 2;
this.stop();
```







![image-20211113163334057](G:\创作\笔记\设计\An\img\image-20211113163334057.png)



## 事件

- 进入帧

  ```javascript
  addEventListener(Event.ENTER_FRAME, fl_EnterFrameHandler);
  function fl_EnterFrameHandler(event:Event):void
  {}
  
  ```

  

```
var pig = this["parent"].pig;
```





file.removeEventListener(Event.COMPLETE, function(e:Event){
             completeHandler(e,参数)
           ;});





```
	var txt: TextField = new TextField();
	txt.htmlText = "<b style='font-size:36px'>AS3开发AS3开发AS3开发AS3开发AS3开发</b>";
	txt.y = 100;
	txt.textColor = 0xff0000; // 文字颜色
	txt.background = true;
	txt.backgroundColor = 0x00ff00;
	txt.height = 100;
	txt.multiline = true; // 可输入多行
	txt.type = TextFieldType.INPUT; // 文字类型
	txt.wordWrap = true; // 是否自动换行
	txt.appendText("追加内容");
	stage.addChild(txt);
```



# 类

1. 在项目根目录创建一个文件夹，名字假如为`script`
2. 在`script`目录创建一个脚本，名字为Person，也就是说，**文件名必须和类名一样**
3. 创建一个类，格式如下
4. 调用时，使用`import script.Person;`即可
5. 然后就可以new这个类了

```assembly
package cn.soft
{
    public class Person
    {
        private var _age:int; 
        private var _name:String;
        /*             getter and setter         */         public function get age():int{ 
            return this._age; 
        } 
        public function set age(value:int):void{ 
            if(value>=0){ //年龄必须大于0                 this._age=value ;
            } 
        }  
        public function get name():String{
            return this._name;
        }
        public function set name(value:String):void{
            if(value!=""){//名字不为空                 this._name=value;
            }
        }
        public function Person(age:String,name:String){//构造函数             this.age=age;
            this.name=name;
        }
    }
}
```

# 播放音乐

```typescript
var s:Sound = new Sound()
var req:URLRequest=new URLRequest("小猫猫.mp3")
s.load(req)
s.addEventListener(Event.COMPLETE, onSoundLoaded)
function onSoundLoaded(event:Event):void {
	trace("加载完毕！")
    s.play()
}
s.close()
 _sound.play(0, 3);//从0毫秒开始，重复3次

```

# 监听舞台

```typescript
stage.removeEventListener(MouseEvent.CLICK,  storyManager.storyMode)
stage.addEventListener(MouseEvent.CLICK, storyManager.battleMode);
```

```js
removeChild(moneys[i])//移除对象
stage.removeChild($battleSystem.enemys[i])
```

# 文本标签

```html
<font color='#bbffcc' >林西镇</font>
```











1. 文字mud类型

2. （）添加动画效果

3. 1. 白点

   2. 

   3. 手绘风格的女主设计

      
