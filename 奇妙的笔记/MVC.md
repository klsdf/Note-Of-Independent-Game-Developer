


1. **mvc中的，model响应，应该只影响ui显示，不应该和逻辑绑定。**
2. **初始化的时候，应该只初始化私有变量，不要初始化带响应式的set的属性。**



下面是nodedraw中出现的典型负面例子：

SkillAddData

```c#
    /// <summary>
    /// 局外宝石的数量
    /// </summary>
    [SerializeField]
    [Header("局外宝石的数量")]
    private int _gemCount;
    public int GemCount
    {
        get => _gemCount;
        set
        {
            _gemCount = value;
            NotifyDataChanged(this);
            YanGF.Save.Save<SkillAddData>(CardSaveType.SkillAddData.ToString(), this);
        }
    }

    public SkillAddData()
    {
        //其余变量
        GemCount = 0;
    }

```



gamecontroller
```c#
private void InitDatas()
    {

        // 初始化SkillData数据
        SkillAddData skillAddData = YanGF.Save.Load<SkillAddData>(CardSaveType.SkillAddData.ToString(), new SkillAddData());
        YanGF.Model.RegisterModule(skillAddData);

        // 初始化GameRuntimeData数据

        YanGF.Model.RegisteOrUpdateModule(new GameRuntimeData(
            drawCost: 0,
            gameProgressIndex: 0,
            population: 0,
            currentScore: 0,
            globalLevel: 1
        ));
    }
```

1. 如上所示，gamecontroller中，需要本地化读取 SkillAddData，如果没有数据则初始化这个数据。
2. 而实际上，不管有没有用到这个初始化数据，new SkillAddData()都会直接调用无参构造函数，导致GemCount被修改了。
3. 而更加逆天的是，GemCount被修改后会自动保存数据。就导致存档数据中永远都是初始化的数据


所以说，初始化的时候不应该修改带响应的数据，也不应该直接对set方法加多余逻辑，单纯NotifyDataChanged就可以了

类似的还有

carddata
```c#
    /// <summary>
    /// 卡牌的永久价值
    /// </summary>
    private int _cardValue;
    public int CardValue
    {
        get
        {
            return _cardValue;
        }
        set
        {
            _cardValue = value;
            OnCardDataChange();
        }
    }

    public CardData Clone()
    {
        CardData clone = new CardData
        {
            cardName = this.cardName,
            cardDescription = this.cardDescription,
            _cardValue = this._cardValue,
            effectTargetTags = new List<string>(this.effectTargetTags),
            effectTargetNames = new List<string>(this.effectTargetNames),
            onInit = this.onInit,
            onTick = this.onTick,
            onValueChange = this.onValueChange,
            onUpdate = this.onUpdate,
            cardTag = new List<string>(this.cardTag),
            cardPrice = this.cardPrice,
            cardRange = this.cardRange != null ? this.cardRange.Clone() : null,
            rangePosition = this.rangePosition,
            CurrentCountdown = this.CurrentCountdown,
            MaxCountdown = this.MaxCountdown,
            // innerCounterSlot_int_2 = this.innerCounterSlot_int_2,
            cardRarity = this.cardRarity,
            // tempValue = this.tempValue,
            tempSources = new List<TempValueSource>(this.tempSources),
            isShopCard = this.isShopCard,
            cardInEvent = this.cardInEvent,
            cardOutEvent = this.cardOutEvent
        };

        return clone;
    }
```


复制原型的时候，对象还没有被创建，因此OnCardDataChange时，修改ui会报空引用的错误。所以复制这种数据的时候，一定不要动响应式属性。