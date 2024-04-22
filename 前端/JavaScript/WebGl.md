# hello world

```html
<!DOCTYPE html>
<html lang="ch">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<canvas></canvas>
</body>
<script src="./lib/cuon-utils.js"></script>
<script src="./lib/webgl-debug.js"></script>
<script src="./lib/webgl-utils.js"></script>
<script>

    var 顶点着色器 =
        `void main() {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);  // 分别是XYZ和齐次坐标的那个1
            gl_PointSize = 10.0;                  // 点的大小
        }`;
    var 片元着色器 =
        `void main() {
            gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); //分别是RGBA
        }`;


    window.onload = function () {

        var canvas = document.querySelector("canvas");
        var ctx = canvas.getContext("webgl");

        // Initialize shaders
        if (!initShaders(ctx, 顶点着色器, 片元着色器)) {
            console.log('Failed to intialize shaders.');
            return;
        }


        ctx.clearColor(0.0, 0.0, 0.0, 1.0);
        ctx.clear(ctx.COLOR_BUFFER_BIT);
        ctx.drawArrays(ctx.POINTS, 0, 1)

    }

</script>
</html>
```



- 顶点着色器：用来绘制顶点
- 片元着色器：着色



# 传参

```html
<!DOCTYPE html>
<html lang="ch">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<canvas></canvas>
</body>
<script src="./lib/cuon-utils.js"></script>
<script src="./lib/webgl-debug.js"></script>
<script src="./lib/webgl-utils.js"></script>
<script>

    var 顶点着色器 =
        `
        attribute vec4 test_point;
        void main() {
            gl_Position = test_point;  // 分别是XYZ和齐次坐标的那个1
            gl_PointSize = 10.0;                  // 点的大小
        }`;


    var 片元着色器 =
        `void main() {
            gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0); //分别是RGBA
        }`;




    window.onload = function () {

        var canvas = document.querySelector("canvas");
        var ctx = canvas.getContext("webgl");

        // Initialize shaders
        if (!initShaders(ctx, 顶点着色器, 片元着色器)) {
            console.log('Failed to intialize shaders.');
            return;
        }


        //获取自定义的坐标
        var temp_point  = ctx.getAttribLocation(ctx.program,'test_point') //在webgl种获取到test_point变量
        ctx.vertexAttrib3f(temp_point,0.5, 0.3, 0.2) //将值传入webgl种，最后一个齐次坐标的参数默认是1.0，不写会默认是1.0

        ctx.clearColor(0.0, 0.0, 0.0, 1.0);
        ctx.clear(ctx.COLOR_BUFFER_BIT);
        ctx.drawArrays(ctx.POINTS, 0, 1)

    }

</script>
</html>
```





# webgl渲染管线

1. 顶点缓冲区
2. **顶点着色器**
3. 图元装配：拿到了顶点之后，还要分辨顶点的图形是什么，最常见的就是三角形
4. 光栅器
5. **片元着色器**
6. 归属测试
7. 模板测试
8. 深度测试
9. 融合
10. 抖动
11. 颜色缓冲区









# 绘制三角形

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <style>
        /* @import url("https://webglfundamentals.org/webgl/resources/webgl-tutorials.css"); */

        body {
            margin: 0;
        }

        canvas {
            width: 100vw;
            height: 100vh;
            display: block;
        }
    </style>
</head>

<body>
    <canvas id="c"></canvas>
    <script id="vertex-shader-2d" type="notjs">
    //顶点着色器
    attribute vec4 a_position;
  
    void main() {
      gl_Position = a_position;
    }
  
  </script>
    <script id="fragment-shader-2d" type="notjs">

    //片元着色器没有默认精度，因此我们需要自己定义
    precision mediump float;
  
    void main() {
      gl_FragColor = vec4(1, 0, 0.5, 1);
    }
  
  </script>

    <script src="https://webglfundamentals.org/webgl/resources/webgl-utils.js"></script>
</body>


<script>
    /* eslint no-console:0 consistent-return:0 */
    "use strict";

    function createShader(gl, type, source) {
        var shader = gl.createShader(type);
        gl.shaderSource(shader, source);
        gl.compileShader(shader);
        var success = gl.getShaderParameter(shader, gl.COMPILE_STATUS);
        if (success) {
            return shader;
        }

        console.log(gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
    }

    function createProgram(gl, vertexShader, fragmentShader) {
        var program = gl.createProgram();
        gl.attachShader(program, vertexShader);
        gl.attachShader(program, fragmentShader);
        gl.linkProgram(program);
        var success = gl.getProgramParameter(program, gl.LINK_STATUS);
        if (success) {
            return program;
        }

        console.log(gl.getProgramInfoLog(program));
        gl.deleteProgram(program);
    }

    function main() {
        // 获取webgl上下文
        var canvas = document.querySelector("#c");
        var gl = canvas.getContext("webgl");

        if (!gl) {
            return;
        }

        // 获取着色器的代码文本
        var vertexShaderSource = document.querySelector("#vertex-shader-2d").text;
        var fragmentShaderSource = document.querySelector("#fragment-shader-2d").text;

        // 创建shader们
        var vertexShader = createShader(gl, gl.VERTEX_SHADER, vertexShaderSource);
        var fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragmentShaderSource);

        // 将两个shader链接入program中
        var program = createProgram(gl, vertexShader, fragmentShader);

        // 从program中获取内部数据
        var positionAttributeLocation = gl.getAttribLocation(program, "a_position");

        // 创建顶点缓冲区
        var positionBuffer = gl.createBuffer();

        // 将它绑定给ARRAY_BUFFER (ARRAY_BUFFER基本上就是positionBuffer)
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);

        var positions = [
            0, 0,
            0, 0.5,
            0.7, 0,
        ];
        gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

        // 在此之上的代码是初始化代码





        // 下面的是渲染代码

        webglUtils.resizeCanvasToDisplaySize(gl.canvas);

        // webgl的显示大小
        gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);

        // 清空canvas
        gl.clearColor(0, 0, 0, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);

        // 使用program (pair of shaders)
        gl.useProgram(program);

        // 开启attribute
        gl.enableVertexAttribArray(positionAttributeLocation);

        // 绑定位置缓冲区
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);

        // Tell the attribute how to get data out of positionBuffer (ARRAY_BUFFER)
        var size = 2;          // 2 components per iteration
        var type = gl.FLOAT;   // the data is 32bit floats
        var normalize = false; // don't normalize the data
        var stride = 0;        // 0 = move forward size * sizeof(type) each iteration to get the next position
        var offset = 0;        // start at the beginning of the buffer
        gl.vertexAttribPointer(
            positionAttributeLocation, size, type, normalize, stride, offset);

        // 绘制
        var primitiveType = gl.TRIANGLES;
        var offset = 0;
        var count = 3;
        gl.drawArrays(primitiveType, offset, count);
    }

    main();
</script>

</html>
```



# GLES

## 数据类型

### 标量

- bool

  ```glsl
  bool b;
  ```

- 整型

  ```glsl
  int a = 5;// 十进制
  uint b = 3u;// 无符号十进制
  int c = 036;// 八进制
  int d = 0x3D;// 十六进制
  ```

- 浮点型

  ```glsl
  float f;// 声明一个float型变量
  float s = 3e2;// 声明变量并赋予指数形式的值，表示3×10^2
  ```

### 向量

```glsl
vec4 //包含四个浮点数
vec2 v2;// 声明一个vec2类型的向量
ivec3 v3;// 声明一个ivec3类型的向量
uvec3 vu3;// 声明一个uvec3类型的向量
bvec4 v4;// 声明一个bvec4类型的向量
```

向量的构造如下：



```glsl

```



### 矩阵

```glsl
mat2 m2;// 声明一个mat2类型的矩阵
mat3 m3;// 声明一个mat3类型的矩阵
mat4 m4;// 声明一个mat4类型的矩阵
mat3x2 m5;// 声明一个mat3x2类型的矩阵
```



### 结构体

```glsl
struct into {// 声明一个结构体info
    vec3 color;// 颜色成员
    vec3 position;// 位置成员
    vec2 textureCoor;// 纹理坐标成员
};
 
info CubeInfo;// 声明一个info类型的变量CubeInfo
```

### 数组

```glsl
vec3 position[20]; 声明一个包含20个vec3的数组
 
float x[] = float[2] {1.0, 2.0};
 
float y[] = float[] {1.0, 2.0, 3.0};
```

