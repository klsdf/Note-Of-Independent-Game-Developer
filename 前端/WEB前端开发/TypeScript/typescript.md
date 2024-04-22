# 起步

1. 全局安装

   ```shell
   npm i -g typescript
   ```

2. 编译

   ```shell
   tsc test.ts
   ```

   接着会发现在同目录下多了一个test.js文件。这个就是ts编译成的js文件。

# 类型声明

## 变量

- 显示类型声明

```typescript
let a:number;
let b:boolean=true;
```

- 隐式推断

在初始化的时候，如果有赋值，那么ts会自动推断出a的类型。

```typescript
let a=1;
```

如果在初始化的时候什么的不写，相当于any

```typescript
let a;
//相当于
let a:any;
```



## 函数

```typescript
function add(a:number,b:number):number{
  return a+b;
}
```

## 联合类型

代表可以有多个类型

- 固定的值

  ```typescript
  let color:"red"|"blue";
  ```

- 多个类型

  ```typescript
  let money:number|string;
  ```

  

## 未知

如果暂时不知道数据类型的话，可以使用unknown

```typescript
let money:unknown;
```

