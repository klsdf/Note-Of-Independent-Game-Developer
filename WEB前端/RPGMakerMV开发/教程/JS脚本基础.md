#  JS基础介绍和配置

## 学习前的科普和准备~

在我们开始学习脚本之前，可能已经有很多同学知道了，MV是使用一种叫做JavaScript的脚本语言的。我们大概明白js可以实现很多事件无法完成的操作，也可以实现很多绚丽的场景效果。但是这些都是一些朦朦胧胧的感觉而已。我们在正式开始学习JavaScript（简称JS）之前，我想首先给各位大致介绍一下JS这门语言。同时说明一下，我们MV和JS究竟有什么关系？MV为什么需要js作为脚本？



什么是JS？一起来了解JS的历史吧！

JS，原名Javascript，最早是为了完成网页端的表单验证所被发明出来的，再后来，JavaScript被引入了ECMA，进行了一代代更新，诞生出了DOM、BOM、node等技术，在现在，JS已经变成了一个真正的世界级语言了。

什么？没看懂这段话？很正常，教科书一般都喜欢写这种绕口的定义，所以说大家看不懂高数书或者线代是很正常的，不是说你学不会，而是说学校的书根本就没打算好好教你！言归正传，我写这个的目的就是想说，**在本文，坚决不会用这种枯燥、乏味的词语来讲解！！**一切的一切都会尽可能的通俗易懂，毕竟对于一个游戏来说，乐趣是最重要的。一个游戏引擎的教程当然也要充满**乐趣**才行啦！

好，再次言归正传，JS为什么会被发明出来呢？在JS之前，已经拥有了横扫千军万马的C++，还有傲视群雄的Java，何必要再推出这么一个新生儿呢？

诸位请搬好小板凳，故事即将开始。



大家都有用过网站吧？在上网的时候，如果单纯浏览还好，如果要发帖或者评论什么的，往往会要求你进行**登录或者注册**。就以哔哩哔哩的注册为例：

<img src="img\image-20211105213051034.png" alt="image-20211105213051034" style="zoom:67%;" />

你看，如果注册时，昵称不符合要求，那么浏览器就会告诉你昵称有问题。直到你把这些都改好之后，才可以点击注册的按钮。这个在现在看来可能是理所应当的设计了，但是在20年前的1995年，这种操作还无法实现。

当时的人们如果想要注册账号，首先需要点击这个注册按钮，然后数据会被传到服务器里面，然后服务器会分析这个昵称是否符合要求，如果不符合，那么服务器会发消息回去告知用户。

一般来说，服务器响应还是很快的，这个设计确实没有什么问题。但是如果服务器在很远的地方呢？或者网速不行呢？我为了注册一个账号，首先发送了一个账号过去，等了一分钟，网页才有了响应，告诉我我的账号格式有问题。然后我又得重新发一遍。如果网速再不行，传不过去，那么用户体验就会非常差。

所以JavaScript就被发明出来了。

JavaScript可以在浏览器里面直接分析你的账号数据是否符合要求，直到你完全修正后之后，才把数据发送过去。这样就可以极大提高用户体验了。



那么为什么非要叫JavaScript？？它和java有什么关系？

答案是：没有关系！就跟雷锋和雷峰塔一样，就和老婆和老婆饼一样。仅仅是名字一样而已。

不过话又说回来，虽然两个语言没啥关系，但是这两个名字确确实实还是有关系的。

其实JavaScript诞生于浏览器大战的时代，这个浏览器大战在这里就不多讲了。如果同志们有兴趣，可以去看我的前端讲解。在1995年，布兰登·艾奇发明了JavaScript语言，但是他也不是兴趣使然，而是他工作的公司Netscape（网景）要求的。

其实啊，Netscape公司当初和发明java的sun公司私下关系密切，最开始Netscape打算用java作为网页端的语言的，但是因为这样会带来很多麻烦，所以不得不放弃了。但是Netscape贼心不死，便要求员工布兰登·艾奇发明一个专门服务于网页的语言，要求就是必须和java足够像。

但是这程序员写起代码来啊，思维就不收他自己控制了。布兰登·艾奇不愧是天才程序员，仅仅用了10天就把JavaScript设计完成了！结果，，，，，因为写的太快，很多地方设计的很不合理，而且最最重要的是，，这个语言和java根本就不像！！！！！！

布兰登·艾奇这下慌了，老板给的任务不能不完成啊！怎么办？没办法了，虽然语言不像，但是至少名字像吧。所以就给这个语言起名为了JavaScript。





如今啊，JavaScript已经不仅仅服务于网页端了，包括我们的RPGMakerMV的这个引擎都是JavaScript写的。可以说是非常非常全能的语言了。













## RPGMV和JS的关系？

RPGMV实际上是用一个叫做nw.js的框架所制作的，这个东西是一个非常非常强大的框架，微信也是用这个开发的。可以简单理解为，游戏引擎是专门来开发游戏的，而这种应用框架是专门用来写应用软件的。RPGMakerMV这个引擎软件就是用nw.js这个框架写的。而这个框架特点就是全面支持JavaScript。所以MV当然也全面支持JavaScript啦。

当然这个理由有点牵强，但是使用nw.js框架，使得RPGMV确实对JS有着完美的支持，我们何乐而不为呢？

RPGMV底层使用的是nw.js框架，同时还在使用PIXI动画框架，这个玩意也是用JavaScript来编写和操作的，我们之后也会学习到这个框架。

另外补充一下，现在nw.js也基本上被淘汰了，现在最主流的开发环境叫做electron ，连VSCode都是用这个开发的。















## 认识我们的新同学——迷子同学

在我们开始学习之前，我还想给给位介绍一个新同学。因为本学期的课程毕竟还是太无聊啦，大家一个人学习很可能就坚持不下去啦。所以我专门请来了一个小姐姐和大家共同学习。在今后的脚本课程中，大家要好好相处哦~。





<div>
	<img src="./img/迷子同学/自我介绍.jpg" alt="加载失败！" height="800px" style=" float:left">
    <div style="">个人简历</div>
	<ul>
       <li>姓名：迷子</li>
       <li>年龄：17</li>
       <li>身高：保密</li>
       <li>性格：高女子力、活泼</li>
       <li>生日：10月24日</li>
       <li>喜欢干的事情：学习JavaScript</li>
       <li>喜欢的食物：草莓味的小蛋糕~</li>
       <li>喜欢的类型：擅长JavaScript的男生</li>
     </ul>
</div>







































## 学习课程简介

教程分为两个部分：第一个是比较有趣的主线课，第二个则是严肃严谨的支线课。主线课中讲授的内容比较简单，面向完全没有编程经验，或者是想系统学习的同学，而且有迷子同学作为陪伴。而支线课则是为主线课做的补充和进阶，而且主要面向已经有开发经验的同学。

之所以采用这种方法，我也是经过了一番思考。如果只是为了刻意营造简单的感觉，而对一些复杂语法避重就轻，只会让更多人懵逼。而如果只是为了严谨和复杂，那么真的还不如去看官方文档。所以采用了这种双线教学。我在这里想说明，支线内容不代表可以真的不看！而是说如果现在看不懂，可以暂时放着，等主线的经验足够高了，再来看也不迟。

支线内容将会在前面标注星号*。

在本课程中将会讲解js语法基础，基础API调用、不带插件指令的插件编写方法等内容。



不过呢，虽然一篇的文章不长，不过我不建议一口气看完哦！建议看的时候每次一个课时即可。

一个课时就是一个主线搭配对应支线这样来看。并且看完之后请务必亲自动手试试看！




## 枯燥的环境安装

虽然很枯燥，但是这个请务必仔细阅读。

1. 下载VS Code

   首先，我们需要下载一个叫做**VS Code**的编辑器，大概这个样子：![img](G:\创作\笔记\游戏开发\RPGMakerMV开发\img\logo.jpg)。这个玩意可以说是非常非常强大了，就算各位以后不继续开发RPGMV了，也强烈建议不要卸载它，以后迟早用得到的。

   下载地址在这里：https://code.visualstudio.com/。点进去后，直接点”Download for Windows“即可。安装的话，就是一路点点点，没有什么难度。各位自行安装即可。

2. 安装插件（请保证有网！）

   在软件的左上角找到一个俄罗斯方块模样的图标，点进去之后，像我这样搜索”chinese“，下载中文插件。

   ![image-20211027225124841](img\image-20211027225124841.png)

   然后再搜索live server，并安装。

   ![image-20211027225309999](img\image-20211027225309999.png)

   

   

3. 安装node环境。（可选）

   因为js脚本可以在node环境和web环境执行，我们为了方便起见直接使用浏览器学习，但是也可以自行下载node环境。
   
   
   
   
   
   
   
   好，我们这节预备课就到这里。
   
   下节课将会开始讲解js脚本的基础。
   
   

# 初识JavaScript脚本

## 你好，世界！

在学习JS之前，我想先考一考各位。事件指令我想各位都已经十分熟练了吧？那么在事件指令的第三页，右下角的两条指令是什么？忘记了？







































![image-20211027231428381](img\image-20211027231428381.png)

   

没错就是脚本和插件指令！！！我们今天学习的脚本就需要写在里面。当然了实际上MV中可以写js脚本的地方有非常非常多，我们今天仅仅只学习这一种而已。

首先我们先来体验一下吧。

点击脚本事件，在里面写上这句代码。

```js
alert("hello world!");
```

然后运行游戏。

就可以看到"hello world"的字样了。如果你成功运行出来了这句话，那么欢迎你进入JS的世界！我们即将开展这场JS的大冒险。





## <del>JS的数据类型</del>，实际上是变量的介绍

我们首先来学习一下js的**基本类型**，然后再学习一下**三种流程控制**的语句。。。。。

你以为我要这么讲？<strong style="font-size: 30px;">不！</strong >  	我们还是直接通过游戏项目来学习吧！题材呢就选《勇者斗恶龙》吧。

不过我要说明一下，之后的内容很多其实都是可以用事件完成的，只不过本课是为了讲解JS脚本，所以尽可能用了脚本。实际上开发中，要尽可能使用事件指令。



那么在开发前，首先我们得要有一个剧本的开头：

> 很久很久以前，遥远的大蛇皮大陆上居住着善良的蛇人，还有可怕的恶龙。
>
> 每年，国王都会派遣大量的勇者去讨伐恶龙。

好，那么我们就先从这两句开始吧，首先当然是创建开场动画了。在事件指令中点击创建脚本的事件，然后把这个代码粘过去并执行。

```js
alert("很久很久以前，遥远的大蛇皮大陆上居住着善良的蛇人，还有可怕的恶龙。每年，国王都会派遣大量的勇者去讨伐恶龙。");
```

怎么样，是否成功出现了这句话呢？

好，那么我们继续，，，

![](G:\创作\笔记\计算机方向\游戏开发\RPGMakerMV开发\教程\img\迷子同学\等等.jpg)

<img src="img/迷子同学/等等.jpg" alt="image-20211027231428381" style="zoom:67%;" />

<div><img src="img\迷子同学\迷子吐槽大蛇皮.jpg" alt="image-20211027231428381" style="zoom: 20%; float:left;" />
<div>欸？有吗？？</div>
<div>唔~~~~~~好吧，那么我们就换一个名字吧，就叫做“肥鲇鱼”吧！</div>
<div>同样的，把刚才那句话里面的“大蛇皮”改成“肥鲇鱼”吧！</div>
<div style="color:pink;">你真的有在反省嘛，，</div>
<div>那再改成无名氏吧！</div>
<div style="color:pink;">。。。。。，，</div>
<div>哈哈哈哈，言归正传。我们在实际开发的时候，确确实实会遇到这种问题，主角的名字也好，各种数值的设定也好，可能会经常变更。我们这个只有一句代码，更改起来还算简单，但是如果游戏已经开发了很久，现在要把游戏里面主角所有的名字进行变更，实在是无法完成的任务。</div>
    <div>所以，我们就可以用一个<strong>变量</strong>来代替主角的名字。</div>
</div>
































```js
var landName = "大蛇皮";
alert(`很久很久以前，遥远的${landName}大陆上居住着善良的蛇人，还有可怕的恶龙。每年，国王都会派遣大量的勇者去讨伐恶龙。`);
```

再去粘贴过去试试看吧！效果是一样的。但是我们之后再次进行更改可就方便多了。

这就是变量的作用，变量就是一个可以储存数据的东西，里面不仅仅可以存放这种文字，也可以存放数字等其他类型，之后会经常看到的。



对于这个代码还有一个要注意的地方。不知道你发现了吗？两句话的颜色，在本教程里面是不一样的！实际上第一个代码用的是==双引号==来把句子包裹起来的，而第二个用的是==反引号==，反引号就是在<kbd>TAB</kbd>键上面那个东西和波浪号在一起。

用反引号包裹起来的语句就叫做==模板字符串==。**只有模板字符串才能够使用变量**。调用变量的语法就是`${变量名}`。



如果不适用模板字符串，那么也可以通过==字符串拼接==的方法实现同样的效果。

在两个字符串之间使用+号连接变量。比如：

```js
var landName="小蛇皮";
alert("很久很久以前，遥远的"+landName+"大陆上居住着善良的蛇人，还有可怕的恶龙。每年，国王都会派遣大量的勇者去讨伐恶龙。");
```



## 第一次调用API

好了，我们继续开始MV的学习吧！

下面我们再增加一段剧情：

```js
var characterName = "大蛇人";
alert(`我们的勇者${characterName}，他的传奇故事就发生在这里。`);
```

再去粘过去试试看吧！



<img src="img\迷子同学\迷子反思alert.jpg" alt="image-20211027231428381" style="zoom: 20%;" />



哈哈哈，迷子同学果然也发现了这个问题吗？

实际上`alert`这种弹窗虽然可以给玩家展示信息，但是表现的效果真的很差，尤其是在写游戏剧情的时候，要是通篇都是这种弹窗，实在是太low啦。

实际上这种弹窗一般都是警示或者是提示语出现的。比如说注册账号成功，会有一个弹窗告知注册成功；而注册失败同样也有弹窗。但是如果是描述剧情的话，用弹窗真的是不合时宜！

那么应该用什么呢？还记得在事件编辑器中是如何打印信息的吗？

是的，就是使用`显示文字`的事件指令，这应该是我们接触到的第一条事件指令了。

<pre><font color="black">◆</font><font color="indigo">文本：</font><font color="gray">无, 窗口, 底部</font>
<font color="black">：</font><font color="white">文本</font><font color="indigo">：</font><font color="navy">没错，我就是<code>显示文字</code>的事件指令！</font></pre>



实际上我们也能用代码来实现这个效果。

**其实所有的事件指令都是可以用代码来实现的。**MV官方把这些事件都封装成了各种代码，这些可以被我们使用的代码就叫API。



那么这些代码在哪里写呢？其中最常见的一个写法，就是通过`脚本`的事件指令，把代码直接写在里面。

我们现在就来试一试吧，把刚才的剧情改写成使用API的版本。





```js
var landName = "大蛇皮";
var characterName = "大蛇人";
$gameMessage.add(`很久很久以前，遥远的${landName}大陆上居住着善良的蛇人，还有可怕的恶龙。每年，国王都会派遣大量的勇者去讨伐恶龙。`);
$gameMessage.add(`我们的勇者${characterName}，他的传奇故事就发生在这里。`);
```



效果如何呢？是否比`alert`强太多了呢？

但是我想，这时候你可能也发现了，，，，

![image-20211031213657213](img\image-20211031213657213.png)

这是怎末回事啊！为什么文字被遮挡住了一半？

实际上这个方法在调用的时候和使用事件是一样的。那就是不能超过那条虚线，在编辑器中我们可以看到虚线，在写代码的时候就只能根据自己的感觉来判断虚线位置了。

![image-20211031213836414](img\image-20211031213836414.png)

那你还记得在编辑器里面是怎么解决这个问题的吗？

对了就是使用回车键换行啊！

但是这时候又有一个问题，在编辑器里面，我们可以通过换行来解决一行显示不下的问题。在代码里面该如何换行呢？

这时候，我们可以通过一种叫做==转义字符==的东西来换行。换行的转义字符就是`\n`。我们把它写在代码里面看看效果吧。

```js
var landName="大蛇皮";
var characterName = "大蛇人";
$gameMessage.add(`很久很久以前，遥远的${landName}大陆上居住着善良的蛇人，\n还有可怕的恶龙。\n每年，国王都会派遣大量的勇者去讨伐恶龙。`);
$gameMessage.add(`我们的勇者${characterName}，他的传奇故事就发生在这里。`);
```

是不是已经成功换行了呢？像这种以反斜杠开头的字符就是转义字符。

这个东西我想你虽然可能用的不熟练，但是你绝对是见过哒。想起来了吗？MV中，在`显示文字`的事件指令中，如果鼠标长时间停留在文本里面，那么就会弹出一个窗口，里面就记录着MV中使用的各种转义字符。

<img src="img\image-20211031214634441.png" alt="image-20211031214634441" style="zoom: 80%;" />

不同的转义字符有着不同的含义，但是最常用的还是换行符：`\n`，在本次的学习中请务必记住换行符的用法。



不过要特别注意！如果在脚本代码中使用MV的转义字符，需要加两个反斜杠。例如：

```js
$gameMessage.add(`本游戏的货币单位：\\G`);
```





因为在代码中，**反斜杠会默认修饰后面那个字符**。比如说`\n`。如果真的想要打印\n该怎么办呢？，答案就是在前面再写一个反斜杠！这样子第一个反斜杠就会修饰第二个反斜杠，就不会影响到n了。而`\\`的意思就是打印一个`\`，所以就能打印出来`\n`了。

MV的这些转义字符并不是JS自带的！所以说，如果是在事件中写 `\G`， 实际上在MV内部，系统会把`\G`转化为货币单位；但是在写代码的时候，首先是编译器来处理代码，它会把`\G`解析为G，（反斜杠+字母，大部分都会直接解析为字母本身），然后再把结果交给MV处理，MV把代码拿到手里的时候，就只剩下`G`了。所以我们要写`\\G`，编译器会把这个解析为`\G`，然后MV再来解析成为货币单位。





## 内容小结

- JS中，如果想定义一个变量需要使用var。
- 字符串就是两个单引号或者双引号或者反引号围起来的文本。
- 用两个反引号括起来的句子叫做模板字符串，里面可以通过`${变量名}`的格式来调用变量。
- MV中有很多API，其实就是可以让我们用代码的方式来实现事件指令。
- 在`脚本`事件指令中，我们可以书写JS代码。
- `$gameMessage.add()`方法可以实现`显示文字`的事件指令，同时要注意没有换行的提示。
- 在一个字符串中，如果想要换行，可以使用`\n`的符号。这个叫做转义字符，MV中也提供了很多转义字符，要记得善于使用这些符号。



# JavaScript急速入门*

相信已经有很多同学之前已经了解过其他语言了，这些同学可能会有以下烦恼：

- 明明已经会其他语言了，，，再从头学一门语言的话，基础语法过于简单，但是不学的话，会导致基础不扎实。
- 之前大概了解过js的基础知识！不要再废话啦，我只想快速学习到进阶部分！

也就是说：

<div style="font-size:30px; color:red;">我已经有编程基础啦！！！！拜托来点干货吧！</div>

以上种种烦恼我大概是能够想象到的，不过不要着急，我们现在就来帮助这些同学快速入门js。而对于已经有js基础的同学，我建议你也还是再看看，权当查漏补缺啦。而对之前完全没有学过程序设计的同学，也不要害怕，我还是建议你看一遍比较好，毕竟如果真的想系统学习js，还是需要看看这些“教科书”比较好哒！



## 基础知识速览

- 注释

  js中的注释和其他语言一样，包括两种

  ```js
  //单行注释
  /*多
  行注释*/
  /*
  *文档注释
  **/
  ```

  

- 控制台输出

  ```js
  console.log("hello world")
  ```

  

- for循环

  ```js
  //打印0到9
  for(let i=0;i<10;i++){
      console.log(i)
  }
  ```

  

- if语句

  ```js
  if(flag){
    //语句
  }else if(flag2){
   //语句2
  }else{
   //语句3
  }
  ```

  

- 函数定义与使用

  注意，不需要在形参前面写声明符号

  ```js
  function add(a,b){
    return a+b;
  }
  add(1+2);
  ```


JS的函数，返回值默认是undefined。而且声明时不需要写形参类型和返回值类型。



- 类与对象（ES5）

  实际上这个说法并不对，js中没有类，只有对象。但是为了大家尽快速成，可以简单理解为类。

  ```js
  function Girl(name,age){
    this.name = name
    this.age = age
  }
  
  var maigo = new Girl("迷子",17); 
  
  console.log(maigo.name,maigo.age);
  ```

  而且我没有写类的继承，这是因为类继承算是JS一个非常重要的语法知识，需要单独来讲。

  

  

- 分号问题

  大家可能已经注意到了，我有时候写分号，有时候不写。那么到底是写还是不写？？？？

  实际上。无所谓。对，js对分号不作要求，所以写不写看自己。但是在MV中，还是**建议都写上**比较好，因为官方都写了。。。
  
- 

## 什么是动态类型语言？

js是一门**动态类型**的脚本语言。所谓的动态类型，就是说变量类型在声明的时候不需要指定数据类型。比如同样定义主角的名字，我们来看看以下几个语言的区别吧：

- java

  ```java
  public class HelloWorld {
      public static void main(String []args) {
  		String characterName = "大蛇皮";
      	System.out.println(characterName);
      }
  }
  ```

  

- C/C++（神）

  ```c++
  #include <iostream>
  using namespace std;
  
  int main()
  {
     const char* characterName = "大蛇皮";
     cout << characterName;
     return 0;
  }
  ```

  

- python3

  ```python
  characterName = "大蛇皮";
  print(characterName);
  ```

  

- matlab

  ```matlab
  characterName = "大蛇皮"
  ```

  

- lua

  ```lua
  characterName = "大蛇皮";
  print(characterName);
  ```

  

- c#

  ```c#
  using System;
  namespace HelloWorldApplication
  {
     class HelloWorld
     {
        static void Main(string[] args)
        {
        	 String characterName = "大蛇皮";
           Console.WriteLine(characterName);
        }
     }
  }
  ```

  

- typescript

  ```typescript
  var characterName : string = "大蛇皮"
  console.log(characterName)
  ```

- JavaScript

  ```javascript
  var characterName = "大蛇皮"
  console.log(characterName)
  ```

  

诸位能够猜到哪些是动态语言吗？对了，如果变量的声明前面没有string之类的类型标志，那么它就是动态语言。可以看到，不同的动态语言对于变量的声明也是不尽相同，像JavaScript还是需要用var来声明的，而python3、lua，他们甚至不需要给变量前写声明标志。

不过，不论怎么样写，他们的语言核心就是不需要写变量的类型，编译器会动态决定其类型，这也导致了其性能的下降。比如说C++分配一个int类型的变量，那么他的内存就是4byte。而js则很活跃，假设设置一个`a=1`，之后a的值还可以随时改变。可能下一秒a又变成了`a=="hello"`，这在其他强类型语言里面是不允许的，但是js允许，所以编译器就不好给a直接分配内存了，它只能动态来推测a的类型，导致运行缓慢。







## js的数据类型

动态类型语言，不代表它没有数据类型。只是说不用在声明时标明类型罢了。

实际上js有8种数据类型：

| 类型             | 值            | 构造函数  |
| ---------------- | ------------- | --------- |
| null             | null          | 无        |
| undefined        | undefined     | 无        |
| string           | "hello world" | Sting()   |
| number           | 123           | Number()  |
| bigint    [ES10] | 123n          | BigInt()  |
| boolean          | true false    | Boolean() |
| symbol   [ES6]   |               | 无        |
| object           | {}            | Object()  |

正如各位所知的，都是一些很常见的数据类型。诸位可能不熟悉的类型就是bigint和symbol了，实际上`bigint`和C#中的`decimal`有点像。都是来对一些超级大的数进行运算时使用的，算是官方提供的一种大数运算的数据类型。



而symbol则是专门给某个对象设置唯一属性的，关于它我们之后会详细讲。



另外还要强调的一点是：null的数据类型在设计的时候有bug！(特性)

```js
typeof null //'object'
null instanceof Object //false
```





如果是之前学C++的同学，可能对typeof很熟悉，而学java的同学会对instanceof很熟悉。

其中typeof是意思是，看看这个null的数据类型是什么。结果答案是'object'，那么之后我们又问编译器，那null是不是object的实例对象呢？答案却是false。

要知道，如果一个数据的类型是object，那么它必定是由Object构造的，但是null却是特例。这是当时设计上的一个bug，不够因为没有及时改正，现在已经来不及改了，成为了js的“特性”之一。



好，我们这次的内容就讲到这里，虽说大家想要急速入门，但是基础还是要打好的，诸位在进行下面的进阶之前，不妨看看主线剧情的内容吧！毕竟js的语法只是理论，具体怎样去用才是最重要的，而主线则更强调如何使用这些脚本。



第一课到此为止啦！大家请务必把课程里面的内容亲自试试！

















# 再探API的世界

## 更改角色的姓名的API

好了，我们继续来创造我们的故事剧本吧。上次我们成功更改了角色的姓名，这次我们将要。。。

> <div style="color:pink;float:left;">等一下啦！</div>
>
> <div style="color:black; float:right;">欸？又怎么了？</div>
>
> <div style="color:pink;float:left;">为什么我的MV里面角色的姓名没有更改成功啊！</div>
>
> <div style="color:black; float:right;">欸？可是我们上节课不是已经验证过了吗？姓名确实是大蛇人啊？</div>
>
> <div style="color:pink;float:left;">我是说游戏里面啦，就算对话里面，点击右键，在菜单栏里面，主角还是叫霍尔德啦！</div>
>
> <div style="color:black; float:right;">原来如此，你是说，就算我们说主角叫大蛇人，但是实际上游戏中主角的姓名还是霍尔德。</div>
>
> <div style="color:black; float:right;">实际上这个也很容易理解，就像<code>$gameMessage.add</code>一样，MV中所有的游戏数据都有自己的API。</div>
>
> <div style="color:black; float:right;">我们自己随便写的变量当然不可能影响游戏里面的数据啦，下面我们就来学习一下如何来更改角色的姓名吧！</div>



还记得在事件中，我们使用哪个指令来更改角色姓名吗？

对了！就是`更改姓名`的事件指令。

<pre><font color="black">◆</font><font color="darkorange">更改名字：霍尔德, 更改姓名</font></pre>

这个API用起来略有点复杂，具体使用方法可以看下面：

```js
 var actor = $gameActors.actor(1) //获取第一个角色的信息（也就是主角）
 actor.setName("新名字");//把角色的名字设置为“新名字”
```





我们现在把之前的代码重新改写一下吧！

```js
var landName="大蛇皮";
var actor = $gameActors.actor(1) //获取第一个角色的信息（也就是主角）
actor.setName("大蛇人");//把角色的名字设置为“大蛇人”
$gameMessage.add(`很久很久以前，遥远的${landName}大陆上居住着善良的蛇人，\n还有可怕的恶龙。\n每年，国王都会派遣大量的勇者去讨伐恶龙。`);
$gameMessage.add(`我们的勇者\\N[1]，他的传奇故事就发生在这里。`);
```



怎么样，是不是成功更改了呢？要注意到，代码里面有一个转义字符的使用，如果忘记了的话，请务必复习上一课的内容。



## VSCode终于派上了用场，初学插件编写

我们接着来完善剧情。

现在，再次把下面的剧情添加到上次的脚本后面吧！



```js
var villageName = "绵水镇"
$gameMessage.add(`每年的10月，是${villageName}猎奇鹿的日子。`);
$gameMessage.add(`而今年，收成似乎格外的好。这次出行，就足足猎到了两只。`);
$gameMessage.add(`按照以往的行情，这两只鹿，就能换到2000\\G。`);
$gameMessage.add(`当然了，除了今年老天爷的恩赐之外，\\N[1]也是村里面一等一的好手。`);
$gameMessage.add(`之前每年的猎鹿大赛上，他的成绩虽然不是年年第一，但也是名列前茅。`);

$gameMessage.add(`现在是正午12时。`);
$gameMessage.add(`他之所以敢这样断言，大概来源于他这么多年以来的生物钟吧。`);
$gameMessage.add(`上午7时，大公鸡晓时会准时叫他起床。`);
$gameMessage.add(`打开房门，一定能看到妹妹在饭桌前昏昏欲睡的的样子。`);
$gameMessage.add(`之后便是珍贵的早餐时间了。`)
$gameMessage.add(`新鲜的牛奶加上一小块粗麦馒头，有时还会有一小盘凉拌野菜。`)
$gameMessage.add(`简朴但是美味的食物，再加上母亲那唠叨但是温馨的家常话，这就是\\N[1]一家平静的早餐。`)
$gameMessage.add(`上午8点是工作的时间，自己猎鹿，妹妹和母亲学习纺织。父亲则去打理自家小小的麦田。`)
$gameMessage.add(`打猎会持续两天到三天，而妹妹和母亲每天正午都会在村口眺望自己，无论哪一天回来。`)
$gameMessage.add(`都能看到迎接自己的笑脸。`)
$gameMessage.add(`这样平静的日子已经不知道持续了多久，但是\\N[1]却没有半点厌倦,`);
$gameMessage.add(`他唯一的愿望就是这平静而幸福的日子能够再长一点。`);

//下一段剧情的转场
$gameMessage.add(`穿过一段悠长的迷木林，阳光开始渐渐的从叶间挤进\\N[1]身边。`);
$gameMessage.add(`“快到了”，\\N[1]压抑不住激动的心情。`);
$gameMessage.add(`“父亲看到这样的收成会怎样想？这笔钱足够给全家都换一身新衣了吧？”`);
$gameMessage.add(`“他不由加快了脚步。“`);

//转折
$gameMessage.add(`远远的，村中那棵古树已经依稀可见，但是，他的心脏却猛然抖了一下。`);
$gameMessage.add(`母亲和妹妹怎么不在？？`);
$gameMessage.add(`是今天我回来的太早了吗？应该是吧，毕竟今天回来的时候跑的比较快。`);
$gameMessage.add(`虽然他的生物钟很确信现在就是正午，但是他还是说服自己不要去想。`);
$gameMessage.add(`刚才如飞的健步，现在却抖了起来，一股不祥的预感莫名袭来。`);


//发展
$gameMessage.add(`过于安静了，虽然镇子并不是什么富裕的村镇，但是正午还是热闹的。`);
$gameMessage.add(`而此刻，除了几家烟囱中缕缕的薄烟之外，镇子里竟然一个人都看不到。`);
$gameMessage.add(`整个村子死一般的宁静，唯一能听到的声音就只有他不止的心跳了。`);
$gameMessage.add(`到底是怎么了？`);


$gameMessage.add(`\\N[1]勉强拖着步子来到家门前。把猎物扔到门口，缓缓敲了敲门。`);
$gameMessage.add(`”进来吧。“一个尖细而慵懒的声音传了出来。`);
$gameMessage.add(`他认识这个声音，每年秋收之后，税收官就回来到镇中收税。`);
$gameMessage.add(`虽然\\N[1]也没有见过税收官几次，但是不知道为何，他对这尖锐的声音却异常的反感。`);

$gameMessage.add(`推开门，一股葡萄酒的香味扑鼻而来。`);
$gameMessage.add(`他不由看向桌子。桌子上摆满了家里平日里舍不得吃的腊肉和糖果。`);
$gameMessage.add(`还有那瓶家里已经传了50年的葡萄酒。`);
$gameMessage.add(`之前父亲还开过玩笑，要把这瓶酒传上100年，然后去城里卖掉，到时候家里可以再买上两瓶`);
$gameMessage.add(`然后过上几百年，说不定就能有钱搬到城里面，甚至买上个小官做做。`);
$gameMessage.add(`但是现在一切都随着这浓郁的酒香一起消散了。`);

$gameMessage.add(`父亲在桌子旁低着头站着，母亲则背着门在偷偷啜泣。`);
$gameMessage.add(`而在桌子旁坐着的当然就是税收官大人了。`);
$gameMessage.add(`你就是\\N[1]吧。`);
$gameMessage.add(`税收官把杯中的酒一饮而尽，缓缓开口。`);
$gameMessage.add(`他心中突然升起一阵无名火，但是仍然恭敬的低头回答。`);
$gameMessage.add(`是的，税收官大人。`);
$gameMessage.add(`虽然他没有抬头，但是还是能感受到税收官那肥硕的身体剧烈的颤抖了一下。`);
$gameMessage.add(`紧接着就是桌子上传来的巨响。`);
$gameMessage.add(`”蠢货，你难道不知道我现在被圣上临时授予了”集英使“的职位吗？“`);
$gameMessage.add(`\\N[1]浑身都渗出了冷汗。`);
$gameMessage.add(`妹妹的哭声也从卧室里面传出来。原来她躲在了卧室啊。`);
$gameMessage.add(`”也罢，念在你无知的份上，这次就不计较了。“`);
$gameMessage.add(`”多谢大人宽容大量，恭贺您高升。“`);


$gameMessage.add(`”嗯，那么说正事吧，“`);
$gameMessage.add(`”今年圣上要再次重启荣耀的猎龙活动，现在要招募勇者，每个村庄只有一个名额。“`);
$gameMessage.add(`而你们的村长把这个光荣的任务让给了你。`);
$gameMessage.add(`猎龙？？这个活动10年前不就被取消了吗？怎么又要开始了`);
$gameMessage.add(`但是\\N[1]没有胆量把话问出来。`);
$gameMessage.add(`”那么，一个月内向你们的直辖市报道。明天早上就出发吧。“`);
$gameMessage.add(`说完，他把葡萄酒一饮而尽，”集英使“很快带着他的仆从们离开了村庄。`);
$gameMessage.add(`对了，路上你可得小心点，如果你路上出了点什么事，没有及时报道`);
$gameMessage.add(`明年你们村庄的税收就多交上2倍税收吧。`);


$gameMessage.add(`远眺着马车留下的灰烟，村庄里悄悄地传出几声开门的声音。`);
$gameMessage.add(`一家人围坐在桌前，门外是明媚的阳光，桌上是丰盛的午餐。但是气氛却沉重的喘不上气。`);
$gameMessage.add(`”我，我这两天猎到了两头奇鹿。“`);
$gameMessage.add(`父亲望了过来，挤出一丝微笑。”不愧是我儿子，好样的。好样的。“`);
$gameMessage.add(`”好了，开饭吧，这可是大丰收啊。父亲给葡萄酒瓶子里灌上稠酒。“`);
$gameMessage.add(`来，咱爷俩好久没有喝过了，今天来久违的庆祝一番吧！`);
$gameMessage.add(`\\N[1]已经想不起来那天是怎末度过的了。虽然大家对当勇者这件事缄默不提`);
$gameMessage.add(`但是半夜还是能看到母亲在缝制的身影。`);

$gameMessage.add(`第二天还是到来了。`);
$gameMessage.add(`父亲不知道从哪里搞来一把长刀，而母亲则拿来了一条厚重的围巾。`);
$gameMessage.add(`”快到深秋了，天冷，你平时多注意保。“`);
$gameMessage.add(`母亲话还没有就哭着紧紧的抱住了\\N[1]。`);
$gameMessage.add(`然后是妹妹，就连平日里性格厚重的父亲也落泪了。`);
$gameMessage.add(`但是分别的时候终究会来临。`);
$gameMessage.add(`就这样，我们的主角带着母亲连夜赶出来的围巾，带着父亲的长刀还有一大堆食物，踏上了成为勇者的道路。`);
```





好了，现在把这些粘过去吧。

欸？是不是报错了？这是怎末回事？我们不妨把这个事件拉到最下面看看，原来啊，这个脚本的命令过长了，编辑器接受不了这么多，所以有一部分代码被截掉了。一种解决方法就是，多开几个事件指令，比如下面这样，这样就可以防止代码被截掉：

![image-20211106165707203](img\image-20211106165707203.png)

另一种方法就是，我们能不能不在这里面写代码啊？？？？？？

这句话可能有点抽象，我再解释一下。

首先各位不觉得在MV这个白框框里面写代码实在是太痛苦了嘛。。。。目前的代码都是我写好的，你们只需要复制粘贴即可，那以后自己再要写代码可就没有这么轻松了。

还记得alert吗？alert是专门负责发送警示和提示消息的。实际上和alert一样，这个`脚本`的事件指令是专门处理简单短小的代码的。如果非要让它处理这种近百行的代码，真的是为难它了。

那么有没有什么地方可以让我们尽情写代码呢？对了，就是插件，虽然很多同学没有写过，但是总该见过吧。

MV中有三处可以编写代码：

- 脚本指令中
- 插件和插件指令中
- 控制台中

我们之前已经学过了第一种，现在就来了解一下第二种吧！

1. 首先打开VSCode，打开游戏所在的文件夹。

2. 在根目录可以找到js文件夹，然后里面可以找到plugins文件夹。

3. 在plugins文件夹中，我们新建一个`Begin_story.js`文件。

4. 然后把下面的代码粘过去

   ```js
   function storyBegin(){
       var villageName = "绵水镇"
       $gameMessage.add(`每年的10月，是${villageName}猎奇鹿的日子。`);
       $gameMessage.add(`而今年，收成似乎格外的好。这次出行，就足足猎到了两只。`);
       $gameMessage.add(`按照以往的行情，这两只鹿，就能换到2000\\G。`);
       $gameMessage.add(`当然了，除了今年老天爷的恩赐之外，\\N[1]也是村里面一等一的好手。`);
       $gameMessage.add(`之前每年的猎鹿大赛上，他的成绩虽然不是年年第一，但也是名列前茅。`);
       $gameMessage.add(`现在是正午12时。`);
       $gameMessage.add(`他之所以敢这样断言，大概来源于他这么多年以来的生物钟吧。`);
       $gameMessage.add(`上午7时，大公鸡晓时会准时叫他起床。`);
       $gameMessage.add(`打开房门，一定能看到妹妹在饭桌前昏昏欲睡的的样子。`);
       $gameMessage.add(`之后便是珍贵的早餐时间了。`)
       $gameMessage.add(`新鲜的牛奶加上一小块粗麦馒头，有时还会有一小盘凉拌野菜。`)
       $gameMessage.add(`简朴但是美味的食物，再加上母亲那唠叨但是温馨的家常话，这就是\\N[1]一家平静的早餐。`)
       $gameMessage.add(`上午8点是工作的时间，自己猎鹿，妹妹和母亲学习纺织。父亲则去打理自家小小的麦田。`)
       $gameMessage.add(`打猎会持续两天到三天，而妹妹和母亲每天正午都会在村口眺望自己，无论哪一天回来。`)
       $gameMessage.add(`都能看到迎接自己的笑脸。`)
       $gameMessage.add(`这样平静的日子已经不知道持续了多久，但是\\N[1]却没有半点厌倦,`);
       $gameMessage.add(`他唯一的愿望就是这平静而幸福的日子能够再长一点。`);
       
       //下一段剧情的转场
       $gameMessage.add(`穿过一段悠长的迷木林，阳光开始渐渐的从叶间挤进\\N[1]身边。`);
       $gameMessage.add(`“快到了”，\\N[1]压抑不住激动的心情。`);
       $gameMessage.add(`“父亲看到这样的收成会怎样想？这笔钱足够给全家都换一身新衣了吧？”`);
       $gameMessage.add(`“他不由加快了脚步。“`);
       
       //转折
       $gameMessage.add(`远远的，村中那棵古树已经依稀可见，但是，他的心脏却猛然抖了一下。`);
       $gameMessage.add(`母亲和妹妹怎么不在？？`);
       $gameMessage.add(`是今天我回来的太早了吗？应该是吧，毕竟今天回来的时候跑的比较快。`);
       $gameMessage.add(`虽然他的生物钟很确信现在就是正午，但是他还是说服自己不要去想。`);
       $gameMessage.add(`刚才如飞的健步，现在却抖了起来，一股不祥的预感莫名袭来。`);
       
       
       //发展
       $gameMessage.add(`过于安静了，虽然镇子并不是什么富裕的村镇，但是正午还是热闹的。`);
       $gameMessage.add(`而此刻，除了几家烟囱中缕缕的薄烟之外，镇子里竟然一个人都看不到。`);
       $gameMessage.add(`整个村子死一般的宁静，唯一能听到的声音就只有他不止的心跳了。`);
       $gameMessage.add(`到底是怎么了？`);
       $gameMessage.add(`\\N[1]勉强拖着步子来到家门前。把猎物扔到门口，缓缓敲了敲门。`);
       $gameMessage.add(`”进来吧。“一个尖细而慵懒的声音传了出来。`);
       $gameMessage.add(`他认识这个声音，每年秋收之后，税收官就回来到镇中收税。`);
       $gameMessage.add(`虽然\\N[1]也没有见过税收官几次，但是不知道为何，他对这尖锐的声音却异常的反感。`);
       $gameMessage.add(`推开门，一股葡萄酒的香味扑鼻而来。`);
       $gameMessage.add(`他不由看向桌子。桌子上摆满了家里平日里舍不得吃的腊肉和糖果。`);
       $gameMessage.add(`还有那瓶家里已经传了50年的葡萄酒。`);
       $gameMessage.add(`之前父亲还开过玩笑，要把这瓶酒传上100年，然后去城里卖掉，到时候家里可以再买上两瓶`);
       $gameMessage.add(`然后过上几百年，说不定就能有钱搬到城里面，甚至买上个小官做做。`);
       $gameMessage.add(`但是现在一切都随着这浓郁的酒香一起消散了。`);
       
       $gameMessage.add(`父亲在桌子旁低着头站着，母亲则背着门在偷偷啜泣。`);
       $gameMessage.add(`而在桌子旁坐着的当然就是税收官大人了。`);
       $gameMessage.add(`你就是\\N[1]吧。`);
       $gameMessage.add(`税收官把杯中的酒一饮而尽，缓缓开口。`);
       $gameMessage.add(`他心中突然升起一阵无名火，但是仍然恭敬的低头回答。`);
       $gameMessage.add(`是的，税收官大人。`);
       $gameMessage.add(`虽然他没有抬头，但是还是能感受到税收官那肥硕的身体剧烈的颤抖了一下。`);
       $gameMessage.add(`紧接着就是桌子上传来的巨响。`);
       $gameMessage.add(`”蠢货，你难道不知道我现在被圣上临时授予了”集英使“的职位吗？“`);
       $gameMessage.add(`\\N[1]浑身都渗出了冷汗。`);
       $gameMessage.add(`妹妹的哭声也从卧室里面传出来。原来她躲在了卧室啊。`);
       $gameMessage.add(`”也罢，念在你无知的份上，这次就不计较了。“`);
       $gameMessage.add(`”多谢大人宽容大量，恭贺您高升。“`);
       $gameMessage.add(`”嗯，那么说正事吧，“`);
       $gameMessage.add(`”今年圣上要再次重启荣耀的猎龙活动，现在要招募勇者，每个村庄只有一个名额。“`);
       $gameMessage.add(`而你们的村长把这个光荣的任务让给了你。`);
       $gameMessage.add(`猎龙？？这个活动10年前不就被取消了吗？怎么又要开始了`);
       $gameMessage.add(`但是\\N[1]没有胆量把话问出来。`);
       $gameMessage.add(`”那么，一个月内向你们的直辖市报道。明天早上就出发吧。“`);
       $gameMessage.add(`说完，他把葡萄酒一饮而尽，”集英使“很快带着他的仆从们离开了村庄。`);
       $gameMessage.add(`对了，路上你可得小心点，如果你路上出了点什么事，没有及时报道`);
       $gameMessage.add(`每年你们村庄的税收就多交上2倍税收吧。`);
       
       $gameMessage.add(`远眺着马车留下的灰烟，村庄里悄悄地传出几声开门的声音。`);
       $gameMessage.add(`一家人围坐在桌前，门外是明媚的阳光，桌上是丰盛的午餐。但是气氛却沉重的喘不上气。`);
       $gameMessage.add(`”我，我这两天猎到了两头奇鹿。“`);
       $gameMessage.add(`父亲望了过来，挤出一丝微笑。”不愧是我儿子，好样的。好样的。“`);
       $gameMessage.add(`”好了，开饭吧，这可是大丰收啊。父亲给葡萄酒瓶子里灌上稠酒。“`);
       $gameMessage.add(`来，咱爷俩好久没有喝过了，今天来久违的庆祝一番吧！`);
       $gameMessage.add(`\\N[1]已经想不起来那天是怎末度过的了。虽然大家对当勇者这件事缄默不提`);
       $gameMessage.add(`但是半夜还是能看到母亲在缝制的身影。`);
       
       $gameMessage.add(`第二天还是到来了。`);
       $gameMessage.add(`父亲不知道从哪里搞来一把长刀，而母亲则拿来了一条厚重的围巾。`);
       $gameMessage.add(`”快到深秋了，天冷，你平时多注意保。“`);
       $gameMessage.add(`母亲话还没有就哭着紧紧的抱住了\\N[1]。`);
       $gameMessage.add(`然后是妹妹，就连平日里性格厚重的父亲也落泪了。`);
       $gameMessage.add(`但是分别的时候终究会来临。`);
       $gameMessage.add(`就这样，我们的主角带着母亲连夜赶出来的围巾，带着父亲的长刀还有一大堆食物，踏上了成为勇者的道路。`);
   }
   ```

5. 把之前事件指令中的代码都删掉

6. 写上

   ```js
   storyBegin();
   ```

7. 在插件中把这个插件打开

   ![image-20211106201746731](G:\创作\笔记\游戏开发\RPGMakerMV开发\img\image-20211106201746731.png)



要注意，这次我们就不要在MV中运行游戏了，我们可以打开根目录下的index.html文件，对其右键选择open with live server

![image-20211106211647103](img\image-20211106211647103.png)

然后游戏就可以在网页中运行了。怎么样，这下是不是就能正常运行了呢？





<img src="img\迷子同学\function是什么.jpg" alt="image-20211027231428381" style="zoom: 20%;" />





这个东西啊，叫做==函数==，是插件编写中最最最重要的东西。我们下面会讲解的，不过在讲解之前我们还是先讲讲插件吧。

刚刚，我们就已经成功编写了一个插件了，有什么想法吗？

没错，相比于在脚本中直接写代码，编写插件可以说是好处多多

1. 代码有了颜色和提示，分辨起来非常舒服
2. 可以一次编写大量的代码
3. 极大程度的简化了事件指令的编写，之前长长的一串代码，被缩略成了短短一句话







但是插件也不是没有缺点，插件往往被封装在一个==函数==中来使用的。

那么函数是什么？不要着急，我们马上就要学到。

如果累了的话休息一下也可以哟。







## 函数与公共事件

函数是js语法中非常非常重要的一个东西，语法上结构如下：

```js
function 函数名(参数1，参数2，，，，){
	return 返回值;
}
```

函数一般用于代码的==封装==。封装、继承、多态是咱们面向对象语言最重要的三个知识。我们今天就来看看封装的知识吧！



就如刚才的例子，如果你的代码太多了，放到事件编辑器里面会显得非常臃肿，所以放到插件里面，以插件的形式调用就显得非常简洁了。而写在插件里面的代码必须封装到函数里面，这个原因比较复杂，有兴趣的同学可以看看下节课的内容，这个是作为支线课程的，

另一方面，如果你的代码比较短，但是要经常被用到，这时候，你是不是会想到些什么呢？是的！就是使用公共事件。公共事件就是用来==封装==代码的一种机制。



光说的话，实在不容易理解，我们不妨把这个做入游戏中看看吧！

刚刚说到主角离开了家乡踏上了成为勇者的道路，但是这路上要是光赶路也太无聊了。按照通常的做法，男主路上肯定会遇到很多野怪，那么有了野怪就要有战斗，有了战斗就要有战斗系统。

我们这次不会写出完整的战斗系统，仅仅是简单的打个草稿。



首先，我们不妨在地图上添加几个怪物。然后在每个怪物的身上都挂载一个脚本：

```js
 $gameMessage.add(`\\N[1]遇到了怪物！开始战斗！`);
```





> <div style="color:pink;float:left;">唔，，，就算是草稿也太简陋了吧。</div>
>
> <div style="color:black; float:right;">说的也是呢</div>
>
> <div style="color:black; float:right;">战斗可以分为进入战斗、战斗处理。战斗结果三部分</div>
>
> 
>
> <div style="color:black; float:right;">我们把剩下的几个部分也加上去吧！</div>
>
> 



现在，再次把脚本更改为：

```js
$gameMessage.add(`\\N[1]遇到了怪物！开始战斗！`);
$gameMessage.add(`战斗中`);
$gameMessage.add(`战斗胜利！获得奖励！`);
```



怎么样？是不是觉得有点麻烦啦？如果今后还要对战斗系统进行什么修改，又得把所有怪物的脚本都再次进行替换。

这个情况我们是不是有些似曾相识呢？

没错！我们第一次接触变量的时候也是这种情况。更改主角名字时，我们希望只用更改一处就可以了，而不想对所有语句一个个修改。所以使用了变量。只有变量存储着真正的值，剩下的代码都是引用这个值而已。

函数也是一样的，只不过函数存放的不是字符串或者数字。它里面储存的就是代码！



如果某个代码需要被多次使用，那么最好把它封装成一个函数。这样以后修改它的时候就可以“牵一发而动全身”，不至于“遍地开花”。

所以我们就不妨把刚才的战斗代码封装一下。

```js
function battle(){
    $gameMessage.add(`\\N[1]遇到了怪物！开始战斗！`);
    $gameMessage.add(`战斗中`);
    $gameMessage.add(`战斗胜利！获得奖励！`);
}
```



现在再次调用它试试看吧！

现在我们如果需要修改战斗的内容，只需要修改函数里面的代码即可，大大的提高了代码的灵活性。



而这种把很多语句封装到一起的操作，我们是不是在哪里见过呢？没错，就是公共事件!

实际上公共事件 就是一个特殊的函数，只不过它是由json存储的。这个之后会讲哒。虽然他们的实现机制不一样，但是核心思想是一样的。那就是 <span style="font-size:20px;">封装</span> <span style="font-size:25px;">封装</span> <span style="font-size:30px;">还是封装！！！</span> 

如果你有一段代码需要反复使用，或者非常非常长，单独放起来很难受，那么请务必使用函数或者公共事件来存储。







## 内容小结

- `$gameActors.actor(1)`可以获取角色信息
- `actor.setName("新名字");`获取了信息之后，可以使用这个API来改名
- 可以使用VScode来调试编辑代码
- 如果你的代码过长，需要用函数封装，然后放到插件里面。
- 函数和公共事件思想是一样的，那就是封装频繁使用或者过长的代码。





# 初探MV的生命周期*

看到这里，想必一些大佬已经试过了吧，为什么非要封装成函数？如果不封装又怎么样？

答案想必各位也知道了吧，那就是：没有反应。

为什么呢？这就得来谈谈MV的生命周期了。



学习unity的同学都知道，unity的代码都是和生命周期息息相关的。比如事件唤醒的`Awake`、以帧数更新的的`Update`、控制物理操作，以赫兹更新的`FixedUpdate`，各司其职。



但是MV真的非常非常离谱，官方没有公开生命周期图。其实也不是不能够理解，因为MV的代码基本上都是写在插件里面的，根本就不需要担心生命周期的问题。但是这也会造成很多问题，比如莫名其妙的BUG出现了，但是又不知道为什么。

如果能知道生命周期就好了，肯定有同学这么想吧！我其实也很想知道，所以，我自己从源码的调用关系中，推导了一下MV的生命周期，这个准确性实在不敢保证。因为我技术也是非常非常废物，所以如果有错误，希望大佬门不吝赐教。

不过MV的生命周期非常复杂，一口气肯定是说不清楚的，我在这里只是简单说明一下插件的执行顺序。







首先不封装函数直接运行代码的结果各位已经看到了吧？为了防止有的同志没有试过，我把结果先贴出来：

![image-20211106211149300](G:\创作\笔记\游戏开发\RPGMakerMV开发\img\image-20211106211149300.png)



是的，居然报错了！而且错误非常诡异，“不能从null身上读取属性。”也就是说，在执行这条命令的时候，$gameMessage对象根本就没有诞生！所以才会出现这个bug。

为了理解这个bug，我们需要知道两个事情，

1. 这条插件是什么时候被执行的？
2. $gameMessage对象是什么时候诞生的？



我首先回答第一点：

插件是在main.js被运行时就调用了。还记得刚才我是不是说过，在index.html中右键可以打开游戏。而这个html就是游戏运行时访问的第一个文件。

写过前端的同志都知道，index.html在前端就相当于main函数的地位，而一进入这个“main函数”，就可以看到里面有一个body。就是这个body加载了MV的各个源代码。

```html
<body style="background-color: black">
    
    <script type="text/javascript" src="js/libs/pixi.js"></script>
    <script type="text/javascript" src="js/libs/pixi-tilemap.js"></script>
    <script type="text/javascript" src="js/libs/pixi-picture.js"></script>
    <script type="text/javascript" src="js/libs/fpsmeter.js"></script>
    <script type="text/javascript" src="js/libs/lz-string.js"></script>
    <script type="text/javascript" src="js/libs/iphone-inline-video.browser.js"></script>
    
    
    <script type="text/javascript" src="js/rpg_core.js"></script>
    <script type="text/javascript" src="js/rpg_managers.js"></script>
    <script type="text/javascript" src="js/rpg_objects.js"></script>
    <script type="text/javascript" src="js/rpg_scenes.js"></script>
    <script type="text/javascript" src="js/rpg_sprites.js"></script>
    <script type="text/javascript" src="js/rpg_windows.js"></script>
    
    
    
    <script type="text/javascript" src="js/plugins.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
</body>
```

在里面可以看到许多的.js文件。

前面6个（我已经给你分好组了）是MV的库文件，也就是比较底层的文件，相当于`<stdio><iostream>`之类的，没事不要去改。

之后6个，都是游戏的各个功能，包括人物的数据、窗体的绘制、战斗的数值计算等等。游戏的运行基本上就是靠的这些，我们今后主要的学习内容就是这些js文件。

plugins.js就是当前MV中所有加载的插件。这个和插件管理器是一一对应的。

最后面这个main.js，就是我们今天要学习的。它负责的功能只有两个：

1. 加载插件
2. 开始游戏

看到了吗？

首先是加载插件，然后才是开始游戏。

也就是说当我们这些语句被写入内存的时候，游戏还没有开始。



然后来回答第二个吧，这个gameMessage是什么时候诞生的？

答案就是：在游戏加载之后被new出来！

我们可以简单看一下执行顺序

```js
//首先，全局的场景启动，加载游戏的各个画面
SceneManager.run(Scene_Boot);

//在SceneManager.run方法中可以看到有一个goto方法
SceneManager.run = function(sceneClass) {
    try {
        this.initialize();
        this.goto(sceneClass);
        this.requestUpdate();
    } catch (e) {
        this.catchException(e);
    }
};

//在goto方法中，Scene_Boot类第一次被实例化
SceneManager.goto = function(sceneClass) {
    if (sceneClass) {
        this._nextScene = new sceneClass();
    }
    if (this._scene) {
        this._scene.stop();
    }
};

//然后回到上面去，进入requestUpdate，在这里就可以看到一个库函数requestAnimationFrame，这个玩意是web自带的底层函数，这个已经很底层了不再赘述，我只能介绍一下这个函数的功能，这个函数的作用定期执行回调函数——SceneManager.update方法。
SceneManager.requestUpdate = function() {
    if (!this._stopped) {
        requestAnimationFrame(this.update.bind(this));
    }
};

//然后在回调函数中，我们可以看到有一个updateMain
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

//进入updateMain，可以看到有一个updateScene
//而且我要特别强调一点，changeScene方法可以在场景切换的时候把this._scene 赋值为 this._nextScene;
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


//然后可以在updateScene看到一个 this._scene.start();
//看到这个是不是有感觉了？我刚才之所以强调changeScene方法，就是因为它会把之前的Scene_Boot设为当前的场景。
//然后执行Scene_Boot的start方法。
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


//下面就是重点了！！
//在Scene_Boot中，有一个setupNewGame方法。
//这个方法就是真正启动游戏的方法了。
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



//进入其中，我们可以看到有一个createGameObjects方法，
//顾名思义，这个方法就是创建游戏对象的
DataManager.setupNewGame = function() {
    this.createGameObjects();
    this.selectSavefileForNewGame();
    $gameParty.setupStartingMembers();
    $gamePlayer.reserveTransfer($dataSystem.startMapId,
        $dataSystem.startX, $dataSystem.startY);
    Graphics.frameCount = 0;
};


//然后就是旅途的终点了，可以看到，我们可爱的$gameMessage就在这里诞生了。
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

所以说，插件的加载比游戏对象要早，当然会显示错误啦！！！





怎么样？是不是有些绕呢？没有关系，本文的主题本来就是js入门，现在看不懂是很正常哒！之后会有专门的进阶课哒！

况且。。。。。。

<img src="img\迷子同学\迷子出现在支线.jpg" alt="image-20211027231428381" style="zoom: 20%;" />





好了，今天的课程就到这里啦！大家辛苦喽！！！









# 战斗系统的设计1——模型建立



上回说到啊，这个大蛇人同志呢，应征入伍踏上了勇者之旅。但是这勇者哪有那么好当，一路上的艰辛自不用说，但是我们最关心的部分想必就是路上，和各种野怪的战斗了吧。（毕竟都拿了村里最好的刀）

那么在进行下面的游戏之前，我们得先把战斗系统设计一下。因为是脚本教学，我们就不采用自带的战斗系统了，我们将采用魔塔的那种简易的战斗系统。

但是我们设计这些什么什么系统之前，千万要记住，不要急着动手写代码，而是要先把你的系统脑补好。





## 分析与问题的提出

首先，我们先来分析一下战斗的流程：

1. 主角碰触到敌人
2. 分析主角和敌人的敏捷值谁高，判断谁先攻击
3. 主角或敌人攻击，被攻击的对象HP减少
4. 如果其中有一个人还活着，那么继续执行3
5. 如果主角失败，进行失败惩罚
6. 如果敌人失败，进行战斗奖励



第一个可以直接使用事件的确定键来解决，而在进行第二步之前，我们得先设计一下主角的各种数值。

## 初始化

```js
var character_dex = 5;
var character_hp = 20;
var character_mp = 15;
var character_atk = 5;
var character_def = 7;


var enemy_dex = 3;
var enemy_hp = 10;
var enemy_mp = 15;
var enemy_atk = 3;
var enemy_def = 4;
```



这几句意思很简单，就是给玩家和敌人设置了各个属性。

但是下面就遇到了问题，第三步要求我们**判断**玩家和敌人的敏捷谁更高，**如果**玩家更高，那么玩家攻击。**如果**敌人更高，那么敌人攻击。

那这个如果和判断到底是怎么实现的呢？

## if语句

我们之前接触到的代码都是一次执行完的，只要写上去就能运行，但是实际开发中怎么可能都这么一帆风顺呢？现在我们就可以请出我们今天的新语法了——if语句。

```js
if (character_dex>enemy_dex){
    console.log("玩家攻击！")
}else{
    console.log("敌人攻击！")
}
```

实际上这个代码还是很显而易见的。在代码中判断如果的语法就是if。if character_dex大于enemy_dex，那么玩家攻击。else，除开之外的情况下，执行敌人攻击语句。非常的直观。

不过要注意的是，if语句的判断条件需要写在括号里面，else则不需要写括号。因为else是if之外的所有条件。

如果我是女孩，我就穿小裙子。要是我不是的话我就穿裤子。

可以看到我后一句话没有再次假设，要是我是男孩的话，，，而是直接说了要是我不是。因为else是除开if之外的情况，可以自己推导出来，所以不需要再写条件。



不过我们的战斗当然不能这么简单的写console啦，我们需要确确实实地把hp扣除掉。下面我们就来详细写一下战斗的过程吧。

```js
if (character_dex>enemy_dex){
    enemy_hp = enemy_hp - character_atk;
    console.log("玩家攻击！")
}else{
    character_hp = character_hp - enemy_atk;
      console.log("敌人攻击！")
}
```



好啦，现在我们去MV中试一下吧！



## do...while循环



刚才我们已经试验过了，确确实实可以扣血，但是我每次碰一下，才战斗一次。有没有什么办法能让我们一次战斗完？直到有一方hp归零才结束战斗呢？

这时候就要请出我们的do...while循环了。这个循环的意思就是一直运行代码，直到...。

来一起看一下吧。

```js
var character_dex = 5;
var character_hp = 20;
var character_mp = 15;
var character_atk = 5;
var character_def = 7;


var enemy_dex = 3;
var enemy_hp = 10;
var enemy_mp = 15;
var enemy_atk = 3;
var enemy_def = 4;
do {
    if (character_dex > enemy_dex) {
        enemy_hp = enemy_hp - character_atk;
        console.log("玩家攻击！")
    } else {
        character_hp = character_hp - enemy_atk;
        console.log("敌人攻击！")
    }
} while  (character_hp > 0 && enemy_hp > 0)
```



这个do while语法有点点复杂，他首先会执行代码块里面的内容，然后去判断while括号里面的内容，如果里面为真，那么就继续执行。但是这样逻辑比较复杂，直接理解的话就是：如果他们两个人还都有hp，那么就要继续战斗。 其中`&&`的意思是并且。也就是说character_hp > 0并且enemy_hp > 0。

但是我们的想要实现的效果是直到有一方hp<0，也就是说我们这个逻辑刚好和代码是反过来的！那么此时就可以使用取反运算符`!`，来操作了。

```js
 while (! (character_hp <= 0 || enemy_hp <= 0) )
```

现在代码是不是清楚了一点了呢？前面那个感叹号就是取反的意思。不用管，只用看下面的逻辑即可：直到有一个人的hp小于0，那么战斗结束，否则继续战斗。这个感叹号建议都加上比较好，这样子跳出循环的逻辑就会清楚一点。

好啦，那么我们战斗系统的一个大致思路就设计完成了。





# 战斗系统的设计2——数值策划

## 战斗流程的修改

是这样的，我们刚才的战斗系统中有一个非常非常致命的bug，那就是！！！谁的敏捷高谁就可以一直攻击！如果连这个bug都没有发现的同学，你真的得好好反思一下啦！不要光用手机看教程，最重要的是自己动手敲！学代码如果光看的话是掌握不了的！

好啦言归正传，我们之所以会出现这个bug，是因为敌我两个人的敏捷一直没有改变，导致每次判断的时候，都会判断主角先攻击。所以，我们不妨设计，每次攻击之后敏捷值减少，这样就可以保证轮流攻击了。

```js

var character_dex = 5;
var character_hp = 50;
var character_mp = 15;
var character_atk = 5;
var character_def = 7;


var enemy_dex = 3;
var enemy_hp = 50;
var enemy_mp = 15;
var enemy_atk = 3;
var enemy_def = 4;
do {
    if (character_dex > enemy_dex) {
        enemy_hp = enemy_hp - character_atk;
        character_dex = character_dex-1;
        console.log("玩家攻击！")
    } else {
        character_hp = character_hp - enemy_atk;
        enemy_dex-=1;
        console.log("敌人攻击！")
    }
} while (character_hp > 0 && enemy_hp > 0)
```

同时，为了让结果更加明显一点，我们还可以把两个人hp都调高。

怎么样，是不是现在就能互相攻击了呢？



## 函数封装

还记得上节课的内容吗？对于一些频繁使用的，或者很长的，或者可能需要频繁修改的代码，我们就需要把它封装成函数。那么我们的战斗系统当然会使用频繁啦，而且随着我们的学习深入也是要进行修改的，所以我们但凡写什么什么系统，一定要记得封装函数。

首先复习一下函数的格式。

```js
function 函数名(){//我是代码
}
```

然后我们就来封装刚才的代码。

```js
function battleBegin() {
    var character_dex = 5;
    var character_hp = 50;
    var character_mp = 15;
    var character_atk = 5;
    var character_def = 7;


    var enemy_dex = 3;
    var enemy_hp = 50;
    var enemy_mp = 15;
    var enemy_atk = 3;
    var enemy_def = 4;
    do {
        console.log(1);
        if (character_dex > enemy_dex) {
            enemy_hp = enemy_hp - character_atk;
            character_dex -= 1;
            console.log("玩家攻击！")
        } else {
            character_hp = character_hp - enemy_atk;
            enemy_dex -= 1;
            console.log("敌人攻击！")
        }
    } while (character_hp > 0 && enemy_hp > 0)
}
```



以后我们想要再次战斗，就不需要再次写这么多代码了，只需要使用`battleBegin()`调用即可。

另外，以后我也不会封装函数了，如果没有特殊情况，我所有的代码都会默认写在函数里面，不再赘述。



## 数值的完善

首先在设计前，我们得要有一个明确的目标，主角的战斗力大约有多强？atk和def对战斗有多大的影响？

我们不妨先进行设计，然后再建模。

咱们的战斗数值设计如下：

- 无论防御力多高，都会受到至少1的攻击
- 攻击力越高，或者防御力越低，受到的攻击就越大
- 攻击要保持平衡



假如有5个角色，有的擅长暴击，有的擅长高命中率，有的则均衡。

必须保证平均伤害必须一样。









那么我们不妨把战斗公式设为：

$$
defender.hp=defender.hp-attacker.atk*\frac{attacker.atk}{defender.def+attacker.atk}
$$
这样用比值来确定伤害的方式可以保证每次攻击都有伤害，在双方攻防相等的情况下攻击力可以被减半。当防御者防御力无穷大时，伤害接近0。攻击力无穷大时，攻击力接近其本身。







> <div style="color:pink;float:left;">唔，，，但是一般战斗系统都是有暴击率和挥空率的设计吧。</div>
>
> <div style="color:black; float:right;">说的也是呢</div>
>
> <div style="color:black; float:right;">每次都命中的话，实际上就真的有点堆数值的感觉了</div>
>
> <div style="color:black; float:right;">那么我们也把这两个看脸的属性加进去吧！</div>
>
> 



说到这个暴击率和挥空率啊， 不管怎么设计，都得要保证一个东西。所受伤害的期望不能发生变化。

（期望就是平均值的意思）

不能说我加了两个功能之后，掉血更快了，或者大家战斗存活时间更久了。

那么我们不妨列出等式：
$$
普通伤害*1=闪避率*0+（1-挥空率）*[暴击率*暴击伤害+（1-暴击率）*普通伤害]
$$
左边就是原本攻击伤害的期望，普通攻击的命中率是100%，所以乘以1，而右边则是综合伤害的期望。

然后我们不妨推导一下：
$$
普通伤害 =[暴击率*暴击伤害+（1-暴击率）*普通伤害]-挥空率*[暴击率*暴击伤害+（1-暴击率）*普通伤害] \\
挥空率*[暴击率*暴击伤害+（1-暴击率）*普通伤害] =[暴击率*暴击伤害+（1-暴击率）*普通伤害]-普通伤害\\
挥空率=\frac{[暴击率*暴击伤害+（1-暴击率）*普通伤害]-普通伤害}{[暴击率*暴击伤害+（1-暴击率）*普通伤害]}
$$


我们不妨把中间这个很长的东西设为攻击期望，那么式子可以化简为
$$
挥空率=\frac{攻击期望-普通伤害}{攻击期望}\\
攻击期望=暴击率*暴击伤害+（1-暴击率）*普通伤害
$$
然后就是暴击率的确定，我们不妨规定其为小概率事件。那么按照正态分布$N(μ,σ^2)$，在$(μ-2σ,μ+2σ)$区间内为普通攻击，之外为暴击，那么暴击率为（1-95.449974），差不多是5%左右。

然后代入闪避率的公式，就可以动态计算挥空率了。







## 实际测试

那么我们不妨代值实际计算一下。

设：

```js
attacker.atk = 10;
defender.def = 15;
```

那么理论伤害值为：$10*(10/(10+15))==4$

暴击伤害不妨设为150%，也就是6。

那么攻击期望为：$0.05*6+0.95*4=4.1$

挥空率=$(4.1-4)/4.1=0.02439024390243894$，差不多是2%。





## 二维随机正态分布点的生成——Box–Muller变换算法*

### 均匀分布的Math.random()

上次我们说到这个战斗策划的内容，在最后，我提到一个正态分布的概念，实际上在游戏中不仅仅是战斗命中率需要满足正态分布，就连世界观中，人口的分布、身高分布、角色能力值等等，都需要满足正态分布。

那么这个代码到底该怎么实现呢？？？



我们知道在JavaScript中有一个`Math.random()`方法，这个玩意我记得在几乎所有语言中都有，实际上我学过的这些语言中，都有这个方法，可以说是万金油。但是这个方法有一个问题，那就是，，，，，他是一个均匀分布！！！！！！

我们不妨来看看：

```html
<!DOCTYPE html>
<html lang="ch-Zh">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <canvas width="1000px" height="1000px">

    </canvas>
    <script>
        var testNum =1000;//样本数
        var testRange = 100;//测试范围
        var array = []

        //初始化
        for (let i =0;i<testRange;i++) 
            array[i] =0;
        //获取随机数
        for (let i = 0; i < testNum; i++) {
            var num = Math.floor(Math.random()*testRange) 
            array[num]++;
        }
        var canvas = document.getElementsByTagName("canvas")[0]
        var ctx = canvas.getContext('2d')
        for(let i=0;i<testRange;i++){
            ctx.strokeRect(i*20,100,20,array[i]*10)//用数组出现的次数来描述长度
        }

        ctx.fillText("Math.random()方法服从均匀分布",400,50);//实心字
    </script>
</body>

</html>
```



### Box–Muller变换（笛卡尔坐标系下）

将一个均匀分布变成正态分布，这就是Box–Muller变换，原理的证明，知乎上写的挺不错的，这里就不再证明了。这里只介绍一下使用方法：

1. 准备两个服从均匀分布的随机变量U1、U2。

2. 那么必然有两个正态分布的变量N1、N2满足。
   $$
   N1 = \sqrt{-2 \ln U_{1}} \cos \left(2 \pi U_{2}\right) \\
   N2 = \sqrt{-2 \ln U_{1}} \sin \left(2 \pi U_{2}\right)
   $$
   

```html
<!DOCTYPE html>
<html lang="ch-Zh">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <canvas width="2000px" height="1000px"></canvas>
    <script>

        function getNumberInNormalDistribution(mean, delta) {//第一个是均值，第二个是浮动的范围
            var x = mean + (randomNormalDistribution()[0] * delta)
            var y = mean + (randomNormalDistribution()[1] * delta)
            return [x, y];
        }

        function randomNormalDistribution() {
            var U1, U2, N1, N2 ;
            U1 = Math.random();
            U2 = Math.random();

            N1 = Math.sqrt(-2 * Math.log(U1)) * Math.cos(2 * Math.PI * U2);
            N2 = Math.sqrt(-2 * Math.log(U1)) * Math.sin(2 * Math.PI * U2);
            return [N1, N2];
        }



        var testNum = 1000;//样本数
        var testRange = 1000;//测试范围
        var array = []

        //初始化
        for (let i = 0; i < testRange; i++)
            array[i] = 0;
        //获取随机数
        for (let i = 0; i < testNum; i++) {
            var num = Math.floor(getNumberInNormalDistribution(30,10)[0])
            array[num]++;
        }
        var canvas = document.getElementsByTagName("canvas")[0]
        var ctx = canvas.getContext('2d')
        for (let i = 0; i < array.length; i++) {
            ctx.strokeRect(i * 20, 100, 20, array[i] * 10)//用数组出现的次数来描述长度
        }

        ctx.fillText("正态分布", 400, 50);//实心字
    </script>
</body>

</html>
```



### Box–Muller变换（极坐标下）

如果在极坐标下，那么其方程会变成：
$$
\begin{aligned}
&z_{0}=\sqrt{-2 \ln U_{1}} \cos \left(2 \pi U_{2}\right)=\sqrt{-2 \ln s}\left(\frac{u}{\sqrt{s}}\right)=u \cdot \sqrt{\frac{-2 \ln s}{s}} \\
&z_{1}=\sqrt{-2 \ln U_{1}} \sin \left(2 \pi U_{2}\right)=\sqrt{-2 \ln s}\left(\frac{v}{\sqrt{s}}\right)=v \cdot \sqrt{\frac{-2 \ln s}{s}} .
\end{aligned}
$$
其中 $s=\sqrt{u^{2}+v^{2}} ， \mathrm{u}$ 和 $\mathrm{v}$ 为均匀分布的随机数。

```html
<!DOCTYPE html>
<html lang="ch-zh">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>

<body>
    <canvas width="2000px" height="2000px">

    </canvas>
    <script>
        //随机数生成

        function getNumberInNormalDistribution(mean, delta) {//第一个是均值，第二个是浮动的范围
            var x = mean + (randomNormalDistribution()[0] * delta)
            var y = mean + (randomNormalDistribution()[1] * delta)
            return [x, y];
        }

        function randomNormalDistribution() {
            var u = 0.0, v = 0.0, s = 0.0, c = 0.0;
            do {
                u = Math.random() * 2 - 1.0;
                v = Math.random() * 2 - 1.0;
                s = u * u + v * v;
            } while (s == 0.0 || s >= 1.0)
            c = Math.sqrt((-2 * Math.log(s)) / s);
            // return u * c; //测试正态分布
            return [u * c, v * c];
        }


        class NormalPoint {
            constructor(mean, delta) {
                var [x, y] = getNumberInNormalDistribution(mean, delta)
                this.x = x;
                this.y = y;
            }

 

            static createPoints(num) {//创造num个点
                var points = [];
                var succeedPoint = 0;
                while (succeedPoint < num) {
                    var tempPoint = new NormalPoint(500, 200);//范围值

                        // console.log(tempPoint.checkValid(points))//永远会输出true
                        points.push(tempPoint);
                        succeedPoint++;
                    
                }
                return points
            }

            static drawPoints(points) {
                var canvas = document.getElementsByTagName("canvas")[0]
                var ctx = canvas.getContext('2d')

                points.forEach(point => {
                    ctx.save();//保存画笔状态
                    ctx.moveTo(point.x + 30, point.y);
                    ctx.arc(point.x, point.y, 30, 0, 2 * Math.PI, false);
                    ctx.stroke();
                    ctx.restore();//恢复画笔状态
                })
            }
        }
         var points = NormalPoint.createPoints(600);//生成600个点
         NormalPoint.drawPoints(points);

    </script>
</body>

</html>
```











# 战斗系统的设计3——对象封装

我们刚才把数值设计完毕，但是我想细心的各位可能已经发现了， 我没有把这些攻击防御一次都写死。而是写成了attacker这种形式。这是因为，游戏中不可能所有人都是一样的攻击力吧？

还记得我当时是怎么设计战斗的吗？我写了一大堆

```js
var character_dex = 5;
var character_hp = 50;
var character_mp = 15;
var character_atk = 5;
var character_def = 7;


var enemy_dex = 3;
var enemy_hp = 50;
var enemy_mp = 15;
var enemy_atk = 3;
var enemy_def = 4;
```

这种东西，来表示玩家的属性，还有敌人的属性。

但是，，，，游戏中不可能只有一个怪物啊！！！

所以这就麻烦了，我写这么一个人都已经这么长代码了，那要是来上100个怪物，好家伙。。可惜啊，我们的代码不是按照行数赚钱的。代码越简洁越好。

此时我们就可以用一种叫做对象的数据结构来存储这些属性、



## 初识对象





首先我们来观察一下这些值都有什么特点？是不是感觉重复率很高啊？大家既然都有hp，atk这些属性。那么何必每个人都要再单独写呢？我们可以像印钞机一样，把需要印刷的东西提前写好，需要的时候再印刷即可。

因为这节课比较理论，所以我准备换一个更加通俗易懂的例子。

大家都见过钞票吧？能说一下钞票是什么样子的吗？





```js
function BattleCharacter(){
    
}
```

















## 小心！forEach的陷阱！

```js
function forTest() {
    console.log("for循环的中断")
    var a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for (let i = 0; i < a.length; i++) {
        if (a[i] == 5)
            return false
        console.log(a[i])

    }
}

function foreachTest() {
    console.log("forEach的中断")
    var a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    a.forEach(element => {
        if (element == 5)
            return false;
        console.log(element)
    })
}


forTest()
foreachTest()

```













# **打包原理与底层nw版本更换方法



## 思考一下

在开始之前，我先卖个关子

诸位有用过控制台吧！那么先来看看我这个demo

诸位有办法写出来同样的效果吗？



在以往的游戏中，我们往往只关注游戏里面的角色与游戏的交互，也就是所谓的RPG，你去扮演一个角色进行冒险。而我现在开发的这个游戏更关注玩家自身和游戏的交互。也就是所谓的meta游戏。

这时候越多的meta元素就能带来越好的效果。



## 第一道门槛，获取调试窗口

姑且不说其他的效果，今天咱们的主题是，如何在游戏中打开控制台？

如果你是开发者的话，应该知道，在调试游戏时按<kbd>F12</kbd>或者<kbd>F8</kbd>，可以查看控制台。

但是问题是，如何让它自动打开呢？也就是让这个控制台**自己**弹出来？

我们不妨抓住这个关键点<kbd>F8</kbd>来进行突破。



首先打开VS Code，来看看源代码中F8究竟是如何运作的。

查看源代码的技巧就是`Ctrl+F`！！！

这个很重要，我每次看源代码都是用的这个技巧。

首先按ctrl+F，然后搜索感兴趣的关键点。

然后在各个源文件中查找。



果不其然，我们很快就找到了F8的源代码。它位于rpg_managers.js中。我们来看看代码吧！

```js
if (Utils.isNwjs() && Utils.isOptionValid('test')) {
    require('nw.gui').Window.get().showDevTools();
}
```

翻译过来就是，如果当前环境是nw,js，并且当前是测试模式的话，那么我就打开调试工具的窗口。



这样我们就度过了第一道门槛。

我们不妨测验一下。



## 第二道门槛，生产模式！

我们现在获得了调试窗口，但是不要因此放松警惕！

现在才是真正的关键点。

我们不妨把游戏打包来看看。

如何，刚才的效果是不是又无法实现了呢？





那么问题来了，什么是开发模式？什么是生产模式？

实际上我们知道RPG MakerMV底层是用的nw.js，但是这个nw,js实际上有两个版本！

一个叫做**SDK版本**，另一个叫做**normal版本**。SDK版本指的是开发版本，在这个SDK版本中，很多底层功能会被开放，以便开发者调试。而normal版本则把很多功能禁用掉了，防止用户接触到底层的东西。

我们不妨去官网看看http://nwjs.net/download.html

或者去英文网：https://nwjs.io/downloads/



当然，这个下载速度可能会比较慢，我教大家一个下载外网资源提速的办法，对于咱们这些程序员来说很有用。

1. 使用百度云离线下载，速度较快

   ![image-20220122123111286](img\image-20220122123111286.png)

2. 使用迅雷下载，速度较慢

   ![image-20220122123142776](img\image-20220122123142776.png)





但是这和RPGMaker有什么关系呢？

当然有了！！！！！！！！不觉得这个特性和RPGMaker很像吗？而且人家就是用nw.js写的！

所以我怀疑RPGMaker底层可能使用了两种版本，在我们进行游戏测试的时候，会临时用SDK版本打包。



## 掌握nw.js打包原理

再继续学习之前，我们先来学习一下nw,js是如何打包的。

可以直接把文件拖进去进行执行

也可以用zip的方法进行。

1. 编写文件，必要文件只有一个`index.html`还有`package.json`。

2. 将所需的文件压缩为zip文件，注意rar不行！

3. 把zip文件的后缀名改为nw

4. 把这个文件放到nw.js环境同级目录下

5. 在nw.js的目录下打开命令行，输入下面的命令

   ```
   copy /b nw.exe+app.nw app.exe
   ```

   注意，nw.exe就是咱nw环境的入口，名字可能会变。后面那个就是咱刚才打包的文件。名字也是随意的。

   最后那个app.exe就是咱打包之后的文件。

   不妨运行一下！

   如何是否成功了呢？



















嗯？你说`package.json`？这个名字怎么这么熟悉？？？

当然熟悉了！rpgmaker里面也有一个这个啊！

实际上我们游戏很多重要的熟悉就是由这个决定的！

下回再细讲。

## 替换底层环境

好了，前提知识都差不多了，现在我们来看看rpgmaker的打包到底是怎末回事吧。

打开steam，访问rpgmaker的根目录

我们很容易就能找到一个熟悉的文件夹

`nwjs-win`还有`nwjs-win-test`

没错。这两个就是nw.js的环境！！！

除此之外还有很多其余的环境，分别的linux和max的环境。



当然了，这两个环境已经被官方进行了魔改，目录结构已经发生了变化。

我们只需要把文件粘贴过去，然后替换重名文件即可





接下来我们再来看看效果如何~

可以发现，我们的控制台还有环境已经焕然一新了！







# 项目实战——文芒

## 项目简介

- 弹幕系统
- 仙剑一的道具交互系统
- 成就系统
- 文字合成系统
- 即时战斗系统

