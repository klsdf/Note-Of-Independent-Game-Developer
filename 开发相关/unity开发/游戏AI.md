

当前游戏中的常用的AI方法，大致有三种：
- 状态机（FSM-Finite State Machine)
- 行为树（BT-Behavior Tree）
- 层次任务网络（HTN-Hiearchical Task Network）
- GOAP（Goal-Oriented Action Planning）






# 状态机（FSM-Finite State Machine)


- 主要由程序使用代码构建状态机进行开发和维护，策划负责发起需求，但不参与逻辑的具体构建和维护，开发速度快，适合AI需求量小或则需求稳定的项目。  
- 状态机最大的问题就是状态间极为复杂的关联关系，给策划后续的拓展和调整是一个极为困难的工作。
- 为了解决这种情况，有些游戏会把相关的状态机归为到一个子集中，例如DOOM2016版：在状态机的基础上将状态进行分类，产生状态集的概念，从而减少集与集之间的关联数量。搞分层状态机。




# 行为树（BT-Behavior Tree）

- 让状态可以复用
- 可以维护更复杂的逻辑





# 层次任务网络（HTN-Hiearchical Task Network）


- 把**复合任务**变为若干的**方法**
- 把**方法**变为若干**原子任务**
- planner输出的都是原子任务
- 每次环境变化都可以会改变当前的任务。如果环境变化影响了当前任务的前提条件（比如原子任务的执行条件不再满足），那么planner通常会**中断当前计划，重新规划**，这意味着之前的任务序列会被清空或废弃。



``` mermaid
flowchart LR
  %% 输入区域
  subgraph 环境输入
    S[🎯 Sensors<br>感知器]
    T[🪓 Task Results<br>任务反馈]
  end

  subgraph 状态更新
    WS[🌍 World States<br>世界状态]
  end

  subgraph 规划输入
    D[📚 Domain<br>任务域知识]
    D --> CT[📦 Compound Tasks<br>复合任务]
    CT --> M[🛠️ Methods<br>方法集]
    M --> PT[🪄 Primitive Tasks<br>原子任务]
  end

  subgraph 规划过程
    P[🧠 Planner<br>任务规划器]
  end

  subgraph 输出
    PL[📜 Plan<br>原子任务序列]
  end

  %% 连接
  S -- 外部影响 --> WS
  T -- 任务影响 --> WS
  WS -- 输入状态 --> P
  CT -. 定义于 .-> D
  M -. 属于 .-> D
  PT -. 属于 .-> D
  D -- 输入结构 --> P
  P -- 输出顺序动作 --> PL

```




```mermaid

flowchart TD

  %% 顶层复合任务
  A[🎯 Compound Task<br>度过愉快的一天]

  %% 子任务分解
  A --> B1[🍽️ 吃早饭]
  A --> B2[🎾 玩耍]
  A --> B3[😴 睡午觉]

  %% 吃早饭的方法分解
  B1 --> C1{Method 1:<br>冰箱有罐头}
  C1 --> D1[➡️ Primitive:<br>走到餐桌]
  C1 --> D2[➡️ Primitive:<br>坐下]
  C1 --> D3[➡️ Primitive:<br>吃罐头]

  B1 --> C2{Method 2:<br>冰箱没罐头}
  C2 --> E1[➡️ Primitive:<br>走到厨房]
  C2 --> E2[➡️ Primitive:<br>打开冰箱]
  C2 --> E3[➡️ Primitive:<br>拿出罐头]
  C2 --> E4[➡️ Primitive:<br>走到餐桌]
  C2 --> E5[➡️ Primitive:<br>坐下]
  C2 --> E6[➡️ Primitive:<br>吃罐头]

  %% 玩耍的方法
  B2 --> F1{Method 1:<br>主人在家}
  F1 --> G1[➡️ Primitive:<br>找主人]
  F1 --> G2[➡️ Primitive:<br>扑进怀里]
  F1 --> G3[➡️ Primitive:<br>一起玩小球]

  B2 --> F2{Method 2:<br>主人不在}
  F2 --> H1[➡️ Primitive:<br>玩毛线球]
  F2 --> H2[➡️ Primitive:<br>看窗外发呆]

  %% 睡午觉直接是原子任务
  B3 --> I1[➡️ Primitive:<br>找到阳光角落]
  B3 --> I2[➡️ Primitive:<br>躺下]
  B3 --> I3[➡️ Primitive:<br>睡觉（打呼噜噜）]

```



# GOAP（Goal-Oriented Action Planning）