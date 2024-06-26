# 通用性RPG游戏的定义

1. 游戏系统有过大量的换皮
    
2. 游戏系统容易独立出来，游戏的玩法和内容耦合性较低
    
3. 存在一个可操控的主角
    

  

  

## 对组件的基本定义

一个组件可以被理解为某种功能，例如某个挂载了对话组件的实体是“能够对话的”，通过对实体挂载不同组件，可以定义一个具体的实体。例如商人NPC是可以对话的，可以交易的，拥有个人信息的实体。

# 2D类型RPG的基本内容概括

RPG游戏存在三个核心——战斗，社交，探索

因此RPG的设计核心本质上是围绕这些功能所抽象出来的游戏系统。城镇，战斗就构成了RPG的战斗要素。对话系统构成了社交，而场景则构成了探索。

而玩家和这这些系统的不同交互就构成了不同的RPG。

这三个系统分别都有各自的核心组件，通过挂载这些组件，RPG就可以形成不同的核心要素，
## 城镇系统

  

这里的城镇并不是字面意义上的城镇，而是泛指玩家可以恢复，购买武器装备等补充战力的地方。野外的商人也是一个城镇，图文游戏的一个节点也可以是一个城镇。城镇往往包含装备商店，旅馆，NPC支线，赌场，小游戏， 宝箱等部分。

  

按照交互源，交互方式，交互目标的方式分解，城镇系统可以分为以下几个部分

- 交易组件
    
    - 交易类型：
        
        - 固定奖励：武器系统装备系统等，也可以是剧情和对话等
            
        - 固定金额，随机奖励：类似于DQ的赌场的机制
            
        - 随机奖励，固定奖励：
            
        - 负面奖励+正面奖励：类似于诅咒获得物品
            
        - 游戏获得奖励：指玩家进行游戏内的独立小游戏获得奖励，类似大富翁的各种小游戏
            
            - 钓鱼
                
            - 转盘
                
            - 猜拳
                
    - 交易内容：
        
        - 交易付出
            
        - 交易得到
            
- 任务组件
    
    - 任务奖励
        
    - 任务达成条件：例如当前对象hp<=0，或者和当前对象对话等
        
    - 任务基本信息：名称，描述
        
    
      
    

  

挂载这些组件的实体可以出现在任何一个地方。

  

  

## 战斗系统

战斗系统是指玩家发生战斗的一切对象。主要包括以下几个组件：

  

  

- 战斗属性：
    
    - 基本属性：HP，MP，移动速度等等
        
    - 特殊属性：技能，自身buff等
        
- 战斗特殊buff：指战前玩家某种属性临时提升，或者一些特殊效果。
    
- 战斗逻辑：（以权重的形式反应）
    
    - 攻击状态机：
        
        - 当没有遇到玩家时
            
        - 当进入发现范围时
            
        - 当进入攻击范围时
            
        - 当离开攻击范围时
            
        - 当离开发现范围时
            
    - 攻击方式
        
        - 攻击
            
            - 攻击距离
                
            - 攻击范围
                
        - 技能
            
            - 参考技能组件
                
        
          
        
- 战斗阵营：int，如果相同阵营，则不会互相攻击，0代表中立，不会对任何人发动攻击，但是可以被攻击。-1代表会攻击任何人的敌人。**当和主角一个阵营时，默认都为主角的队友。**
    

  

  

## 玩家（角色）

玩家可以是任何一个角色，NPC的大部分属性都和玩家相同。玩家的大部分组件也和战斗系统相同，但是会多出来一些额外的组件和属性。而玩家组件则是挂载了玩家属性和可操控组件的组件，挂载了玩家组件的实体会被认为是玩家。

- 个人信息：玩家的名字，昵称
    
- 装备和物品
    
- 玩家组件：
    
    - 玩家属性：多出来金币，经验值，等级等
        
    - 移动方式：RPG中存在三种移动方式：
        
        - 传统移动：用鼠标或者wasd移动
            
        - 鼠标点击，不移动：类似于《废都物语》的点击式触发
            
        - ~~节点式：类似于《迷托邦》的节点式移动触发（可以用鼠标点击实现）~~
            
    - 天赋：玩家自带的独有buff，例如《杀戮尖塔》中战士可以回血。
        

  

  

  

  

  

  

## 场景系统

场景系统是基于上述系统所拓展的，一般RPG都不会发生在单一的场景内，存在若干的连续场景。

  

- 可达方式：可达方式是或的关系，比如《古剑奇谭1》中，蓬莱就只能御剑飞行过去，而江南则可以步行过去也可以飞过去。
    
    - 默认。默认需要用图的结构来描述各个节点的可达与否
        
        - 2d场景的拓扑关系：指多个场景地图中的关联关系。例如ab是单向连通，bc是双向连通等。
            
    - 飞行（传送），飞行时不需要指定拓扑关系，注册了飞行的节点够可以到达
        
- 基本信息：场景名等
    
- 战斗方式（表现方式）：将战斗抽象为地点和逻辑可以组合多种战斗方式，例如类似古剑奇谭2的半回合制，以及for the king的战棋机制。
    
    - 战斗地点：
        
        - 地图内
            
        - 单独开一个场景
            
    - 战斗逻辑和表现
        
        - 俯视角ARPG
            
        - 横板ARPG（需要刚体）
            
        - 放置类回合制（图文游戏）
            
        - 战棋
            
        - sv回合制：可以看到自己的横板站位
            
        - 传统JRPG回合制：只能看到敌人例会和自己头像
            
        
          
        
          
        

  

  

## 对话系统

  

对一个实体挂载对话系统的组件之后，触发实体会进行对话。

- 简单对话内容。当配置多条的时候会随机对话
    
- 连续对话：复杂剧情实现起来会非常复杂，需要变量控制，以及需要对话脚本的支持
    
    ```Python
    你好
    选择(再见，你好)
    再见：
    别走啊，我会给你一个苹果的
    
    那不行，我需要两个（说服）：根据运气值。30%概率成功
    好吧（获得苹果）
    无视
    
    你好：
    给你一个苹果（HP+5）
    
    
    ```
    

  

  

## 实体的基本组件

一个RPG是一个世界，而世界填充了很多挂载了组件的实体。

通过为实体挂载上述的若干组件就可以形成不同的功能。实体还额外拥有很多默认的组件，这些组件默认挂载

- 位置坐标：（x,y）
    
- 显示：
    
    - 变量控制（读取调用某对象身上的可变变量，例如主角.金币>1000）
        
    - 直接控制：true或者false
        
- 移动方式：（当挂载了玩家组件的时候默认玩家的移动方式）
    
    - 循环移动
        
    - 随机移动
        
    - 跟随移动
        
    - 远离移动
        
    - 静止
        
- 触发方式：
    
    - 点击触发
        
        - 触发条件
            
    - 接触触发
        
        - 触发条件
            
    - 并行触发
        
        - 触发条件
            
    - 自动触发
        
        - 触发条件
            
- 组件们：挂载上述的若干组件。
    
    - 组件的触发优先级，需要来判断哪个组件优先执行
        
- 系统回调组：一个对象身上可以挂载多个触发条件，会依次进行触发
    
    - 触发条件：一些特殊效果可以在这里实现。例如遇到魔王的时候，场景的tilemap图块发生变化等。
        
    - 效果：
        
- 触发回调组：指当实体被触发之后产生的回调，一些宝箱事件只允许被触发一次，因此需要触发回调来取消实体显示。
    
- 可变变量组：实体身上可以挂载可变变量，例如可以定义这个变量为好感度。一个实体可以挂载多个可变变量。
    

  

## 其他

- 装备组件
    
    - 装备信息
        
    - 战斗属性
        
    - 技能/buff
        
    
      
    
- 物品组件
    
    - 物品信息
        
    - 物品价值
        
    - 是否可以被使用
        
    - 作用对象/范围
        
- buff组件
    
    - buff效果
        
    - buff作用时机
        
    
      
    

  

  

- 技能组件
    
    - 技能信息
        
    - 技能效果
        
    - 技能动画
        
    - 技能触发时机
        
        - 战时
            
        - 非战时
            
        - 任意
            
- buff组件
    
    - buff效果
        
    - 触发时机
        
        - 战时
            
        - 非战时
            
        - 任意
            
    

  

  

  

# 组件触发条件的判断

所有基本类型的组件都是可以被判断的。

例如希望实现一个当队友NPC好感度达到100的时候，触发对话剧情。那么实现逻辑如下：

1. 为NPC挂载战斗组件，并且和玩家同一阵营
    
2. 配置可变变量1
    
3. 在NPC身上配置触发条件：
    
    1. 触发类型：自动触发
        
    2. 触发条件：NPC.可变变量1 >= 100
        
    3. 触发方法：触发时对象身上的对话id为2的对话组件生效，触发对话。
        

  

  

除了这种某个具体对象的回调，也可以为全局挂载回调：例如打过boss之后，新手村的NPC对话会发生变化。

在新手村NPC身上配置触发条件：

- 触发类型：接触触发
    
- 触发条件：boss身上的可变变量2（被击败）为true
    
- 变化内容：触发时对象身上的对话id为3的对话组件生效