



## 事件数据的前世今生

RPG Maker MV的核心就是各种事件，而这些事件对象是不能直接被访问到的。实际上你在地图编辑器里面写的事件，这些数据都会被存到data文件夹下的Map00X.json中。而这些json文件最后都会被DataManager转换为dataMap对象。我们所写的这些事件数据就会被转换为$dataMap.events。

但是这还没有完，\$dataMap只是储存了初始化的地图数据，游戏中真正所需要处理的数据应该是 $gameMap 对象。\$gameMap对象在初始化的过程中会不断访问 \$dataMap的数据，最终形成一个实实在在管理游戏地图的对象。

我们的事件就被存放在$gameMap._events中。但是正如我所说，\$gameMap的数据才是真数据。

比如说，修改游戏事件的坐标，

```javascript
$gameMap._events[1]._x+=2
```



$gameMap._events[1] = new Game_Event($gameMap._mapId, 1);







## 设置事件位置

### 获取位置

```javascript
$gameMap._events[this._eventId]._x //x坐标
$gameMap._events[this._eventId]._y //y坐标
```



### 事件移动

事件的`._x`属性代表事件的当前的**绝对位置**，这个属性和\$dataMap.events的属性是对应的。也就是理论上的位置。

但是我们的事件不可能一直不动啊，比如npc移动什么的，位置会经常改变，那么就需要一个描述实际位置的坐标，那就是`._realX`。如果直接修改`._realX`之后，这个事件会缓慢地滑到绝对位置，很有趣。

所以说如果我们想让一个事件对象移动，**请直接修改`._x`属性**！！！！只有这样才能真真正正改变对象的位置。

同样的，官方的指定位置都是整数，**但是通过代码的话，可以进行小数位的移动！**这样子你的移动会相当丝滑。

### 事件瞬移

原理很简单，`._x`是绝对位置，`._realX`是临时位置。`._realX`会一直向绝对位置移动，如果两个同时改变的话，那么就不会发生移动了，相当于瞬移。

```javascript
//向右瞬移2单位
$gameMap._events[this._eventId]._x+=2
$gameMap._events[this._eventId]._realX+=2
```



### 官方源码解读

官方的代码还是很复杂的。这个源代码在rpg_objects.js中，由Game_Interpreter实现，代码编号为203。

首先我们要知道官方提供的功能都有什么。打开事件编辑器，进入设定事件位置这个命令，可以看到有这么几个参数：

1. 事件：指定事件的ID
2. 位置：指定把事件移动到哪里
3. 方向，事件的方向

接下来我们看代码。

```javascript
// Set Event Location
Game_Interpreter.prototype.command203 = function() {
 		//获取参数列表的第一项作为事件对象，这个参数保存着事件ID
    var character = this.character(this._params[0]);
    if (character) {
      //如果._params[1]的参数为0，就代表直接指定位置，直接更改坐标
        if (this._params[1] === 0) {  
            character.locate(this._params[2], this._params[3]);
        } else if (this._params[1] === 1) {  //为1的话说明是参数指定位置，先获取参数再更改坐标。
            var x = $gameVariables.value(this._params[2]);
            var y = $gameVariables.value(this._params[3]);
            character.locate(x, y);
        } else {  // 与其他事件交换位置
            var character2 = this.character(this._params[2]);
            if (character2) {
                character.swap(character2);
            }
        }
        if (this._params[4] > 0) {
            character.setDirection(this._params[4]);
        }
    }
    return true;
};
```

官方获取了参数列表的第一项，然后又赋值给了character变量什么什么的。这都是啥？？？？？我为了看懂这个真的可以说看了整整两天，具体细节我就不多说了，说重点。这个参数就是该地图Map00X.json中，events中代码为203的该事件的参数。

比如说

```json
{"code":203,"indent":0,"parameters":[0,0,24,34,0]}, //直接指定
{"code":203,"indent":0,"parameters":[0,1,3,5,0]}, //变量指定
```

这个203就代表了设置事件位置这个功能，后面那个parameters就是参数列表。

1. 第一个参数为0就代表本事件，为3就代表3号事件，以此类推。
2. 第二个参数代表是否使用变量指定，如果为0就代表直接指定，坐标为(24,23)。如果为1就代表变量指定，后面两个就是变量的ID。比如下面这个就是指定3号和5号变量作为坐标。
3. 最后一个就是方向。

## 设置事件的移动路线和状态

直接把脚本写在事件里面，或者先获取事件ID再访问事件对象，这两种都可以。核心就是找到事件对象就行。

下面以插件的格式为例，展示如何在脚本中控制NPC移动路线。











## 事件触发

我并没有找到真正的触发器的实现原理，但是找到了这个。

```javascript
$gameMap._events[11].isCollidedWithCharacters(32,35)
```

如果玩家在(32,35)的坐标的话，那么就会返回true



```javascript
$gameMap._events[11].isCollidedWithEvents(32,35)
```

如果某个事件到了这个(32,35)的位置就会返回true。

​           

```javascript
$gameMap._events[11].isCollidedWithPlayerCharacters(32,35)
```

这个也是判断玩家是否到达某一个位置，目前我还没有搞清楚和上面的区别。

## 事件是否靠近玩家

可以用来设置一些简单的AI

```javascript
Game_Event.prototype.isNearThePlayer = function() {
    var sx = Math.abs(this.deltaXFrom($gamePlayer.x));
    var sy = Math.abs(this.deltaYFrom($gamePlayer.y));
    return sx + sy < 20;
};
```



### 动态加载公共事件

在游戏中，可能经常需要加载一些公共事件，虽然可以用编辑器来实现，但是未免过于麻烦，所以我们可以通过代码来实现。

直接在事件编辑器中写。

```js
this.setupChild($dataCommonEvents[53].list, 0)
```

这句代码的意思就是说，把53号公共事件的所有事件都加载并且执行，并且把该事件插入到0号位置，这样可以防止事件被多次执行。







































## 物品相关*

## 查看物品信息

- 数量

```javascript
$gameParty._items[1]   
//查看队伍内1号物品的数量
```

- 名称

```javascript
$dataItems[1].name
//第一个物品的名称
```

- 价格

```javascript
$dataItems[1].price
```

- 物品类型

1代表普通物品

2代表重要物品

3代表隐藏物品A

4代表隐藏物品B

```javascript
$dataItems[1].itypeId
```

















# 插件速查

## MV官方插件

### AltMenuScreen.js

转换菜单模式

开启后，菜单会变成横板模式

开启前：

<img src="img\image-20201213180407905.png" alt="image-20201213180407905" style="zoom:67%;" />

开启后：

<img src="img\image-20201213180441930.png" alt="image-20201213180441930" style="zoom:67%;" />





### AltSaveScreen.js

转换存档界面

开启前：

<img src="G:\创作\笔记\游戏开发\RPGMakerMV开发\MV引擎相关\img\image-20201213180901371.png" alt="image-20201213180901371" style="zoom:67%;" />

开启后：

<img src="G:\创作\笔记\游戏开发\RPGMakerMV开发\MV引擎相关\img\image-20201213180937971.png" alt="image-20201213180937971" style="zoom:67%;" />





### Community_Basic.js

基础的指令

参数：

- cacheLimit：图片缓存的数量

- screenWidth：调整窗口大小，但是不会修改分辨率，其余部分用黑色填充
- screenHeight：

- changeWindowWidthTo：调整窗口大小，而且会修改游戏分辨率
- changeWindowHeightTo

- renderingMode：渲染模式，建议直接auto

- alwaysDash：角色是否一直奔跑

### EnemyBook.js

敌人图鉴

参数：

- unknown data：对没取得的物品以什么来填充，默认是问号。

使用方法：

1. 创建公共事件，里面直接用插件指令`EnemyBook open`
2. 直接创建一个特殊物品，里面的效果放入这个公共事件。

3. 直接使用这个物品就能打开图鉴了
4. 然后每次打完怪什么的，给后面可以加一个`EnemyBook add 某某某 `，这样子就能增加图鉴了。

插件指令：

```pseudocode
插件指令:
  EnemyBook open         # 打开图鉴
  EnemyBook add 3        # 在图鉴里面增加3号敌人
  EnemyBook remove 4     # 在图鉴里面移除4号敌人
  EnemyBook complete     # 图鉴全部显示
  EnemyBook clear        # 清空图鉴

//下面的代码要放在敌人的备注里面
Enemy Note:
  <desc1:foobar>         # Description text in the enemy book, line 1
  <desc2:blahblah>       # Description text in the enemy book, line 2，
  /*以此类推，可以一直写下去*/
  <book:no>              # 在图鉴里面不显示
```



### ItemBook.js

物品图鉴

参数：

- unknown data：？？？？ 对于未获取的数据以？？？填充
- Price Text：价格
- Equip Text ：装备
- Type Text：类型

使用方法：

和上面那个怪物图鉴一样

插件指令：

```pseudocode
Plugin Command:
  ItemBook open            # Open the item book screen
  ItemBook add weapon 3    # Add weapon #3 to the item book
  ItemBook add armor 4     # Add armor #4 to the item book
  ItemBook remove armor 5  # Remove armor #5 from the item book
  ItemBook remove item 6   # Remove item #6 from the item book
  ItemBook complete        # Complete the item book
  ItemBook clear           # Clear the item book

Item (Weapon, Armor) Note:
  <book:no>                # This item does not appear in the item book
```

### MadeWithMv.js

显示LOGO

参数：

- Show Made With MV：是否开启插件
- Made with MV Image：选择显示的图片
- Show Custom Splash：是否显示第二张图
- Custom Image：第二张图片
- Fade Out Time
- Fade In Time
- Wait Time

### SimpleMsgSideView.js

精简战斗信息的

参数：

- displayAttack：是否显示战斗信息
- position：战斗信息的位置



### TitleCommandPosition.js

标题指令的位置

就是“开始游戏“那些按钮的位置。

参数：

- Offset X：正数向右，负数向左
- Offset Y：正数向下，负数向右
- Width：宽度
- Background：0，1，2



### WeaponSkill.js

武器附魔

就是给普通攻击加上魔法效果

使用方法：

- 直接在武器的备注里面写上下面的代码，直接武器附魔

```pseudocode
<skill_id:3> /*调用3号技能*/
```



## YEP插件

![image-20201214003826374](G:\创作\笔记\游戏开发\RPGMakerMV开发\MV引擎相关\img\image-20201214003826374.png)

### YEP_CoreEngine.js

核心插件

主要用于修改游戏中一些常数，比如最大等级、最大金币等等。

| 参数 | 数值类型 |      |      |
| ---- | -------- | ---- | ---- |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |
|      |          |      |      |



### SceneGlossary

这个插件可以为MV内置一个收集的菜单。可以用于图鉴，战利品展示，以及词典等各种收集类的用途。我下面统一把这个叫做小词典吧，我觉得比较形象。

使用方法：

1. 双击第一个GlossaryInfo

<img src="img\image-20201212194436860.png" alt="image-20201212194436860" style="zoom:80%;" />

2. 点进去之后里面会有很多选项，意思如下

<img src="img\image-20201212194720759.png" alt="image-20201212194720759" style="zoom:80%;" />

- GlossaryType：这个就是这个小词典的编号，必须是int类型，不能重复。也就是说你可以同时建立很多个小词典。

- CommandName：就是这个词典的名字。

- UseCategory：就是说这个里面是否有分目录，比如说我这个程序设计词典里面还可以放一个前端和后端，而前端里面才放着真正的数据。

- GlossaryHelp：点进分目录里面的说明

  ![image-20201212195423988](img\image-20201212195423988.png)

- CategoryHelp：主页面的说明

  <img src="img\image-20201212195547427.png" alt="image-20201212195547427" style="zoom:80%;" />

- ShowingItemNumber：展示物品所持有的数量

- SelectAction：选择物品是否可以被使用

- ConfirmHelp：

- UsingHelp：**不要写！！！有bug！**

- 未入手item的表示：也就是说如果没有获得这个东西时，显示为什么，一般来说写上？？？比较好。





3. 之后就是添加物品了，直接去数据库里面添加物品。把物品类型设置为隐藏物品A或者B。

   <img src="img\image-20201212195920856.png" alt="image-20201212195920856" style="zoom:80%;" />

4. 添加备注

```pseudocode
<SG種別:1> //这个就是所属词典的id，和刚才的GlossaryType是对应关系
<SGカテゴリ:前端> //如果你点了UseCategory，那么这个就要写上，这个就是这个物品所属的分目录，就是前端那些
<SG説明:很难> //描述信息
```



如果想在游戏中打开某个菜单，可以直接使用`GLOSSARY_CALL 1`，这种方式来打开某本词典。

## GALV插件



### AUDIO/VISUAL 





### GALV_MessageBusts（立绘）

1. 导入之后把插件的两个参数改为1

![image-20210317200250476](img\image-20210317200250476.png)

2. 在picture中放入和face同名的文件。

<img src="G:\创作\笔记\游戏开发\RPGMakerMV开发\MV引擎相关\img\image-20210317200346027.png" alt="image-20210317200346027" style="zoom: 67%;" />

<img src="G:\创作\笔记\游戏开发\RPGMakerMV开发\MV引擎相关\img\image-20210317200425317.png" alt="image-20210317200425317" style="zoom:67%;" />

这样子，在对话中选择的face就会映射到pictures里面。



插件指令

```pseudocode
BUST FALSE   /*关闭立绘效果*/
BUST TRUE   /*关闭立绘效果*/
```

### GALV_CharacterFrames（修改人物行走图帧数）







