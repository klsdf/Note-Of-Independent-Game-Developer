# DOM（文档对象模型）

## 简介

文档对象模型（Document Object Model），是W3C制定的一系列操作网页的接口。

DOM主要的工作原理就是把整个HTML页面当作一个文档（document）；然后把标签当作元素（element）；把剩下所有的内容都当成结点（node），从而生成DOM树。

![image-20210327184935935](image-20210327184935935.png)



DOM脚本的书写位置有两个：

1. 写window的回调函数

```js
window.onload = function(){}
```



2. 把script放到body下面。





## 获取节点

- 通过id

  ```js
  document.getElementById("");
  ```

  **注意：只需要定义id，也可以直接在dom中使用这个元素。也就是说只要标签有id这个属性，不使用getElementById方法，也可以直接用id获取dom元素。前提是这个元素不能被其他的js变量占用，比如说我写一个'var app= new Vue()'，那么app这个标签就表示vue对象，而不再是dom元素对象。**

  ```html
  <!DOCTYPE html>
  <html>
  
  <head></head>
  
  <body>
    <div id="test">
      测试数据
    </div>
  </body>
  <script>
    test.innerHTML = "获取成功";
  </script>
  </html>
  ```

  

- 通过类

  ```js
  document.getElementsByClassName(""); //返回值为伪数组
  ```

- 通过标签名

  ```js
  document.getElementsByTagName("div"); //返回值为伪数组
  ```

- 通过选择器

  ```js
  document.querySelector("#id");//直接可以用CSS选择器的方法，来获取元素，只返回第一个元素，推荐选id之类的
  document.querySelectorAll(".class");//直接可以用CSS选择器的方法，来获取元素，返回所有元素
  ```
  
- 获取html和body

  这两个标签非常特殊，所以dom提供了专门获取它们的方法

  ```js
  document.body//获取body元素
  document.documentElement//获取html元素
  ```




**注意，除了document可以获取元素之外，也可以通过父对象来获取。**



实际上是对HTML元素的属性进行操作，一般的属性包括`style`、`value`等等。

## 创建并增加节点

- 创建普通节点

  ```js
  var para = document.createElement("p");
  element.appendChild(para);
  ```

- 创建文本节点

  ```js
  var node = document.createTextNode("text");
  ```

- 创建属性节点

  ```
  
  ```

  
  
  







## 增加节点



1. 原生方法

   ```js
   
   ```



###    document.write(``)

```js
document.write("<h1>This is a heading</h1>");
```





## 删除节点

```js
fireFoxLi.parentNode.removeChild(fireFoxLi);

parent.removeChild(child);
```



## 修改节点内容

### innerHTML和innerText

这两个都可以在标签里面添加文字，区别有两个

1. 是`innerHTML`会识别HTML标签，而`innerText`不识别。

```js
document.body.innerText="<b>测试文字</b>";//会把<b>测试文字</b>打印出来
document.body.innerHTML="<b>测试文字</b>";//会打印加粗的测试文字
```

2. `innerHTML`会保留空格与回车，而`innerText`不保留。

### 操作内置属性

可以参考HTML，HTML的元素具有哪些属性，就可以来操作哪些。包括id什么的都可以操作，但是样式和类需要单独讨论。

### 操作自定义属性

- 自定义属性的书写

  直接在标签里面写就可以了。

  ```html
  <div id="age" age="18">年龄</div>
  ```

  也可以通过js来书写

  ```js
  age.setAttribute('age','18');
  ```

- 获取

  通过`getAttribute`方法来获取。

  ```js
  age.getAttribute('age');
  ```

  也可以通过`element.dataset.属性`来获取自定义属性。注意这个只能获取data-开头的属性

- 操作

  ```js
  age.setAttribute('age','14');
  ```

- 删除

  ```js
  age.removeAttribute('age');
  ```

  

### 操作类

- 增加一个类

  ```js
  document.body.classList.add("snow-container"); 
  ```

- 删除一个类

  ```js
  content.classList.remove("whitePoint"); 
  ```
  
- 覆盖之前的类

  ```js
  document.body.className = "test"; //添加一个类
  document.body.className = "test test2"; //添加多个类
  ```

## 增加id

```js
para.id="achievement";
```



### 操作样式

js中，样式采用驼峰命名法。比如`backgroundColor`、`fontSize`等等。

js修改的样式是行内样式，权重很高。

## 增删元素

### 原生

```js

para.appendChild(node);

var element = document.body;
element.appendChild(para);
```





### 利用innerHtml

```js
var ul = document.getElementsByTagName("ul")[0];
ul.innerHTML += "<li id='li1'>我是innerHTML创建的</li>"
```











### 多个事件的绑定

事件监听是通过给按钮绑定单击响应函数实现的，但是在绑定时可能会出现一些意想不到的bug。

比如说，我现在打算给页面里的所有button绑定单击响应函数

```javascript
var buttons = document.getElementsByTagName('button')
for(var i=0;i<buttons.length;i++)
{
	buttons[i].onclick=function(){
		console.log("点的是第"+i+"个")
	}
}
```

但是实际上无论点哪一个按钮，结果永远是第总数个。这是因为var声明的是全局变量，在for循环结束后，i就永远被固定成了`buttons.length`，这就导致虽然给每一个按钮都绑定了函数，但是i却已经失效了。



- 解决方法1：使用块作用域

也就是说使用let，将i变成局部变量

```javascript
var buttons = document.getElementsByTagName('button')
for(let i=0;i <buttons.length;i++)
{
	buttons[i].onclick=function(){
		console.log("点的是第"+i+"个")
	}
}
```

- 解决方法2：为每个按钮都储存i的值

其实解决方法的本质就是为每个按钮都创建一个独立作用域，那么刚好可以利用每个对象独立储存的特点，直接把index绑定成按钮对象的属性。

```javascript
var buttons = document.getElementsByTagName('button')
for(var i=0;i <buttons.length;i++)
{
	buttons[i].index=i
	buttons[i].onclick=function(){
		console.log("点的是第"+this.index+"个")
	}
}
```

- 解决方法3：使用闭包

闭包可以为每个按钮创立一个独立的作用域，可以使i不受影响。

```javascript
var buttons = document.getElementsByTagName('button')
for (var i = 0; i < buttons.length; i++) {
	(function(index) {
		buttons[index].onclick = function() {
			console.log("点的是第" + index + "个")
		}
	})(i)
}
```











## 网页跳转

```js
window.open("http://www.baidu.com");
```



## 修改标题



document.title = '需要设置的值';   



# 媒体对象

## Audio 

直接写这个就可以了，另外需要注意，必须等用户和document交互之后才能play否则会报错，建议写在onmousedown之类的方法里面，总之就是需要用户和页面交互。

```js
var audio = new Audio("./music/吕圣斐 - 野玫瑰.mp3");
audio.play();//播放
```



# 本地储存

## localStorage

### 存储

- setItem

  这个需要传入两个参数，这两个参数都必须是字符串。一般数据都是json字符串。

  ```js
  localStorage.setItem("变量的名字", '数据');
  ```

- 直接赋值

  ```js
  localStorage.变量的名字 = '数据';
  localStorage['变量的名字'] = '数据';
  ```

  

### 读取

- getItem

  ```js
  localStorage.getItem("变量的名字");
  ```

- 直接读取

  ```js
  localStorage.变量的名字;
  localStorage['变量的名字'];
  ```




### 删除

- clear

  删除所有的数据

  ```js
  storage.clear()//清除所有记录
  ```

- removeItem

  移除某一条数据

  ```js
  localStorage.removeItem("键名")
  ```

  



### 其他

- key()

  可以按照索引来获取键名。

  ```js
  localStorage.key(0)
  ```

- length

  可以查看当前数据的数量，从1开始。

  ```
  localStorage.length
  ```

  





特点：

- 数据永久储存
- 在同一个域名下各个页面数据共享



```js
var storage = window.localStorage;

storage.getItem("变量的名字");//读取数据
```



```js

```



除了length以外，其他属性方法都在原型里面。

```js
save: function () {
    var storage = window.localStorage;
    storage.setItem("character", JSON.stringify(this.character));
    //储存故事进度
    storage.setItem("storyPosition", story.data.content_num);
    alert("保存成功！")
},
    load: function () {
        var storage = window.localStorage;
        var temp = JSON.parse(storage.getItem("character"));
        for (let key in temp) {
            this.character[key] = temp[key];
        }

        //读取故事进度

        story.data.content_num = storage.getItem("storyPosition");
        story.data.ableToContinue = true;

        alert("读取成功！")
    },
```


# indexDB

一种非关系型数据库，indexdb里面没有表的概念，但是有仓库（store）。可以把仓库理解为表。

索引（index），在关系型数据库当中也有索引的概念，我们可以给对应的表字段添加索引，以便加快查找速率。在IndexedDB中同样有索引，我们可以在创建store的时候同时创建索引，在后续对store进行查询的时候即可通过索引来筛选，给某个字段添加索引后，在后续插入数据的过成功，索引字段便不能为空。

游标（cursor）：游标是IndexedDB数据库新的概念，大家可以把游标想象为一个指针，比如我们要查询满足某一条件的所有数据时，就需要用到游标，我们让游标一行一行的往下走，游标走到的地方便会返回这一行数据，此时我们便可对此行数据进行判断，是否满足条件。


## 打开数据库

```js
var request = window.indexedDB.open(databaseName, version);
```

这个方法接受两个参数，第一个参数是字符串，表示数据库的名字。如果指定的数据库不存在，就会新建数据库。第二个参数是整数，表示数据库的版本。如果省略，打开已有数据库时，默认为当前版本；新建数据库时，默认为`1`。


打开之后会有成功和失败的回调函数
```javascript

request.onerror = function (event) {
  console.log('数据库打开报错');
};
```


```javascript
var db;

request.onsuccess = function (event) {
  db = request.result;
  console.log('数据库打开成功');
};
```
这时，通过`request`对象的`result`属性拿到数据库对象。



如果指定的版本号，大于数据库的实际版本号，就会发生数据库升级事件`upgradeneeded`。

 ```javascript
 var db;
 
 request.onupgradeneeded = function (event) {
    db = event.target.result;
 }
 ```


这时通过事件对象的`target.result`属性，拿到数据库实例。



## 新建对象仓库

当数据库是新的时候，会触发`onupgradeneeded`，因为这时版本从无到有，所以会触发这个事件
```javascript

request.onupgradeneeded = function(event) {
	db = event.target.result;
	var objectStore;
	if (!db.objectStoreNames.contains('person')) {
		objectStore = db.createObjectStore('person', { keyPath: 'id' });
		objectStore.createIndex('name', 'name', { unique: false });
		objectStore.createIndex('email', 'email', { unique: true });
	}


}
```
上面代码中，`IDBObject.createIndex()`的三个参数分别为索引名称、索引所在的属性、配置对象（说明该属性是否包含重复的值）。


主键（key）是默认建立索引的属性。比如，数据记录是`{ id: 1, name: '张三' }`，那么`id`属性可以作为主键。主键也可以指定为下一层对象的属性，比如`{ foo: { bar: 'baz' } }`的`foo.bar`也可以指定为主键。
如果数据记录里面没有合适作为主键的属性，那么可以让 IndexedDB 自动生成主键。

```javascript
var objectStore = db.createObjectStore(
  'person',
  { autoIncrement: true }
);
```


## 新增数据



```javascript
function add() {
  var request = db.transaction(['person'], 'readwrite') //创建事务
    .objectStore('person')//获得db对象
    .add({ id: 1, name: '张三', age: 24, email: 'zhangsan@example.com' });//新增数据

  request.onsuccess = function (event) {
    console.log('数据写入成功');
  };

  request.onerror = function (event) {
    console.log('数据写入失败');
  }
}

add();
```

上面代码中，写入数据需要新建一个事务。新建时必须指定表格名称和操作模式（"只读"或"读写"）。新建事务以后，通过`IDBTransaction.objectStore(name)`方法，拿到 IDBObjectStore 对象，再通过表格对象的`add()`方法，向表格写入一条记录。

写入操作是一个异步操作，通过监听连接对象的`success`事件和`error`事件，了解是否写入成功。



## 读取数据

```javascript
function read() {
   var transaction = db.transaction(['person']);
   var objectStore = transaction.objectStore('person');
   var request = objectStore.get(1);

   request.onerror = function(event) {
     console.log('事务失败');
   };

   request.onsuccess = function( event) {
      if (request.result) {
        console.log('Name: ' + request.result.name);
        console.log('Age: ' + request.result.age);
        console.log('Email: ' + request.result.email);
      } else {
        console.log('未获得数据记录');
      }
   };
}

read();
```

上面代码中，`objectStore.get()`方法用于读取数据，参数是主键的值。



## 遍历数据


```javascript
function readAll() {
  var objectStore = db.transaction('person').objectStore('person');

   objectStore.openCursor().onsuccess = function (event) {
     var cursor = event.target.result;

     if (cursor) {
       console.log('Id: ' + cursor.key);
       console.log('Name: ' + cursor.value.name);
       console.log('Age: ' + cursor.value.age);
       console.log('Email: ' + cursor.value.email);
       cursor.continue();
    } else {
      console.log('没有更多数据了！');
    }
  };
}

readAll();
```


## 更新数据

更新数据要使用`IDBObject.put()`方法。

```javascript
function update() {
  var request = db.transaction(['person'], 'readwrite')
    .objectStore('person')
    .put({ id: 1, name: '李四', age: 35, email: 'lisi@example.com' });

  request.onsuccess = function (event) {
    console.log('数据更新成功');
  };

  request.onerror = function (event) {
    console.log('数据更新失败');
  }
}

update();
```



## 删除数据


```javascript
function remove() {
  var request = db.transaction(['person'], 'readwrite')
    .objectStore('person')
    .delete(1);

  request.onsuccess = function (event) {
    console.log('数据删除成功');
  };
}

remove();
```



# 复制粘贴

可以直接读取用户的缓存区，但是在使用的时候，需要用户授权



```js
//复制信息
navigator.clipboard
    .writeText("需要复制的文本")
    .then(()=>{
    alert("成功！")
})


//粘贴信息
navigator.clipboard
    .readText()
    .then((text)=>{
    console.log(text)
})
```



# 多线程

如果某个js文件过大，很可能造成页面阻塞。这时候就可以开启多线程，来加载那个大文件。

```js
new Worker('test.js')
```

# 鼠标控制页面滚动

```js
let container = document.querySelector("#app");
container.addEventListener("wheel", (event) => {
  event.preventDefault();
  container.scrollLeft += event.deltaY;
  console.log(container.scrollLeft)
});
```





# 事件

## DOM事件流

点击一个元素的时候，有两个截断，第一个是捕获阶段，第二个是冒泡阶段

捕获阶段指的是从文档底部一点点到顶部，而冒泡阶段则是说从顶部到底部

## 事件监听

1. 在元素上直接绑定

   ```html
   <h1 onclick="this.innerHTML='文本改变！'">请点击这个</h1>
   ```

2. 先获取元素，再绑定

   给一个元素，只能绑定一个同名的响应，如果再次绑定会覆盖之前的
   
   ```js
   canvas.onmousedown =function(){}
   ```
   
3. 监听

   可以给一个元素同时绑定多个监听器，彼此不会覆盖

   ```js
   element.addEventListener("click", function(){
     
   });
   ```



## 删除事件

```js
.removeEventListener("mousemove", myFunction);
```

## 事件对象

事件的回调函数会传回来一个事件对象

```js
canvas.onmousedown =function(event){}
```



event.target：哪个元素触发了事件

target和this的区别是，target指向触发的元素，而this指向绑定的元素。虽然大多数情况下都是this和target一样，但是如果是在冒泡阶段就不一样了



## 鼠标事件对象

```js
e.clientX //鼠标在窗口可视区的坐标
e.clientY
e.pageX //鼠标在整个文档的坐标
e.screenX //鼠标在电脑屏幕上的坐标
```



## 阻止默认行为和事件冒泡

```js
e.preventDefault();//阻止默认行为
e.stopPropagation();//阻止事件冒泡
```

## 事件委托

如果有多个子节点有事件，那么只需要给父节点绑定事件监听，这样点击子节点，事件就会冒泡到父节点上面去。可以让父节点统一管理。

而且事件的target是触发事件的元素，也就是子节点。

```js
e.target.style.coloe = 'red'
```

这样就可以实现子节点变红了

# 附录1—HTML事件

## 表单事件

| 事件          | 说明                 |
| ------------- | -------------------- |
| onchange      | 下拉框发生变化       |
| form.onsubmit | 点击submit按钮的时候 |
|               |                      |



## 鼠标事件

| 事件        | 说明                       |
| ----------- | -------------------------- |
| onclick     | 单击鼠标                   |
| onmouseover | 鼠标滑过                   |
| onmouseout  | 鼠标离开                   |
| onfoucs     | 获得焦点                   |
| onblur      | 失去焦点                   |
| onresize    | 当调整浏览器窗口大小时触发 |
| onscroll    | 拖动滚动条                 |
| onmousemove | 在鼠标指针移动时触发       |
| onmousedown | 鼠标按钮在元素上按下时触发 |
| onmouseup   | 在元素上松开鼠标按钮时触发 |
| onsubmit    | 表单中确认按钮被点击时发生 |
| selectstart | 鼠标选中文字时             |
| contextmenu | 点击右键出现上下文菜单     |



## 键盘事件

```js
document.onkeydown = function(event) {
  var e = event || window.event || arguments.callee.caller.arguments[0];

  if (e && e.keyCode == 27) { // 按 Esc 

    //要做的事情

  }

  if (e && e.keyCode == 113) { // 按 F2 

    //要做的事情

  }

  if (e && e.keyCode == 13) { // enter 键

    //要做的事情

  }

};
```

# 附录2——键码映射表

## 字母与数字

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

## 小键盘和功能键

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

## 控制键

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

## 多媒体键

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







# setTimeout的第三个参数

用这个可以实现闭包的效果

```js
for(var i=0;i<5;i++){
    setTimeout(function(k){
        console.log(k)
    },i*1000,i)
}
```



# video对象





# BOM（浏览器对象模型）

browser object model，BOM并不是一个官方命名，也没有统一标准，仅仅是对浏览器API的统称。

BOM中的API都放到了window中，而DOM则也属于BOM的一部分。因为DOM是属于document的。



# 模拟按键

```js
  document.onkeydown=function(ev){
        var event=ev ||event
        if(event.keyCode==13){
            alert("按了enter键")
        }
    };
    var e = new KeyboardEvent('keydown',{'keyCode':13,'which':13});
    document.dispatchEvent(e);
```

