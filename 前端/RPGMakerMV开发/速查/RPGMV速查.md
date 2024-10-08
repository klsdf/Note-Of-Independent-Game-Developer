# RPGMV脚本API速查

## 信息

### 显示文字（Show Text）

一共有4个需要设定的地方：

#### 设置脸图（可选）

如果想给弹出的文本框设置脸图，那么就可以用这个代码。

| 参数      | 参数类型/参数内容          | 默认值 | 说明                                                         |      |
| --------- | -------------------------- | ------ | ------------------------------------------------------------ | ---- |
| faceName  | 字符串，内容就是脸图的名字 |        | 就是脸图文件的名字，事件编辑器那里面选择显示文字，然后点击脸图，就会有一个弹窗。弹窗里面就是脸图的文件，这个faceName就是这些文件的名字。 |      |
| faceIndex | 0到8                       |        | 一个脸图有8个头像，从零开始数，第一行是0到4，第二行是5到7。写几就是第几个图。 |      |

```javascript
$gameMessage.setFaceImage(faceName, faceIndex);
```

#### 设置背景（可选）

| 参数       | 参数类型/参数内容                   | 默认值 | 说明                             |      |
| ---------- | ----------------------------------- | ------ | -------------------------------- | ---- |
| background | 0：窗口 <br />1：暗淡 <br />2：透明 |        | 这个参数就对应着背景下拉框的属性 |      |

```javascript
$gameMessage.setBackground(background);
```

#### 设置窗口位置（可选）-

| 参数         | 参数类型/参数内容                   | 默认值 | 说明                             |      |
| ------------ | ----------------------------------- | ------ | -------------------------------- | ---- |
| positionType | 0：顶部 <br />1：中间 <br />2：底部 |        | 这个参数就对应着背景下拉框的属性 |      |

```javascript
$gameMessage.setPositionType(positionType);
```

#### 文本内容

这个就是本指令的核心方法，效果就是弹出来文本框。如果没有配置前面的样式，那么会按照默认样式来显示。

- text：这个就是一个普通的字符串

```javascript
$gameMessage.add(text);
```



示例：

```javascript
$gameMessage.setFaceImage("Actor1",0);
$gameMessage.setBackground(0);
$gameMessage.setPositionType(2);
$gameMessage.add("内容");
```





### 显示选项（Show Choices）

#### 选项框背景

| 参数       | 参数类型/参数内容                       | 默认值 | 说明       |      |
| ---------- | --------------------------------------- | ------ | ---------- | ---- |
| background | 0：窗口<br />1：暗淡<br />2：透明<br /> |        | 窗体的样式 |      |

```js
$gameMessage.setChoiceBackground(0);
```



#### 窗口位置

positionType：有三个固定的数值  

- 0：顶部
- 1：中间
- 2：底部

```js
$gameMessage.setChoicePositionType(positionType);
```



#### 选项本体

| 参数        | 参数类型/参数内容 | 默认值 | 说明                                                         |      |
| ----------- | ----------------- | ------ | ------------------------------------------------------------ | ---- |
| choices     | 数组              |        | 数组的内容就是选项的内容，比如["是","否"]。**注意！元素必须是字符串类型。** |      |
| defaultType | 0，1，2，，，     | 0      | 光标默认移动到第几个选项，从0开始。就是说一进入这个选择页面。 |      |
| cancelType  | 0，1，2，，，     | 0      | 取消选项时，默认选择哪个选项。                               |      |

```js
  $gameMessage.setChoices(choices, defaultType, cancelType);
```



#### 选项的回调函数



```js
 $gameMessage.setChoiceCallback(callback);
```




  示例：

  ```javascript
  $gameMessage.setChoices([ "我","是","选","项"],0,2);
  $gameMessage.setChoiceBackground(1);
  $gameMessage.setChoicePositionType(1);
  $gameMessage.setChoiceCallback(function(n){
    console.log("你选择的是第"+(n+1)+"项！")
  });
  ```

  



### 数值输入处理（Input Number）



| 参数       | 参数类型/参数内容 | 默认值 | 说明                                                         |
| ---------- | ----------------- | ------ | ------------------------------------------------------------ |
| variableId | 正整数            |        | 所要输入进的变量ID，变量ID可以在编辑器里面直接找到。         |
| maxDigits  | 正整数            |        | 输入的位数。你可以发现，在事件编辑器里面，这个是最多8位的，但是用代码的话，可以想写几位就写几位。非常自由。 |
|            |                   |        |                                                              |

示例：

```javascript
$gameMessage.setNumberInput(6,20);
```





### 物品选择处理（Select Item）

这个函数可以储存所选物品的物品ID，前提是你必须拥有这个物品。虽然我从来没有用过，但是我想这个功能还是很有用的。

参数

- variableId：要把物品ID存入哪个变量中，变量ID可以在编辑器里面直接找到。
- itemType：物品的类型，一共有四种数值，而且是从1开始的。真搞不懂官方怎么设计的。
  - 1：普通物品
  - 2：重要物品
  - 3：隐藏物品A
  - 4：隐藏物品B 

```javascript
$gameMessage.setItemChoice(5,1);
```







### 显示滚动文字（Show Scrolling Text）

| 参数   | 参数类型/参数内容 | 默认值 | 说明                                        |
| ------ | ----------------- | ------ | ------------------------------------------- |
| speed  | 正数，可以有小数  | 2      | 文字滚动的速度                              |
| noFast | true/false        | false  | 文字是否可以快进，false为可以，true为不可以 |

```
$gameMessage.setScroll(speed,noFast);
```



示例：

```javascript
$gameMessage.add("内容1");
$gameMessage.add("内容2");
$gameMessage.add("内容3");
$gameMessage.setScroll(2,false);
```





## 游戏进程

### 开关操作（Control Switches）



| 参数       | 参数类型/参数内容   | 默认值 | 说明     |
| ---------- | ------------------- | ------ | -------- |
| variableId | 正整数，**从1开始** |        | 开关的id |
| value      | true/false          |        | 开关的值 |

```js
$gameSwitches.setValue(variableId, value);
```



### 获得开关的值

同样从1开始

```js
$gameSwitches.value(1)
```



### 变量操作（Control Variables）



```js
$gameVariables.value(1);//查询某个变量的值
$gameVariables.setValue(1,100);//修改某个变量的值
```



### 独立开关操作（Control Self Switch）

需要传递四个参数

1. 地图ID，表示第几张地图
2. 变量ID
3. 独立开关名称
4. true还是false

```js
$gameSelfSwitches.setValue([4,287,'A'],false)
```



查询值

```js
$gameSelfSwitches.value([4,72,'A'])
```



### 计时器操作（Control Timer）

```js
$gameTimer.start(count);//开始倒计时，count为秒数
$gameTimer.stop();
$gameTimer.seconds();//返回秒数
```



## 流程控制

### 分支条件（Conditional Branch）

在脚本中建议使用if else来代替

### 循环（Loop）

在脚本中建议使用for循环替代

### 跳出循环（Break Loop）



### 终止事件处理

### 公共事件（Common Event）

```js
var commonEvent = $dataCommonEvents[公共事件id];
var temp =  = new Game_Interpreter(this._depth + 1);
temp.setup(commonEvent.list, eventId);
```



### 标签（Label）

### 转到标签（Jump to Label）

### 注释（Comment）





## 队伍

### 增减金币（Change Gold）

实际上源代码中，loseGold直接调用了gainGold(-amount)，就离谱。

```javascript
$gameParty.gainGold(300);//得到300块钱
$gameParty.loseGold(300);//失去300块钱
```

### 增减物品（Change Items）

实际上源代码还是比较复杂的，我这个把源代码提炼精简了一下，你只管放心用。

参数

- item：需要传递一个物品对象，可以直接传递`$dataItems[1]`这种格式。代表第一个物品，注意这些`$`开头的都是从1开始的。
- amount：得到的数量



示例：

```javascript
$gameParty.gainItem($dataItems[1], 30);//得到30个1号物品
$gameParty.loseItem($dataItems[1], 10);//失去10个1号物品
```

### 增减武器（Change Weapons）



```js
 $gameParty.gainItem($dataWeapons[this._params[0]], value, this._params[4]);
```



### 增减护甲（Change Armors）



```js
$gameParty.gainItem($dataArmors[this._params[0]], value, this._params[4]);
```



### 队伍管理（Change Party Member）

注意！如果你队伍中已经有了1号角色，那么再调用增加1号角色的代码将不会有效果（你应该庆幸没有报bug）。

```javascript
$gameParty.addActor(1);//为队伍增加1号角色
$gameParty.removeActor(1);//1号角色离队
```

### 获取领队信息*

领队一般是指队伍中第一个玩家角色

```javascript
$gameParty.leader();
```



### 获取某个角色的信息*

注意，这里标号从1开始

```js
$gameActors.actor(1)
```

### 玩家队伍总人数*

```
$gameParty.allMembers().length
```



### 队伍最高等级

```
$gameParty.highestLevel()
```



## 角色



### 增减HP（Change HP）

```js
Game_Interpreter.prototype.changeHp(target, value, allowDeath)

$gameParty.leader().gainHp(-30)
```



示例：

```js
Game_Interpreter.prototype.changeHp($gameParty.leader(),-300,true)
```



### 增减MP（Change MP）

```js
$gameParty.leader().gainMp(-30)
```



### 增减TP（Change TP）

```
$gameParty.leader().gainTp(-30)
```

### 更改状态（Change State）

```js
   actor.addState(this._params[3]);
actor.removeState(this._params[3]);
```

### 完全恢复（Recover All）

```
actor.recoverAll();
```

### 增减经验值（Change EXP）



```js
 actor.changeExp(exp, show);//show代表是否展示升级信息，exp代表经验值
```



### 增减等级（Change Level）

```js
 actor.changeLevel(level, show);//同上
```



### 增减能力值（Change Parameter）





### 增减技能（Change Skill）

### 更改装备（Change Equipment）

### 更改名字（Change Name）

```js
$gameParty.leader().setName("起的名字");
$gameParty.leader().setName(prompt("自己起一个名字吧") );
```



### 更改职业（Change Class）

### 更改昵称（Change Nickname）

```js
var actor = $gameActors.actor(this._params[0]);
if (actor) {
    actor.setNickname(this._params[1]);
}
```



### 更改简介（Change Profile）

```js
var actor = $gameActors.actor(1);
    if (actor) {
        actor.setProfile(this._params[1]);
    }
```



### 角色信息查看*

$gameActors.actor(n)可以获得队伍中某个角色，n为正整数，从1开始。

```js
$gameActors.actor(n).agi //角色敏捷
$gameActors.actor(n).atk //角色atk
$gameActors.actor(n).cev //角色会心一击闪躲率
$gameActors.actor(n).cnt //角色反击机率
$gameActors.actor(n).cri //角色会心攻击机率
$gameActors.actor(n).currentExp() //角色当前经验值
$gameActors.actor(n).def //角色防御力
$gameActors.actor(n).eva //角色闪躲率
$gameActors.actor(n).exr //角色经验获得倍率
$gameActors.actor(n).fdr //地板类伤害倍率
$gameActors.actor(n).grd //角色防御倍率
$gameActors.actor(n).hit //角色命中率
$gameActors.actor(n).hp //角色hp
$gameActors.actor(n).hrg //角色hp再生率
$gameActors.actor(n).level //角色lv
$gameActors.actor(n).luk //角色幸运度
$gameActors.actor(n).mat//角色魔法攻击力
$gameActors.actor(n).mcr//角色MP消耗率
$gameActors.actor(n).mdf//角色魔法防御力
$gameActors.actor(n).mdr//角色魔法伤害率(减轻)
$gameActors.actor(n).mev//角色魔法回避率
$gameActors.actor(n).mhp//角色最大HP
$gameActors.actor(n).mmp//角色最大MP
$gameActors.actor(n).mp//角色MP
$gameActors.actor(n).mrf//角色魔法反射率
$gameActors.actor(n).mrg//角色MP再生率
$gameActors.actor(n).nextLevelExp()//角色至下个等级的累计经验值
$gameActors.actor(n).nextRequiredExp()//角色至下个等级的经验值
$gameActors.actor(n).pdr//角色物理伤害率
$gameActors.actor(n).pha//薬の知识
$gameActors.actor(n).rec//角色恢复效果率
$gameActors.actor(n).tcr//角色TP累积率
$gameActors.actor(n).tgr//角色仇恨度(高的容易被怪物瞄准)
$gameActors.actor(n).tp//角色TP
$gameActors.actor(n).trg//角色TP恢复率
$gameActors.actor(n).name()//角色名字
$gameActors.actor(n).actorId()//角色在数据库中的id
```





## 移动

### 场所移动（Transfer Player）

第一种就是直接移动，但是画面不会移动。

```javascript
$gamePlayer.setPosition(23,24)
```

第二种就是编辑器里面那个



fadeType:

0：黑

1：白

2：无

```javascript
$gamePlayer.reserveTransfer(mapId, x, y, d, fadeType);
//d代表direction，默认写0.fadetype也写0
$gamePlayer.reserveTransfer(3,33,34,0,0)
```









### 设置载具位置（Set Vehicle Location）

### 设置事件位置（Set Event Location）



### 滚动地图（Scroll Map）

| 参数      | 参数类型/参数内容                                            | 默认值 | 说明                                                         |
| --------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| direction | 8：向上<br />4：向左<br />6：向右<br />2：向下               | 2      | 滚动方向，和小键盘是对应的。8，2代表上下，4，6代表左右。     |
| distance  |                                                              | 1      | 距离，代表滚动的格子数                                       |
| speed     | 1 ：1/8速度<br />2：1/4速度<br />3：1/2速度<br />4：标准速度<br />5：2倍速<br />6：4倍速 | 4      | 速度，其中速度不一定按照正整数填写，可以自定义小数。参数每+1，速度提升一倍。 |



```js
$gameMap.startScroll(direction, distance, speed);
```



示例：

```js
$gameMap.startScroll(2, 1, 4);
```



### 设置移动路线（Set Movement Route）

n从1开始，n代表事件的id。

```js
$gameMap.event(n).moveStraight(2);//向下移动
$gameMap.event(n).moveStraight(4);//向左移动
$gameMap.event(n).setThrough(true); //开启穿透
$gameMap.event(n).setThrough(false); //关闭穿透
$gameMap.event(n).setTransparent(true); //开启透明状态
$gameMap.event(n).setTransparent(false);//关闭透明状态
$gameMap.event(n).turnRandom(); //随机转向
$gameMap.event(n).turnTowardPlayer(); //朝向玩家
$gameMap.event(n).turnAwayFromPlayer(); //背向玩家
$gameMap.event(n).moveTowardPlayer();//朝向玩家移动
$gameMap.event(n).moveAwayFromPlayer();//远离玩家移动
$gameMap.event(n).setMoveFrequency(3); //移动频率
$gamePlayer.setMoveSpeed(4); //角色移动速度   4是默认速度，要注意，这个速板是指数增加的，一旦变了一点点，速度就有极大变化。所以每次增加0.01之类的比较好，如果直接加1速度会太快。
$gameMap.event(n).moveDiagonally(4, 2);//左下移动
$gameMap.event(n).moveDiagonally(6, 2);//右下移动
$gameMap.event(n).moveDiagonally();//左上移动
$gameMap.event(n).moveDiagonally(6, 8);//右上移动
$gameMap.event(n).moveStraight(6);//向右移动
$gameMap.event(n).moveStraight(8);//向上移动
$gameMap.event(n).moveRandom();//随机移动
$gameMap.event(n).moveForward(); //接近玩家
$gameMap.event(n).moveBackward();//远离玩家
$gameMap.event(n).jump(params[0], params[1]); //跳跃
$gameMap.event(n).setDirection(2); //设置朝向下方
$gameMap.event(n).setDirection(4);//设置朝向左方
$gameMap.event(n).setDirection(6);//设置朝向右方
$gameMap.event(n).setDirection(8);//设置朝向上方
$gameMap.event(n).turnRight90();//右转90°
$gameMap.event(n).turnLeft90(); //左转90°
$gameMap.event(n).turn180(); //后转180°
$gameMap.event(n).turnRightOrLeft90();//向左或向右转90°
        this.setWalkAnime(true);

switch (command.code) {
    case gc.ROUTE_END:
        this.processRouteEnd();
        break;



    case gc.ROUTE_WAIT:
        this._waitCount = params[0] - 1;
        break;


    case gc.ROUTE_WALK_ANIME_OFF:
        this.setWalkAnime(false);
        break;
    case gc.ROUTE_STEP_ANIME_ON:
        this.setStepAnime(true);
        break;
    case gc.ROUTE_STEP_ANIME_OFF:
        this.setStepAnime(false);
        break;
    case gc.ROUTE_DIR_FIX_ON:
        this.setDirectionFix(true);
        break;
    case gc.ROUTE_DIR_FIX_OFF:
        this.setDirectionFix(false);
        break;

    case gc.ROUTE_CHANGE_IMAGE:
        this.setImage(params[0], params[1]);
        break;
    case gc.ROUTE_CHANGE_OPACITY:
        this.setOpacity(params[0]);
        break;
    case gc.ROUTE_CHANGE_BLEND_MODE:
        this.setBlendMode(params[0]);
        break;
    case gc.ROUTE_PLAY_SE:
        AudioManager.playSe(params[0]);
        break;

    }
```







### 载具乘降（Getting On and Off Vehicles）

## 人物

在这里特指地图上那个人物的动画。要和角色区分开。角色是记录角色数据信息的，而人物则反映了在画面上的移动速度、动画等信息。

### 更改透明状态（Change Transparency）

```js
$gamePlayer.setTransparent(true)//开启透明
```



### 更改队列行进（Change Player Followers）

```js
$gamePlayer.showFollowers();
$gamePlayer.hideFollowers();
```



### 集合队列成员（Gather Followers）

```js
$gamePlayer.gatherFollowers();
this.setWaitMode(‘gather’);
```



### 显示动画（Show Animation）

```js
$gamePlayer.requestAnimation(1);
```



### 显示气泡图标（Show Balloon Icon）

```js
$gamePlayer.requestBalloon(1) //显示惊讶
```



要注意理论上来说这个id可以无限大1

有多大取决于系统中Ballon.png有多高，默认720像素，每一个小方块48像素。默认有10个，其图片还预留了5个扩展位置，开发者可以自己画，如果不够了只需要向下拓展即可。

例如多扩展48*5像素，那么就可以多画5个气泡，最多可以访问到20号气泡。

### 暂时消除事件（Erase Event）

```javascript
$gameMap.eraseEvent(this._eventId);
```



### 设置人物位置*

注意！这个设置不会使画面一起移动。如果想要画面也一起移动，建议使用移动中的”场所移动“。

```js
$gamePlayer.setPosition(3,6)
```



### 查看队伍朝向*

MV中朝向被定义为4个数字

- 左：4
- 右：6
- 上：8
- 下：2

其实，，这个和小键盘的方向是一一对应的。

```javascript
$gamePlayer.direction() //查看队伍方向
```







## 图片

### 显示图片（Show Picture）

| 参数      | 参数类型/参数内容                                  | 默认值 | 说明       |
| --------- | -------------------------------------------------- | ------ | ---------- |
| pictureId |                                                    |        | 编号       |
| name      |                                                    |        | 图像名称   |
| origin    | 0：左上<br />1：中心                               | 0      | 原点的位置 |
| x         |                                                    | 0      |            |
| y         |                                                    | 0      |            |
| scaleX    |                                                    | 100    | 宽度缩放   |
| scaleY    |                                                    | 100    | 高度缩放   |
| opacity   | 0到255                                             | 255    | 透明度     |
| blendMode | 0：正常<br />1：叠加<br />2：正片叠底<br />3：滤色 | 0      | 合成模式   |

```js
$gameScreen.showPicture(pictureId, name, origin, x, y,scaleX, scaleY, opacity, blendMode)
```



例如：

```js
$gameScreen.showPicture(1,"图片名称", 0, 0, 0,100, 100, 255, 0)
```



### 移动图片（Move Picture）

参数如上

```js
$gameScreen.movePicture(pictureId, origin, x, y, scaleX,scaleY, opacity, blendMode, duration);
```



### 旋转图片（Rotate Picture）

```js
$gameScreen.rotatePicture(this._params[0], this._params[1]);
```



### 更改图片色调（Tint Picture）

```js
$gameScreen.tintPicture(this._params[0], this._params[1], this._params[2]);
```



### 消除图片（Erase Picture）



```js
$gameScreen.erasePicture(pictureId);
```



### 清除所有图片*

```js
$gameScreen.clearPictures();
```



## 计时

### 等待

要注意，这个脚本需要写在事件中

```js
this.wait(duration);
```









## 画面



### 淡出画面（Fadeout Screen）

```
$gameScreen.startFadeOut(duration) //淡出
```

### 淡入画面（Fadein Screen）

```
$gameScreen.startFadeIn(duration) //淡入
```



### 更改画面色调（Tint Screen）



```javascript
$gameScreen.startTint(tone, duration);
```

这个tone同样是一个颜色。数组各项分别为RGB+灰度。



```javascript
//下面是官方的预设值：
$gameScreen.startTint([0, 0, 0, 0], 60); //正常
$gameScreen.startTint([-68, -68, -68, 0], 60); //黑暗
$gameScreen.startTint([34, -34, -68, 170], 60); //茶色
$gameScreen.startTint([68, -34, -34, 0], 60); //黄昏
$gameScreen.startTint([-68, -68, 0, 68], 60); //夜晚

//下面是我自己总结的
$gameScreen.startTint([50, 50, 50, 0], 60); //正午
$gameScreen.startTint([-120, -100, 0, 68], 60);//深夜
```





### 闪烁画面（Flash Screen）

```javascript
$gameScreen.startFlash(color, duration);
```

颜色使用的是RGB+强度，调用时使用数组

```javascript
$gameScreen.startFlash([255, 0, 0, 128], 8);
```





### 震动屏幕（Shake Screen）

默认5，5，60

```javascript
$gameScreen.startShake(power, speed, duration);
```



### 设置天气（Set Weather Effect）

|          |                                     | 默认值 |                        |
| -------- | ----------------------------------- | ------ | ---------------------- |
| type     | none<br />rain<br />storm<br />snow | none   | 天气类型               |
| power    |                                     | 5      | 强度                   |
| duration |                                     | 60     | 持续时间，单位为帧数。 |

```js
$gameScreen.changeWeather(type, power, duration);
```



示例：

```
$gameScreen.changeWeather("storm", 10, 60);
```



### 查看天气信息*



```js
$gameScreen.weatherType()//查看天气类型
```



## 音频&视频

### 播放BGM（Play BGM）

注意，如果之前已经有bgm的话，这个会把之前的给挤掉。

```javascript
var bgm = new Object();
bgm.name = "对峙";//bgm的名称
bgm.volume = 100;//响度
bgm.pitch = 100;//音调
bgm.pan = 0;//偏移
AudioManager.playBgm(bgm);
//AudioManager.playBgm(bgm,pos);//pos可以缺省
```

### 淡出BGM（Fadeout BGM）

参数为秒数

```javascript
AudioManager.fadeOutBgm(duration);
```

### 保存BGM（Save BGM）

```js
$gameSystem.saveBgm();
```



### 还原BGM（Resume BGM）

```js
$gameSystem.replayBgm();
```



### 播放BGS（Play BGS）

```js
 AudioManager.playBgs(this._params[0]);
```



### 淡出BGS（Fadeout BGS）

```js
AudioManager.fadeOutBgs(this._params[0]);
```



### 播放ME（Play ME）

```js
var me = new Object();
se.name = Inn";//me的名称
se.volume = 100;//响度
se.pitch = 100;//音调
se.pan = 0;//偏移
AudioManager.playMe(me);
```



### 播放SE（Play SE）

```javascript
var se  = new Object();
se.name = "Bell3";//se的名称
se.volume = 100;//响度
se.pitch = 100;//音调
se.pan = 0;//偏移
AudioManager.playSe(se);//播放音效
```

经过我的感觉，一些音名对照表如下。

| C    | D    | E    | F    | G    | A    | B    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 40   | 45   | 50   | 52   | 58   | 65   | 75   |



### 停止SE（Stop SE）

```js
AudioManager.stopSe();
```



### 播放影像（Play Movie）

```js
Graphics.playVideo('movies/PV.webm');
```



### 播放系统音效*

这个所谓的系统，并不是说windows系统，而是说MV数据库里面那个系统。这个音效的顺序和MV系统里面的音保持一致。

```javascript
SoundManager.playCursor()//光标
SoundManager.playOk()//确定
SoundManager.playCancel()//取消
SoundManager.playBuzzer()//无效
SoundManager.playEquip()//装备
SoundManager.playSave()//存档
SoundManager.playLoad() //读档
SoundManager.playBattleStart() //战斗开始
SoundManager.playEscape() //逃跑
SoundManager.playEnemyAttack() //敌人攻击 
SoundManager.playEnemyDamage() //敌人受伤
SoundManager.playEnemyCollapse() //敌人消失
SoundManager.playBossCollapse1() //Boss消失1
SoundManager.playBossCollapse2() //Boss消失2
SoundManager.playActorDamage() //角色受伤
SoundManager.playActorCollapse() //角色无法战斗 
SoundManager.playRecovery() //恢复
SoundManager.playMiss() //未命中
SoundManager.playEvasion() //回避
SoundManager.playMagicEvasion() //魔法回避
SoundManager.playReflection() //魔法反射 
SoundManager.playShop() //商店
SoundManager.playUseItem() //使用物品
SoundManager.playUseSkill() //使用技能
```



## 场景控制

### 战斗处理（Battle Processing）

- troopId：敌群id

  

```js
BattleManager.setup(troopId, true/false, true/false);
```



### 商店处理（Shop Processing）

```
SceneManager.push(Scene_Shop);
```



### 名字输入处理（Name Input Processing）

```js
SceneManager.push(Scene_Name);
```



### 打开菜单画面（Open Menu Screen）

```javascript
SceneManager.push(Scene_Menu);
```

### 打开存档画面（Open Save Screen）

```javascript
SceneManager.push(Scene_Save);
```



### 游戏结束（Game Over）

```javascript
SceneManager.goto(Scene_Gameover);
```



### 返回标题画面（Return to Title Screen）

```javascript
SceneManager.goto(Scene_Title);
```







## 系统设置

### 更改战斗BGM（Change Battle BGM）

```js
 $gameSystem.setBattleBgm(this._params[0]);
```



### 更改胜利ME（Change Victory ME）

```js
 $gameSystem.setVictoryMe(this._params[0]);
```



### 更改战败ME（Change Defeat ME）

```js
$gameSystem.setDefeatMe(this._params[0]);
```



### 更改载具BGM（Change Vehicle BGM）

```js
var vehicle = $gameMap.vehicle(this._params[0]);
if (vehicle) {
    vehicle.setBgm(this._params[1]);
}
```



### 启用/禁用存档（Change Save Access）

```js
$gameSystem.disableSave();
$gameSystem.enableSave();
```



### 启用/禁用菜单（Change Menu Access）

```js
$gameSystem.disableMenu();
$gameSystem.enableMenu();
```



### 启用/禁用遇敌（Change Encounter Disable）

```
 $gameSystem.disableEncounter();
 $gameSystem.enableEncounter();
```



### 启用/禁用整队（Change Formation Access）

```js
$gameSystem.disableFormation();
$gameSystem.enableFormation();
```



### 更改窗口颜色（Change Window Color）

value是一个长度为4 的数组，4个元素分别是rgba

```js
$gameSystem.setWindowTone(value);
```



例如：

```js
$gameSystem.setWindowTone([200,100,100,0]);//设置窗口rgb为200，100，100
```



### 更改角色图像

```js
$gameActors.actor(actorId).setCharacterImage(characterName, characterIndex);
$gameActors.actor(actorId).setFaceImage(faceName, faceIndex):
$gameActors.actor(actorId).setBattlerImage(battlerName);
```



### 更改载具图像

```js
 $gameMap.vehicle(vehicleId).setImage(name, index);
```



### 游戏时间*



```js
$gameSystem.playtimeText() //游戏时间，用时分秒表示
$gameSystem.playtime() //游戏时间，用秒表示
```

### 显示帧数*

```js
Graphics.showFps();
```



### 关闭游戏*

这个是直接暴力关闭窗口，不会有任何弹窗！！！慎用！

```javascript
window.close()
```





## 地图

### 启用/禁用显示地图名称（Change Map Name Display）

```js
$gameMap.enableNameDisplay();//启用
$gameMap.disableNameDisplay();//禁用
```



### 更改地图图块（Change Tileset）



### 更改战斗背景（Change Battle Back）



### 更改远景（Change Parallax）



```javascript
$gameMap.changeParallax(this._params[0], this._params[1],
        this._params[2], this._params[3], this._params[4]);
```





### 获取指定位置的信息（Get Location Info）

- 变量

  ```
  
  ```

- 

### 地图尺寸*

```js
$gameMap.height()
$gameMap.width()
```



## 战斗

### 增减敌人HP（Change Enemy HP）

```js
$gameTroop.members()[enemyIndex].gainHp(value);
```

### 增减敌人MP（Change Enemy MP）

```
$gameTroop.members()[enemyIndex].gainMp(value);
```



### 增减敌人TP（Change Enemy TP）

```
$gameTroop.members()[enemyIndex].gainTp(value);
```



### 更改敌人状态（Change Enemy State）

```js
$gameTroop.members()[enemyIndex].addState(n);
$gameTroop.members()[enemyIndex].removeState(n);
```



### 敌人完全恢复（Enemy Recover All）

```js
$gameTroop.members()[enemyIndex].recoverAll();
```



### 敌人出现（Enemy Appear）

```
$gameTroop.members()[enemyIndex].appear();
```



### 敌人变身（Enemy Transform）

```
$gameTroop.members()[enemyIndex].transform(n);
```



### 显示战斗动画（Show Battle Animation）

```js
    $gameTroop.members()[enemyIndex].startAnimation(animationId, true/false, delayN);
```



### 强制战斗行动（Force Action）

我方强制动作

```
$gameParty.members()[index].forceAction(skillId, targetIndex);
BattleManager.forceAction($gameParty.members()[index]);
```

敌人强制动作

```
$gameTroop.members()[index].forceAction(skillId, targetIndex);
BattleManager.forceAction($gameTroop.members()[index]);
```



### 中断战斗（Abort Battle）

```js
BattleManager.abort();
```



### 获取敌人名字*

```js
$gameTroop.enemyNames()
```

### 获取敌人对象*

```js
$gameTroop._enemies[0]
```

### 战斗状态判断*

是否处于战斗状态

```js
$gameTroop._inBattle
```



## 高级

### 脚本（Script）

请使用eval()代替

### 插件指令（Plugin Command）

```js

function 调用插件指令(插件指令){
    var args =插件指令.split(" ");
    var command = args.shift();
    Game_Interpreter.prototype.pluginCommand(command, args);
}
//使用时，直接把需要的插件指令复制到形式参数里面就可以了
//比如说
调用插件指令（"我的插件 参数"）

```



## 动画*

### 播放动画

直接可以用事件来播放动画，动画会作用在其身上。

里面的参数只需要传递动画的编号即可

```javascript
$gameMap._events[11].requestAnimation(1)
```





## 事件*



### 获取所有事件

```js
$gameMap.events()
```



### 获取指定id的事件

这个id可以在编辑器中，点开某个事件，查看其左上角得到。id从1开始。

```js
$gameMap.event(1)
```



### 获取事件注释

```js
//这个方法可以直接获得注释的内容
$dataMap.events[eventID].note

//如果注释是以对象形式写的，那么可以用meta属性进行访问
//<name:莲华><age:13>
$dataMap.events[eventID].meta.name
$dataMap.events[eventID].meta.age
```

### 获取指定位置的事件编号

如果指定的位置没有事件，那么返回0。

```javascript
$gameMap.eventIdXy(x,y);
```

### 运行事件

可以直接用脚本来开启事件

```javascript
$gameMap.event(1).start()
```

### 访问事件对象

在地图上，直接在对象的事件指令里面创建一个脚本，里面写上下面这个，就可以打印出该事件对象。

```
console.log($gameMap._events[this._eventId])
```

如果不是写在事件编辑器的话，可以指定事件ID来进行访问。

```
console.log($gameMap._events[11])
```

也可以直接根据坐标来访问

```javascript
$gameMap.eventsXy(31, 33)
```



### 事件对象的移动速度

标准速度是4，也就是人物的速度。

```javascript
$gameMap._events[11]._moveSpeed
```

### 事件是否靠近玩家



```js
$gameMap.event(1).isNearThePlayer()
```



## 鼠标*



### 鼠标移动

这个函数也比较特殊，并不是只要你移动了鼠标就能被检测到，而是说你必须一直按着并且移动才会true。这个其实是为触摸板设计的。

```javascript
TouchInput.isMoved() //是否按下鼠标左键同时移动了鼠标
```



### 鼠标左键是否正在被按下

```js
TouchInput.isPressed()  //鼠标左键是否正在被按下
```



### 是否切换为鼠标左键

```js
TouchInput.isTriggered() //鼠标左键刚刚是否按下
```

### 鼠标左键是否连续按下

```js
TouchInput.isRepeated() //鼠标左键是否连续点击，或者一直处于按下状态
TouchInput.isLongPressed() //鼠标左键是否一直按下
```

要注意的就是这个`isRepeated()`和`isLongPressed()`，这两个比较像，但是还是有很大区别的。如果你鼠标一直狂点，那么`isRepeated()`会返回true，但是`isLongPressed()`不会。而长按鼠标左键，两个都会返回true。

### 鼠标左键释放

```javascript
TouchInput.isReleased() //鼠标左键是否释放
```

### 鼠标右键点击

```javascript
TouchInput.isCancelled() //鼠标右键是否点击
```



### 鼠标位置

```js
TouchInput.x
TouchInput.y
```



## 键盘*



### 增加WASD控制方向

```js
Input.keyMapper = {
    9: 'tab',      
    13: 'ok',       
    16: 'shift',    
    17: 'control',  
    18: 'control',  
    27: 'escape',   
    32: 'ok',       
    33: 'pageup',   
    34: 'pagedown', 
    37: 'left',     
    38: 'up',       
    39: 'right',   
    40: 'down',     
    45: 'escape',  
    81: 'pageup',   
    87: 'pagedown', 
    88: 'escape',  
    90: 'ok',      
    96: 'escape',   
    98: 'down',     
    100: 'left',    
    102: 'right',   
    104: 'up',      
    120: 'debug',   
    //WASD的按键
    65: 'left',     // 左箭头键
    87: 'up',       // 上箭头键
    68: 'right',    // 右箭头键
    83: 'down'     // 下箭头键
};
```





### 检测键盘事件

下面这些函数要传递一个参数，也就是要检测的按键的名字，刚刚那个映射表里面都写了，直接复制就行。（注意把引号也带上）

```javascript
Input.isPressed('ok')  //按键是否正在被按下
Input.isTriggered() //按键刚刚是否按下
Input.isRepeated() //按键是否连续点击，或者一直处于按下状态
Input.isLongPressed() //按键是否一直按下
```

这个和上面的鼠标一模一样，不多做解释。









## 存档*

### 载入存档

-1：载入配置文件

0：载入第一个文件

```javascript
StorageManager.load(savefileId);//返回一个json文件
```

### 载入全局配置

```javascript
DataManager.loadGlobalInfo();//返回一个数组，从1开始。
```

## 武器与装备*



### 查看武器信息

```js
$dataWeapons[$gameParty.leader()._equips[0]._itemId].name
```







### 获取装备信息*



```javascript
$gameParty.leader()._equips//获取领队的装备数据
```

这个会返回一个数组，里面有5个元素，分别对应游戏里面的装备信息

- 0：武器
- 1：盾牌
- 2：头部
- 3：身体
- 4：装饰品



但是这个的信息非常简陋，里面只存放了武器和装备的编号而已，并没有真正地存放物品信息。所以如果想获取真正的数据，还得去访问$dataWeapons。

```javascript
$dataWeapons[$gameParty.leader()._equips[0]._itemId]
```

这样子，先获取玩家的装备编号，再进行查询。然后就好了。

这个$dataWeapons的数据如下：

| 属性        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| animationId | 动画编号                                                     |
| description | 说明                                                         |
| etypeId     |                                                              |
| iconIndex   | 图标编号                                                     |
| id          | 武器的编号                                                   |
| maxItem     | 最大持有量                                                   |
| meta        | 注释的JSON                                                   |
| name        | 武器名字                                                     |
| note        | 备注                                                         |
| params      | 武器数据的数组，从0到7分别是[0:最大HP，1:最大MP，2:攻击力，3:防御力，4:魔法攻击，5:魔法防御，6:敏捷，7:幸运] |
| price       | 价格                                                         |
| traits      | 特性，比如追加能力什么的                                     |
| wtypeId     | 武器类型的编号                                               |





另外，装备里面的备注是可以直接用对象的形式访问的。

```javascript
$dataWeapons[$gameParty.leader()._equips[0]._itemId].meta.你写的标签属性
```







## 系统*

### 显示与隐藏游戏FPS

```js
Graphics.showFps()
Graphics.hideFps()

```



### 判断游戏的运行环境



```js
Utils.isNwjs() //是否是nwjs环境
Utils.isNwjs() && process.platform === 'win32' //是否为windows系统
Utils.isNwjs() && process.platform === 'darwin' //是否为mac系统
Utils.isMobileDevice() //是否为手机设备
Utils.isMobileSafari() //是否为手机端Safari
Utils.isAndroidChrome() //是否为安卓端chrome
```









# nw.js配置速查

## 配置

### 必要字段

每个配置文件中必须要提供以下属性:

#### main

> 属性:**应用起始页**

- String - 如 `index.html`也可以是 `.js`文件或url,该文件与 `package.json`统计目录.

```json
"main": "index.html",  
```



#### name

> 属性:**应用名称,应确保该字段内容全局唯一性**

- String - 名称由数字 , 小写字母 , "." , "_"或者"-"组成,其它内容会被忽略.





### 扩展字段

控制NW.js应提供的功能及如何打开主窗口.

#### nodejs

> 属性:**是否支持Node**

- Boolean - `false`时将禁用Node.

  

#### node-main

> 属性:**指定Node.js脚本文件路径 . 并且它将在加载DOM窗口之前启动Node环境时执行**

- String - Node.js脚本文件路径

#### domain

> 属性:**指定主机域名**

- String - 在 `chrome-extension://`协议URL指定主机域名 . WEB引擎将是应用和同一域名的网站之间共享cookie

#### single-instance

> 属性:**是否以单实例运行**

- Boolean - `true`即单实例运行, `false`则允许应用多开,默认 `true`

#### bg-script

> 属性:**后台脚本**

- String - 应用启动时执行的后台脚本 .





#### window

> 属性:**窗体样式控制**

- Object - 详见窗体子字段章节

#### webkit

> 属性:**WebKit特性控制**

- Object - 详见WebKit子字段章节

#### user-agent

> 属性:**重写应用请求页面中的 `User-Agent`信息**

- String - 重写的 `User-Agent`信息

以下变量内容可以动态设置 `User-Agent`内容:

- `%name`: 替换配置文件中的`name`字段 .
- `%ver`: 替换配置文件中的`version`字段 .
- `%nwver`: 替换NW.js版本 .
- `%webkit_ver`: 替换WebKit引擎版本 .
- `%osinfo`: 替换系统以及CPU信息 .

#### node-remote

> 属性:**从远程页面启用Node**

- Array 或 String - 数组中的各项均需遵循在Chrome扩展中使用的[匹配模式](https://developer.chrome.com/extensions/match_patterns)

匹配模式本质上为URL , 由 `http`, `https`, `file` , `ftp`或者 `'*'`开始 . 其中 `'*'`代表匹配所有URL . 每个匹配模式由三部分组成:

基础语法:

```none
<url-pattern> := <scheme>://<host><path>
<scheme> := '*' | 'http' | 'https' | 'file' | 'ftp'
<host> := '*' | '*.' <any char except '/' and '*'>+
<path> := '/' <any chars>
```

#### chromium-args

> 属性:**分发应用时自定义chromium命令行参数至应用**

- String - 指定的chromium命令行参数

例如:想要禁用GPU加速视频显示,只需添加添加参数 `"chromium-args" : "--disable-accelerated-video"`.

如果添加多个参数,则使用空格进行分割,该字段也可使用单引号括起标记.命令行详细信息,请参阅 [Command-Line-Options](https://nwjs.org.cn/doc/api/Command-Line-Options.html)

#### crash_report_url

> 属性:**应用崩溃时,崩溃转存报告将被发送到设定的服务器**

- String - 崩溃报告服务器的URL

与Chromium浏览器发送方式相同,发送具有 `multipart/form-data`内容的HTTP POST请求. 理论上来讲, 任意 breakpad/crashpad 都可以处理该请求,因为 breakpad/crashpad 与NW相仿,. 请参阅 [简单服务器的小案例](https://github.com/nwjs/nw.js/blob/nw21/test/sanity/crash-dump-report/crash_server.py)或使用现有的[simple-breakpad-server](https://github.com/acrisci/simple-breakpad-server).

该请求至少包含以下字段:

- `prod` - 配置文件中的 `name` 属性
- `ver` - 配置文件中的 `version` 属性
- `upload_file_minidump` - minidump文件的二进制内容
- `switch-n` - 崩溃过程的命令行切换开关,每个切换有多个字段,其中 `n`从1起始.

#### js-flags

> 属性:**指定JS引擎(V8)可用特性**

- String - 可用特性如打开协调代理( `Harmony Proxies`)以及集合( `Collections`):

```json
{
  "name": "nw-demo",
  "main": "index.html",
  "js-flags": "--harmony_proxies --harmony_collections"
}
```

#### inject_js_start

#### inject_js_end

> 属性:**执行JavaScript代码**

- String -相对于应用程序路径的本地文件名，期望执行的JavaScript文件

`inject_js_start`: CSS文件执行之后 , 其他DOM或脚本运行之前 , 执行的JavaScript代码 .

`inject_js_end`: 页面document对象加载之后 , 触发 `onload`之前 , 执行的JavaScript代码 . 主要作为新窗口中 `Window.open()`的参数执行JavaScript代码 .

#### additional_trust_anchors

> 属性:**证书作为附加可用的根证书使用 , 允许连接自签名证书或者CA签发机构颁发证书的服务**

- Array - 数多个PEM编码的证书组成的数组 , 例如 `"-----BEGIN CERTIFICATE-----\n...certificate data...\n-----END CERTIFICATE-----\n"`

#### dom_storage_quota

> 属性:**Mb为单位的DOM存数限制数量**

- Integer - 建议设置为期望值的两倍



## 窗口子字段

> 属性:**窗口子字段默认情况被继承到使用 `window.open()`或 `<a target="_blank">`打开的子窗口 .未继承子字段将被设置为打开窗口时的默认值**

列表如下：

- `fullscreen` -> `false`
- `kiosk` -> `false`
- `position` -> `null`
- `resizable` -> `true`
- `show` -> `true`

所有窗口子字段可以使用[`new-win-policy`事件](https://nwjs.org.cn/doc/api/Window.html#事件-new-win-policy-frame-url-policy)重写 .

### id

> 属性:**内含窗口尺寸与位置的状态的窗口ID,打开同ID的窗口时会还原该状态**
>
> - String - 窗口ID,细节请另见[Chrome应用文档](https://developer.chrome.com/apps/app_window#type-CreateWindowOptions)

### title

> 属性:**NW.js创建的窗口标题 . 在应用启动时显示的标题信息**

- String -标题

### width

### height

> 属性:**主窗口初始宽高**

- Integer - 宽高

### toolbar

> 属性:**是否显示导航栏中的工具条**

- Boolean - `true`显示, `false`不显示

### icon

> 属性:**窗口图标**

- String - 图标路径

### position

> 属性:**窗口位置**

- String - 默认 `null`(不固定) , `center`(屏幕居中) , `mouse`(鼠标所在位置)

### min_width

### min_height

> 属性:**窗口最小宽高**

- Integer - 最小宽高值

### max_width

### max_height

> 属性:**窗口最大宽高**

- Integer - 最大宽高值

### as_desktop*Linux*

> 属性:**X11环境下,作为桌面背景显示**

- Boolean - `true`显示, `false`不显示

### resizable

> 属性:**是否可调整窗口大小**

- Boolean - `true`允许, `false`不允许

**【注意】** ,在OS X上将该属性设置为 `false`，并将frame设置为 `true`，用户还是可以将窗口全屏显示。只有将全屏也设置为 `false`才可禁用全屏控件。

### always_on_top

> 属性:**是否允许窗口始终置顶(在其余窗口之上)**

- Boolean - `true`允许, `false`不允许

### visible_on_all_workspaces *Mac & Linux*

> 属性:**支持多工作区的系统(如Mac & Linux)中,将窗口同时显示在所有工作区中**

- Boolean - `true`允许, `false`不允许

### fullscreen

> 属性:**是否允许窗口全屏**

- Boolean - `true`允许, `false`不允许

**【注意】** ,窗体和全屏框架应当一致,窗口设置为 `false`时,则全屏框架不应设为 `true`,避免窗体将阻止鼠标获取屏幕边缘.

### show_in_taskbar

> 属性:**是否允许显示在任务栏或停靠栏中**

- Boolean - `true`允许, `false`不允许,默认 `true`.

### frame

> 属性:**窗口是否为框架**

- Boolean - 设为 `false`时即无框窗口.

**【注意】** ,窗体和全屏框架应当一致,窗口设置为 `false`时,则全屏框架不应设为 `true`,避免窗体将阻止鼠标获取屏幕边缘.

### show

> 属性:**启动时是否显示应用**

- Boolean - `true`显示, `false`不显示

### kiosk

> 属性:**是否使用 `Kiosk`模式(该模式即应用将全屏并阻止用户离开应用,比如常见的公共触摸屏演示)**

- Boolean - `true`使用, `false`不使用

### transparent

> 属性:**窗口是否透明**

- Boolean - `true`允许, `false`不允许,默认 `false`.

窗口的透明度由CSS中的背景透明值控制,

使用命令行参数 `--disable-transparency` 可完全禁止透明功能.

使用命令行参数 `--disable-gpu` 禁用GPU后,可实现透明窗体的穿透点击

## WebKit子字段

### double_tap_to_zoom_enabled

> 属性:**是否启用两指缩放功能**

- Boolean - `true`允许, `false`不允许,默认 `false`.

### plugin

> 属性:**是否可加载扩展插件,比如Flash插件**

- Boolean - `true`允许, `false`不允许,默认 `true`.

## 其他字段

关于`package.json`的更多字段,请参考[Packages/1.0](http://wiki.commonjs.org/wiki/Packages/1.0)

### description

> 属性:**配置的描述说明,以`.`结束**

### version

> 属性:**应用版本信息**

### maintainers

> 属性:**维护成员**

```base
"maintainers":[ {
   "name": "Bill Bloggs",
   "email": "billblogs@bblogmedia.com",
  " web": "http://www.bblogmedia.com",
}]
```

### contributors

> 属性:**贡献者,与维护成员格式一致,但首个应为作者**

### bugs

> 属性:**提交错误的网址,如mail或http地址**

### licenses

> 属性:**许可证列表**
>
> ```base
> "licenses": [
> {
>  "type": "GPLv2",
>  "url": "http://www.example.com/licenses/gpl.html",
> }
> ]
> ```
>
> ### dependencies
>
> 属性:**必要依赖,组的顺序非常重要,较前条目具有较高优先级.**

```base
"dependencies": {
       "webkit": "1.2",
       "ssl": {
           "gnutls": ["1.0", "2.0"],
           "openssl": "0.9.8",
       },
}
```

### homepage

> 属性:**网站URL地址**



## package.json配置速查

### 示例

```json
{  
    /**指定程序的起始页面。*/  
 	"main": "index.html",  
    
    /**字符串必须是小写字母或者数字，可以包含.或者_或者-不允许带空格。name必须全局唯一。*/  
    "name": "demo",  
    
    /**程序描述*/  
    "description": "demo app of node-webkit",  
    
    /**程序版本号*/  
    "version": "0.1.0",  
    
    /**关键字*/  
    "keywords": ["demo","node-webkit"],  
    
    /**bool值，如果设置为false，将禁用webkit的node支持。*/  
    "nodejs": true,  
    /**  
    * 指定一个node.js文件，当程序启动时，该文件会被运行，启动时间要早于node-webkit加载html的时间。  
    * 它在node上下文中运行，可以用它来实现类似后台线程的功能。  
    * （不需要可注释不用）  
    */  
    "node-main": "js/node.js",  
    
    
    /**  
    * bool值。默认情况下，如果将node-webkit程序打包发布，那么只能启动一个该应用的实例。  
    * 如果你希望允许同时启动多个实例，将该值设置为false。  
    */  
    "single-instance": true,  
    
    /**窗口属性设置 */  
    "window": {  
        /**字符串，设置默认title。*/  
        "title": "demo",  
        /**窗口的icon。*/  
        "icon": "link.png",  
        /**bool值。是否显示导航栏。*/  
        "toolbar": false,  
        /**bool值。是否允许调整窗口大小。*/  
        "resizable": true,  
        /**是否全屏*/  
        "fullscreen": false,  
        /**是否在win任务栏显示图标*/  
        "show_in_taskbar": true,  
        /**bool值。如果设置为false，程序将无边框显示。*/  
        "frame": true,  
        /**字符串。窗口打开时的位置，可以设置为“null”、“center”或者“mouse”。*/  
        "position": "center",  
        /**主窗口的的宽度。*/  
        "width": 800,  
        /**主窗口的的高度。*/  
        "height": 670,  
        /**窗口的最小宽度。*/  
        "min_width": 400,  
        /**窗口的最小高度。*/  
        "min_height": 335,  
        /**窗口显示的最大宽度，可不设。*/  
        "max_width": 800,  
        /**窗口显示的最大高度，可不设。*/  
        "max_height": 670,  
        /**bool值，如果设置为false，启动时窗口不可见。*/  
        "show": true,  
        /**是否在任务栏显示图标。*/  
        "show_in_taskbar":true,  
        /**  
         * bool值。是否使用kiosk模式。如果使用kiosk模式，  
         * 应用程序将全屏显示，并且阻止用户离开应用。  
         * */  
        "kiosk": false  
    },  
    
    /**webkit设置*/  
    "webkit": {  
        /**bool值，是否加载插件，如flash，默认值为false。*/  
        "plugin": true,  
        /**bool值，是否加载Java applets，默认为false。*/  
        "java": false,  
        /**bool值，是否启用页面缓存，默认为false。*/  
        "page-cache": false  
    }  
}  
```





## RPGMaker原生配置

```json
{
    "name": "",
    "main": "index.html",
    "js-flags": "--expose-gc",
    "window": {
        "title": "",
        "toolbar": false,
        "width": 816,
        "height": 624,
        "icon": "icon/icon.png"
    }
}

```





1. 




# nw.js脚本API速查



## 安装原生模块

查看nw版本

```shell
nw.process.versions.nw
```

```SHELL
＃全局安装nw-gyp
npm install -g nw-gyp
＃设置目标NW.js版本
set npm_config_target=0.31.4
＃设置构建架构，ia32或x64，win10, osx为x64操作系统
set npm_config_arch=x64
set npm_config_runtime=node-webkit
set npm_config_build_from_source=true
set npm_config_node_gyp=C:\Users\NALA\AppData\Roaming\npm\node_modules\nw-gyp\bin\nw-gyp.js
 
#win10下还要设置python路径：
set PYTHON=C:\Users\NALA\.windows-build-tools\python27\python.exe
 
最后 npm install —msvs_version=2015 安装编译不成功，就多试几次，删除package-lock.json
 
```

## 窗口

> `Window` 是DOM中 顶层 `window`对象的包装类 . 可扩展操作以及接收窗口事件 .
>
> 每个 `Window`都是EventEmitter类实例 , 使用 `Window.on(...)`可响应窗口事件 .



### 获取当前窗口

有两种等价写法

```js
var win = require('nw.gui').Window.get();
var win2 = nw.Window.get();
```

但是实际上`win===win2`，因为窗口是一个非常重要的对象，所以这个是一个单例，不管是谁，获取到的对象都是一个。



### 打开新窗口

一共三个参数，其中，第二个是配置信息，详情参考配置中的窗口子字段。

```js
nw.Window.open('test.html', {}, function (new_win) {
    //新窗口创建时的回调函数
    new_win.on('focus', function () {
        console.log('点击了新窗口！');
    });
});
```



### 窗口的位置

#### 属性

窗口相对于显示器的位置

```js
nw.Window.get().x
nw.Window.get().y
```

#### 通过坐标移动

```js
nw.Window.get().moveTo(x, y)//移动窗口到指定位置,将窗口的左上角移动到指定的坐标
nw.Window.get().moveBy(x, y)//移动窗口到相对于当前窗口左上角的横纵偏移,比如窗口上移10px
```



#### 通过默认值移动

`position` String -指定的窗口位置,可选值: `null`(不固定) , `center`(屏幕居中) , `mouse`(鼠标所在位置)

```js
nw.Window.get().setPosition('mouse')//移动窗口到鼠标所在位置
```





### 窗口的大小

#### 属性

```js
nw.Window.get().width
nw.Window.get().height
```

#### 设置大小

```js
nw.Window.get().resizeTo(width, height)//重设窗口尺寸为 width 和 height
nw.Window.get().resizeBy(width, height)//调整窗口尺寸为相对于当前窗口尺寸的width 和 height,比如窗口加宽10px
```

#### 设置最大/最小值

```js
nw.Window.get().setMaximumSize(width, height)//设置窗口的最大宽高
nw.Window.get().setMinimumSize(width, height)//设置窗口的最小宽高
```

#### 是否允许玩家调整大小

```js
nw.Window.get().setResizable(true)
```



### 聚焦窗口

就是让窗口保持最前面,

```
nw.Window.get().focus()
```



### 永久置顶

```js
nw.Window.get().setAlwaysOnTop(false) //是否允许窗口总是置顶(在其余窗口上面)
```









### 控制台窗口（仅SDK模式下可用）

#### 打开/关闭控制台

```js
require('nw.gui').Window.get().showDevTools();//打开
require('nw.gui').Window.get().closeDevTools()；//关闭
```



#### 是否打开了控制台

```js
nw.Window.get().isDevToolsOpen()
```



#### 窗口最大化/最小化

```js
nw.Window.get().enterFullscreen();//全屏
nw.Window.get().leaveFullscreen() //退出全屏

nw.Window.get().minimize();//最小化

nw.Window.get().maximize()//最大化
用途:Linux和Window中最大化窗口 , Mac中放大窗口

win.minimize()
用途:Windows/Mac中最小化窗口 , Linux中图标化窗口
```

#### 隐藏窗口

```js
nw.Window.get().hide()
```



## 窗口事件和监听

### 最小化/最大化时

```js
// 监听最小化事件
nw.Window.get().on('minimize', function() {
  console.log('最小化了！');
});

// 移除最小化监听事件
nw.Window.get().removeAllListeners('minimize');

```



```js
// 监听最大化事件
nw.Window.get().on('maximize', function() {
  console.log('最大化了！');
});

// 移除最大化监听事件
nw.Window.get().removeAllListeners('maximize');
```



### 窗口关闭时

```js
nw.Window.get().on('close', function () {
    this.hide(); // 关闭窗口
    this.close(true); // 真正关闭窗口进程，注意一旦里面写false，就会无限循环
});

nw.Window.get().removeAllListeners('close');
```



### 窗口获得/失去焦点时

```js
//获取焦点事件
nw.Window.get().on('focus', function () {

});

nw.Window.get().removeAllListeners('focus');
```



```js
//失去焦点事件
nw.Window.get().on('blur', function () {

});

nw.Window.get().removeAllListeners('blur');
```



### 全屏时

```js
//失去焦点事件
nw.Window.get().on('enter-fullscreen', function () {

});

nw.Window.get().removeAllListeners('enter-fullscreen');
```



### 调试工具被关闭时

```js
//阻止游戏关闭
nw.Window.get().on('devtools-closed', function () {
    this.hide(); // 关闭窗口
    this.close(true); // 真正关闭窗口进程，注意一旦里面写false，就会无限循环
});


nw.Window.get().removeAllListeners('devtools-closed');
```





## 注册快捷键

```js
var option = {
    key : "Ctrl+Shift+A",
    active : function() {
        console.log("发现快捷键: " + this.key + " 被激活！"); 
    },
    failed : function(msg) {
        //报错信息
        console.log(msg);
    }
};

var shortcut = new nw.Shortcut(option);
nw.App.registerGlobalHotKey(shortcut);
  
```





下面是一些支持的快捷键

- 字母表的: `A`-`Z`
- 数字: `0`-`9`
- 功能键: `F1`-`F24`
- `Comma`
- `Period`
- `Tab`
- `Home` / `End` / `PageUp` / `PageDown` / `Insert` / `Delete`
- `Up` / `Down` / `Left` / `Right`
- `MediaNextTrack` / `MediaPlayPause` / `MediaPrevTrack` / `MediaStop`
- `Comma` or `,`
- `Period` or `.`
- `Tab` or `\t`
- `Backquote` or ```
- `Enter` or `\n`
- `Minus` or `-`
- `Equal` or `=`
- `Backslash` or `\`
- `Semicolon` or `;`
- `Quote` or `'`
- `BracketLeft` or `[`
- `BracketRight` or `[`
- `Escape`



## 打开默认应用

```js
// 默认浏览器中打开指定URL
nw.Shell.openExternal('https://github.com/nwjs/nw.js');

// 默认编辑器中打开指定文件。
nw.Shell.openItem('test.txt');

// 文件管理器中显示指定文件所在目录。
nw.Shell.showItemInFolder('test.txt');
```





## 访问剪切板

```js
// 获取系统中剪贴板对象
var clipboard = nw.Clipboard.get();

// 剪贴板中读取信息
var text = clipboard.get('text');
console.log(text);

// 向剪贴板写入
clipboard.set('I love NW.js :)', 'text');

// 清空剪贴板
clipboard.clear();
```



## 全局对象

```
global.a =1;
```























# 窗体重写速查

### 自定义类似血条的各种条

```js


    窗体名.prototype.饥饿条颜色1= function() {
        return this.textColor(4);
    };
    窗体名.prototype.饥饿条颜色2= function() {
        return this.textColor(5);
    };
    窗体名.prototype.饥饿条长度比例= function(饥饿度,满饥饿度) {
        return 饥饿度 / 满饥饿度;
    };

    //自定义内容，例如，当饥饿度比值低于某个值的时候，会显示红色
    窗体名.prototype.饥饿文字颜色 = function(饥饿度比值)
    {
        if(饥饿度比值<0.1)
            return this.textColor(10);
        else
            return this.textColor(0);
    }


    窗体名.prototype.画饥饿条 = function(actor, x, y, width)
    {
        var 当前饥饿= 20
        var 最大饥饿 =100 
        width = width || 186;
        var color1 = this.饥饿条颜色1();
        var color2 = this.饥饿条颜色2();
        var 饥饿度比值  = this.饥饿条长度比例(当前饥饿,最大饥饿)
        this.drawGauge(x, y, width, 饥饿度比值, color1, color2);//这个是用来画条的。比值就控制的是其长度。

        this.changeTextColor(this.textColor(0));//文字颜色
        this.drawText("饥饿度", x, y, 44);//绘制文字的内容和位置
         this.drawCurrentAndMax(当前饥饿, 最大饥饿, x, y, width,
                                this.饥饿文字颜色(饥饿度比值), this.normalColor());//绘制具体的数值。例如饥饿度是20，中国就会显示20
    
    }

```



### 自定义开始界面按钮

就是游戏一进去那个场景，有开始游戏，继续游戏那个。

```js
Window_TitleCommand.prototype.makeCommandList = function () {
    this.addCommand(TextManager.newGame, 'newGame');
    this.addCommand(TextManager.continue_, 'continue', this.isContinueEnabled());
    this.addCommand(TextManager.options,   'options');

    this.addCommand("测试",   'test');//第一个是按钮名称，第二个是绑定的方法名
};


//重写窗体
Scene_Title.prototype.createCommandWindow = function () {
    this._commandWindow = new Window_TitleCommand();
    this._commandWindow.setHandler('newGame', this.commandNewGame.bind(this));
    this._commandWindow.setHandler('continue', this.commandContinue.bind(this));
    this._commandWindow.setHandler('options',  this.commandOptions.bind(this));
    
    //test方法在这里写，以此类推，可以写很多的方法。
    this._commandWindow.setHandler('test',  this.test.bind(this));
    this.addWindow(this._commandWindow);
};

//这个是test方法的具体功能，也就是点击之后触发的事件
Scene_Title.prototype.test  = function(){
    console.log("点击了按钮！！！")
}
```





### 自定义菜单指令

```js
(() => {

    //1.自己的自定义窗体
    function Window_Test() {
        this.initialize.apply(this, arguments);
    }

    //2.继承一个窗体类，根据不同需求可以自行改动
    Window_Test.prototype = Object.create(Window_Command.prototype);

    //3.把构造函数指向自己
    Window_Test.prototype.constructor = Window_Test;

    //4.写初始化函数
    Window_Test.prototype.initialize = function (x, y) {
        Window_Command.prototype.initialize.call(this, x, y)//xy代表位置
        this.refresh();//刷新窗口
        this.activate();//激活
    }

    //窗口类的核心方法，自定义代码就在这里写
    Window_Test.prototype.makeCommandList = function () {
        this.addCommand("自定义的指令", '指令名', true);//指令名是代码内部调用的，可以通过setHandler来使用
        //自定义代码，都在这里写。
    }


    //右侧的说明区域
    function 自定义HELP(){
        this.initialize.apply(this, arguments);
    }
    自定义HELP.prototype = Object.create(Window_Base.prototype);
    自定义HELP.prototype.constructor = 自定义HELP;

    自定义HELP.prototype.initialize = function () {
        var x = 250;
        var y = 0;
        var width = 500;
        var height = this.fittingHeight(2);//行宽
        Window_Base.prototype.initialize.call(this, x, y, width, height);
        this._text = '';
    }

    //窗口类的核心方法，自定义代码就在这里写
    自定义HELP.prototype.setInfo = function(text){
        this.contents.clear();
        this._text =text;
        this.drawTextEx(this._text, this.textPadding(), 0);
    }



    //这个就是点击指令后的场景
    function Scene_Test() {
        this.initialize.apply(this, arguments)
    }

    Scene_Test.prototype = Object.create(Scene_MenuBase.prototype);//自行查看窗体所在的场景
    Scene_Test.prototype.constructor = Scene_Test;
    Scene_Test.prototype.initialize = function () {
        Scene_MenuBase.prototype.initialize.call(this)
    }

    Scene_Test.prototype.create = function () {
        Scene_MenuBase.prototype.create.call(this)
        this.createTestWindow();
        this.createHelpWindow();
        this.bindCommands();
    }

    Scene_Test.prototype.start = function () {
        Scene_MenuBase.prototype.start.call(this)
        this.windowTest.refresh();
    }

    Scene_Test.prototype.createHelpWindow =function(){
        this._helpWindow = new 自定义HELP();
        this._helpWindow.setInfo("hello world");
        this.addWindow(this._helpWindow);
    } 

    Scene_Test.prototype.createTestWindow = function () {

        var x = 0;
        var y = 0;
        // console.log(xx,yy)
        this.windowTest = new Window_Test(x, y)
        this.addWindow(this.windowTest);//根据需求，可以添加很多个窗口

    }

    Scene_Test.prototype.bindCommands = function () {
        this.windowTest.setHandler('ok', this.windowOK.bind(this));
        this.windowTest.setHandler('cancel', this.windowCancel.bind(this));
    }

    //当点击时触发
    Scene_Test.prototype.windowOK = function () {
        console.log("ok")
        this.windowTest.activate();

        // 监听按键，改变说明区域的文字
        this._helpWindow.setInfo("我是自定义的指令哟");

    }

    //当返回时除法
    Scene_Test.prototype.windowCancel = function () {
        console.log("cancel")
        SceneManager.pop();//返回上一级
    }
   



    Window_MenuCommand.prototype.addOriginalCommands = function () {//这个方法是专门给我们提供的，可以用来重写。
        //在菜单指令中添加指令，但是要注意，如果只写了这个，是没有效果的，
        //必须在createCommandWindow中，给test注册响应函数才能点进去
        this.addCommand('指令名', 'test', true);
    }

       
    Scene_Menu.prototype.commandTest = function () {
        SceneManager.push(Scene_Test);
    }


    Scene_Menu.prototype.createCommandWindow = function () {

        this._commandWindow = new Window_MenuCommand(0, 0);
        this._commandWindow.setHandler('item', this.commandItem.bind(this));
        this._commandWindow.setHandler('skill', this.commandPersonal.bind(this));
        this._commandWindow.setHandler('equip', this.commandPersonal.bind(this));
        this._commandWindow.setHandler('status', this.commandPersonal.bind(this));
        this._commandWindow.setHandler('formation', this.commandFormation.bind(this));
        this._commandWindow.setHandler('options', this.commandOptions.bind(this));
        this._commandWindow.setHandler('save', this.commandSave.bind(this));
        this._commandWindow.setHandler('gameEnd', this.commandGameEnd.bind(this));
        this._commandWindow.setHandler('cancel', this.popScene.bind(this));
        this._commandWindow.setHandler('test', this.commandTest.bind(this));
        this.addWindow(this._commandWindow);
    }

})()
```



### 状态界面

```javascript
(function () {

    //1.创建一个函数，名字就是你自定义窗体的名字

    function 窗体名() {
        this.initialize.apply(this, arguments);
    }
    //2.继承Window_Base类
    窗体名.prototype = Object.create(Window_Base.prototype);
    窗体名.prototype.constructor = 窗体名;

    //3.初始化窗体大小
    var statusWindow = {
        x: 240,
        y: 0,
        width: 576,
        height: 624
    };
    窗体名.prototype.initialize = function () {
        Window_Base.prototype.initialize.call(this, statusWindow.x, statusWindow.y,
            statusWindow.width, statusWindow.height);
    };

    //4.写刷新函数，系统会自动调用这个函数
    窗体名.prototype.refresh = function () {
        this.contents.clear();
        this.drawText("hello world", 144, 0, 200);
    };



    //5.将窗口布局到游戏里面
    Scene_Menu.prototype.createStatusWindow = function () {
        this._statusWindow = new 窗体名();
        this.addWindow(this._statusWindow);
    };

})();
```





地图界面

```js
(function () {
  //1.创建一个函数，名字就是你自定义窗体的名字
  function 窗体名() {
    this.initialize.apply(this, arguments);
  }
  //2.继承Window_Base类
  窗体名.prototype = Object.create(Window_Base.prototype);
  窗体名.prototype.constructor = 窗体名;

  //3.初始化窗体大小
  窗体名.prototype.initialize = function () {
    Window_Base.prototype.initialize.call(this, 0, 0, 100, 100);//分别代表位置和长宽
    this.drawText('莲华', 5, 5, 100, 'left');
  };

  //4.写创建窗体函数
  Scene_Base.prototype.创建窗体 = function () {
    this.addWindow(new 窗体名());
  };


  //5.创建窗体
  var _Scene_Map_createDisplayObjects = Scene_Map.prototype.createDisplayObjects;
  Scene_Map.prototype.createDisplayObjects = function () {
    _Scene_Map_createDisplayObjects.call(this);
    this.创建窗体();
  };

})();
```





### 自定义右键菜单按钮

这个是指左下角那个窗口

```js
//构造函数体
function Window_PlayerCount() {
    this.initialize.apply(this, arguments);
}
//继承自Window_Base
Window_PlayerCount.prototype = Object.create(Window_Base.prototype);
//设定构造函数
Window_PlayerCount.prototype.constructor = Window_PlayerCount;
//初始化
Window_PlayerCount.prototype.initialize = function (x, y) {
    var width = 240;
    var height = this.fittingHeight(1);
    Window_Base.prototype.initialize.call(this, x, y, width, height);
    this.drawText('团伙中有' + $gameParty.members().length + '人', 0, 0, 200);
};
//重写Scene_Menu，加入我们自定窗口
Scene_Menu.prototype.create = function () {
    Scene_MenuBase.prototype.create.call(this);
    this.createCommandWindow();
    this.createGoldWindow();
    this.createStatusWindow();
    //加入我们自己的窗口
    var win = new Window_PlayerCount(0, this._commandWindow.height);
    this.addWindow(win);
};
```







### 自定义精灵类

```js
//我们对系统提供的精灵类进行复制，创建一个"自定义精灵类"
function 自定义精灵类() {
    this.initialize.apply(this, arguments);
}
自定义精灵类.prototype = Object.create(Sprite.prototype);
自定义精灵类.prototype.constructor = 自定义精灵类;
自定义精灵类.prototype.initialize = function () {
    Sprite.prototype.initialize.call(this);
    //以上为固定写法，不需要弄清楚
    //以下是设置这个精灵类的共同属性，所有这个对象构造的精灵都具有的属性，类比C++中的类
    /*设置框架，即精灵所处矩形范围，精灵的活动区域被限制在此框架内，四个参数分别为左上角的X,Y的坐标，宽度（横），长度（竖）
    需要注意的是X和Y一般是负数，如果大于0图片就会往屏幕外移动*/
    this.setFrame(0, 0, 1000, 1500);

    //运行创造子精灵的函数
    this.createAll();

    //绘制位图（bitMap）的文字函数
    this.drawText();

    //move作用和setFrame是一样的，两个数值相当于把框架沿x轴y轴移动多少单位
    this.move(20, 10);
};

自定义精灵类.prototype.createAll = function () {
    //使用图片来建立精灵
    this._clock = new Sprite(ImageManager.loadBitmap('img/pictures/', "SF_Actor3_8", true));
    //使用系统提供的位图对象建立精灵,这里使用的是一个空位图，具体的文字会用drawText函数上描绘
    this._cont = new Sprite(new Bitmap(380, 418));       //定义位图的宽和高      
    //anchor，范围0-1，设置精设置绘制精灵的起始坐标，0.5可以令其居中显示
    this._clock.anchor.x = this._clock.anchor.y = 0.5;         
    /*这里的setFrame是精灵中的精灵活动范围，低级精灵不能超过其容器活动范围，不然无法显示
    _clock精灵属于mySprite类，其活动范围不能超过他的类，如果不setFrame，系统将会给一个默认值*/
    this._clock.setFrame(0, 0, 100, 100);
    this._clock.move(32, 42);                         
    this.addChild(this._clock);
    this.addChild(this._cont);
};

//这里定义了一个函数，是用于对前面构建_cont精灵所用位图进行描绘的
自定义精灵类.prototype.drawText = function () {
    this._cont.bitmap.fontSize = 30;    //设置字型大小
    this._cont.bitmap.textColor ="rgb(255,255,255)"||'red';  //设置字体颜色，可用RGB表示法或者英文字符
    //'' +：根据JavaScript语法规则，可以将后面的数据强制转化为字符串，这里$spriteTest.Parameters.text原本就是字符串，这样做法是为了防止出错
    var text = "测试文本 ";  //设置文本
    this._cont.bitmap.drawText(text,0, 88, 136, 44);
}


SUBupdate = Scene_Map.prototype.update;
Scene_Map.prototype.update = function () {
    SUBupdate.call(this);
    this.myMapSprite = new 自定义精灵类();
    //前面已经说过，在构建对象的函数里面已经设置了对象初始值，这里就不需要再设置了
    this.addChild(this.myMapSprite);
    //用addChild函数将精灵加入场景中
};
```









# 文件和文件格式速查

## audio

### 文件分类

存放音频素材，下分4个子类

- bgm（background music）：背景音乐
- bgs（background sound）：背景音效：
- me（music effect）：音乐效果
- se（sound effect）：声音效果

### 音频分类

- m4a文件：用于手机端，加密后变成rpgmvm文件。
- ogg文件：用于PC端，加密后形成rpgmvo文件。



## data

### 文件分类

- Actor.json——角色数据

- Animations.json——动画模块

- Armor.json——装备数据

- Classes.json——职业数据

- CommonEvents.json——公共事件数据

- Enemies.json——敌人数据

- Items.json——道具数据

- MapXXX.json——各地图的详细信息（包括事件

- MapInfos.json——各地图的大致信息

- Skills.json——技能数据

- States.json——状态数据

- System.json——系统、类型、用语

- Tileset.json——图块组模块

- Troop.json——敌群数据

- Weapons.json——武器数据

  

## fonts

游戏的字体文件



1. 去根目录下fonts文件夹中

2. 打开gamefont.css文件，这个里面就存着字体的信息。

   ```css
   @font-face {
       font-family: GameFont;
     	/*url里面就是字体文件的路径*/
       src: url("mplus-1m-regular.ttf");
   }
   
   .IIV::-webkit-media-controls-play-button,
   video::-webkit-media-controls-start-playback-button {
       opacity: 0;
       pointer-events: none;
       width: 5px;
   }
   ```

3. 把自己下载的ttf文件放入fonts文件夹中，把url里面的名字换成你下载的就行了



顺便一说，fonts文件都放在了C:\Windows\Fonts中，有需要可以自取。









## icon

游戏的图标文件

## img

游戏中所有的图片素材





## js

游戏源代码，包括官方的代码和插件代码



## movies

游戏中的视频文件





## 素材格式和尺寸



| 素材类型     | 大小        |
| ------------ | ----------- |
| 立绘         | 高度为600px |
| CG           | 816\*624px  |
| 脸图         | 144\*144px  |
| 一个图块大小 | 48*48px     |
|              |             |
| 标题图片     | 816*624px   |





## 常用屏幕分辨率

- PC：16:9

  1920*1080

  1600*900

## 文件目录

- animations：动画特效

- battlebacks1：战斗背景图，一般都是地面或者战斗近景图

- battlebacks2：战斗的远景图，远景图可以省略，近景图必须指定。

- characters：角色的行走图，或者其他物品的动作图，大小为48*48

  **在文件名前面加上半角符号“$”，那么该文件就只能容纳一个角色元。**

- enemies：敌人的战斗图，也就是战斗时看到的立绘

- faces：各种角色的头像，144*144

- parallaxes：远景图，尺寸没有限制

- pictures：这些图片可以通过事件指令中的显示图片指令显示在游戏中，图片尺寸大小不限。

- titles1：标题的背景图

- titles2：标题背景图的边框，图片的大小为 816x624 ，Titles1 包含标题画面的背景，titles2 则主要是边框，使用它们可以组成标题画面。











# 插件脚本案例编写速查



## 自定义事件的触发条件

让RPGMV的事件可以自定义触发条件。例如我正在编写一个有时间系统的游戏，我希望这个事件在早晨或者下午触发。改如何实现呢？

可以考虑使用事件的备注来实现。例如可以备注`<触发条件:早晨，中午，下午>`

编写插件

```js
Game_Event.prototype.meetsConditions = function(page) {
    var c = page.conditions;
    if (c.switch1Valid) {
        if (!$gameSwitches.value(c.switch1Id)) {
            return false;
        }
    }
    if (c.switch2Valid) {
        if (!$gameSwitches.value(c.switch2Id)) {
            return false;
        }
    }
    if (c.variableValid) {
        if ($gameVariables.value(c.variableId) < c.variableValue) {
            return false;
        }
    }
    if (c.selfSwitchValid) {
        var key = [this._mapId, this._eventId, c.selfSwitchCh];
        if ($gameSelfSwitches.value(key) !== true) {
            return false;
        }
    }
    if (c.itemValid) {
        var item = $dataItems[c.itemId];
        if (!$gameParty.hasItem(item)) {
            return false;
        }
    }
    if (c.actorValid) {
        var actor = $gameActors.actor(c.actorId);
        if (!$gameParty.members().contains(actor)) {
            return false;
        }
    }
    
    //////////////这里是增加的代码/////////
     var 触发条件  = $dataMap.events[this._eventId].meta.触发条件
    时间 = $gameVariables.value(3);//获得游戏中控制时间的变量
    //这个变量的不同数值代表不同时间段。
    
    if (触发条件) {
        //如果当前游戏时间为1，而且备注中出现了早晨，那么这个事件就会被触发。以此类推。
        if(时间==1 &&触发条件.indexOf("早晨")!== -1 )
        {
            return true;
        }
        if(时间==2 &&触发条件.indexOf("上午")!== -1 )
        {
            return true;
        }
        if(时间==3 &&触发条件.indexOf("中午")!== -1 )
        {
            return true;
        }
        if(时间==4 &&触发条件.indexOf("下午")!== -1 )
        {
            return true;
        }
        if(时间==0 &&触发条件.indexOf("晚上")!== -1 )
        {
            return true;
        }
  
    }
    /////////////////////
    
    return true;
};

```



## 自定义按键映射



在游戏开发中经常出现需要自己添加一个新按钮或者快捷键的需求。

实现自定义映射其实很简单，我们首先需要知道JS里面如何给一个对象增加属性。其中就有一个**对象键值对的赋值**。不懂的可以看我的JS基础。

在脚本中，左边写所映射按键的键码，右边写你给这个键起的keyName。

```javascript
Input.keyMapper[65] = "A";
```

这样就把A，这个按键绑定到MV里面了。

具体的键码可以参考附录1。





```js
Input.isPressed('A')  //按键是否正在被按下
Input.isTriggered() //按键刚刚是否按下
Input.isRepeated() //按键是否连续点击，或者一直处于按下状态
Input.isLongPressed() //按键是否一直按下
```



但是这就有一个问题，在脚本中如果直接使用if语句，会造成一些问题





## 禁用鼠标

```js
TouchInput._onMouseDown = function(event) {
	// 什么都不要写
};
```



## 修改姓名输入界面的字符

```js
Window_NameInput.LATIN1 =
        [ '赵','钱','孙','李','王',  '马','朱','雷','冯','叔',
          '张','闫','何','庞','郭',  '魏','田','和','依','姬',
          '白','丽','展','羽','彭',  'k','l','穆','奴','欧',
          '文','礼','月','日','芳',  '鑫','梦','世','叶','晨',
          '华','如','幸','雅','知',  '昕','微','杰','悦','翊',
          '荣','美','梅','兰','竹',  '菊','珍','镇','|','兴',
          '零','一','二','三','四',  '杨','#','$','百','己',
          '五','六','七','八','九',  '真','鉴','定','为','建',
          '雷','电','尔','这','边',  '可','以','点','换页','确认' ];
Window_NameInput.LATIN2 =
        [ '熊','大','二','砍','树',  '光','头','强','狗','猫',
          '克','苏','鲁','小','师',  '丛','雨','时','乃','宁',
          '斯','坦','纳','亚','总',  '锉','刀','枣','子','姐',
          '洛','必','达','桐','人',  '宫','保','鸡','丁','香',
          '深','见','夏','彦','爷',  '曼','珠','沙','华','ū',
          '少','中','哥','狡','滑',  '莲','花','我','老','婆',
          '奈','亚','拉','托','提',  '普','信','男','女','子',
          '帽','子','社','绊','爱',  '皮','卡','丘','冒','险',
          '萤','雪','映','月','蛇',  '人','乔','的','换页','确认' ];
Window_NameInput.RUSSIA =
        [ 'А','Б','В','Г','Д',  'а','б','в','г','д',
          'Е','Ё','Ж','З','И',  'е','ё','ж','з','и',
          'Й','К','Л','М','Н',  'й','к','л','м','н',
          'О','П','Р','С','Т',  'о','п','р','с','т',
          'У','Ф','Х','Ц','Ч',  'у','ф','х','ц','ч',
          'Ш','Щ','Ъ','Ы','Ь',  'ш','щ','ъ','ы','ь',
          'Э','Ю','Я','^','_',  'э','ю','я','%','&',
          '0','1','2','3','4',  '(',')','*','+','-',
          '5','6','7','8','9',  ':',';',' ','','OK' ];
Window_NameInput.JAPAN1 =
        [ 'あ','い','う','え','お',  'が','ぎ','ぐ','げ','ご',
          'か','き','く','け','こ',  'ざ','じ','ず','ぜ','ぞ',
          'さ','し','す','せ','そ',  'だ','ぢ','づ','で','ど',
          'た','ち','つ','て','と',  'ば','び','ぶ','べ','ぼ',
          'な','に','ぬ','ね','の',  'ぱ','ぴ','ぷ','ぺ','ぽ',
          'は','ひ','ふ','へ','ほ',  'ぁ','ぃ','ぅ','ぇ','ぉ',
          'ま','み','む','め','も',  'っ','ゃ','ゅ','ょ','ゎ',
          'や','ゆ','よ','わ','ん',  'ー','～','・','＝','☆',
          'ら','り','る','れ','ろ',  'ゔ','を','　','カナ','決定' ];
Window_NameInput.JAPAN2 =
        [ 'ア','イ','ウ','エ','オ',  'ガ','ギ','グ','ゲ','ゴ',
          'カ','キ','ク','ケ','コ',  'ザ','ジ','ズ','ゼ','ゾ',
          'サ','シ','ス','セ','ソ',  'ダ','ヂ','ヅ','デ','ド',
          'タ','チ','ツ','テ','ト',  'バ','ビ','ブ','ベ','ボ',
          'ナ','ニ','ヌ','ネ','ノ',  'パ','ピ','プ','ペ','ポ',
          'ハ','ヒ','フ','ヘ','ホ',  'ァ','ィ','ゥ','ェ','ォ',
          'マ','ミ','ム','メ','モ',  'ッ','ャ','ュ','ョ','ヮ',
          'ヤ','ユ','ヨ','ワ','ン',  'ー','～','・','＝','☆',
          'ラ','リ','ル','レ','ロ',  'ヴ','ヲ','　','英数','決定' ];
Window_NameInput.JAPAN3 =
        [ 'Ａ','Ｂ','Ｃ','Ｄ','Ｅ',  'ａ','ｂ','ｃ','ｄ','ｅ',
          'Ｆ','Ｇ','Ｈ','Ｉ','Ｊ',  'ｆ','ｇ','ｈ','ｉ','ｊ',
          'Ｋ','Ｌ','Ｍ','Ｎ','Ｏ',  'ｋ','ｌ','ｍ','ｎ','ｏ',
          'Ｐ','Ｑ','Ｒ','Ｓ','Ｔ',  'ｐ','ｑ','ｒ','ｓ','ｔ',
          'Ｕ','Ｖ','Ｗ','Ｘ','Ｙ',  'ｕ','ｖ','ｗ','ｘ','ｙ',
          'Ｚ','［','］','＾','＿',  'ｚ','｛','｝','｜','～',
          '０','１','２','３','４',  '！','＃','＄','％','＆',
          '５','６','７','８','９',  '（','）','＊','＋','－',
          '／','＝','＠','＜','＞',  '：','；','　','かな','決定' ];
```

## 自定义姓名输入

```js
$gameParty.leader()._name =  prompt("请输入姓名！")
```



## 修改存档最大数量

直接修改数字。

```javascript
DataManager.maxSavefiles = function() {
    return 你想要的数字;
};
```



## 自定义存档内容以及自动读档存档



RPGMV如果想要存档，在以往只能通过 **场景控制**中的**打开存档界面**进行保存。这就会产生一个很难解决的需求问题。

如何在RPGMV播放剧情的时候存档？比如在制作GalGame的时候，如何做到随时存档？

而且在自动保存的时候，也需要保存很多自定义的变量。如何操作呢？



```js
/*:
 * @plugindesc
 * 管理和处理游戏剧情用
 * 
 * @help
 * 本插件提供了全局存档的控制接口，以及如何保存读取自定义的数据。如果没有自定义数据，不要修改$gloablData的内容即可
 * 如果想要控制全局存档需要两个步骤
 * 1. 在$storyGlobalInfo中添加变量
 * 2. 在使用后要记得保存，例如：
 *      $gloablData.某个自定义数据 = true;
 *      StoryControl.autoSave();
 *      window.close()
 */

class StoryControl {
    //自动保存
    static autoSave(savePosition = 1) {//默认第一个存档，可以改
        console.log("保存成功")
        $gameSystem.onBeforeSave();
        DataManager.saveGame(savePosition)
    }
    //自动加载
    static autoLoad(savePosition = 1) {

        DataManager.loadGame(savePosition)
    }

    //加载存档的全局数据
    static loadStoryInfo() {

        //游戏每次加载的时候，首先加载存档，如果没有存档，那么就先保存再加载。

        var tempGlobalInfo = DataManager.loadGlobalInfo() || [];
        try {
            //tempGlobalInfo[0]是个null，真正的数据在1
            $gloablData = tempGlobalInfo[1].自定义数据;
        } catch (error) {
            //要是第一次游戏，那么递归一下，再次加载存档
            this.autoSave();
            //把读取的数据存到$gloablData，以便使用
            $gloablData = this.loadStoryInfo();
        }
        return $gloablData;
    }

    //保存全局数据
    static saveGlobalInfo(){
        var tempGlobalInfo = DataManager.loadGlobalInfo();
        tempGlobalInfo[1].自定义数据=$gloablData;
        DataManager.saveGlobalInfo(tempGlobalInfo)
    }
}


//自定义数据，这个是初始值，之后会被覆盖
$gloablData = {
    某数据: 0,
};


//重写全局存档的内容
DataManager.makeSavefileInfo = function () {
    var info = {};
    info.globalId = this._globalId;
    info.title = $dataSystem.gameTitle;
    info.characters = $gameParty.charactersForSavefile();
    info.faces = $gameParty.facesForSavefile();
    info.playtime = $gameSystem.playtimeText();
    info.timestamp = Date.now();

    //如果希望保存自定义的内容，只需要给info添加属性即可。
    //但是为了更好地获得数据，可以用一个新变量$gloablData来保存这个值。
    info.自定义数据 = $gloablData;//自定义的数据
    return info;
};

```





## 弹幕系统



在一些创意性游戏中，弹幕可以增加氛围和趣味性。



```js
/*:
* @plugindesc  弹幕系统
* @author  闫辰祥
* @help  可以发送弹幕
* 使用时可以使用默认值，比如 new Danmaku(['测试','文字'])
* 也可以详细进行配置，比如  new Danmaku(['测试','文字'],{color:"red"}),
* 也可以同时对多个弹幕进行配置，比如  new Danmaku(['测试','文字',"123"],{color:"red"},{fontSize:"100px"})
* new Danmaku(['测试','文字'],{color:"red",fontSize:"100px"})
*/



class DannmakuConfig {
    constructor(config) {
        config = config || {};
        this.time = config.time || 1;//每隔几秒发送一个弹幕
        this.speed = config.speed || 5;//弹幕速度
        this.color = config.color || 'black';//弹幕颜色
        this.fontSize = config.fontSize || '30px';//弹幕大小
    }
}

class Danmaku {
    constructor(texts, ...config) {
        let tempThis = this
        let configs = [new DannmakuConfig()]//
        for (let i = 0; i < config.length; i++) {
            configs[i]= new DannmakuConfig(config[i])
        }

        for (let i = 0; i < texts.length; i++) {
            let useconfig = {}
            if(i>=configs.length)
            {
                useconfig =  configs[configs.length-1]
        
            }else{
                useconfig =  configs[i]
            }

            setTimeout(function () {
 
               tempThis.send(texts[i],useconfig)
            }, i*useconfig.time* 1000)
        }
    }

    send(text, config) {
        let 弹幕 = document.createElement("div");
        let node = document.createTextNode(text);
        弹幕.appendChild(node);

        弹幕.style.position = "fixed";
        弹幕.style.zIndex = "20"
        弹幕.style.whiteSpace = 'nowrap '
        let height = window.innerHeight;
        let width = window.innerWidth;
        弹幕.style.top = Math.random() * height * 0.8 + "px";
        弹幕.style.left = width - 300 + "px"

        //可修改变量
        弹幕.style.color = config.color;
        弹幕.style.fontSize = config.fontSize;
        

        document.body.appendChild(弹幕);

        let timeControler = setInterval(() => {
            弹幕.style.left = parseInt(弹幕.style.left) - config.speed + "px";
            if (parseInt(弹幕.style.left) < -50) {
                clearInterval(timeControler);
                弹幕.parentNode.removeChild(弹幕)
            }
        }, 10);
    }
}
```



## 成就系统

成就系统理论上来说并不是游戏内的一部分，不过随着游戏理论的发展，成就已经成了游戏内不可或缺的一部分。今天我就来给各位科普一下在RPGMV中，成就系统的编写原理。







在css文件夹下创建achievement.css文件

```css
.achievment-node{
    background-color: rgba(0, 0, 0, 0.4);

    z-index: 10;
    position: absolute;
    left: 50%;
    top: 0%;
    transform: translate(-50%, 0);
    animation: showAchievement 2s;
    color :white;
    
    padding:5%;
}
.title-node{
    font-size : x-large;
}

.info-node{
    font-size: large;
}

@keyframes showAchievement {
    0% {
        top: -100px;
    }

    50% {
        top: 50px;
    }

    70% {
        top: 50px;
    }

    100% {
        top: 0px;
    }
}
```



```js
/*:
 * @plugindesc  成就系统
 * @author  闫辰祥
 * @help  直接使用 例如 $gameAchievement.add("梦之始","开始游戏")
 */


(function () {
    var stylesheet = document.createElement("link")
    stylesheet.rel = "stylesheet"
    stylesheet.href = "./css/achievement.css"
    stylesheet.type = "text/css"
    document.head.appendChild(stylesheet)
})()




//游戏成就系统
var $gameAchievement = {}
$gameAchievement._achievements = [];

$gameAchievement.add = function (title, info) {

    //如果已经获得了这个成就，那么就不添加这个了
    for (let i = 0; i < $gameAchievement._achievements.length; i++) {
        if ($gameAchievement._achievements[i].title == title)
            return false;

    }
    //添加成就信息
    var achievmentRecord = { title, info }
    $gameAchievement._achievements.push(achievmentRecord);


    var achievmentNode = document.createElement("div");
    achievmentNode.classList += "achievment-node"

    var titleNode = document.createElement("div");
    titleNode.appendChild(document.createTextNode("获得成就：" + title))
    titleNode.classList += "title-node"


    var infoNode = document.createElement("div");
    infoNode.appendChild(document.createTextNode(info))
    infoNode.classList += "info-node"

    achievmentNode.appendChild(titleNode);
    achievmentNode.appendChild(infoNode);
    document.body.appendChild(achievmentNode);



    setTimeout(() => {

        achievmentNode.parentNode.removeChild(achievmentNode);

    }, 10000)

    return true;
}


```











## 类废都物语的鼠标点击触发事件

```js
/*:
* @plugindesc 本插件用于给一个事件添加可以鼠标左键点击的效果
* 
* @author 闫辰祥
* 
*
* 
* 
* @help 
* 插件指令：
* 事件点击 开始
* 事件点击 关闭
* 
* 安装好之后，用鼠标点击事件，然后事件就会被触发
* 对不希望触发的事件，可以在备注加上   <不可点击>  来关闭触发
*
*
* 技术群：529245311
*/


var 闫 = 闫 || {};

闫.Parameters = PluginManager.parameters('闫_鼠标触发事件');


var _Game_Interpreter_pluginCommand = Game_Interpreter.prototype.pluginCommand;
Game_Interpreter.prototype.pluginCommand = function (command, args) {
    _Game_Interpreter_pluginCommand.call(this, command, args);

    if (command === '事件点击') {
        switch (args[0]) {
            case '开始':
                可以开始点了 = true
                break;
            case '关闭':
                可以开始点了 = false
                break;
        }
    }
};

var 可以开始点了 = true
var temp_TouchInput_onMouseDown = TouchInput._onMouseDown

TouchInput._onMouseDown = function (event) {
    temp_TouchInput_onMouseDown.call(this, event)

    if($dataMap == null)
    {
        return
    }
    if (event.button === 0 && 可以开始点了) {
        var x = Graphics.pageToCanvasX(event.pageX);
        var y = Graphics.pageToCanvasY(event.pageY);

        x = $gameMap.canvasToMapX(TouchInput.x);
        y = $gameMap.canvasToMapY(TouchInput.y);

        var event = $gameMap.eventsXy(x, y)[0];

       
        var eventId = $gameMap.eventIdXy(x,y);
        if (!event)
            return
        if(!event.page())
            return
        if ($dataMap.events[eventId].meta.不可点击)
            return

        event.start();
    }
};

```





## 类仙剑1的对某事件使用物体

```js
/*:
 * @plugindesc  可以对某一个事件来使用道具
 * @author  闫辰祥
 * @help   首先对需要使用的事件写上注释，格式为 <name:xxx>
 * case里面的是使用道具的名称  meta.name就是对应的事件名称
 */

function itemUse(itemName) {

    var eventID = getEventID();
    if (!eventID) {
        $gameMessage.add("似乎没有什么用");
        $gameAchievement.add("虚空对线", "对着空地使用道具")
        return false;
    }

    var metaData = $dataMap.events[eventID].meta
    switch (itemName) {
        case "钥匙":
            if (metaData.name == "门") {
                if (metaData.switch) {
                    $gameSwitches.setValue(metaData.switch, true);
                }
                if (metaData.info) {
                    $gameMessage.add(metaData.info);
                }
                return true;
            }

            break;
        case "除草镰":
            if (metaData.name == "草") {
                $gameSelfSwitches.setValue([metaData.mapID, eventID, 'A'], true)
                let value = $gameVariables.value(1) + 1
                $gameVariables.setValue(1, value);
                $gameMessage.add("目前一共除草了" + $gameVariables.value(1) + "个")

                if ($gameVariables.value(1) == 15)
                    $gameAchievement.add("除草狂魔", "除了15个艹")
                if ($gameVariables.value(1) == 25)
                    $gameAchievement.add("手不累吗？", "除了所有的草")
                return true;
            }
            else if (metaData.name == "草字头") {
                if (metaData.word == "荚") {
                    $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                    return true;
                }
            }
            else if (metaData.name == "方妍") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                return true;
            }
            else if (metaData.name == "草席") {
                $gameMessage.add("（还是不要动人家东西吧，）")
                return true;
            }
            else if (metaData.name == "芳") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                return true;
            }    
            else if (metaData.name == "小兰") {
                $gameMessage.add("，，，，，，")
                $gameMessage.add("你在干什么？")
                $gameMessage.add("（糟糕，她好像生气了）")
                $gameAchievement.add("见人就砍", "试图用除草镰去砍小兰")
                return true;
            }

            else if(metaData.name == "花"){
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                $gameAchievement.add("辣手摧花","除掉了花")
                return true;
            }

            else if(metaData.name == "莲华"){
                console.log(metaData.name)
                if($gameTroop._inBattle){
                    $gameSwitches.setValue(30, true);
                }
                return true;
            }
         
            break;
        case "苗":
            if (metaData.name == "犬") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                $gameAchievement.add("我虽然不是人，但你是真的狗", "把犬变成猫")
                return true;
            }
            break;
        case "伐木斧":
            if (metaData.name == "栅") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                $gameMessage.add("砍掉了栅的木，掉落了册")
                return true;
            }
            
            else if (metaData.name == "栏") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                $gameMessage.add("砍掉了栅的木，掉落了兰")
                return true;
            }
            else if (metaData.name == "樯") {
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                $gameMessage.add("木墙被轻易地砍坏了")
                return true;
            }
            else if (metaData.name == "树") {
                $gameMessage.add("乱砍别人家树，人家会生气的。")
                $gameAchievement.add("光头强", "不分青红皂白砍别人的树")
                return true;
            }
            else if(metaData.name == "渠"){
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                return true;
            }
            else if(metaData.name == "桌子"){
                $gameMessage.add("（如果把人家桌子砍坏了，估计会被打死吧——__——）")
                return true;
            }
            else if(metaData.name == "椅子"){
                $gameMessage.add("（为什么最近总想着去砍东西呢）")
                return true;
            }
            else if(metaData.name == "木门"){
                $gameMessage.add("门被劈开了")
                $gameSelfSwitches.setValue([$gameMap._mapId, eventID, 'A'], true)
                return true;
            }
            break;

        default:
            return false;
    }
    $gameAchievement.add("判断失败", "道具没有生效")
    $gameMessage.add("似乎没有什么用");
    return false;
}

function getEventID() {
    var vector = [0, 0];
    switch ($gamePlayer.direction()) {
        case 2:
            vector = [0, 1]
            break
        case 4:
            vector = [-1, 0]
            break
        case 6:
            vector = [1, 0]
            break
        case 8:
            vector = [0, -1]
            break
        default:
    }
    var eventPosition = {}
    eventPosition.x = $gamePlayer.x + vector[0]
    eventPosition.y = $gamePlayer.y + vector[1]
    return $gameMap.eventIdXy(eventPosition.x, eventPosition.y)
}


```





## 文件读写系统

```js
/*:
 * @plugindesc 用于文件的读写
 * 
 * @author 闫辰祥
 *
 * @param 文件
 * @desc 文件名
 * @default test
 *
 * @param 文件夹
 * @desc 保存文件的文件夹名
 * @default ./
 * 
 * 
 * @param 扩展名
 * @desc 文件扩展名，默认txt
 * @default txt
 * 
 * 
 * @param 内容
 * @desc 需要写入的内容
 * @default hello world
 * 
 * 
 * @help
 * MV是不支持fs模块的，但是还是需要文件读写怎么办呢？
 * 这时候就可以用这个插件了。
 * 
 * 
 * 其中文件夹的路径是从游戏项目根目录开始的
 * 你不需要写引号，MV会自己给你加上
 * 比如你想访问 "./data/test.txt"
 * 那么你的参数应该这样写
 * 
 * - 文件：test
 * - 文件夹 ./data/
 * - 扩展名 txt
 * 
 * 然后游戏的data文件夹下就会出现test.txt
 * 
 * 插件指令：
 * FileAccess write //写入文件
 * FileAccess isEqualTo "某某某字符串"  //是否和文件的内容一致
 * 
 * ！！！！！！！注意！！！！！！！！！！！
 * 本代码是基于node环境的，
 * 也就是说如果用网页打开的话，
 * 本代码将会报错
 * 
 * 很容易理解，因为浏览器要是可以随随便便读写文件的话，
 * 那么你的网络环境也太危险了。
 * 
 * 所以说，调试这个插件的时候，请直接在工程里面打开游戏，
 * 不要点index.html打开游戏。
 * 
 * 
 *
 */
//作者：闫辰祥
var Yan = Yan || {};
Yan.Parameters = PluginManager.parameters('Yan_FileAccess');
Yan.Parameters.folder = String(Yan.Parameters['文件夹'] || './');
Yan.Parameters.file = String(Yan.Parameters['文件'] || 'test');
Yan.Parameters.extension = String(Yan.Parameters['扩展名'] || 'txt');
Yan.Parameters.content = String(Yan.Parameters['内容'] || 'hello world');


var _Game_Interpreter_pluginCommand = Game_Interpreter.prototype.pluginCommand;

Game_Interpreter.prototype.pluginCommand = function (command, args) {
  _Game_Interpreter_pluginCommand.call(this, command, args);
  if (command === 'FileAccess') {
    switch (args[0]) {
      case 'write':
        write();
        break;
      case 'isEqualTo':
        isEqualTo(args[1]);
        break;
    }
  }
};


function isEqualTo(string){
  const fs = require('fs');

  let folder = Yan.Parameters.folder;
  let file = Yan.Parameters.file;
  let extension = Yan.Parameters.extension;
  let path = folder + file + "." + extension;

  fs.readFile(path,'utf-8', function (err, data) {
    if (err) 
      alert("读取失败！");

    alert(data.toString()=="true");
  });
}

function write() {
  const fs = require('fs');

  let folder = Yan.Parameters.folder;
  let file = Yan.Parameters.file;
  let extension = Yan.Parameters.extension;
  let content = Yan.Parameters.content;

  content = `<!DOCTYPE html>
  <html lang="ch">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    hello world
  </body>
  </html>
  `

  let path = folder + file + "." + extension;
  //writeFile会覆盖原有的内容,而且若找不到文件,会自己创建一个文件
  fs.writeFile(path, content, (err) => {
    if (err)
      alert("写入失败！");
  });
}

```



## 昼夜系统

```js
/*:
 * @plugindesc 本游戏专用的数据脚本
 * @author 闫辰祥
 */

function Data(year, month, day) {
  this.year = year;
  this.month = month;
  this.day = day;
}

function Game_Infor_Manager(chapter, title, date) {
  this.chapter = chapter; //章节数
  this.title = title;  //标题
  this.date = date;  //日期
  //this.gamePlayedNums = 1;//周目数
}


//注意这里明显没写完，因为我懒得写
//而且我估计应该没有人能打完这么多天
Game_Infor_Manager.prototype.datePlus = function () {
  this.date.day++;
  if (this.date.day == 31) {
    this.month++;
    this.date.day = 1;
  }

}

Game_Infor_Manager.prototype.dateMinus = function () {
  this.date.day--;
  if (this.date.day == 0) {
    this.month++;
    this.date.day = 31;
  }

}

Game_Infor_Manager.prototype.dateChange = function (year, month, day) {
  this.date.day = day;
  this.date.month = month;
  this.date.year = year;
}





// 时间循环
Game_Infor_Manager.prototype.time = 0;
Game_Infor_Manager.prototype.bgmPlay = true;
Game_Infor_Manager.prototype.timeToSleep = true;

Game_Infor_Manager.prototype.timeControler = function () {



  if (this.bgmPlay == false) return;



  var bgm = new Object();
  bgm.volume = 100;//响度
  bgm.pitch = 100;//音调 
  bgm.pan = 0;//偏移


  //$gameVariables._data[4]代表一天的时间
  //0代表清晨，1代表正午，2代表下午，3黄昏，4代表夜晚，5代表深夜。

  if ($gameVariables._data[6])
    this.time = $gameVariables._data[6];
  this.time += 0.4;
  $gameVariables._data[6] = this.time;



  if (this.time < 1000) {
    $gameScreen.startTint([0, 0, 0, 0], 1); //清晨
    bgm.name = "晨曦";//bgm的名称
    AudioManager.playBgm(bgm);
    $gameVariables._data[4] = 0;
    this.timeToSleep = true;
  }

  if (this.time >= 1000 && this.time < 2500) {
    $gameScreen.startTint([60, 60, 60, 0], 800); //正午
    AudioManager.fadeOutBgm(40);
    $gameVariables._data[4] = 1;

  }



  if (this.time >= 2500 && this.time < 3500) {
    $gameScreen.startTint([0, 0, 0, 0], 600); //下午
    bgm.name = "黄昏";//bgm的名称
    AudioManager.playBgm(bgm);
    $gameVariables._data[4] = 2;
  }

  if (this.time >= 3500 && this.time < 4500) {
    $gameScreen.startTint([68, -34, -34, 0], 1000); //黄昏
    $gameVariables._data[4] = 3;
    AudioManager.fadeOutBgm(30);
  }


  if (this.time >= 4500) {
    $gameScreen.startTint([-68, -68, 0, 68], 1000);  //夜晚
    bgm.name = "深夜";//bgm的名称
    AudioManager.playBgm(bgm);
    $gameVariables._data[4] = 4;
  }




  if (this.time >= 6000) {
    $gameScreen.startTint([-120, -100, 0, 68], 200); //深夜

    if (this.timeToSleep) {
      if ($gameMap._mapId == 6) {
        //如果已经在房子里面的话，不进行跳转
      } else {
        $gameMessage.add("太晚了，回去睡觉吧。");
        $gamePlayer.reserveTransfer(6, 8, 14, 0, 0);

      }
      this.timeToSleep = false;

    }
    $gameVariables._data[4] = 5;
  }

}


Game_Infor_Manager.prototype.setTime = function (num) {
  this.time = num;
  $gameVariables._data[6]=num;
}

Game_Infor_Manager.prototype.bgmClose = function () {
  this.bgmPlay = false;
}

Game_Infor_Manager.prototype.bgmOpen = function () {
  this.bgmPlay = true;
}

Game_Infor_Manager.prototype.clearItems = function () {
  for (let i = 0; i < 21; i++)
    $gameParty._items[i] = 0;
}




var $gameInfor = new Game_Infor_Manager(1, "美好的美一天", new Data(2021, 3, 15));

```



## 更换首页背景图

可以在标题页更换标题图

```js
let leftBtn= document.createElement("div");
leftBtn.id = "leftBtn"
leftBtn.innerText ="左翻页"
leftBtn.style.fontSize = "30px"
leftBtn.style.color = "pink"
leftBtn.style.position = "fixed" 
leftBtn.style.top = "500px"
leftBtn.style.left = "0px"
leftBtn.style.zIndex = 9999;
document.body.appendChild(leftBtn);



leftBtn.onclick = function(){
  $dataSystem.title1Name="CrossedSwords"
  SceneManager.goto(Scene_Title);
}



let rightBtn= document.createElement("div");
rightBtn.id = "rightBtn"
rightBtn.innerText ="右翻页"
rightBtn.style.fontSize = "30px"
rightBtn.style.color = "pink"
rightBtn.style.position = "fixed" 
rightBtn.style.top = "500px"
rightBtn.style.right = "0px"
rightBtn.style.zIndex = 9999;
document.body.appendChild(rightBtn);

rightBtn.onclick = function(){
  $dataSystem.title1Name="Castle"
  SceneManager.goto(Scene_Title);
}
```



## 即时战斗系统

```js

var Yan_util = Yan_util || {}

Yan_util.getTouchEvent = function () {
    var vector = [0, 0];
    switch ($gamePlayer.direction()) {
        case 2:
            vector = [0, 1]
            break
        case 4:
            vector = [-1, 0]
            break
        case 6:
            vector = [1, 0]
            break
        case 8:
            vector = [0, -1]
            break
        default:
    }
    var eventPosition = {}
    eventPosition.x = $gamePlayer.x + vector[0]
    eventPosition.y = $gamePlayer.y + vector[1]
    return $gameMap.eventsXy(eventPosition.x, eventPosition.y)[0]
}





Yan_util.addMethod = function (object, name, fn) {
    var old = object[name]; object[name] = function () {
        if (fn.length == arguments.length)
            return fn.apply(this, arguments)
        else if (typeof old == 'function')
            return old.apply(this, arguments);
    };
}

Yan_util.random = function (m, n) {
    return Math.ceil(Math.random() * (n - m + 1) + m - 1);
}






/**
 * 即时战斗系统，共分为以下几个部分：
 * 全局初始化
*/



var RealtimeBattleSystem = RealtimeBattleSystem || {}



// 初始化
RealtimeBattleSystem.init = function () {


    nw.Window.get().maximize()//最大化


    this.attack = true;

    this._callbackQueue = [];//回调函数队列，用于事件触发
    RealtimeBattleSystem.enemyInit()//更新敌人

    RealtimeBattleSystem.bindUpdate()

    RealtimeBattleSystem.UIInit()
}




RealtimeBattleSystem.getWeapon = function () {
    let weapon = $dataWeapons[$gameParty.leader()._equips[0]._itemId]
    return weapon ? weapon.name : '空手'
}


RealtimeBattleSystem.getHat = function () {
    let armor = $dataArmors[$gameParty.leader()._equips[2]._itemId]
    return armor ? armor.name : '没穿'
}



RealtimeBattleSystem.getArmor = function () {
    let armor = $dataArmors[$gameParty.leader()._equips[3]._itemId]
    return armor ? armor.name : '空手'
}


RealtimeBattleSystem.creatUI = function () {

    // 左侧的状态栏
    var stateBar = document.createElement('div')
    stateBar.classList += "state-bar"

    var hpBar = document.createElement('div')
    hpBar.id = "hp-bar"


    var mpBar = document.createElement('div')
    mpBar.id = "mp-bar"


    var defBar = document.createElement('div')
    defBar.id = "def-bar"


    var atkBar = document.createElement('div')
    atkBar.id = "atk-bar"




    stateBar.appendChild(hpBar);
    stateBar.appendChild(mpBar);
    stateBar.appendChild(defBar);
    stateBar.appendChild(atkBar);
    document.body.appendChild(stateBar)



    //右侧的装备栏
    var equipBar = document.createElement('div')
    equipBar.classList += "equip-bar"


    var weaponBar = document.createElement('div')
    weaponBar.innerHTML = `手持：${RealtimeBattleSystem.getWeapon()} `


    var headBar = document.createElement('div')
    headBar.innerHTML = `头戴：${RealtimeBattleSystem.getHat()} `


    var clothesBar = document.createElement('div')
    clothesBar.innerHTML = `身披：${RealtimeBattleSystem.getArmor()} `

    equipBar.appendChild(weaponBar);
    equipBar.appendChild(headBar);
    equipBar.appendChild(clothesBar);
    document.body.appendChild(equipBar)
}


RealtimeBattleSystem.updateUI = function () {

    var hpBar = document.querySelector("#hp-bar")
    hpBar.innerHTML = `生命值：${$gameParty.leader()._hp} 之于 ${$gameParty.leader().mhp}`

    var mpBar = document.querySelector("#mp-bar")
    mpBar.innerHTML = `法术值：${$gameParty.leader()._mp} 之于  ${$gameParty.leader().mmp}`

    var defBar = document.querySelector("#def-bar")
    defBar.innerHTML = `防御力：${$gameParty.leader().def}`


    var atkBar = document.querySelector("#atk-bar")
    atkBar.innerHTML = `攻击力：${$gameParty.leader().atk}`
}



RealtimeBattleSystem.普通攻击 = function () {
    //普通攻击
    if (Input.isTriggered('ok')) {

        var targetEvent = Yan_util.getTouchEvent()
        if (targetEvent == void 0)
            return
        targetEvent.hp -= $gameParty.leader().atk
        targetEvent.requestAnimation(2)

    }  //按键是否正在被按下
}


RealtimeBattleSystem.远程攻击 = function () {

}

RealtimeBattleSystem.蓄力攻击 = function () {

    //蓄力攻击
    if (Input.isLongPressed('ok')) {
        if (this._attack && $gameParty.leader()._mp >= 10) {
            this._attack = false;
            $gamePlayer.requestAnimation(1);
            $gameParty.leader().gainMp(-10)
        }
    }
    if (Input.isPressed('ok') === false) {
        this._attack = true;
    }
}



RealtimeBattleSystem.checkAttack = function () {
    this.普通攻击()
    this.蓄力攻击()
}



//判断玩家相对于事件到底在哪个方向
RealtimeBattleSystem.eventPositionToPlayer = function (gameEvent) {
    if ($gamePlayer._realX > gameEvent._realX && $gamePlayer._realY > gameEvent._realY) {
        return "右下"
    }
    else if ($gamePlayer._realX > gameEvent._realX && $gamePlayer._realY < gameEvent._realY) {
        return "右上"
    } else if ($gamePlayer._realX < gameEvent._realX && $gamePlayer._realY > gameEvent._realY) {
        return "左下"
    } else if ($gamePlayer._realX < gameEvent._realX && $gamePlayer._realY < gameEvent._realY) {
        return "左上"
    }
}


RealtimeBattleSystem.loadCSS = function () {
    var stylesheet = document.createElement("link")
    stylesheet.rel = "stylesheet"
    stylesheet.href = "./css/realtimeBattleSystem.css"
    stylesheet.type = "text/css"
    document.head.appendChild(stylesheet)
}

RealtimeBattleSystem.UIInit = function () {
    RealtimeBattleSystem.loadCSS()//加载UI样式
    RealtimeBattleSystem.creatUI()//创建UI
}

RealtimeBattleSystem.cheackEnemyAttack = function (enemyEvent) {

    var vector = [0, 0];
    switch (enemyEvent._direction) {
        case 2:
            vector = [0, 1]
            break
        case 4:
            vector = [-1, 0]
            break
        case 6:
            vector = [1, 0]
            break
        case 8:
            vector = [0, -1]
            break
        default:
    }

    if (enemyEvent._x + vector[0] == $gamePlayer._x && enemyEvent._y + vector[1] == $gamePlayer._y) {

        $gameParty.leader().gainHp(-enemyEvent.attack)
        $gamePlayer.requestAnimation(2)

        return true;
    }
    return false;


}


RealtimeBattleSystem.enemyInit = function () {
    RealtimeBattleSystem._enemys = []


    for (let i = 1; i < $dataMap.events.length; i++) {


        let dataEvent = $dataMap.events[i]
        let gameEvent = $gameMap._events[dataEvent.id]


        if (!dataEvent) {
            break;
        }
        if(!dataEvent.meta.type){
            break
        }


        RealtimeBattleSystem._enemys.push(gameEvent)


        if (dataEvent.meta.type == "车") {
            gameEvent.hp = 300;
            gameEvent.attack = 3;

            gameEvent.setMoveSpeed(4.3);
            setInterval(function () {
                gameEvent.moveTowardPlayer();//朝向玩家移动
                gameEvent.turnTowardPlayer();
                RealtimeBattleSystem.cheackEnemyAttack(gameEvent)

            }, 700)
        }

        if (dataEvent.meta.type == "马") {

            gameEvent.hp = 350;
            gameEvent.attack = 5;



            setInterval(function () {
                gameEvent.moveTowardPlayer();//先直线走一步

                setTimeout(function () {

                    switch (RealtimeBattleSystem.eventPositionToPlayer(gameEvent)) {
                        case "右下":
                            gameEvent.moveDiagonally(6, 2); //右下移动
                            break;
                        case "左下":
                            gameEvent.moveDiagonally(4, 2);//移动
                            break;
                        case "右上":
                            gameEvent.moveDiagonally(6, 8);//移动
                            break;
                        case "左上":
                            gameEvent.moveDiagonally(4, 8);//左上移动
                            break
                    }
                    RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
                }, 500)

            }, 1000)
        }

        if (dataEvent.meta.type == "象") {

            gameEvent.hp = 250;
            gameEvent.attack = 10;

            setInterval(function () {


                switch (RealtimeBattleSystem.eventPositionToPlayer(gameEvent)) {
                    case "右下":
                        gameEvent.moveDiagonally(6, 2); //右下移动
                        break;
                    case "左下":
                        gameEvent.moveDiagonally(4, 2);//移动
                        break;
                    case "右上":
                        gameEvent.moveDiagonally(6, 8);//移动
                        break;
                    case "左上":
                        gameEvent.moveDiagonally(4, 8);//左上移动
                        break
                }

                setTimeout(function () {

                    switch (RealtimeBattleSystem.eventPositionToPlayer(gameEvent)) {
                        case "右下":
                            gameEvent.moveDiagonally(6, 2); //右下移动
                            break;
                        case "左下":
                            gameEvent.moveDiagonally(4, 2);//移动
                            break;
                        case "右上":
                            gameEvent.moveDiagonally(6, 8);//移动
                            break;
                        case "左上":
                            gameEvent.moveDiagonally(4, 8);//左上移动
                            break
                    }
                    RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
                }, 500)
            }, 2000)
        }

        if (dataEvent.meta.type == "士") {

            gameEvent.hp = 200;
            gameEvent.attack = 30;
            setInterval(function () {
                if ($gamePlayer.x == 4 && $gamePlayer.y == 2)
                    gameEvent.moveTowardPlayer();//朝向玩家移动
                RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
            }, 1000)
        }
        if (dataEvent.meta.type == "将") {
            gameEvent.hp = 50;
            gameEvent.attack = 5;
            setInterval(function () {
                RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
            }, 1000)
        }
        if (dataEvent.meta.type == "砲") {
            gameEvent.hp = 200;
            gameEvent.attack = 15;
            setInterval(function () {
                gameEvent.moveTowardPlayer();//朝向玩家移动
                RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
            }, 3000)
        }

        if (dataEvent.meta.type == "卒") {
            gameEvent.hp = 300;
            gameEvent.attack = 20;
            setInterval(function () {
                gameEvent.moveTowardPlayer();
                RealtimeBattleSystem.cheackEnemyAttack(gameEvent)
            }, 1000 * Yan_util.random(1, 5))
        }

    }

}



//增加事件

RealtimeBattleSystem.addEventCallback = function (func) {
    this._callbackQueue.push(func);
}


RealtimeBattleSystem.updateEventCallback = function () {
    if (this._callbackQueue.length == 0)
        return
    (this._callbackQueue.shift())();

}


RealtimeBattleSystem.update = function () {
    RealtimeBattleSystem.checkAttack()

    RealtimeBattleSystem.updateEventCallback()

    RealtimeBattleSystem.updateUI()
    RealtimeBattleSystem.updateEnemy()

}


RealtimeBattleSystem.checkWin = function () {
    return   RealtimeBattleSystem.winFlag
}


RealtimeBattleSystem.updateEnemy = function () {


    RealtimeBattleSystem.winFlag = true
 

    for (let i = 0; i < RealtimeBattleSystem._enemys.length; i++) {
        if (RealtimeBattleSystem._enemys[i].hp <= 0) {
            $gameMap.eraseEvent(RealtimeBattleSystem._enemys[i]._eventId);
        } else {

            RealtimeBattleSystem.winFlag = false
        }
    }

  
}


RealtimeBattleSystem.bindUpdate = function () {
    var tempUpdate = Scene_Map.prototype.update

    Scene_Map.prototype.update = function () {
        tempUpdate.call(this)

        RealtimeBattleSystem.update()
    }
}


//动态事件

function Dynamic_Event() {
    var newId = $dataMap.events.length

    $dataMap.events[newId] = {
        "id": newId,
        "name": "子弹",
        "note": "",
        "pages": [{
            "conditions": {
                "actorId": 1,
                "actorValid": false,
                "itemId": 1,
                "itemValid": false,
                "selfSwitchCh": "A",
                "selfSwitchValid": false,
                "switch1Id": 1,
                "switch1Valid": false,
                "switch2Id": 1,
                "switch2Valid": false,
                "variableId": 1,
                "variableValid": false,
                "variableValue": 0
            },
            "directionFix": true,
            "image": {
                "tileId": 0,
                "characterName": "文字板",
                "direction": 4,
                "pattern": 2,
                "characterIndex": 4
            },
            "list": [{
                "code": 0,
                "indent": 0,
                "parameters": []
            }],
            "moveFrequency": 3,
            "moveRoute": {
                "list": [{ "code": 0, "parameters": [] }],
                "repeat": true,
                "skippable": false,
                "wait": false
            },
            "moveSpeed": 3,
            "moveType": 0,
            "priorityType": 1,
            "stepAnime": false,
            "through": false,
            "trigger": 0,
            "walkAnime": false
        }],
        "x": 6, "y": 6
    }

    $gameMap._events[newId] = new Game_Event($gameMap._mapId, newId);

    $gamePlayer.reserveTransfer(1, 8, 8, 0, 2)

    setInterval(function () {
        $gameMap._events[newId].moveRandom()
    }, 1000)
}
```



# 原理

## 窗口函数的绑定原理

1. 看一个示例

```js
  
Window_TitleCommand.prototype.makeCommandList = function() {

    this.addCommand(TextManager.newGame,   'newGame');

    this.addCommand(TextManager.continue_, 'continue', this.isContinueEnabled());

    this.addCommand(TextManager.options,   'options');

    this.addCommand("测试",   'test');

};



Scene_Title.prototype.createCommandWindow = function() {

    this._commandWindow = new Window_TitleCommand();

    this._commandWindow.setHandler('newGame',  this.commandNewGame.bind(this));

    this._commandWindow.setHandler('continue', this.commandContinue.bind(this));

    this._commandWindow.setHandler('options',  this.commandOptions.bind(this));

    this._commandWindow.setHandler('test',  this.Test.bind(this));

    this.addWindow(this._commandWindow);

};

  

Scene_Title.prototype.Test = function() {

    alert("hello world")

};
```

  

makeCommandList 可以来创建一个函数的显示层。
this.addCommand("测试",   'test'); 前面是显示的内容，后面的绑定的标识符（symbol）


标识符的绑定需要在Scene_Title中完成。this._commandWindow.setHandler('test',  this.Test.bind(this));可以来绑定test标识符对应的回调函数


原理是
setHandler函数可以把一个标识符通过数组的索引，绑定到_handlers

```js
Window_Selectable.prototype.setHandler = function(symbol, method) {

    this._handlers[symbol] = method;

};
```

通过callhandler来调用

```js
Window_Selectable.prototype.callHandler = function(symbol) {

    if (this.isHandled(symbol)) {

        this._handlers[symbol]();

    }

};
```


addCommand方法可以把一个函数的标识符和窗体名绑定到window中

```js
Window_Command.prototype.addCommand = function(name, symbol, enabled, ext) {

    if (enabled === undefined) {

        enabled = true;

    }

    if (ext === undefined) {

        ext = null;

    }

    this._list.push({ name: name, symbol: symbol, enabled: enabled, ext: ext});

};
```









# 技巧速查

## 让RPGMV完全透明化

如果要让RPGMV完全透明，首先我们需要理解以下几个知识点：

1. RPGMV是一个网页，因此想让他透明本质上是需要网页透明
2. RPGMV运行在nwjs框架上，因此也需要让nwjs透明
3. pixijs是控制RPGMV显示的动画库，同样会控制游戏的透明



1. 因此，首先需要让rpgmv的html页面透明

   在index.html中，修改背景颜色为透明

   ```html
   <body style="background-color:rgba(0, 0, 0, 0);">
   ```

2. 修改并增加package.json的配置，让html的透明能显示到桌面

   ```json
    "window": {
       "frame": false,
       "transparent": true
     },
   ```

   frame可以取消游戏的框架，取消关闭按钮和最小化最大化按钮。transparent可以让游戏框架透明。

3. 修改pixi.js的源码

   ctrl+f，找到下面的代码

   ```js
   _this._backgroundColorRgba[3] = _this.transparent ? 0 : 1;
   ```

   可以看到，虽然框架透明了，但是因为pixi也渲染了游戏，导致游戏还是没有透明。这个_backgroundColorRgba，前三个变量控制rgb，第三个控制alpha通道。

   所以我们要把这个代码修改为：

   ```
   _this._backgroundColorRgba[3] = 0;
   ```

   当然，也可以自定义小数，实现半透明

4. 这样配置还是无法实现，透明。因为pixi.js在配置时，默认了禁止透明。所以还要开启透明配置。在RENDER_OPTIONS中，修改transparent为true

   ```js
    RENDER_OPTIONS: {
       transparent: true,
   ```

   如果配置加载还是不透明，可以强制修改透明度。

   ctrl+f找到下面的代码

   ```js
   _this.transparent = options.transparent
   ```

   修改为

   ```js
   _this.transparent = true;
   ```

5. 此时游戏的标题界面已经透明了，但是游戏画面仍不透明，此时我们要注意，游戏的图块本身就不是透明的，为了测试。我们需要新建一个场景，里面什么都不要加。仅仅测试透明效果。

6. 但是，这时候却发现，屏幕都是黑色。并没有透明。这是很正常的，查看源码发现Spriteset_Base中，this._blackScreen.opacity透明度默认为255。所以我们需要修改。

   ```
   this._blackScreen.opacity = 10;
   ```

   这个值同样是自定义的。

7. 这时，我们发现，右键菜单，还是无法透明。这是因为Scene_MenuBase中，没有设置透明。查看源码发现Scene_MenuBase.prototype.createBackground时，没有默认透明，因此修改代码为：

   ```js
   Scene_MenuBase.prototype.createBackground = function() {
   
       this._backgroundSprite = new Sprite();
       //闫修改，增加了这个
       this._backgroundSprite.opacity = 0;
   
       this._backgroundSprite.bitmap = SceneManager.backgroundBitmap();
       this.addChild(this._backgroundSprite);
   };
   ```

8. 此时，游戏已经全部透明。如果画上图块没有透明，这是因为，图块素材本身也需要透明。

   此时只要远景图是透明的，图块是透明的，就可以完全透明化。









## 更换nw底层版本以及手动打包游戏

注意：nwjs有两个版本NORMAL和SDK。

开发请使用SDK，因为可以debug。

打包使用NORMAL，不支持debug

nw.process.versions.nw



s



1. 将所需的文件压缩为zip文件，注意rar不行！

2. 把zip文件的后缀名改为nw

3. 把这个文件放到nw.js环境同级目录下

4. 在nw.js的目录下打开命令行，输入下面的命令

   ```
   copy /b nw.exe+app.nw app.exe
   ```

   注意，nw.exe就是咱nw环境的入口，名字可能会变。后面那个就是咱刚才打包的文件。名字也是随意的。

   最后那个app.exe就是咱打包之后的文件。

## 使用RPGMAker调用Unity游戏





1. Compression Format设置为disabled



> Javascript调用c#



> C#调用JavaScript

1. Assets/Plugins/WebGl，用来放置浏览器要执行的JavaScript代码,插件扩展名为**.jslib**,将代码文件保存在此路径,当你发布时,这段代码(具体来说)将在build JS中扩展.

2. 代码

   ```js
   mergeInto(LibraryManager.library, {
    
     Hello: function () {
       window.alert("Hello, world!");
     },
    
     HelloString: function (str) {
       window.alert(Pointer_stringify(str));
     },
    
     PrintFloatArray: function (array, size) {
       for(var i = 0; i < size; i++)
       console.log(HEAPF32[(array >> 2) + i]);
     },
    
     AddNumbers: function (x, y) {
       return x + y;
     },
    
     StringReturnValueFunction: function () {
       var returnStr = "bla";
       var bufferSize = lengthBytesUTF8(returnStr) + 1;
       var buffer = _malloc(bufferSize);
       stringToUTF8(returnStr, buffer, bufferSize);
       return buffer;
     },
    
     BindWebGLTexture: function (texture) {
       GLctx.bindTexture(GLctx.TEXTURE_2D, GL.textures[texture]);
     },
    
   });
   
   ```

3. 使用C#调用

   ```c#
   using System.Runtime.InteropServices;
   
   [DllImport("__Internal")]
   private static extern void Hello();
   
   [DllImport("__Internal")]
   private static extern void HelloString(string str);
   
   [DllImport("__Internal")]
   private static extern void PrintFloatArray(float[] array, int size);
   
   [DllImport("__Internal")]
   private static extern int AddNumbers(int x, int y);
   
   [DllImport("__Internal")]
   private static extern string StringReturnValueFunction();
   
   [DllImport("__Internal")]
   private static extern void BindWebGLTexture(int texture);
   
   void Start()
   {
       Hello();
   
       HelloString("This is a string.");
   
       float[] myArray = new float[10];
       PrintFloatArray(myArray, myArray.Length);
   
       int result = AddNumbers(5, 7);
       Debug.Log(result);
   
       Debug.Log(StringReturnValueFunction());
   
       var texture = new Texture2D(0, 0, TextureFormat.ARGB32, false);
       BindWebGLTexture((int)texture.GetNativeTexturePtr());
   }
   
   ```





# 附录



## 插件模板

```javascript
/*:
 * @plugindesc 对插件的描述
 * 
 * @author 作者
 *
 * @param 插件的第一个参数
 * @desc 描述
 * @default 默认值
 *
 * @param 插件的第一个参数
 * @desc 描述
 * @default 默认值
 * 
 * 
 * 
 * @help
 * 下面这些是对脚本的说明，格式没有强制要求
 * 但是至少应该把使用方法和插件指令列出来。
 *
 */

//这个一般都是你的名字，但是没有强制要求，
//只要是一个对象就可以
var Yan = Yan || {};
//下面这个就是来注册插件，格式是固定的
//注意名字要和文件名一样
Yan.Parameters = PluginManager.parameters('你插件的名字');

//下面这个就是插件的参数，
Yan.Parameters.参数1 = String(Yan.Parameters['参数'] || '默认值');
Yan.Parameters.参数2 = String(Yan.Parameters['参数2'] || '默认值');

//下面这个格式也是固定的
//注意，要是不需要插件指令的话，可以不写
var _Game_Interpreter_pluginCommand = Game_Interpreter.prototype.pluginCommand;
Game_Interpreter.prototype.pluginCommand = function (command, args) {
  _Game_Interpreter_pluginCommand.call(this, command, args);
  //设计你的插件指令，command就是你插件指令的名字，当然这个可以不止一个，可以用else来创建多个指令
  if (command === '插件指令名字') {
    //参数0就是你的第一个参数
    //比如说插件指令为command 第一个参数为one
    //那么指令就是这样调用的  command one 
    switch (args[0]) {
      case '某':
       //代码
        break;
      case '某某某':
       //代码
        break;
    }
  }
};
```







## 键码映射表

- 字母与数字

| 按键 | 键码 | 按键 | 键码 | 按键 | 键码 | 按键 | 键码 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 65   | J    | 74   | S    | 83   | 1    | 49   |
| B    | 66   | K    | 75   | T    | 84   | 2    | 50   |
| C    | 67   | L    | 76   | U    | 85   | 3    | 51   |
| D    | 68   | M    | 77   | V    | 86   | 4    | 52   |
| E    | 69   | N    | 78   | W    | 87   | 5    | 53   |
| F    | 70   | O    | 79   | X    | 88   | 6    | 54   |
| G    | 71   | P    | 80   | Y    | 89   | 7    | 55   |
| H    | 72   | Q    | 81   | Z    | 90   | 8    | 56   |
| I    | 73   | R    | 82   | 0    | 48   | 9    | 57   |

- 小键盘和功能键

| 按键 | 键码 | 按键  | 键码 | 按键 | 键码 | 按键 | 键码 |
| ---- | ---- | ----- | ---- | ---- | ---- | ---- | ---- |
| 0    | 96   | 8     | 104  | F1   | 112  | F7   | 118  |
| 1    | 97   | 9     | 105  | F2   | 113  | F8   | 119  |
| 2    | 98   | *     | 106  | F3   | 114  | F9   | 120  |
| 3    | 99   | +     | 107  | F4   | 115  | F10  | 121  |
| 4    | 100  | Enter | 108  | F5   | 116  | F11  | 122  |
| 5    | 101  | -     | 109  | F6   | 117  | F12  | 123  |
| 6    | 102  | .     | 110  |      |      |      |      |
| 7    | 103  | /     | 111  |      |      |      |      |

- 控制键

| 按键      | 键码 | 按键       | 键码 | 按键        | 键码 | 按键 | 键码 |
| --------- | ---- | ---------- | ---- | ----------- | ---- | ---- | ---- |
| BackSpace | 8    | Esc        | 27   | Right Arrow | 39   | -_   | 189  |
| Tab       | 9    | Spacebar   | 32   | Dw Arrow    | 40   | .>   | 190  |
| Clear     | 12   | Page Up    | 33   | Insert      | 45   | /?   | 191  |
| Enter     | 13   | Page Down  | 34   | Delete      | 46   | `~   | 192  |
| Shift     | 16   | End        | 35   | Num Lock    | 144  | [{   | 219  |
| Control   | 17   | Home       | 36   | ;:          | 186  | \|   | 220  |
| Alt       | 18   | Left Arrow | 37   | =+          | 187  | ]}   | 221  |
| Cape Lock | 20   | Up Arrow   | 38   | ,<          | 188  | '"   | 222  |

- 多媒体键

| 按键   | 键码 |
| ------ | ---- |
| 音量加 | 175  |
| 音量减 | 174  |
| 停止   | 179  |
| 静音   | 173  |
| 浏览器 | 172  |
| 邮件   | 180  |
| 搜索   | 170  |
| 收藏   | 171  |

## 转义字符速查

| 控制字符 | 功能                        |
| -------- | --------------------------- |
| \V[n]    | 替换为第n个变量的值。       |
| \N[n]    | 替换为第 n个角色的名字。    |
| \P[n]    | 替换为第n个队伍成员。       |
| \G       | 替换为货币单位。            |
| \C[n]    | 后方的文字显示为第n号颜色。 |
| \I[n]    | 绘制第n个图标。             |
| \\{      | 将字体大小增加一级。        |
| \\}      | 将字体大小减小一级。        |
| \\\      | 替换为反斜杠字符。          |
| \\$      | 打开金钱窗口。              |
| \\.      | 等待1/4秒。                 |
| \\|      | 等待1s                      |
| \\\      | 反斜杠                      |
| \\!      | 等待按键输入。              |
| \\>      | 立刻显示一行内剩余的文字。  |
| \\<      | 取消立刻显示文字的效果。    |
| \\^      | 显示文本后不等待输入。      |



## RPGMV的键盘映射

定义在rpg_core中。Input.keyMapper

MV里面键盘的按键名字和真正的键盘名字是**不一样**的，一个名字会对应多个实际按钮，所以要特别注意。

| keyName    | 实际按钮                |
| ---------- | ----------------------- |
| 'tab'      | tab                     |
| 'ok'       | enter、空格、Z          |
| 'shift'    | shift                   |
| 'control'  | ctrl、alt               |
| 'escape'   | esc、小键盘0、insert、X |
| 'pageup'   | pageup、Q               |
| 'pagedown' | pagedown、W             |
| 'left'     | 方向键左、小键盘4       |
| 'up'       | 方向键上、小键盘8       |
| 'right'    | 方向键右、小键盘6       |
| 'down'     | 方向键下、小键盘2       |
| 'debug'    | F9                      |





## 类继承表

### 场景的继承关系

- Scene_Base：所有场景的基类

  - Scene_Boot：用于初始化整个游戏

  - Scene_Title：标题界面的场景

  - Scene_Map：地图界面的场景

  - Scene_MenuBase：所有菜单类型的基类，也就是游戏中点右键那个菜单

    - Scene_Menu：主菜单的场景

      调用窗口：`Window_MenuCommand`、`Window_Gold`、`Window_MenuStatus`

    - Scene_ItemBase：技能界面和物品界面的基类

      - Scene_Item：物品界面

        调用窗口：`Window_Help`

      - Scene_Skill：技能界面

    - Scene_Equip：装备界面

    - Scene_Status：状态界面

    - Scene_Options：选项界面

    - Scene_File：储存和读取界面的基类

      - Scene_Save：储存界面
      - Scene_Load：读取界面

    - Scene_GameEnd：游戏结束界面（点击结束游戏时那个界面）

    - Scene_Shop：商店界面

    - Scene_Name：姓名输入界面

    - Scene_Debug：Debug界面

  - Scene_Battle：战斗场景

  - Scene_Gameover：游戏结束场景



### 窗体的继承关系

- Window_Base：所有窗体的基类

  - Window_Selectable：可以用鼠标点击和滑轮滑动的的窗体

    - Window_Command：选择指令的父类窗口

      - Window_HorzCommand：The command window for the horizontal selection format.
        - Window_ItemCategory： The window for selecting a category of items on the item and shop screens.
        - Window_EquipCommand： The window for selecting a command on the equipment screen.
        - Window_ShopCommand：展示选择买卖的商店窗口
      - Window_MenuCommand：主菜单可选指令的窗口，也就是鼠标右键之后，左边那一栏
      - Window_SkillType： The window for selecting a skill type on the skill screen.
      - Window_Options：选项屏幕上用于更改各种设置的窗口。（就是选项的窗口）
      - Window_ChoiceList：对应着事件中`显示选项`的窗口。
      - Window_PartyCommand： The window for selecting whether to fight or escape on the battle screen.
      - Window_ActorCommand：The window for selecting an actor's action on the battle screen.
      - Window_TitleCommand： The window for selecting New Game/Continue on the title screen.
      - Window_GameEnd：在游戏结束屏幕上选择“转到标题”的窗口.

    - Window_MenuStatus：展示角色成员状态的窗口

      - Window_MenuActor：The window for selecting a target actor on the item and skill screens.

    - Window_ItemList：The window for selecting an item on the item screen.

      - Window_EquipItem：The window for selecting an equipment item on the equipment screen.
      - Window_ShopSell：he window for selecting an item to sell on the shop screen.
      - Window_EventItem：对应着事件中`物品选择处理`的窗口
      - Window_BattleItem：The window for selecting an item to use on the battle screen.

    - Window_SkillList：The window for selecting a skill on the skill screen.

      - Window_BattleSkill：The window for selecting a skill to use on the battle screen.

    - Window_EquipSlot：The window for selecting an equipment slot on the equipment screen.

    - Window_Status：The window for displaying full status on the status screen.

    - Window_SavefileList：The window for selecting a save file on the save and load screens.

    - Window_ShopBuy：The window for selecting an item to buy on the shop screen.

    - Window_ShopNumber： The window for inputting quantity of items to buy or sell on the shop

      // screen.

    - Window_NameInput：选择玩家姓名的窗口，里面全都是各种字母还有50音。

    - Window_NumberInput：对应着事件指令`数值输入处理`的窗口。 

    - Window_BattleLog： The window for displaying battle progress. No frame is displayed, but it is handled as a window for convenience.

    - Window_BattleStatus： The window for displaying the status of party members on the battle screen.

    - Window_BattleEnemy：The window for selecting a target enemy on the battle screen.

    - Window_DebugRange：The window for selecting a block of switches/variables on the debug screen.

    - Window_DebugEdit：The window for displaying switches and variables on the debug screen.

  - Window_Help：描述选择物品的窗口

  - Window_Gold：展示队伍金币数量的窗口

  - Window_SkillStatus：The window for displaying the skill user's status on the skill screen.

  - Window_EquipStatus：The window for displaying parameter changes on the equipment screen.

  - Window_ShopStatus：The window for displaying number of items in possession and the actor's equipment on the shop screen.

  - Window_NameEdit：编辑角色姓名的窗口，特指上面那个。

  - Window_Message：展示文字信息的窗口

  - Window_ScrollText：The window for displaying scrolling text. No frame is displayed, but it

    // is handled as a window for convenience.

  - Window_MapName：展示地图名字的窗口



### 精灵的继承关系

- Sprite_Base：具有显示动画功能的精灵类
  - Sprite_Character：显示角色的精灵
  - Sprite_Battler：Sprite_Actor 和 Sprite_Enemy 的父类
    - Sprite_Actor：显示主角的精灵
    - Sprite_Enemy：显示敌人
  - Sprite_StateOverlay：The sprite for displaying an overlay image for a state.
  - Sprite_Weapon：显示武器攻击图像的精灵
  - Sprite_Balloon：显示气泡图标的精灵
- Sprite_Button：显示按钮的精灵
- Sprite_Animation：播放动画的精灵
- Sprite_Damage：显示弹出式伤害的精灵
- Sprite_StateIcon：展示状态图标的精灵
- Sprite_Picture：显示图片的精灵
- Sprite_Timer：显示时间的精灵
- Sprite_Destination：显示输入区域的精灵
- Spriteset_Base：Spriteset_Map 和 Spriteset_Battle 的父类
  - Spriteset_Map：在地图屏幕上的一组精灵
  - Spriteset_Battle：战斗屏幕的一组精灵





### 游戏全局对象类继承关系

- Game_Temp：用于并不会保存到存档里面的临时数据

- Game_System：系统数据

- Game_Message：就是用来显示文本或者选择的类

- Game_Switches：开关的类

- Game_Variables：变量的类

- Game_SelfSwitches：独立开关的类

- Game_Screen：用于游戏屏幕特效的类，；例如色调更改或者闪屏等

- Game_Picture：显示图片的类

- Game_Item：

- Game_Action：

- Game_ActionResult：

- Game_BattlerBase：

  - Game_Battler

    - Game_Actor

    - Game_Enemy

- Game_Actors：游戏主角们数组的封装类

- Game_Unit： Game_Party 和Game_Troop的父类

  - Game_Party ：游戏队伍的类，里面包含着金币和道具等数据
  - Game_Troop：

- Game_Map：

- Game_CommonEvent：

- Game_CharacterBase：

  - Game_Character： Game_Player, Game_Follower, GameVehicle和Game_Event的父类

    - Game_Player
    - Game_Follower
    - GameVehicle
    - Game_Event

- Game_Interpreter：

  





## 颜色编号表

<table>
    <caption>颜色编号对照表</caption>
    <tr>
        <td style="background-color:rgb(255,255,255);">0</td>
        <td style="background-color:rgb(32,160,214);">1</td>
        <td style="background-color:rgb(255,120,76);">2</td>
        <td style="background-color:rgb(102,204,64);">3</td>
        <td style="background-color:rgb(153,204,255);">4</td>
        <td style="background-color:rgb(204,191,255);">5</td>
        <td style="background-color:rgb(255,255,154);">6</td>
        <td style="background-color:rgb(128,128,128);">7</td>
    </tr>
    <tr>
        <td style="background-color:rgb(192,192,192);">8</td>
        <td style="background-color:rgb(32,128,204);">9</td>
        <td style="background-color:rgb(255,56,16);">10</td>
        <td style="background-color:rgb(0,160,16);">11</td>
        <td style="background-color:rgb(62,154,222);">12</td>
        <td style="background-color:rgb(160,152,255);">13</td>
        <td style="background-color:rgb(255,204,32);">14</td>
        <td style="background-color:rgb(0,0,0);">15</td>
    </tr>
    <tr>
        <td style="background-color:rgb(132,170,255);">16</td>
        <td style="background-color:rgb(255,255,64);">17</td>
        <td style="background-color:rgb(255,32,32);">18</td>
        <td style="background-color:rgb(32,32,64);">19</td>
        <td style="background-color:rgb(224,128,64);">20</td>
        <td style="background-color:rgb(240,192,64);">21</td>
        <td style="background-color:rgb(64,128,192);">22</td>
        <td style="background-color:rgb(64,192,240);">23</td>
    </tr>
    <tr>
        <td style="background-color:rgb(128,255,128);">24</td>
        <td style="background-color:rgb(192,128,128);">25</td>
        <td style="background-color:rgb(128,128,255);">26</td>
        <td style="background-color:rgb(255,135,255);">27</td>
        <td style="background-color:rgb(0,160,64);">28</td>
        <td style="background-color:rgb(0,224,96);">29</td>
        <td style="background-color:rgb(160,96,224);">30</td>
        <td style="background-color:rgb(194,127,255);">31</td>
    </tr>
</table>





# 作者信息

姓名：闫辰祥

QQ交流群：529245311

B站教程：https://www.bilibili.com/video/BV1Vb4y1q717?spm_id_from=333.999.0.0

教程地址链接：https://klsdf.github.io/

GitHub项目链接：https://github.com/klsdf/klsdf.github.io

# 更新日志

- 2023年4月29日：修复了其中一些错误描述，增加了新api，增加了窗体透明化的方法。

- 2023年5月4日：将窗体的模板单独提出来了，并补充了自定义窗体的模板，把插件模板放到了附录。补充了很多RPGMV的api。增加了自定义事件触发条件的插件。优化了自定义存档的插件。

  





























# 使用方法

本文档收录了RPGMakerMV的若干api，以及nwjs的api。供广大RPGMaker的开发者参考学习。



