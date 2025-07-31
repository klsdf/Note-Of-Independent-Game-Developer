# 创建

```js
//创建Pixi应用，里面会自动生成一个canvas
let app = new PIXI.Application({ 
  //下面是对canvas的一些设置
    width: 256,         // default: 800 宽度
    height: 256,        // default: 600 高度
    antialias: true,    // default: false 反锯齿
    transparent: false, // default: false 透明度
    resolution: 1,      // default: 1 分辨率
  	backgroundColor: 0x1d9ce0
  }
);
//把canvas元素加入到body里面
document.body.appendChild(app.view);
```

在`Application`里面的对象叫做`options`

## 更改canvas的背景颜色

```js
app.renderer.backgroundColor = 0xbbffcc;//颜色需要使用16进制
```

## 查看和更改canvas大小

```js
//查看
app.renderer.view.width
app.renderer.view.height
//更改
app.renderer.autoResize = true;
app.renderer.resize(512, 512);
```

## canvas画布填充

```js
app.renderer.view.style.position = "absolute";
app.renderer.view.style.display = "block";
app.renderer.autoResize = true;
app.renderer.resize(window.innerWidth, window.innerHeight);
```

并且设置css

```css
* {padding: 0; margin: 0}
```









# 加载器

## 基础写法

```js
const loader = new PIXI.Loader();
loader
  .add("testImage", "1.jpg")//testImage是别名，也可以不写，直接写"1.jpg"
  .load(setup);

//加载成功后调用setup函数
function setup() {
  let sprite = new Sprite(
    loader.resources.testImage.texture
  );
  app.stage.addChild(sprite);
}
```

## add方法

add方法有四个参数

```js
add(name, url, optionObject, callbackFunction)
```

- name：文件的别名
- url：文件的路径（必须）
- optionObject：加载配置项，不用管
- callbackFunction：资源完成加载时要调用的函数



实例：

```js
.add('别名', 'http://...', function () {})
.add('http://...', function () {})
.add('http://...')
```



## 四个回调函数

```js
// 每个加载/错误的文件调用一次
loader.onProgress.add(() => {
  console.log("有一个文件被加载成功、或者加载错误");
});

// 每个错误文件调用一次
loader.onError.add(() => {
  console.log("有一个文件加载错误");
});

// 每个加载文件调用一次
loader.onLoad.add(() => {
  console.log("有一个文件加载成功");
});

// 排队的资源全部加载时调用一次。
loader.onComplete.add(() => {
  console.log("所有文件均被加载成功");
});
```

范例：

```js
loader
  .add("testImage", "1.jpg")
  .load(setup);

function setup() {
  let sprite = new Sprite(
    loader.resources.testImage.texture
  );
  app.stage.addChild(sprite);
}


loader.onComplete.add(() => {
  console.log("所有文件均被加载成功");
});
```

## 回调函数的参数

```js
  loader.onComplete.add((loader, resource) => {

    //可以查看当前文件加载的进度
      console.log("progress: " + loader.progress + "%");

    });
```

# 精灵

## 显示精灵

```js
let app = new PIXI.Application({});

const Application = PIXI.Application,
      loader = new PIXI.Loader(),
      resources = loader.resources,
      Sprite = PIXI.Sprite;

document.body.appendChild(app.view);

//加载图像
loader
  .add("1.jpg")
  .load(setup);

//图片加载好后
function setup() {
  //利用加载好的图像纹理来创建精灵
  let sprite = new Sprite(
    loader.resources["1.jpg"].texture
  );
  

  //将精灵送到舞台上面
  app.stage.addChild(sprite);
}
```

## 定位

- 可以单独设置

```js
sprite.x=100;
sprite.y=100;
```



- 也可以直接设置

```js
sprite.position.set(x, y);
```

## 大小和缩放

- 可以直接设置大小

```js
sprite.width=600;
sprite.height = 300;
```

- 也可以按照比例缩放

```js
sprite.scale.x = 0.5;
sprite.scale.y = 0.5;
sprite.scale.x = 2;
sprite.scale.y = 2;
```

- 也可以使用方法

```js
sprite.scale.set(0.5, 0.5);
```

## 旋转

- 围绕自身旋转

  anchor的值为[0,1]，0.5代表居中

```js
sprite.anchor.x = 0.5;
sprite.anchor.y = 0.5;//旋转点居中

cat.anchor.set(x, y)//或者使用这个来居中

sprite.rotation = 0.5;//旋转角度
```

- 围绕某个点旋转

```js
cat.pivot.set(32, 32)
sprite.rotation = 0.5;//旋转角度
```

# 精灵组

```js
//The cat
let cat = new Sprite(id["cat.png"]);
cat.position.set(16, 16);

//The hedgehog
let hedgehog = new Sprite(id["hedgehog.png"]);
hedgehog.position.set(32, 32);

//The tiger
let tiger = new Sprite(id["tiger.png"]);
tiger.position.set(64, 64);

let animals = new PIXI.Container();

animals.addChild(cat);
animals.addChild(hedgehog);
animals.addChild(tiger);

app.stage.addChild(animals);
```



# 使用雪碧图

```js
loader
  .add("testImage", "女主.png")
  .load(setup);



function setup() {

  //Create the `tileset` sprite from the texture
  let texture = TextureCache["testImage"];

  //Create a rectangle object that defines the position and
  //size of the sub-image you want to extract from the texture
  //(`Rectangle` is an alias for `PIXI.Rectangle`)
  let rectangle = new PIXI.Rectangle(0, 0, 50, 50);

  //Tell the texture to use that rectangular section
  texture.frame = rectangle;

  //Create the sprite from the texture
  let girl = new Sprite(texture);

  //Position the rocket sprite on the canvas
  girl.x = 32;
  girl.y = 32;

  //Add the rocket to the stage
  app.stage.addChild(girl);

  //Render the stage   
  app.renderer.render(app.stage);
}

```

# 游戏循环

这个函数每秒被调用60次。

```js
function setup() {
  app.ticker.add(delta => gameLoop(delta));
}
```



在这个函数里面

```js
    function gameLoop(delta) {

      //Move the cat 1 pixel 
      girl.x += 1;
    }

```



# 键盘监听

```js
function setup() {

  //Create the `cat` sprite 
  cat = new Sprite(resources["images/cat.png"].texture);
  cat.y = 96; 
  cat.vx = 0;
  cat.vy = 0;
  app.stage.addChild(cat);

  //Capture the keyboard arrow keys
  let left = keyboard("ArrowLeft"),
      up = keyboard("ArrowUp"),
      right = keyboard("ArrowRight"),
      down = keyboard("ArrowDown");

  //Left arrow key `press` method
  left.press = () => {
    //Change the cat's velocity when the key is pressed
    cat.vx = -5;
    cat.vy = 0;
  };
  
  //Left arrow key `release` method
  left.release = () => {
    //If the left arrow has been released, and the right arrow isn't down,
    //and the cat isn't moving vertically:
    //Stop the cat
    if (!right.isDown && cat.vy === 0) {
      cat.vx = 0;
    }
  };

  //Up
  up.press = () => {
    cat.vy = -5;
    cat.vx = 0;
  };
  up.release = () => {
    if (!down.isDown && cat.vx === 0) {
      cat.vy = 0;
    }
  };

  //Right
  right.press = () => {
    cat.vx = 5;
    cat.vy = 0;
  };
  right.release = () => {
    if (!left.isDown && cat.vy === 0) {
      cat.vx = 0;
    }
  };

  //Down
  down.press = () => {
    cat.vy = 5;
    cat.vx = 0;
  };
  down.release = () => {
    if (!up.isDown && cat.vx === 0) {
      cat.vy = 0;
    }
  };

  //Set the game state
  state = play;
 
  //Start the game loop 
  app.ticker.add(delta => gameLoop(delta));
}
```



# 附录1——模块代码

```js
<!DOCTYPE html>
<html lang="zh-ch">

<head>
  <meta charset="UTF-8">

  <title>Document</title>
  <style>
    * {
      padding: 0;
      margin: 0
    }
  </style>
  <script src="pixi.min.js"></script>
</head>

<body>
  <script type="text/javascript">

    let app = new PIXI.Application({
      width: 256,         // default: 800 宽度
      height: 256,        // default: 600 高度
      antialias: true,    // default: false 反锯齿
      transparent: false, // default: false 透明度
      resolution: 1,      // default: 1 分辨率
      backgroundColor: 0x1d9ce0
    });

    const Application = PIXI.Application,
      loader = new PIXI.Loader(),
      resources = loader.resources,
      Sprite = PIXI.Sprite,
      TextureCache = PIXI.utils.TextureCache;



    // 全屏
    app.renderer.view.style.position = "absolute";
    app.renderer.view.style.display = "block";
    app.renderer.autoResize = true;
    app.renderer.resize(window.innerWidth, window.innerHeight);

    //把canvas元素加入到body里面
    document.body.appendChild(app.view);


    //加载图片
    loader
      .add("testImage", "女主.png")
      .load(setup);


    var girl;
    function setup() {

      let texture = TextureCache["testImage"];
      let rectangle = new PIXI.Rectangle(0, 0, 50, 50);//切割精灵图
      texture.frame = rectangle;
      girl = new Sprite(texture);

      //精灵图的位置
      girl.x = 32;
      girl.y = 32;

      //精灵图sudu
      girl.vx = 0;
      girl.vy = 0;
      //把精灵图放到舞台上面
      app.stage.addChild(girl);
      app.renderer.render(app.stage);



      //按键监听
      let left = keyboard("ArrowLeft"),
        up = keyboard("ArrowUp"),
        right = keyboard("ArrowRight"),
        down = keyboard("ArrowDown");

      left.press = () => {
        girl.vx = -5;
        girl.vy = 0;
      };


      left.release = () => {
        if (!right.isDown && girl.vy === 0) {
          girl.vx = 0;
        }
      };

      //Up
      up.press = () => {
        girl.vy = -5;
        girl.vx = 0;
      };
      up.release = () => {
        if (!down.isDown && girl.vx === 0) {
          girl.vy = 0;
        }
      };

      //Right
      right.press = () => {
        girl.vx = 5;
        girl.vy = 0;
      };
      right.release = () => {
        if (!left.isDown && girl.vy === 0) {
          girl.vx = 0;
        }
      };

      //Down
      down.press = () => {
        girl.vy = 5;
        girl.vx = 0;
      };
      down.release = () => {
        if (!up.isDown && girl.vx === 0) {
          girl.vy = 0;
        }
      };



       state = play;
    app.ticker.add(delta => gameLoop(delta));
    }

    function gameLoop(delta) {
      state(delta)
    }

    function play(delta) {
      girl.x += girl.vx;
      girl.y += girl.vy;

    }





    function keyboard(value) {
      let key = {};
      key.value = value;
      key.isDown = false;
      key.isUp = true;
      key.press = undefined;
      key.release = undefined;
      //The `downHandler`
      key.downHandler = event => {
        if (event.key === key.value) {
          if (key.isUp && key.press) key.press();
          key.isDown = true;
          key.isUp = false;
          event.preventDefault();
        }
      };

      //The `upHandler`
      key.upHandler = event => {
        if (event.key === key.value) {
          if (key.isDown && key.release) key.release();
          key.isDown = false;
          key.isUp = true;
          event.preventDefault();
        }
      };

      //Attach event listeners
      const downListener = key.downHandler.bind(key);
      const upListener = key.upHandler.bind(key);

      window.addEventListener(
        "keydown", downListener, false
      );
      window.addEventListener(
        "keyup", upListener, false
      );

      // Detach event listeners
      key.unsubscribe = () => {
        window.removeEventListener("keydown", downListener);
        window.removeEventListener("keyup", upListener);
      };

      return key;
    }

  </script>
</body>

</html>
```

