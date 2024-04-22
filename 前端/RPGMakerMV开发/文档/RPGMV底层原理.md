# 窗体重写

## 基本原理

该功能由脚本负责。游戏中，所有的窗口界面都是基于这个脚本实现的。

在MV中，有window和scene这么两种东西，scene就是游戏的大场景，而我们看到的东西则是窗口展现的。举个例子，我们平时可以在家吃饭，也可能在学校吃饭，这就是不同的场景。但是家和学校并不是饭，但是我们要吃饭必须得回家，或者去学校。也就是说首先得有scene，然后才能把window放到里面去。

scnen和window分别对应`rpg_scenes.js`和`rpg_windows.js` 我们重新绘制的界面都是继承于这个两个js文件。



window在scene中被实例化，而scene在manager中被实例化。

一个scene必须具有create和start两个方法。create方法就是把窗体添加到scene中，而start就是开始场景。

在编写窗体类的时候，尽量不要写基类，建议从后面的子类来写。

## RPGmaker界面的加载过程

1. 游戏进入时首先进入 Scene_Boot，完成加载游戏图片资源，音频资源，数据文件等工作(本场景没有界面)。资源加载完成后会自动切换到主界面(Scene_Title)

2. 主界面绘制城堡背景，显示游戏标题，播放背景音乐，然后展示一个“新游戏，继续，选项”的选择窗口。并监测用户的选择情况，当原则新游戏时：直接跳转到地图场景中（Scene_Map），继续时：则跳转到加载存档的场景（Scene_Load），选项就跳转到选项场景（Scene_Options）配置选项。

3. Scene_Load的功能就是列举出已经保存的存档，监测玩家选中哪一个，然后加载存档再切换到Scene_Map。

4. Scene_Map根据角色现在所在的地图生成很多小方块精灵（Sprite）拼接成地图，然后监控玩家操控。方向键时滚动地图，如果遇敌就切换到战斗场景 （Scene_Battle），战斗输了就切换到游戏结束场景 （Scene_GameEnd）。esc时显示菜单场景 （Scene_Menu）。

5. Scene_Menu菜单场景中有角色列表、装备、技能、等等窗口和子场景，根据用户操作来回切换，当再按esc时，就切换回Scene_Map地图场景。

## 窗体构建的基础流程

## 基本API



- 绘制文字

  test：所需打印的字符串

  x，y：xy坐标

  maxWidth（可选）：宽度

  align（可选）：排版，包括   'center'    'left'     'right'

  ```javascript
  this.drawText(text, x, y, maxWidth, align);
  ```



- 打印图标

  iconIndex：图标的id

  x,y：坐标

  ```js
  this.drawIcon(iconIndex, x, y);
  ```



- 打印角色头像

  **要注意，角色头像的编号从0开始。**

  ```js
  this.drawFace(faceName, faceIndex, x, y, width, height);
  ```





实际上官方这些代码里面大部分都是封装的`this.drawText()`函数，所以说熟练掌握上面的，就无敌了。

- 绘制角色的名字

  ```js
  this.drawActorName(actor, x, y, width);
  ```

  

- 绘制角色绰号

```javascript
this.drawActorNickname(actor, x, y, width);
```

- 绘制角色职业

```javascript
this.drawActorClass(actor, x, y, width);
```

- 绘制角色等级和经验

```javascript
this.drawActorLevelAndExp(actor, x, y, width);
```

- 绘制角色HP

```javascript
this.drawActorHp(actor, x, y, width);
```

- 绘制角色MP

```javascript
this.drawActorMp(actor, x, y, width);
```

- 绘制角色头像

```javascript
this.drawActorFace(actor, x, y, width, height);
```

- 绘制角色图标（完全没看懂啥意思）

```javascript
this.drawActorIcons(actor, x, y, width, height);
```



# 游戏生命周期

# game全局对象生成原理

1. 首先，全局的场景启动，加载游戏的各个画面

   ```js
   SceneManager.run(Scene_Boot);
   ```

2. 在SceneManager.run方法中可以看到有一个goto方法

   ```js
   SceneManager.run = function(sceneClass) {
       try {
           this.initialize();
           this.goto(sceneClass);
           this.requestUpdate();
       } catch (e) {
           this.catchException(e);
       }
   };
   ```

3. 在goto方法中，Scene_Boot类第一次被实例化

   ```js
   SceneManager.goto = function(sceneClass) {
       if (sceneClass) {
           this._nextScene = new sceneClass();
       }
       if (this._scene) {
           this._scene.stop();
       }
   };
   ```

4. 然后回到上面去，进入requestUpdate，在这里就可以看到一个库函数`requestAnimationFrame`，这个玩意是web自带的底层函数，这个已经很底层了不再赘述，我只能介绍一下这个函数的功能，这个函数的作用定期执行回调函数——`SceneManager.update`方法。

   ```js
   SceneManager.requestUpdate = function() {
       if (!this._stopped) {
           requestAnimationFrame(this.update.bind(this));
       }
   };
   ```

5. 然后在回调函数中，我们可以看到有一个updateMain

   ```js
   SceneManager.update = function() {
       try {
           this.tickStart();
           if (Utils.isMobileSafari()) {
               this.updateInputData();
           }
           this.updateManagers();
           this.updateMain();//这个就是主更新函数
           this.tickEnd();
       } catch (e) {
           this.catchException(e);
       }
   };
   ```

6. 进入updateMain，可以看到有一个updateScene

   而且我要特别强调一点，changeScene方法可以在场景切换的时候把this.\_scene 赋值为 this._nextScene;

   ```js
   SceneManager.updateMain = function() {
       if (Utils.isMobileSafari()) {
           this.changeScene();
           this.updateScene();
       } else {
           var newTime = this._getTimeInMsWithoutMobileSafari();
           var fTime = (newTime - this._currentTime) / 1000;
           if (fTime > 0.25) fTime = 0.25;
           this._currentTime = newTime;
           this._accumulator += fTime;
           while (this._accumulator >= this._deltaTime) {
               this.updateInputData();
               this.changeScene();
               this.updateScene();//我在这里！
               this._accumulator -= this._deltaTime;
           }
       }
       this.renderScene();
       this.requestUpdate();
   };
   
   ```

7. 然后可以在updateScene看到一个 this._scene.start();
   看到这个是不是有感觉了？我刚才之所以强调changeScene方法，就是因为它会把之前的Scene_Boot设为当前的场景。
   然后执行Scene_Boot的start方法。

   ```js
   SceneManager.updateScene = function() {
       if (this._scene) {
           if (!this._sceneStarted && this._scene.isReady()) {
               this._scene.start();
               this._sceneStarted = true;
               this.onSceneStart();
           }
           if (this.isCurrentSceneStarted()) {
               this._scene.update();
           }
       }
   };
   
   ```

8. 下面就是重点了！！在Scene_Boot中，有一个setupNewGame方法。这个方法就是真正启动游戏的方法了。

   ```js
   Scene_Boot.prototype.start = function() {
       Scene_Base.prototype.start.call(this);
       SoundManager.preloadImportantSounds();
       if (DataManager.isBattleTest()) {
           DataManager.setupBattleTest();
           SceneManager.goto(Scene_Battle);
       } else if (DataManager.isEventTest()) {
           DataManager.setupEventTest();
           SceneManager.goto(Scene_Map);
       } else {
           this.checkPlayerLocation();
           DataManager.setupNewGame();//我在这里！！
           SceneManager.goto(Scene_Title);
           Window_TitleCommand.initCommandPosition();
       }
       this.updateDocumentTitle();
   };
   
   ```

9. 进入其中，我们可以看到有一个createGameObjects方法，顾名思义，这个方法就是创建游戏对象的。

   ```js
   DataManager.setupNewGame = function() {
       this.createGameObjects();
       this.selectSavefileForNewGame();
       $gameParty.setupStartingMembers();
       $gamePlayer.reserveTransfer($dataSystem.startMapId,
           $dataSystem.startX, $dataSystem.startY);
       Graphics.frameCount = 0;
   };
   ```

10. 然后就是旅途的终点了，可以看到，我们可爱的$gameMessage就在这里诞生了。

    ```js
    DataManager.createGameObjects = function() {
        $gameTemp          = new Game_Temp();
        $gameSystem        = new Game_System();
        $gameScreen        = new Game_Screen();
        $gameTimer         = new Game_Timer();
        $gameMessage       = new Game_Message();
        $gameSwitches      = new Game_Switches();
        $gameVariables     = new Game_Variables();
        $gameSelfSwitches  = new Game_SelfSwitches();
        $gameActors        = new Game_Actors();
        $gameParty         = new Game_Party();
        $gameTroop         = new Game_Troop();
        $gameMap           = new Game_Map();
        $gamePlayer        = new Game_Player();
    };
    ```

    





# 存档与读档原理

## 存档的基本流程

1. 首先我们知道，如果想要进行存档，需要弹出一个存档页面，然后，点击存档的功能。

   那么我们首先就是找到这个存档功能的界面。

   既然是界面，那么必然是在scene中找到的。

   可以在我的速查文档中找到。

   负责存储管理的界面是Scene_Save。

   所以找到这个类。

2. 找到这个类之后，可以轻松发现里面有一个onSavefileOk方法。

   当存储文件OK时，进行游戏保存的操作。

   然后把当前保存的文件ID传递给saveGame方法。

   ```js
   Scene_Save.prototype.onSavefileOk = function() {
       Scene_File.prototype.onSavefileOk.call(this);
       $gameSystem.onBeforeSave();
       if (DataManager.saveGame(this.savefileId())) {//我在这里！！！
           this.onSaveSuccess();
       } else {
           this.onSaveFailure();
       }
   };
   ```

3. 这个方法干了两件事，第一个是backup，也就是准备存储。如果存储文件不存在就创建，如果是浏览器环境，就赶紧申请local storage之类的。但是真真正正存储文件的方法是`saveGameWithoutRescue`。

   ```js
   DataManager.saveGame = function(savefileId) {
       try {
           StorageManager.backup(savefileId);//进行游戏存储前的准备
           return this.saveGameWithoutRescue(savefileId);
       } catch (e) {
           console.error(e);
           try {
               StorageManager.remove(savefileId);
               StorageManager.restoreBackup(savefileId);
           } catch (e2) {
           }
           return false;
       }
   };
   ```

4. 这个方法首先用`JsonEx.stringify`方法，把`this.makeSaveContents()`的内容封装成了json。然后又保存了json文件。

   ```js
   DataManager.saveGameWithoutRescue = function(savefileId) {
       var json = JsonEx.stringify(this.makeSaveContents());//转为json
       if (json.length >= 200000) {
           console.warn('Save data too big!');
       }
       StorageManager.save(savefileId, json);//存储游戏
       this._lastAccessedId = savefileId;
       var globalInfo = this.loadGlobalInfo() || [];
       globalInfo[savefileId] = this.makeSavefileInfo();//全局存档的形成
       this.saveGlobalInfo(globalInfo);
       return true;
   };
   ```

   ​	

   先来看看`makeSaveContents`里面的内容吧！

   原来啊，我们的游戏存档里面只包含了这么点数据啊！ \$gameTemp, \$gameMessage和 $gameTroop。木有在存档里面。

   ```js
   DataManager.makeSaveContents = function() {
       // A save data does not contain $gameTemp, $gameMessage, and $gameTroop.
       var contents = {};
       contents.system       = $gameSystem;
       contents.screen       = $gameScreen;
       contents.timer        = $gameTimer;
       contents.switches     = $gameSwitches;
       contents.variables    = $gameVariables;
       contents.selfSwitches = $gameSelfSwitches;
       contents.actors       = $gameActors;
       contents.party        = $gameParty;
       contents.map          = $gameMap;
       contents.player       = $gamePlayer;
       return contents;
   };
   ```
   
5. 接下来就是`save`方法了。这个很简单。

   ```js
   StorageManager.save = function(savefileId, json) {
       if (this.isLocalMode()) {
           this.saveToLocalFile(savefileId, json);
       } else {
           this.saveToWebStorage(savefileId, json);
       }
   };
   ```

6. 我们先来看非web的存储。

   这个实际上就已经是真正的写入文件的函数了。但是我们的存储文件那个rpgsave是哪里来的呢？

   ```js
   StorageManager.saveToLocalFile = function(savefileId, json) {
       var data = LZString.compressToBase64(json);//用base64编码
       var fs = require('fs');
       var dirPath = this.localFileDirectoryPath();
       var filePath = this.localFilePath(savefileId);
       if (!fs.existsSync(dirPath)) {
           fs.mkdirSync(dirPath);
       }
       fs.writeFileSync(filePath, data);//写入文件
   };
   ```

   我们可以看到里面那个文件路径，他就是决定文件类型的方法。

7. 打开之后，终于真相大白

   ```js
   StorageManager.localFilePath = function(savefileId) {
       var name;
       if (savefileId < 0) {
           name = 'config.rpgsave';
       } else if (savefileId === 0) {
           name = 'global.rpgsave';
       } else {
           name = 'file%1.rpgsave'.format(savefileId);
       }
       return this.localFileDirectoryPath() + name;
   };
   ```

   

## 全局存档的形成

1. 回到saveGameWithoutRescue方法，可以看到里面有一个globalInfo什么什么的，这个就是全局存档啦。里面可以看到一个`makeSavefileInfo`方法，而且用对象的计算属性来接收了返回值对象。那么这个实际上就是全局存档的内容啦。

   ```js
   DataManager.saveGameWithoutRescue = function(savefileId) {
       var json = JsonEx.stringify(this.makeSaveContents());
       if (json.length >= 200000) {
           console.warn('Save data too big!');
       }
       StorageManager.save(savefileId, json);
       this._lastAccessedId = savefileId;
       var globalInfo = this.loadGlobalInfo() || [];
       globalInfo[savefileId] = this.makeSavefileInfo();
       this.saveGlobalInfo(globalInfo);
       return true;
   };
   ```

2. 跟踪这个方法之后，我们就可以看到全局对象的内容啦。这个东西自己也可以修改哦。

   ```js
   DataManager.makeSavefileInfo = function() {
       var info = {};
       info.globalId   = this._globalId;
       info.title      = $dataSystem.gameTitle;
       info.characters = $gameParty.charactersForSavefile();
       info.faces      = $gameParty.facesForSavefile();
       info.playtime   = $gameSystem.playtimeText();
       info.timestamp  = Date.now();
       return info;
   };
   ```

   

## 存档的加密

## 读档的基本流程

1. 读取存档的时候，我们首先会想到开始界面可以继续游戏。那么我们不妨找到标题页面。然后很容易就能看到createCommandWindow。

   ```js
   Scene_Title.prototype.createCommandWindow = function() {
       this._commandWindow = new Window_TitleCommand();
       this._commandWindow.setHandler('newGame',  this.commandNewGame.bind(this));
       this._commandWindow.setHandler('continue', this.commandContinue.bind(this));
       this._commandWindow.setHandler('options',  this.commandOptions.bind(this));
       this.addWindow(this._commandWindow);
   };
   ```

   这个里面就有continue的命令。

2. 然后来到绑定的`commandContinue`这里

   ```js
   Scene_Title.prototype.commandContinue = function() {
       this._commandWindow.close();
       SceneManager.push(Scene_Load);
   };
   ```

   可以看到，这个方法实际上就是把Scene_Load场景加载进来了而已。

   push方法在其他章节会详细讲述，这里不再赘述。只需要记住，push方法会new出来goto的场景。

3. 然后可以看到Scene_Load在构造的时候，继承了Scene_File类

   ```js
   Scene_Load.prototype = Object.create(Scene_File.prototype);
   Scene_Load.prototype.constructor = Scene_Load;
   ```
   
   
   
3. 然后去Scene_File的create方法中，可以看到有两个新窗体被创建。

   其中这个createListWindow就是创建各种存档文件窗口。
   
   ```js
   Scene_File.prototype.create = function() {
       Scene_MenuBase.prototype.create.call(this);
       DataManager.loadAllSavefileImages();
       this.createHelpWindow();
       this.createListWindow();
   };
   ```
   
5. 然后进入createListWindow方法，可以看到又有两个句柄被绑定了。

   ```js
   Scene_File.prototype.createListWindow = function() {
       var x = 0;
       var y = this._helpWindow.height;
       var width = Graphics.boxWidth;
       var height = Graphics.boxHeight - y;
       this._listWindow = new Window_SavefileList(x, y, width, height);
       this._listWindow.setHandler('ok',     this.onSavefileOk.bind(this));
       this._listWindow.setHandler('cancel', this.popScene.bind(this));
       this._listWindow.select(this.firstSavefileIndex());
       this._listWindow.setTopRow(this.firstSavefileIndex() - 2);
       this._listWindow.setMode(this.mode());
       this._listWindow.refresh();
       this.addWindow(this._listWindow);
   };
   ```
   
   这两个句柄就代表，当点击存档时，执行`onSavefileOk`方法。
   
6. 然后再进去，发现。。。

   ```js
   Scene_File.prototype.onSavefileOk = function() {
   };
   ```

   ！！！！！里面方法居然是空的。

   实际上这很正常。因为。。。。。。。

7. Scene_Load类在调用的时候，并不是被自己调用的。而是由Scene_Load来调用的。所以此时this指向是Scene_Load，真正的onSavefileOk还是由Scene_Load负责的。然后就可以看到，此时DataManager.loadGame方法被调用了。

   ```js
   Scene_Load.prototype.onSavefileOk = function() {
       Scene_File.prototype.onSavefileOk.call(this);
       if (DataManager.loadGame(this.savefileId())) {
           this.onLoadSuccess();
       } else {
           this.onLoadFailure();
       }
   };
   ```

8. DataManager.loadGame方法就是加载游戏的地方了。

   ```js
   DataManager.loadGame = function(savefileId) {
       try {
           return this.loadGameWithoutRescue(savefileId);
       } catch (e) {
           console.error(e);
           return false;
       }
   };
   
   ```

9. 又是我们熟悉的loadGameWithoutRescue

   ```js
   
   ```

   



# 事件对象生成原理















# 游戏对象类的继承关系

- Game_Temp：游戏中临时对象的类，这些数据不会被储存到存档之中。
- Game_System：系统数据的对象类
- Game_Timer：计时器的对象类
- Game_Message： 用于显示文本或选择等的信息窗口的状态的游戏对象类。
- 













# 菜单中按钮的形成原理





# 游戏文件加密与解密原理



# 自定义界面原理

5. 



## 自定义NPC对话

需要扩展Game_Interpreter类，事件解释器，用于将json命令翻译成js脚本并执行





# rpg_core.js

## Input——按键输入系统

> 这个静态类管理着键盘和手柄的输入

### 属性

```javascript
/**
 * The wait time of the key repeat in frames.
 *
 * @static
 * @property keyRepeatWait
 * @type Number
 */
Input.keyRepeatWait = 24;

/**
 * The interval of the key repeat in frames.
 *
 * @static
 * @property keyRepeatInterval
 * @type Number
 */
Input.keyRepeatInterval = 6;
```

### 按键映射

```javascript

/**
 * A hash table to convert from a virtual key code to a mapped key name.
 * 将一些键盘的按钮映射成数字
 * @static
 * @property keyMapper
 * @type Object
 */
Input.keyMapper = {
    9: 'tab',       // tab
    13: 'ok',       // enter
    16: 'shift',    // shift
    17: 'control',  // control，ctrl键
    18: 'control',  // alt
    27: 'escape',   // escape，ESC键
    32: 'ok',       // space
    33: 'pageup',   // pageup，就是小键盘的9
    34: 'pagedown', // pagedown，就是小键盘的3
    37: 'left',     // left arrow
    38: 'up',       // up arrow
    39: 'right',    // right arrow
    40: 'down',     // down arrow
    45: 'escape',   // insert，就是小键盘的0
    81: 'pageup',   // Q
    87: 'pagedown', // W
    88: 'escape',   // X
    90: 'ok',       // Z
    96: 'escape',   // numpad 0
    98: 'down',     // numpad 2
    100: 'left',    // numpad 4
    102: 'right',   // numpad 6
    104: 'up',      // numpad 8
    120: 'debug'    // F9
};

/**
 * A hash table to convert from a gamepad button to a mapped key name.
 *
 * @static
 * @property gamepadMapper
 * @type Object
 */
Input.gamepadMapper = {
    0: 'ok',        // A
    1: 'cancel',    // B
    2: 'shift',     // X
    3: 'menu',      // Y
    4: 'pageup',    // LB
    5: 'pagedown',  // RB
    12: 'up',       // D-pad up
    13: 'down',     // D-pad down
    14: 'left',     // D-pad left
    15: 'right',    // D-pad right
};
```

### 按键检测

```javascript
/**
 * 检查某按键现在是否被按下
 * @static
 * @method isPressed
 * @param {String} keyName The mapped name of the key
 * @return {Boolean} 如果按键正被按下的话，返回ture
 */
Input.isPressed = function(keyName) {

    if (this._isEscapeCompatible(keyName) && this.isPressed('escape')) {
        return true;
    } else {
        return !!this._currentState[keyName];
    }
};


/**
 *检测一个键是否刚刚按下
 * @static
 * @method isTriggered
 * @param {String} keyName The mapped name of the key
 * @return {Boolean} True if the key is triggered
 */
Input.isTriggered = function(keyName) {
    if (this._isEscapeCompatible(keyName) && this.isTriggered('escape')) {
        return true;
    } else {
        return this._latestButton === keyName && this._pressedTime === 0;
    }
};

/**
 * Checks whether a key is just pressed or a key repeat occurred.
 *检测某按键是否持续按下(持续按下的判定标准为该键按住持续的帧数大于keyRepeatWait)。
 * @static
 * @method isRepeated
 * @param {String} keyName The mapped name of the key
 * @return {Boolean} True if the key is repeated
 */
Input.isRepeated = function(keyName) {
    if (this._isEscapeCompatible(keyName) && this.isRepeated('escape')) {
        return true;
    } else {
        return (this._latestButton === keyName &&
                (this._pressedTime === 0 ||
                 (this._pressedTime >= this.keyRepeatWait &&
                  this._pressedTime % this.keyRepeatInterval === 0)));
    }
};

/**
 * Checks whether a key is kept depressed.
 * 检测某键是否长按
 * @static
 * @method isLongPressed
 * @param {String} keyName The mapped name of the key
 * @return {Boolean} True if the key is long-pressed
 */
Input.isLongPressed = function(keyName) {
    if (this._isEscapeCompatible(keyName) && this.isLongPressed('escape')) {
        return true;
    } else {
        return (this._latestButton === keyName &&
                this._pressedTime >= this.keyRepeatWait);
    }
};
```

## TouchInput——鼠标和触屏的检测

```

```



# rpg_objects.js

## Game_Temp

The game object class for temporary data that is not included in save data.

## Game_System

The game object class for the system data.

## Game_Timer

## Game_Actor

> 角色的对象类

所有的主角都是用这个类来实例化的。

### 初始化

- initialize

```javascript
Game_Actor.prototype.initialize = function(actorId) {
    Game_Battler.prototype.initialize.call(this);
    this.setup(actorId);
};
```

- setup

```javascript
Game_Actor.prototype.setup = function(actorId) {
  	//从$dataActors获取对象，并且把数据都拷贝到$gameActors对象上去
    var actor = $dataActors[actorId];
    this._actorId = actorId;
    this._name = actor.name;
    this._nickname = actor.nickname;
    this._profile = actor.profile;
    this._classId = actor.classId;
    this._level = actor.initialLevel;
    this.initImages();
    this.initExp();
    this.initSkills();
    this.initEquips(actor.equips);
    this.clearParamPlus();
    this.recoverAll();
};
```



- initMembers

```javascript
Game_Actor.prototype.initMembers = function() {
    Game_Battler.prototype.initMembers.call(this);//调用了Game_Battler的initMembers方法
    this._actorId = 0;
    this._name = '';
    this._nickname = '';
    this._classId = 0;
    this._level = 0;
    this._characterName = '';
    this._characterIndex = 0;
    this._faceName = '';
    this._faceIndex = 0;
    this._battlerName = '';
    this._exp = {};
    this._skills = [];
    this._equips = [];
    this._actionInputIndex = 0;
    this._lastMenuSkill = new Game_Item();
    this._lastBattleSkill  = new Game_Item();
    this._lastCommandSymbol = '';
};
```

## Game_Character

> 是Game_Player, Game_Follower, GameVehicle, 和 Game_Event 的父类

### NPC移动的方向常量

```javascript
Game_Character.ROUTE_END               = 0;
Game_Character.ROUTE_MOVE_DOWN         = 1;//向下移动
Game_Character.ROUTE_MOVE_LEFT         = 2;//向左移动
Game_Character.ROUTE_MOVE_RIGHT        = 3;//向右移动
Game_Character.ROUTE_MOVE_UP           = 4;//向上移动
Game_Character.ROUTE_MOVE_LOWER_L      = 5;//向左下移动
Game_Character.ROUTE_MOVE_LOWER_R      = 6;//向右下移动
Game_Character.ROUTE_MOVE_UPPER_L      = 7;
Game_Character.ROUTE_MOVE_UPPER_R      = 8;
Game_Character.ROUTE_MOVE_RANDOM       = 9;//随即移动
Game_Character.ROUTE_MOVE_TOWARD       = 10;//接近玩家
Game_Character.ROUTE_MOVE_AWAY         = 11;//远离玩家
Game_Character.ROUTE_MOVE_FORWARD      = 12;//前进一步
Game_Character.ROUTE_MOVE_BACKWARD     = 13;//后退一步
Game_Character.ROUTE_JUMP              = 14;//跳跃
Game_Character.ROUTE_WAIT              = 15;//等待
Game_Character.ROUTE_TURN_DOWN         = 16;
Game_Character.ROUTE_TURN_LEFT         = 17;
Game_Character.ROUTE_TURN_RIGHT        = 18;
Game_Character.ROUTE_TURN_UP           = 19;
Game_Character.ROUTE_TURN_90D_R        = 20;
Game_Character.ROUTE_TURN_90D_L        = 21;
Game_Character.ROUTE_TURN_180D         = 22;
Game_Character.ROUTE_TURN_90D_R_L      = 23;
Game_Character.ROUTE_TURN_RANDOM       = 24;
Game_Character.ROUTE_TURN_TOWARD       = 25;
Game_Character.ROUTE_TURN_AWAY         = 26;
Game_Character.ROUTE_SWITCH_ON         = 27;
Game_Character.ROUTE_SWITCH_OFF        = 28;
Game_Character.ROUTE_CHANGE_SPEED      = 29;//更改移动速度
Game_Character.ROUTE_CHANGE_FREQ       = 30;//更改移动频率
Game_Character.ROUTE_WALK_ANIME_ON     = 31;
Game_Character.ROUTE_WALK_ANIME_OFF    = 32;
Game_Character.ROUTE_STEP_ANIME_ON     = 33;
Game_Character.ROUTE_STEP_ANIME_OFF    = 34;
Game_Character.ROUTE_DIR_FIX_ON        = 35;
Game_Character.ROUTE_DIR_FIX_OFF       = 36;
Game_Character.ROUTE_THROUGH_ON        = 37;
Game_Character.ROUTE_THROUGH_OFF       = 38;
Game_Character.ROUTE_TRANSPARENT_ON    = 39;
Game_Character.ROUTE_TRANSPARENT_OFF   = 40;
Game_Character.ROUTE_CHANGE_IMAGE      = 41;
Game_Character.ROUTE_CHANGE_OPACITY    = 42;
Game_Character.ROUTE_CHANGE_BLEND_MODE = 43;
Game_Character.ROUTE_PLAY_SE           = 44;//播放SE
Game_Character.ROUTE_SCRIPT            = 45;//使用脚本
```

### 自动接近目标的算法

- 向某个对象移动

```javascript
Game_Character.prototype.moveTowardCharacter = function(character) {
    var sx = this.deltaXFrom(character.x);
    var sy = this.deltaYFrom(character.y);
    if (Math.abs(sx) > Math.abs(sy)) {
        this.moveStraight(sx > 0 ? 4 : 6);
        if (!this.isMovementSucceeded() && sy !== 0) {
            this.moveStraight(sy > 0 ? 8 : 2);
        }
    } else if (sy !== 0) {
        this.moveStraight(sy > 0 ? 8 : 2);
        if (!this.isMovementSucceeded() && sx !== 0) {
            this.moveStraight(sx > 0 ? 4 : 6);
        }
    }
};
```

- 向玩家移动

```javascript
Game_Character.prototype.moveTowardPlayer = function() {
    this.moveTowardCharacter($gamePlayer);
};
```



## Game_Unit

> 是Game_Party和Game_Troop的父类



## Game_Party

> 这个对象类是为队伍准备的，里面记录着金币、物品之类的东西。



## Game_Map

> 游戏地图的对象类，It contains scrolling and passage determination functions. 

## Game_Event

> 游戏事件的对象类，它包含了事件页切换，还有运行并行事件。

## Game_Troop

> 这个对象类是有关于敌群和战斗数据的



### 初始化

- **initialize：初始化**

非常重要，可以看到这个初始化的时候，给对象添加了很多属性。`$gameParty `对象的属性就是这么来的。

```javascript
Game_Party.prototype.initialize = function() {
    Game_Unit.prototype.initialize.call(this);
    this._gold = 0;//为实例对象添加金币属性
    this._steps = 0;
    this._lastItem = new Game_Item();
    this._menuActorId = 0;
    this._targetActorId = 0;
    this._actors = [];
    this.initAllItems();
};
```

- initAllItems：物品初始化

```javascript
Game_Party.prototype.initAllItems = function() {
    this._items = {};
    this._weapons = {};
    this._armors = {};
};
```

### 队伍长度

- exists：队伍是否存在

```javascript
Game_Party.prototype.exists = function() {
    return this._actors.length > 0;
};
```

- size：队伍长度

```javascript
Game_Party.prototype.size = function() {
    return this.members().length;
};
```

- isEmpty：是否为空

```javascript
Game_Party.prototype.isEmpty = function() {
    return this.size() === 0;
};
```

### 队伍成员

- members

```javascript
Game_Party.prototype.members = function() {
    return this.inBattle() ? this.battleMembers() : this.allMembers();
};
```

- allMembers

```javascript
Game_Party.prototype.allMembers = function() {
    return this._actors.map(function(id) {
        return $gameActors.actor(id);
    });
};
```

- battleMembers

```javascript
Game_Party.prototype.battleMembers = function() {
    return this.allMembers().slice(0, this.maxBattleMembers()).filter(function(actor) {
        return actor.isAppeared();
    });
};
```

- **maxBattleMembers：战斗时最大参战人数**

```javascript
Game_Party.prototype.maxBattleMembers = function() {
    return 4;
};
```

- leader：队伍领袖

```
Game_Party.prototype.leader = function() {
    return this.battleMembers()[0];
};
```

- reviveBattleMembers：全员复活

```javascript
Game_Party.prototype.reviveBattleMembers = function() {
    this.battleMembers().forEach(function(actor) {
        if (actor.isDead()) {
            actor.setHp(1);
        }
    });
};
```



### 金币相关

- gold：查看当前队伍所持金币的数量

直接返回属性值，其实我觉得就很神秘，JavaScript并没有访问控制，你直接调用属性也可以啊，何必再写一个getter。可能这就是大佬的代码风格吧。

```javascript
Game_Party.prototype.gold = function() {
    return this._gold;
};
```

- gainGold： 获取金币

难点在于clamp是什么意思，这个其实就是取整，把范围控制在区间内。

```javascript
Game_Party.prototype.gainGold = function(amount) {
    this._gold = (this._gold + amount).clamp(0, this.maxGold());
};
```

- loseGold：失去金币

```javascript
Game_Party.prototype.loseGold = function(amount) {
    this.gainGold(-amount);
};
```

- **maxGold：最大金币数**

```javascript
Game_Party.prototype.maxGold = function() {
    return 99999999;
};
```



## Game_Interpreter

> 运行事件命令的解释器

就是编辑器里面那些事件的代码。





### character

```javascript
Game_Interpreter.prototype.character = function(param) {
    if ($gameParty.inBattle()) {
        return null;
    } else if (param < 0) {
        return $gamePlayer;
    } else if (this.isOnCurrentMap()) {
        return $gameMap.event(param > 0 ? param : this._eventId);
    } else {
        return null;
    }
};
```



### 设置事件位置

```javascript
// Set Event Location
Game_Interpreter.prototype.command203 = function() {
    var character = this.character(this._params[0]);
    if (character) {
        if (this._params[1] === 0) {  // Direct designation
            character.locate(this._params[2], this._params[3]);
        } else if (this._params[1] === 1) {  // Designation with variables
            var x = $gameVariables.value(this._params[2]);
            var y = $gameVariables.value(this._params[3]);
            character.locate(x, y);
        } else {  // Exchange with another event
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



### 初始化

```javascript
Game_Interpreter.prototype.initialize = function(depth) {
    this._depth = depth || 0;
    this.checkOverflow();
    this.clear();
    this._branch = {};
    this._params = [];
    this._indent = 0;
    this._frameCount = 0;
    this._freezeChecker = 0;
};
```



# rpg_managers.js

这里面的类都是静态类。也就是说在manager里面的类都是可以直接使用的，而不能创建对象。

比如：

```javascript
SoundManager.playSystemSound(1);//播放系统的1号音效
```





下面的书写顺序是完全按照MV脚本的顺序写的，可以直接对着来看。因为这些代码实在是很长，所以我不可能一一讲述，我只能讲一些比较重要的地方。


## DataManager

>  这个静态类管理着数据库和游戏对象

这个类负责把你在编译器中写的那些数据进行解析，然后分发给其他其他manager。你在编译器中所写的数据一部分会被解析为json文件，这个类就可以处理这些json文件。



## ConfigManager

> 这个静态类管理着设置的数据





## StorageManager

> 这个静态类是来管理游戏存档的



## ImageManager

> 这个静态类是来加载图像，创建位图对象并保留它们的



## AudioManager

> 这个静态类是来控制BGM, BGS, ME 和 SE的



### 属性

```javascript
AudioManager._masterVolume   = 1;   // (min: 0, max: 1)
AudioManager._bgmVolume      = 100;
AudioManager._bgsVolume      = 100;
AudioManager._meVolume       = 100;
AudioManager._seVolume       = 100;
AudioManager._currentBgm     = null;
AudioManager._currentBgs     = null;
AudioManager._bgmBuffer      = null;
AudioManager._bgsBuffer      = null;
AudioManager._meBuffer       = null;
AudioManager._seBuffers      = [];
AudioManager._staticBuffers  = [];
AudioManager._replayFadeTime = 0.5;
AudioManager._path           = 'audio/';
AudioManager._blobUrl        = null;
```



## SoundManager

> 这个静态类可以播放数据库中所定义的音效

### 播放音效

```javascript
SoundManager.playSystemSound = function(n) {
    if ($dataSystem) {
        AudioManager.playStaticSe($dataSystem.sounds[n]);
    }
};
```



## TextManager

> 这个静态类用于管理游戏用语和消息



## SceneManager

> 这个静态类管理着场景变换

### run

```javascript
SceneManager.run = function(sceneClass) {
    try {
        this.initialize();//场景初始化，包括音频，文件，插件等各种东西
        this.goto(sceneClass);//前往该场景
        this.requestUpdate();//场景刷新
    } catch (e) {
        this.catchException(e);
    }
};
```

## BattleManager

> 这个静态类管理战斗的进行

### 初始化

- setup

```javascript
BattleManager.setup = function(troopId, canEscape, canLose) {
    this.initMembers();//初始化各种东西，不仅仅是成员
    this._canEscape = canEscape;//允许逃跑
    this._canLose = canLose;//允许失败
    $gameTroop.setup(troopId);
    $gameScreen.onBattleStart();
    this.makeEscapeRatio();
};
```

- initMembers

```javascript
BattleManager.initMembers = function() {
    this._phase = 'init';
    this._canEscape = false;//允许逃跑
    this._canLose = false;//允许失败
    this._battleTest = false;
    this._eventCallback = null;
    this._preemptive = false;//是否是先手
    this._surprise = false;
    this._actorIndex = -1;
    this._actionForcedBattler = null;
    this._mapBgm = null;
    this._mapBgs = null;
    this._actionBattlers = [];
    this._subject = null;
    this._action = null;
    this._targets = [];
    this._logWindow = null;
    this._statusWindow = null;
    this._spriteset = null;
    this._escapeRatio = 0;
    this._escaped = false;
    this._rewards = {};
    this._turnForced = false;
};
```

- 



## PluginManager

> 这个静态类管理着插件们

### setup

调用一个插件。

```javascript
PluginManager.setup = function(plugins) {
    //遍历插件
    plugins.forEach(function(plugin) {
        //如果插件存在，并且不在_scripts里面的话
        if (plugin.status && !this._scripts.contains(plugin.name)) {
            //给插件起名，加载，并且给_scripts加入该插件
            this.setParameters(plugin.name, plugin.parameters);
            this.loadScript(plugin.name + '.js');
            this._scripts.push(plugin.name);
        }
    }, this);
};
```





# RPG Maker MV 运行原理

## main.js

main.js里面只有两句代码，但是是核心。

我们可以把main.js的功能分为两个：

1. 启动脚本插件
2. 启动场景

```javascript
PluginManager.setup($plugins);//启用插件

window.onload = function() {
    SceneManager.run(Scene_Boot);
};
```



### 启动插件

运行游戏时，首先会启用插件。这个`PluginManager`是在`rpg_managers.js`中的定义的，可以去看上边的代码。

这个`$plugins`是存放在js文件夹中的plugins.js里面，里面放着你所有在项目中用到的插件。



### 启动场景

`window.onload`对于前端工程师来说实在是非常熟悉了，在原生DOM中，绑定HTML标签的时候就需要用到这个。`window.onload`就是指当 HTML 文档加载完毕后，立刻回调function里面的内容。在MV里面就是说当游戏资源都加载完毕后，立刻进行场景渲染。

`SceneManager.run`也是在`rpg_managers.js`中的定义的。





## 保存游戏

1. DataManager.saveGame

```javascript
DataManager.saveGame = function(savefileId) {
    try {
        StorageManager.backup(savefileId);
        return this.saveGameWithoutRescue(savefileId);
    } catch (e) {
        console.error(e);
        try {
            StorageManager.remove(savefileId);
            StorageManager.restoreBackup(savefileId);
        } catch (e2) {
        }
        return false;
    }
};
```



2. 

```javascript
StorageManager.backup = function(savefileId) {
    if (this.exists(savefileId)) {
        console.log("保存游戏2 StorageManager.backup")
        if (this.isLocalMode()) {
            var data = this.loadFromLocalFile(savefileId);
            var compressed = LZString.compressToBase64(data);
            var fs = require('fs');
            var dirPath = this.localFileDirectoryPath();
            var filePath = this.localFilePath(savefileId) + ".bak";
            if (!fs.existsSync(dirPath)) {
                fs.mkdirSync(dirPath);
            }
            fs.writeFileSync(filePath, compressed);
        } else {
            var data = this.loadFromWebStorage(savefileId);
            var compressed = LZString.compressToBase64(data);
            var key = this.webStorageKey(savefileId) + "bak";
            localStorage.setItem(key, compressed);
        }
    }
};
```





# 控制台

```js
require('nw.gui').Window.get().showDevTools();
```

 Utils.isOptionValid('test');







```
 var button = new Sprite_Button();
 var x = buttonWidth * [1, 2, 4][i];
 var w = buttonWidth * (i === 2 ? 2 : 1);
 button.bitmap = bitmap;
 button.setColdFrame(x, 0, w, buttonHeight);
 button.setHotFrame(x, buttonHeight, w, buttonHeight);
 button.visible = false;
 this._buttons.push(button);
 this.addChild(button);
```





# 调试模式

## 为什么可以穿墙

当按住ctrl键，并且在测试模式下，可以进行穿墙

```js
Game_Player.prototype.isDebugThrough = function() {
    return Input.isPressed('control') && $gameTemp.isPlaytest();
};
```





```
Game_Temp.prototype.isPlaytest = function() {
    return this._isPlaytest;
};

```

# 修改游戏模板

打开steam中RPGMakerMV的文件夹，找到NewData文件夹，里面就是新游戏创建时的模板文件，如果修改其中的文件，那么如果再次创建一个新游戏，那么就可以按照你自己修改的模板来创建，一些DLC也可以直接加进来这样一劳永逸。
