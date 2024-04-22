# 配置

## 必做

1. 初始化

   ```shell
   npm init -y
   ```

2. 安装express

   ```shell
   npm install express --save
   ```

3. hello world

   ```js
   //1.引入express
   const express = require('express')
   //2.创建应用对象
   const app = express();
   //3.创建路由规则
   app.get('/',(require,response)=>{
     //解决跨域问题
   	response.setHeader('Access-Control-Allow-Origin', '*');
     response.send('hello world');
   })
   //4.监听端口
   app.listen(3000,()=>{
     console.log('服务器启动！localhost:3000')
   })
   ```
   
   然后在console里面使用node命令来运行，然后在http://127.0.0.1:3000/点开网页

## 选做

1. 若项目发生了改变，可以自动重启项目

```shell
npm install nodemon
```

安装了之后，必须用以下方法来启动项目

```shell
nodemon '.\项目名.js'
```



# 路由

路由从只需要记住两个核心点，第一，URL是什么？第二，get方法还是post方法。

## 响应类型

- get

  ```js
  app.get('/',(request,response)=>{
    response.send('hello world');
  })
  ```

- post

  ```js
  app.post('/',(request,response)=>{
    response.send('hello world');
  })
  ```

- put

  ```js
  app.put('/',(request,response)=>{
    response.send('hello world');
  })
  ```

- delete

  ```js
  app.delete('/',(request,response)=>{
    response.send('hello world');
  })
  ```








## request的方法和属性

Express不对Node.js已有的特性进行二
次抽象，只是在它之.上扩展了web应用
所需的基本功能。
●内部使用的还是http模块
●请求对象继承自
http.IncomingMessage
●响应对象继承自:
http.ServerResponse 







- 请求url

  ```js
  console.log("请求url："+request.url)
  ```

- 请求的类型

  ```js
  console.log("请求方法："+request.method)
  ```

- 请求头

  ```js
  console.log("请求头："+request.header)
  ```

- 请求参数

  url中？后面的就是请求参数，例如http://127.0.0.1:3000/?loli_age=14，这个方法会返回一个对象。

  ```js
  console.log("请求参数："+request.query)
  ```

- 请求动态参数

  如果访问的url不确定，可以使用冒号`:`的格式来实现动态参数。

  例如url可能是http://127.0.0.1:3000/loli/3，也有可能是http://127.0.0.1:3000/loli/4，此时request接收的URL不确定，这时候就需要用下面的格式。

  ```js
  const app = express();
  app.get('/loli/:id',(request,response)=>{
  	response.send(`你所查询的萝莉数据是+${request.params.id}`)
  }) 
  ```

- 获取请求体

  ```javascript
  //首先需要解析表单请求体，以json格式为例
  app.use(express.json())
  //然后才能获取到请求体
  request.body
  ```

  

## response的方法和属性

- 设置响应码

  设置了这个之后，前端请求的码就会变成这个，所以可以手动来发送404什么的。

  ```js
  response.statusCode = 200;
  ```

- 发送数据

  功能非常强大，不仅可以发送字符串，也能发送其他格式的数据。

  send方法，也可以结束响应，和`response.end()`一样。

  ```js
  //发送字符串
  response.send('hello world');
  
  //发送JSON格式的对象
  response.send({name:'小丛雨',age:114});
  
  //设置响应码，并发送数据
  response.status(404).send("ok");
  response.status(404).err("不可访问！！！");
  res.status(200).json(JSON.parse(data));//里面只能响应json文件
  
  //响应一个cookie，前面是name，后面那个是value
  response.cookie('name','value')
  ```

- 发送数据

  write需要和end搭配使用，否则响应不会结束

  ```js
  response.write('hello');
  response.write('b');
  response.end();
  ```

- 设置响应头（解决跨域问题）

  ```js
  response.setHeader('Access-Control-Allow-Origin', '*')
  ```








## 实例



通过接口读取本地文件



```js
var express = require('express')
const fs = require("fs")

const app = express()

app.get("/getJson", (request, require) => {
    fs.readFile("./test.json", (err, data) => {

        if (err) {
            return require.status(500).json({
                err: err.message
            })
        }

        require.status(200).json(JSON.parse(data))

    })

})

app.listen(3000, function () {
    console.log('服务器启动！localhost:3000')
})
```





# 中间件

所谓的中间件，顾名思义，就是在执行响应之前，先执行一个中间函数。比如想在所有的响应之前都console一个“hello world”，如果给每一个app.get都写这个代码，实在是太累人，所以就可以用中间件。

```js
app.use((req,res,next)=>{
  console.log("我是中间件");
  next();//交出执行权，继续执行代码，否则服务器会卡在这里。
})
```

这样，无论对哪个接口发送请求，都会优先执行中间件，打印这句话。有点像黄牛的感觉。





## 中间件的执行顺序

首先来看一个例子。

```js
app.get('/loli', (req, res) => {
  res.send('loli')
})

app.use((req,res,next)=>{
  console.log("我是中间件");
  next();//交出执行权，继续执行代码，否则服务器会卡在这里。
})

app.get('/futa', (req, res) => {
  res.send("/futa")
})
```

假如现在访问'/loli'接口和'/futa'接口，**那么中间件都会被打印出来吗？**

答案是只有futa的中间件会被打印出来。

实际上中间件的执行顺序和js的执行顺序是一样的，每当后端收到一个访问时，就会先从上开始顺序解析。比如收到了'/futa'端口的请求，那么就会先进入'/loli'的接口，发现不是要访问的，然后到了下一个，发现这个是一个中间件，直接执行，然后执行next继续运行，最后到达'/futa'端口。

而如果访问了loli接口，`res.send()`之后就结束响应了。



## 中间件函数与next

形似这样，带req,res,next的回调函数就是中间件函数。不是说这个整体是中间件函数，而是里面那个才是中间件函数。

```js
app.use((req,res,next)=>{
  console.log("我是中间件");
  next();
})
```

事实上，所有的路由里面都是一个中间件函数。它也拥有next函数。

```js
app.get('/loli', (req, res,next) => {
  res.send('loli')
  next();
})
```



那么next到底是什么意思呢？我们下面就可以来再次说一说了。

还记得上面那个例子吗？

刚才我们对loli接口进行了访问，但是没有打印中间件，如果此时再加一个next，那么在访问完loli之后，就会再次访问下一个中间件，也就是app.use那个，然后，以此类推。要注意的是，next方法会允许该中间件运行到下一个中间件，但是下一个中间件不一定能运行。

```js
app.get('/loli', (req, res,next) => {
  res.send('loli')
  next();
})

app.use((req,res,next)=>{
  console.log("我是中间件");
  next();
})

app.get('/futa', (req, res) => {
  res.send("/futa")
})
```



## 中间件函数保存数据

```js
app.use((req,res,next)=>{
    req.foo = "test"
    next()
})

app.get("/", (req, res) => {
    res.send(req.foo)
})
```



## 中间件函数的封装

还记得`app.use(express.json())`吗，不觉得它和中间件函数非常非常一样吗？

实际上中间件函数就是这样封装的。可以看到，这个东西还能传参，非常非常强大。

```js
function test(param){
  return (req,res,next)=>{
    console.log(`我是中间件，参数为+${param}`);
    next();
  }
}
app.use(test(0721))
```

## 中间件的分类

### 指定路径触发中间件

```js

//限制请求路径
app.use("/test",(req,res,next)=>{
    console.log("我是中间件")
    next()
})

app.get("/", (req, res) => {
    res.send("ok")
})
```



实际上app.get本质上是限制了请求路径和请求方法的中间件。



## 多个中间件的触发

这两个中间件会以此触发

```js
app.use((req,res,next)=>{
    console.log("我是中间件")
    next()
},(req,res,next)=>{
    console.log("我是中间件2")
    next()
})
```





## 异常处理中间件



用于处理所有中间件之后的错误，放到代码最后面

在遇到err的时候，会直接跳转到app.use((err,req,res,next)=>{这里，忽略中间的所有中间件。

**next中间只要带了对象的参数，就会判断为发生异常。**除非是next('route')，会执行堆栈里面的下一个中间件

```js

app.get("/getJson", (request, require,next) => {
    fs.readFile("./xxxxx.json", (err, data) => {

        if (err) {
              next(err)
        }

        require.status(200).json(JSON.parse(data))

    })

})
app.use((req,res,next)=>{
    console.log("我是中间件，但是遇到err的时候会跳过我直接执行异常处理中间件");
    next();
  })

//这里必须写成4个参数，缺一不可
app.use((err,req,res,next)=>{

   res.status(500).send("GGGGG")
})

```



## 两个常用中间件



```js
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
```

这两行代码都是Express应用的内置中间件。中间件可以理解为处理请求的函数的列表，每个函数可以访问请求对象，响应对象以及该列表中的下一个函数。

1. `app.use(express.json())`: 这行代码告诉Express应用，它应该解析来自客户端的JSON数据。当你发送POST或PUT请求时，你的请求体可能包含JSON数据。Express需要解析这个数据以便你可以在路由处理程序中使用(或处理)这个数据。在Express的早期版本中，我们需要使用一个叫做`body-parser`的单独模块才能做到这一点。但在Express4.16.0及以后的版本中，`express.json`中间件已经被包含在Express模块中了。
2. `app.use(express.urlencoded({ extended: false }))`: 这行代码告诉Express应用，它应该解析来自客户端的URL编码数据。URL编码数据是一种HTTP协议中用来在查询字符串或POST请求体中发送数据的方式。`{ extended: false }`参数告诉Express使用querystring库解析URL编码数据，这个库可以正确处理任何字符。如果设置`{ extended: true }`，Express会使用qs库来解析URL编码数据，这个库支持嵌套的对象和数组，但会降低性能。所以，除非你需要qs库提供的嵌套数据的功能，否则推荐你使用`{ extended: false }`配置来提高性能。





## 跨域中间件



```js
app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*"); // 允许所有来源的访问
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept"); // 允许的请求头
    res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"); // 允许的请求方法
    next();
});
```



## 对路由的封装

如果app.get的api特别特别多，都写到一个文件是不可能的，因此需要进行封装。

单独开一个router.js，把api的一部分写到这里，最后导出模块即可。

```js
const express = require("express")

const router  = express.Router()
router.get("/routerTest",(req,res)=>{

    res.end("我是router哦")
})

module.exports = router
```

使用的时候只需要引入模块

```js
const router  = require('./router')

const app = express()

app.use(router)
```



因为中间件也可以指定路径触发，因此也可以对api的url也进一步封装。

```js
//在所有的router中，url前面都加上test
app.use("/test",router)
```

这样请求路径就变成了http://127.0.0.1:3000/test/routerTest







# RESTful API标准





# 项目案例

```js
在介绍修改方案前，需要对你描述的情境有一个澄清。在一个Web应用中，通常会使用某种形式的会话管理，以在服务端跟踪用户的身份。当你描述“前端获取了cookie”，我假定你是指浏览器被发送了一个会话cookie。当浏览器与服务器进行进一步交互时，会话cookie会被连同请求一起发送回服务器，这使得服务器能够识别请求的来源。
在上述背景下，我们修改代码：




// 使用scripts库将会话存储在cookie
const sessions = require('client-sessions');

// 使用sessions库进行cookie的设置
router.use(sessions({
  cookieName: 'session',
  secret: 'random_secret_string',
  duration: 24 * 60 * 60 * 1000,
  activeDuration: 1000 * 60 * 5
}));

router.post('/login', (req, res) => {
    let userName = req.body.user_name;
    let userPassword = req.body.user_password;
    
    let sql = `SELECT * FROM YingxueUser WHERE user_name = ? AND user_password = ?`;
    db.get(sql, [userName, userPassword], (err, row) => {
        if (err) {
           return res.status(500).send('An error occurred during login.');
        }
        if (row) {
            // 如果存在用户，则在session中设置user
            req.session.user = row;
            console.log('Login successful!')
           
        } else {
            res.send('Invalid username or password.')
        }
    });
});

router.get('/test', (req, res, next) => {
  if (req.session && req.session.user) {
    res.send('ok');
  } else {
    res.send('no');
  }
});
这个例子假设你已经设置了一个名为"user"的会话cookie（当用户登录成功时）。现在，当你的服务器接收到一个包含这个cookie的请求时，它就会知道这个请求来自于已登录的用户。如果用户未登录，那么cookie就会不存在，于是server就会返回'no'。
```

