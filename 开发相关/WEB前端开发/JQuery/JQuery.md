# 

点击元素的下标

```js
    $("#content .content-element").mouseenter(function(){
        console.log($(this).index())
    });
```





# 注意this的下标



如果想用jquery获取一个dom元素，那么必须用`$(this)[0]`，不能直接用this

```js
$(document).ready(function(){

    $("#content .content-element").mouseenter(function(){
        anime({
            targets: $(this)[0],
            translateX: 250
        });
    });
});
```

