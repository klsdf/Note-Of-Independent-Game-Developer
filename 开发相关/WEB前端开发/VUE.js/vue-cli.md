# 起步

CLI是Command-Line Interface，翻译为命令行界面,但是俗称脚手架。CLI可以快速搭建Vue开发环境以及对应的webpack配置。

## 安装

首先需要node和webpack环境。之后全局安装。

```shell
npm install -g @vue/cli
```

最后可以用大写-V查看版本号。

```shell
vue -V
```

但是我们这个安装的默认最高版本，所以导致旧版的项目可能不兼容，所以还要安装一下旧版本的模板。

```shell
npm install @vue/cli -init -g
```

## 项目创建与运行

不同版本的创建命令不一样，需要特别注意：

```shell
//cli2
vue init webpack 项目名

//cli3及以上
vue create 项目名
```

以cli3为例，输入指令以后会出现下面的提示

```shell
? Please pick a preset: (Use arrow keys)
> Default ([Vue 2] babel, eslint)
  Default (Vue 3 Preview) ([Vue 3] babel, eslint) 
  Manually select features
```

方向键选择`Manually select features`，然后回车。接下来出现这个。

注释是我加的。

```shell
? Please pick a preset: Manually select features
? Check the features needed for your project: (Press <space> to select, <a> to toggle all, <i> to invert selection)
 (*) Choose Vue version     //自己选vue版本
 (*) Babel									//es6转es5
>( ) TypeScript           //支持typescript
 ( ) Progressive Web App (PWA) Support   //先进网络应用支持
 ( ) Router        //vue静态路由
 ( ) Vuex          //vuex
 ( ) CSS Pre-processors    //css预处理器
 (*) Linter / Formatter  //ESlint严格语法标准，别选
 ( ) Unit Testing				//单元测试
 ( ) E2E Testing				//端到端测试
```

之后出现这个，选第一个

```shell
? Where do you prefer placing config for Babel, ESLint, etc.? (Use arrow keys)    
> In dedicated config files   //独立配置文件
  In package.json    //全放到package.json
```

最后，是否把刚才的设置保存下来？目前建议选N。

```shell
Save this as a preset for future projects? (y/N)
```

如果不小心保存了，在哪里删呢？

C:\Users\用户名   里面有一个.vuerc文件，里面的presets就保存了你的配置，删掉presets里面的内容就行了。

最后使用serve运行

```shell
npm run serve
```

想要打包项目，使用

```shell
 npm run build
```

具体在package.json中都有写到。

## 目录结构

- node_modules：通过npm安装的一大推包
- public：公用的文件，最后直接原封不动封进dist文件夹
- src：源代码
- .browserslistrc：浏览器配置
- .gitignore：git的配置，选择上传git时忽略哪些文件
- babel.config.js：不懂
- package-lock.json：记录着各个插件的版本信息
- package.json：主要配置，以后经常要写
- README.md：记录版权信息，使用方法，作者吐槽什么什么的，没有固定用法。

## vue ui 

cli3以上版本超级无敌牛逼的东西，也就是可视化配置，再也不需要去手动改json了，直接可视化全自动操作，我爱死这个东西了。

开启方法很简单：

```shell
vue ui
```

# vue-router

这个router并不是路由器，而是指前端的静态路由。

### 安装

```shell
npm install vue-router --save
```

或者直接在vue ui安装，或者一开始安装cli的时候就把router选上。

建议去vue ui里面安装，vue-router属于插件，直接去插件里面安装。

### 路由映射的配置

在router文件夹下的index.js文件配置，这个是注册路由的。

```javascript
import Home from '../views/Home.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]
```

之后在App.vue里面写上注册过路由的组件，不过直接用肯定没有效果啦，vue提供了一个``<router-link>`标签，便于实现路由跳转，这个标签里面有一个to属性，写要转去的url。最后一定要加上`<router-view/>`，以便显示路由的内容。

```vue
<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view/>
</template>
```

### 代码控制路由跳转

` router-link`是vue自己封装的组件，但是我们有时候并不想用这种固定的方式来跳转路由，这时候我们就可以手动用JS来跳转。比如可以写一个v-on来绑定一个响应函数，里面写上

```javascript
itemClick(){
  this.$router.push('需要跳转的url')
}
```

这个方法会让你的浏览器加载下一个url，也就是说浏览记录里面可能会有一大堆无用的记录，建议换成下面的。

```javascript
itemClick(){
	this.$router.replace('需要跳转的url')
}
```

如果是新版的cli，点两次可能会报错，这是因为新版的router重写了push方法，导致重复跳转时会报错。这时只需要在router下的index.js里面加上这个代码，直接粘过去就行。

```javascript
//重写push和replace方法，防止路由重复跳转报错。
import VueRouter from "vue-router";

//push
const VueRouterPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (to) {
    return VueRouterPush.call(this, to).catch(err => err)
}

//replace
const VueRouterReplace = VueRouter.prototype.replace
VueRouter.prototype.replace = function replace (to) {
  return VueRouterReplace.call(this, to).catch(err => err)
}
```



### 路由重定向

一般来说，我们打开网站，都是默认在首页。这个就是靠路由默认跳转到首页来实现的，如何做到这个效果呢？靠的就是路由重定向。也就是说如果一旦进入某个url，立刻跳转到指定的url。有点像钓鱼网站。

path指的是用户输入的url，redirect就是默认跳转的url。

```javascript
{
  path:'/',
  redirect:'/home'
},
```

### router-link标签的属性

vue-router中引入了router-link标签，用于用户点击来实现页面跳转，这个标签功能非常强大，有很多重要的属性。

- to：用于标记跳转的页面url
- tag：一般情况下，router-link会被渲染成a标签，但是这个tag可以指定最终渲染成的标签  tag='div'
- replace：写了这个，跳转页面的时候就会用replace方法，而不是push，可以避免不必要的历史记录。

### 动态路由

所谓动态路由就是在网页的url后面，动态地添加所需的内容。比如说商品网的url为 /shop/，接下来需求是每点一个商品，后面的url自动拼接商品名。比如 /shop/cat/     /shop/pen/  这样子可以标记每一个组件的url。但是商品这么多，又不可能把所有的url提前写好，并且一旦商品替换，url又得重写。为了避免这个问题，我们可以使用动态路由技术。

第一步，创建一个商品组件，并且注册路由。不多说了。

第二步，修改路由配置，给shop后面加一个`:id`，这个id就是一个变量，表示往url后面拼接的那个变量。

```javascript
{
  path: '/shop/:id',
  name:'Shop',
  component:()=>import('../views/Shop.vue')
}
```

第三步，来给这个id变量绑定值吧。我们这个shop组件是在App组件中引用的，也是在这个里面进行路由跳转的，所以当然也是在这个里面进行id的绑定。核心步骤只有一个，就是让data返回一个商品id，然后用v-bind后面拼接上这个变量。这样点看网页，url后面就会自动拼接上猫娘了。

```vue
//App.vue
<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>|
    <router-link v-bind:to="'/shop/'+goodsId">Shop</router-link>
  </div>
  <router-view/>
</template>

<script>
export default {
  name:'App',
  data() {
    return {
      goodsId:"猫娘"
    }
  },
}
</script>
```

第四步，如果需要在商品页使用这个goodsId的话，那么就会有第四步。首先，自定义一个计算属性，return  当前活跃路由的变量值，这个id并不是本身带的，而是刚刚在路由配置里面咱自己定义的。拿到的这个id，其实就是goodsId:"猫娘"。App.vue先把数据传给了url，之后商品页又从url那里拿到了这个值。之后就可以愉快地使用了。

```vue
<template>
  <div class="shop">
    <span>我是商品页</span>
    <span>当前浏览的商品是{{goodsId}}</span>
  </div>
</template>

<script>
export default {
  name: 'Home',
  computed: {
    goodsId(){
      return this.$route.params.id
    }
  },
}
</script>
```

### 路由懒加载

当打包构建应用时，Javascript包会变得非常大，影响页面加载。如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的时候才加载对应组件，这样就更加高效了。

虽然早期路由懒加载非常复杂，但是新版本的写法已经很简单了。其实`component: () => import()`就是路由懒加载，而Home也是懒加载，也就是说只要是import进来的数据就是懒加载。

```javascript
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/shop/:id',
    name:'Shop',
    component:()=>import('../views/Shop.vue')
  }
]
```

### 子路由

这个其实就是子页面，首页下可能有多个子页面，比如说新闻，推荐之类的。单独再开一个页面肯定不合适，所以可以在首页创建子页面。比如 /Home要和上面那个动态路由区分，上面那个是重开了一个新页面。

首先，建立子组件，不多说了。

之后，配置路由，直接在home中写一个children就可以了，注意，子组件的path不需要写/，编译器会自动帮你拼接斜线的。因为以“/”开头的嵌套路径会被当作根路径，所以子路由上不用加“/”。

```javascript
  {
    path: '/home',
    component: Home,
    children: [
      {
        path: 'news',
        component: () => import('../components/homeNews.vue')
      },
      {
        path: 'recommend',
        component: () => import('../components/homeRec.vue')
      },
    ]
  },
```

之后，跟之前一样，在home页，把这两个router-link写上，以便访问。最后别忘了router-view

```vue
<template>
  <div class="home">
    <div>我是首页</div>
    <router-link to="/home/news">新闻</router-link>|
    <router-link to="/home/recommend">推荐</router-link>
    <router-view></router-view>
  </div>
</template>
```

最后如果想要重定向首页到某个具体组件，可以这么修改。

```javascript
{
  path: '/',
  redirect: '/home/news'
},
```



我发现如果有多层子路由，那么不能一下子跳转到多层子路由。比如说我现在有了多层子路由，但是从Computer这个页面只能跳转到FrontEnd，就算写了HTML的页面，爷跳不过去。非常神秘，难以理解。

```javascript
const routes = [
	// 默认路由重定向
	{
		path: '',
		redirect: '/Home',
	},
	{
		path: '/Home',
		name: 'Home',
		component: () => import('views/Home/Home.vue')
	},
	{
		path: '/Computer',
		name: 'Computer',
		component: () => import('views/Computer/Computer.vue'),
		children:[
			{
				path: 'FrontEnd',
				name: 'FrontEnd',
				component: () => import('views/Computer/FrontEnd/FrontEnd.vue'),
				children:[
					{
							path: 'HTML',
							name: 'HTML',
							component: () => import('views/Computer/FrontEnd/HTML/HTML.vue')
					},
					{
						path: 'CSS',
						name: 'CSS',
						component: () => import('views/Computer/FrontEnd/CSS/CSS.vue')
				},
				]
      },
		]
```

![image-20201023230412696](image-20201023230412696.png)

可以看到，无法进行多层跳转，最多跳一层。

# vuex

vuex是一个状态管理工具，我们的项目开发到后期，组件之间相互调用形成的组件树非常复杂，而有一些全局的变量，在组件相互调用时就会非常难以管理。为了管理这些组件的公有变量，我们就需要vuex来统一管理。

vuex是一个单例模式，这是为了更加清除地管理，如果允许多个store，那么数据就太混乱了，日后管理维护就是噩梦。

### 安装

可以用

```shell
npm install vuex --save
```

或者用万能的vue ui 来可视化安装。之后会多出来一个store文件夹。

### 结构

```javascript
export default createStore({
  state: {
    //存放数据
  },
  mutations: {
    //存放方法
  },
  actions: {
  },
  modules: {
  }
})
```

### 使用方法

- 通过`this.$store.state.属性`的方式来访问数据
- 通过`this.$store.commit('mutation中的方法')`来调用mutation中的方法

# axios

### 安装

```shell
 npm install axios --save
```

### get请求

```javascript
import axios from 'axios'

axios({
  //请求的服务器url
  url:"http://123.207.32.32:8000/home/multidata",
  //请求类型
  method:'GET',
  //针对get请求的参数拼接
  params:{
    type:'pop',
    page:1
  }
}).then(resualt=>{
  console.log(resualt)
})
```

### post请求

```javascript
import axios from 'axios'

axios({
  //请求的服务器url
  url:"http://123.207.32.32:8000/home/multidata",
  //请求类型
  method:'POST',
  //针对get请求的参数拼接
  data:{
    type:'pop',
    page:1
  }
}).then(resualt=>{
  console.log(resualt)
})
```



### axios全局配置

一些经常使用的变量，可以抽出来全局配置。这些变量都是axios提前定义好的，可以直接用defaults来引用。

```javascript
//主机url
axios.defaults.baseURL = "http://123.207.32.32:8000"
//延时时间
axios.defaults.timeout = 3000
axios({
  url: "/home/multidata",
  method: 'GET',
  params: {
    //针对get请求的参数拼接
    type: 'pop',
    page: 1
  }
}).then(resualt => {
  console.log(resualt)
})
```

### 创建axios实例对象

我们刚才所使用的都是一个axios对象，同样的，刚才那些使用方法也都是在一个服务器上的。如果后端的服务器采用分布式设计，那么不同服务器就有不同的url，设置的baseURL就不能满足所有人需求。

此时，我们可以直接创建多个axios的实例对象，每一个都拥有自己的baseURL和timeout等属性。

```javascript
import axios from 'axios'
//创建一个axios的实例对象
const axiosInstance=axios.create({
  baseURL:"http://123.207.32.32:8000",
  timeout:3000
})
//直接用实例对象发送请求
axiosInstance({
  url: "/home/multidata",
  method: 'GET',
  params: {
    type: 'pop',
    page: 1
  }
}).then(resualt => {
  console.log(resualt)
})
```

这样子，对每个服务器都可以创建一个独有的axios对象，进行特别配置。

### Promise封装

我们可以对网络请求进行一个封装，把请求的方法封装进一个js文件，这个文件里面再封装axios的各种方法和配置。

```javascript
import axios from 'axios'

export default request(config){
  return new Promise((resolve,reject)=>{
    const instance = axios.create({
      baseURL:"http://123.207.32.32:8000",
      timeout:5000
    })
    instance(config)
    .then(res=>{
      resolve(res)
    })
    .catch(err=>{
      reject(err)
    })
  })
}
```

但是实际上，`axios.create`的结果本身就自带一个promise，所以我们可以直接用就行了。

```javascript
import axios from 'axios'

export default request(config){
    const instance = axios.create({
      baseURL:"http://123.207.32.32:8000",
      timeout:5000
    })
    return instance(config)
}
```

### 拦截器

这个东西可以把服务器那里请求过来的数据做一个拦截，进行修改或者什么神秘操作。

1. 修改config中不符合服务器规范的配置
2. 在发送网络请求时，在页面显示加载图片
3. 某些网络请求（比如登录），要求用户输入一些特殊信息，

```javascript
import axios from 'axios'

export default request(config){
    const instance = axios.create({
      baseURL:"http://123.207.32.32:8000",
      timeout:5000
    })


    //发送request的拦截
    instance.interceptors.request.use(request=>{
      console.log("已经拦截到用户请求")
      //把拦截掉的请求释放
      return request
    },error=>{
      //当用户请求发不出去时调用，比如断网
      console.log("用户请求发送失败")
    })

    //服务器响应结果的拦截
    instance.interceptors.response.use(response=>{
      console.log("已经拦截到服务器响应")
      //把拦截掉的响应释放
      return response.data
    },error=>{
      //当服务器响应失败时执行，比如404
      console.log("用户请求发送失败")
    })

    return instance(config)
}
```

