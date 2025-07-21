# HTML基础

## 基本结构

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>test</title>
	</head>
	<body>
    Hello World!
	</body>
</html>
```



## 专业术语

### 标签

HTML标签是HTML的基本组成,一般由一对<>组成,比如`<p>hello world</p>`对于只有一个<>的标签,我们叫单标签,单标签最后需要加`/`表示结束,比如`<img/>`

### 属性

每一个标签的开头,都可以加属性,比如`<a href=""></a>`,这个href就是属性,每一个元素都有一些自己独有的属性,而script 和style属性则是每个标签都有的.

### 文档

HTML文档从`<html>`开始,在`</html>`结束,这里面包裹的内容就是HTML文档,文档头由`<head>`定义,而文档主体由`<body>`定义.

## 标记省略

HTML的标签并不是都要写结束标签的。根据对标签省略的力度来划分，标签可以分为3种：

1. 不允许写结束标签

   比如`meta`、`input`等

2. 可以省略结束标签

   li、dt、p、thead等

3. 可以完全省略

   html、head、body、colgroup



## 标签属性

如果属性为boolean类型，那么属性有三种写法来开启属性。

```html

<!-- 只写属性，不写属性值 -->
<input type="checkbox" checked>

<!-- 属性值==属性名 -->
<input type="checkbox" checked="checked">


<!-- 属性值==空串 -->
<input type="checkbox" checked="">
```







属性两边对于字符串并不敏感，可以加双引号、单引号，也可以不加。





```html
<input type="checkbox">
<input type='checkbox'>
<input type=checkbox>
```



## 元素

- 置换元素（replaced element）：指的是元素的内容不由文档直接表示，例如`<img>`。
- 非置换元素（nonreplaced element）：指的是在元素自身生成的框中显示的元素。比如`<span>`，绝大多数元素都是非置换元素。



# 文档相关标签

## !DOCTYPE

文档类型声明标签

其实!DOCTYPE并不属于HTML的标签，他的功能是声明文档的类型：表明了本HTML究竟采用哪一版html语言写的,因为除了HTML5之外还有XHTML,HTML 4.01 Strict、HTML 4.01 Transitional等等。不过现在一般都用的是HTML5.

`<!DOCTYPE>` 声明必须是 HTML 文档的第一行，位于` <html>` 标签之前。之后写上你需要的版本属性

```html
<!-- 声明HTML5 -->
<!DOCTYPE html>
```



## html

标志文档起点与终点，还用于定义文档的语言。

- lang=“zh-CN”

  规定文档所使用的语言（自然语言）





## meta

mtea可以提供有关页面的元信息,就是说,可以给搜索引擎提供一个简历,以确保被搜索到.

- charset="utf-8”

  告诉浏览器web显示页面的时候使用什么字符集，但是要注意浏览器首先会从HTTP响应头来确定字符集，之后才会从文档中查看。但是最好还是写上



## link

一般常用于引用外部样式,或者JavaScript文件。

还可以用于图标的修改。

- rel

  规定当前文档与被链接文档之间的关系。

- type

  引用的类型

- href

  引用的路径

```html
<link rel="stylesheet" type="text/css" href="引用的路径" />
<link rel="shortcut icon" href="引用的路径" />
```



## script



# 文档结构

## main

\<main> 标签规定文档的主要内容。

<main> 元素中的内容对于文档来说应当是唯一的。它不应包含在文档中重复出现的内容，比如侧栏、导航栏、版权信息、站点标志或搜索表单。


**注释：**在一个文档中，不能出现一个以上的 `<main>` 元素。`<main> `元素不能是以下元素的后代：`<article>`、`<aside>`、\<footer>、\<header> 或 \<nav>。



## section

定义文档中的节（section、区段）。比如章节、页眉、页脚或文档中的其他部分。

## body

## header

## footer

## nav

 navigation

## section



## aside

## article

## p

paragraph

定义段落

```html
<p>块级元素的标签</p>
```

# 文档内容

## figure和figcaption

用于文档的插图

```html
<figure>
    <img src="./img/faces/People3.png" alt="">
    <figcaption>图片描述</figcaption>
</figure>
```



## details和summary

设置本地折叠功能

- open

  如果设置了这个属性，那么就会展开

```html
<details>
    <summary>总结</summary>
    <p>1</p>
    <p>2</p>
    <p>3</p>
</details>
```

 <details>
       <summary>总结</summary>
       <p>1</p>
       <p>2</p>
       <p>3</p>
   </details>

# 基础标签

## div

division的缩写，表示分割。

```html
<div>块级元素</div>
```

## span

span表示跨度。

```html
<span>行内元素的标签</span>
```

## hr

```html
<p>
	hr在换行后加水平线<hr/>就像这样
</p>
```

<hr/>

上面就是水平线了

## br

```html
<p>
	br仅仅表示换行<br>就像这样
</p>
```

## 注释

```html
<!-- 我是注释 -->
```



# 链接

## a

anchor（锚点）的缩写。

a标签一共有5种链接：

- 外部链接

```html
<a href="超链接连接的网址">外部链接</a>
```

- 内部链接

```html
<a href="index.html">内部链接</a>
```

- 下载链接：如果链接的是一个zip文件或者其他文件，点击就会下载该文件

```html
<a href="game.zip">下载链接</a>
```

- 锚点链接：可以在页面内跳转，跳转到指定的id。

```html
<a href="#pos">点我定位到指定位置!</a>
<p id="pos">定位点</p>
```

- 空连接：没有指定id的锚点，会默认跳到页面最上面。

```html
<a href="#">返回首部</a>
```



a标签还有一个target属性，用来表示目标窗口的弹出方式。

```html
<a href="#" target="_self">默认打开方式，在当前页面打开</a>
<a href="#" target="_blank">新窗口打开</a>  
```



# 列表

## ul,li

无序列表

```html
<ul>
  <li>我</li>
  <li>是</li>
  <li>无序列表</li>
</ul>
```

<ul>
  <li>我</li>
  <li>是</li>
  <li>无序列表</li>
</ul>

## ol,li

顺序列表

```html
<ol>
  <li>我</li>
  <li>是</li>
  <li>有序列表</li>
</ol>
```
<ol>
  <li>我</li>
  <li>是</li>
  <li>有序列表</li>
</ol>

| 属性     | 值       | 描述                                                         |
| -------- | -------- | --------------------------------- |
| reversed | reversed | 规定列表顺序为降序。\(9,8,7\.\.\.\) |
| start    | 数字 | 规定有序列表的起始值。 |
| type     |1 A a I i  | 规定在列表中使用的标记类型。    |

## dl,dt,dd

```html
<dl>
  <dt>定义列表</dt>
  <dd>是专门写定义的列表,如下</dd>
  <dt>定义:</dt>
  <dd>我是内容</dd>
</dl>
```

<dl>
  <dt>定义列表</dt>
  <dd>是专门写定义的列表,如下</dd>
  <dt>定义:</dt>
  <dd>我是内容</dd>
</dl>

# 表单

## form

form可以规定表单的范围，也就是所谓的**表单域**。

一个表单由表单域、控件和提示信息三部分组成。

控件就是输入框那些，提示信息就是姓名，性别那些信息。



```html
<form action="/demo/demo_form.asp">
	form表示一个表单，里面本身啥都没有，但是可以放各种表单的标签
	<br>
	我是一个input：
	<input type="text" name="firstname" value="我是一个text input">
	<br>
	<button type="button">我是一个button</button>
</form> 
```

## input

input下有很多属性

- number

  ```html
  <input type="number" min="14" max="27" step="3">
  ```

  

- search

  ```html
  <input type="search">
  ```

- date

  输入日期

  ```html
  <input type="search">
  ```

- time

  

- text

  value里面输入的值就是默认值，maxlength可以来规定最大的输入字符数。

  ```html
  <form>
  输入框：<input type="text" value = "默认值" maxlength="6" placeholder="提示文字">
  </form>
  ```

  <form>
  输入框：<input type="text" value = "默认值" maxlength="6" placeholder="提示文字">
  </form>

- password

  ```html
  <input type="password">
  ```
  
- file

  文件限制中间用逗号隔开

  ```html
  <input type="file" name="img" accept="image/gif, image/jpeg">
  ```
  
- reset

  点这个按钮会自动把所有的控件信息**初始化**。如果把控件信息用JS清空，也会默认初始化。

  ```html
  <input type="reset">
  ```
  
  <form>
    <input type="reset">
  </form>
  
- button

  ```html
  <input type="button" value="按钮">
  ```
  
  <form>
  <input type="button" value="按钮">
  </form>
  
- submit

  ```html
  <input type="submit">
  ```
  
  <form>
  <input type="submit">
  </form>
  
- url
  
- radio,checkbox

  value属性的值是发送给后端的。name是用于分组的，只有同一组name下，控件才能生效。

  ```html
  <input type="radio" name="sex" checked>男
  <input type="radio" name="sex">女
  ```

  <form>
  <input type="radio" name="sex" checked>男
  <input type="radio" name="sex" >女
  </form>

  

  ```html
  <input type="checkbox" name="vehicle">姐姐<br>
  <input type="checkbox" name="vehicle">妹妹
  ```

  <form>
  <input type="checkbox" name="vehicle" value="Bike">姐姐
  <input type="checkbox" name="vehicle" value="Car">妹妹
  </form>

- range

  ```html
  <input type="range" min="1" max="99" step=".5" value="70">
  ```
  
- color

  ```html
  <input type="color" >
  ```






required

如果加了这个属性，那么这个表单必须填写之后才能提交



autofocus

自动聚焦

 pattern=""

使用正则表达式来匹配内容



## fieldset,legend

```html
<form>
  <fieldset>
	<legend>我是legend，我是这个表单的边框信息</legend>
	周围这一圈框框就是fieldset控制的
	<br>
	输入框：<input type="text" />
  </fieldset>
</form>
```

## button

```html
<button type="button">button就是一个按钮</button>
```

## select,optgroup,option 

select定义选择列表（下拉列表）,option就是里面的选项，optgroup则是选项的分组

```html
<select>
  <optgroup label="我是optgroup,我是第一组选项">
	<option value ="被送去服务器的值">option1</option>
	<option>选项2</option>
  </optgroup>
  <optgroup label="我也是optgroup,我是第二组选项">
	<option>option3</option>
	<option>选项4</option>
  </optgroup>
</select>
```

<select>
  <optgroup label="我是optgroup,我是第一组选项">
	<option value ="被送去服务器的值">option1</option>
	<option>选项2</option>
  </optgroup>
  <optgroup label="我也是optgroup,我是第二组选项">
	<option>option3</option>
	<option>选项4</option>
  </optgroup>
</select>
## label

label标签可以让你点到某个文字就能选中选项，可以提高用户体验，这个标签需要搭配id才能使用。

```html
<input type="radio" name="type" id="萝莉"><label for="萝莉">萝莉</label> 
<input type="radio" name="type" id="御姐"><label for="御姐">御姐</label> 
```

## textarea

clos代表每行的字符数

rows代表显示的行数

```html
<textarea cols="30" rows="10"></textarea>
```

<textarea cols="30" rows="10"></textarea>

## datalist

在文本输入的时候，可以作为建议文本

```html

<input type="text" list="test">
<datalist id="test">
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
    <option value="4">4</option>
</datalist>
```





# 表格

## table,td,tr,th

table用于定义表格,tr表示这是一行,td表示是一个元素.有几个tr就有几行,一个tr里面几个td就代表这行有几列.

要注意的是,第一行一般都是表格的头,所以用th修饰

```html
<table>
  <tr>
    <th>th表示表格头</td>
    <th>我也是表头</td>
    <th>我也是</td>
  </tr>
  <tr>
    <td>table表示一个表格，里面虽然啥都没有，但是可以放表格标签</td>
    <td>一个tr就用来表示一行表格</td>
    <td>td就表示每个单元格</td>
  </tr>
  <tr>
    <td>我是第2个tr，表示第二行</td>
  </tr>
</table>
```

<table>
  <tr>
    <th>th表示表格头</td>
    <th>我也是表头</td>
    <th>我也是</td>
  </tr>
  <tr>
    <td>table表示一个表格，里面虽然啥都没有，但是可以放表格标签</td>
    <td>一个tr就用来表示一行表格</td>
    <td>td就表示每个单元格</td>
  </tr>
  <tr>
    <td>我是第2个tr，表示第二行</td>
  </tr>
</table>
**注意:!!!!!!表格默认是没有边框的,这个之所以有,是因为typora自动给我加了样式.**

table的属性:

<table>
	<tbody>
		<tr>
			<th style="width:20%;">属性</th>
			<th style="width:20%;">值</th>
			<th style="width:60%;">描述</th>
		</tr>
		<tr>
			<td>border</td>
			<td><i>pixels</i></td>
			<td>规定表格边框的宽度。</td>
		</tr>
		<tr>
			<td>cellpadding</td>
			<td>
				<ul>
					<li><i>pixels</i></li>
					<li><i>%</i></li>
				</ul>
			</td>
			<td>就是表格文字和格子边框的距离</td>
		</tr>
		<tr>
			<td>cellspacing</td>
			<td>
				<ul>
					<li><i>pixels</i></li>
					<li><i>%</i></li>
				</ul>
			</td>
			<td>每个单元格之间的距离</td>
		</tr>
		<tr>
			<td>frame</td>
			<td>
				<ul>
					<li>void</li>
					<li>above</li>
					<li>below</li>
					<li>hsides</li>
					<li>lhs</li>
					<li>rhs</li>
					<li>vsides</li>
					<li>box</li>
					<li>border</li>
				</ul>
			</td>
			<td>规定外侧边框的哪个部分是可见的。</td>
		</tr>
		<tr>
			<td>rules</td>
			<td>
				<ul>
					<li>none</li>
					<li>groups</li>
					<li>rows</li>
					<li>cols</li>
					<li>all</li>
				</ul>
			</td>
			<td>规定内侧边框的哪个部分是可见的。</td>
		</tr>
		<tr>
			<td>width</td>
			<td>
				<ul>
					<li><i>%</i></li>
					<li><i>pixels</i></li>
				</ul>
			</td>
			<td>规定表格的宽度。</td>
		</tr>
	</tbody>
</table>


td,th的属性

<table>
	<tbody>
		<tr>
			<th style="width:20%;">属性</th>
			<th style="width:20%;">值</th>
			<th style="width:60%;">描述</th>
		</tr>
		<tr>
			<td>align</td>
			<td>
				<ul>
					<li>left</li>
					<li>right</li>
					<li>center</li>
					<li>justify</li>
					<li>char</li>
				</ul>
			</td>
			<td>规定单元格内容的水平对齐方式。</td>
		</tr>
		<tr>
			<td>axis</td>
			<td><i>category_name</i></td>
			<td>对单元格进行分类。</td>
		</tr>
		<tr>
			<td>char</td>
			<td><i>character</i></td>
			<td>规定根据哪个字符来进行内容的对齐。</td>
		</tr>
		<tr>
			<td>charoff</td>
			<td><i>number</i></td>
			<td>规定对齐字符的偏移量。</td>
		</tr>
		<tr>
			<td>colspan</td>
			<td><i>number</i></td>
			<td>设置单元格可横跨的列数。</td>
		</tr>
		<tr>
			<td>headers</td>
			<td><i>idrefs</i></td>
			<td>由空格分隔的表头单元格 ID 列表，为数据单元格提供表头信息。</td>
		</tr>
		<tr>
			<td>rowspan</td>
			<td><i>number</i></td>
			<td>规定单元格可横跨的行数。</td>
		</tr>
		<tr>
			<td>scope</td>
			<td>
				<ul>
					<li>col</li>
					<li>colgroup</li>
					<li>row</li>
					<li>rowgroup</li>
				</ul>
			</td>
			<td>定义将表头数据与单元数据相关联的方法。</td>
		</tr>
		<tr>
			<td>valign</td>
			<td>
				<ul>
					<li>top</li>
					<li>middle</li>
					<li>bottom</li>
					<li>baseline</li>
				</ul>
			</td>
			<td>规定单元格内容的垂直排列方式。</td>
		</tr>
	</tbody>
</table>

## thead,tbody,tfoot

刚才那个表格其实不是完整版的,虽然也能用.但是实际开发中,能多严谨就要多严谨.

- thead用于表示表头
- tbody表示表格主题内容
- tfoot用于总结表的内容,当然你也随便写点啥
- **注意:这三个的顺序是thead,tfoot,tbody**

```html
<table>
	<thead>
		<tr>
			<th>妹子</th>
			<th>特征</th>
		</tr>
	</thead>
	<tfoot>
		<tr>
			<th>总体评价</th>
			<th>都是我老婆</th>
		</tr>
	</tfoot>
	<tbody>
		<tr>
			<td>牛顿</td>
			<td>金毛双马尾</td>
		</tr>
		<tr>
			<td>哈雷</td>
			<td>大胸软萌</td>
		</tr>
		<tr>
			<td>拉瓦锡</td>
			<td>腹黑</td>
		</tr>
	</tbody>
</table>
```



<table>
	<thead>
		<tr>
			<th>妹子</th>
			<th>特征</th>
		</tr>
	</thead>
	<tfoot>
		<tr>
			<th>总体评价</th>
			<th>都是我老婆</th>
		</tr>
	</tfoot>
	<tbody>
		<tr>
			<td>牛顿</td>
			<td>金毛双马尾</td>
		</tr>
		<tr>
			<td>哈雷</td>
			<td>大胸软萌</td>
		</tr>
		<tr>
			<td>拉瓦锡</td>
			<td>腹黑</td>
		</tr>
	</tbody>
</table>

## caption

表示表格的标题

```html
<table>
  <caption>牛顿与苹果树鉴赏表</caption>
	<thead>
		<tr>
			<th>妹子</th>
			<th>特征</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>牛顿</td>
			<td>金毛双马尾</td>
		</tr>
		<tr>
			<td>哈雷</td>
			<td>大胸软萌</td>
		</tr>
		<tr>
			<td>拉瓦锡</td>
			<td>腹黑</td>
		</tr>
	</tbody>
</table>
```

<table>
  <caption>牛顿与苹果树鉴赏表</caption>
	<thead>
		<tr>
			<th>妹子</th>
			<th>特征</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>牛顿</td>
			<td>金毛双马尾</td>
		</tr>
		<tr>
			<td>哈雷</td>
			<td>大胸软萌</td>
		</tr>
		<tr>
			<td>拉瓦锡</td>
			<td>腹黑</td>
		</tr>
	</tbody>
</table>


# 文本

## kbd

用于描述键盘上的按键

```html
<kbd>quit</kbd>
```

<kbd>quit</kbd>


## abbr

用于定义缩写,并且鼠标滞留时还可以有提示

```html
镜5莲华下海了,<abbr title="爷的青春结束了">爷青结</abbr>.
```

镜5莲华下海了,<abbr title="爷的青春结束了">爷青结</abbr>.



## blockquote

```html
blockquote是一个长引用，
<blockquote>
  它里面的内容会根据编译器自动排版，表示一个段落的引用
</blockquote>
```

blockquote是一个长引用，
<blockquote>
  它里面的内容会根据编译器自动排版，表示一个段落的引用
</blockquote>

## cite

```html
<cite>cite语义表示引用，可以表示书名，电影什么的，表现为斜体</cite>
```

<cite>cite语义表示引用，可以表示书名，电影什么的，表现为斜体</cite>

## ruby，rt，rb

```html
ruby用来表示
<ruby>注<rt>zhù</rt></ruby>
<ruby>音<rt>yīn</rt></ruby>。
ruby里面表示要注音的内容，rt里面表示拼音<br>
若浏览器不支持，就需要用rp了，<br>
rp标签在 ruby 注释中使用，以定义不支持 ruby 元素的浏览器所显示的内容。<br>
我是<ruby>注音<rt><rp>(</rp>zhù yīn<rp>)</rp></rt></ruby>
```

ruby用来表示<ruby>注<rt>zhù</rt></ruby><ruby>音<rt>yīn</rt></ruby>。
		ruby里面表示要注音的内容，rt里面表示拼音,若浏览器不支持，就需要用rp了，rp标签在 ruby 注释中使用，以定义不支持 ruby 元素的浏览器所显示的内容。
		我是<ruby>注音<rt><rp>(</rp>zhù yīn<rp>)</rp></rt></ruby>.

## ins，u

```html
<ins>这个表示下划线，填空题经常会看到</ins>
<u>u也有同样的下划线</u>
```

<ins>这个表示下划线，填空题经常会看到</ins>

<u>u也有同样的下划线</u>

## del

```html
<del>del里面的内容会被加入删除线，语义上就是删掉的内容</del>
```

<del>del里面的内容会被加入删除线，语义上就是删掉的内容</del>

## em，i

```html
<em>em语义上表示强调语气，表现为斜体</em>
<i>i一般表示成语，一些关键术语之类的</i>
```

<em>em语义上表示强调语气，表现为斜体</em>

<i>i一般表示成语，一些关键术语之类的</i>

## pre

```html
<pre>
pre 元素可定义预格式化的文本。被包围在 pre 元素中的文本通常会保留空格和换行符。而文本也会呈现为等宽字体。
说白了就是，pre里面怎么写，浏览器就怎么显示，因为一般浏览器会忽略多个回车和空格
int main()
{
	return 0;
}
但是注意标签不能放进去,有的不会显示
</pre>
```

<pre>
pre 元素可定义预格式化的文本。被包围在 pre 元素中的文本通常会保留空格和换行符。而文本也会呈现为等宽字体。
说白了就是，pre里面怎么写，浏览器就怎么显示，因为一般浏览器会忽略多个回车和空格
int main()
{
	return 0;
}
但是注意标签不能放进去,有的不会显示
</pre>

## q

```html
<q>q标签表示短引用，一般语义上表示说话之类的，表现为在标签里面的内容，自动被加了双引号 </q>
<p>比如说，子曰:<q>知之为知之。</q></p>
<p>这个引号并不是HTML加的，所以鼠标也不能选中</p>
```

<q>q标签表示短引用，一般语义上表示说话之类的，表现为在标签里面的内容，自动被加了双引号 </q>

<p>比如说，子曰:<q>知之为知之。</q></p>
<p>这个引号并不是HTML加的，所以鼠标也不能选中</p>

## strong

```html
<strong>strong表示强烈强调，语气上非常激动，表现为黑体</strong>
```

<strong>strong表示强烈强调，语气上非常激动，表现为黑体</strong>

## bdo

可以将文本反向，dir设置rlt就是从右到左，ltr就是从左到右

```html
<bdo dir="rtl">12345</bdo>
```

<bdo dir="rtl">12345</bdo>

## bdi

bdi内的文本可以脱离父元素的文本方向。

```html
<bdo dir="rtl">01234<bdi>56789<bdi></bdo>
<br/>
<bdo dir="rtl">01234<span>56789<span></bdo>
```

第一行首先从右开始，发现是bdi标签，里面的内容脱离父元素的文本方向，然后正常输出56789，之后逆向输出01234

第二行则一直逆向输出。

<bdo dir="rtl">01234<bdi>56789<bdi></bdo>

<bdo dir="rtl">01234<span>56789<span></bdo>

## mark

可以让被mark的文本高亮显示

```html
<p><mark>高亮</mark>显示</p>
```

<p><mark>高亮</mark>显示</p>

## sub

```html
sub表示 <sub>下标</sub>，经常用于x<sub>1</sub>之类的数学符号
```

sub表示 <sub>下标</sub>，经常用于x<sub>1</sub>之类的数学符号

## sup

```html
sup可以用来表示 <sup>上标</sup>,最常见就是y=x<sup>2</sup>
```

sup可以用来表示 <sup>上标</sup>,最常见就是y=x<sup>2</sup>



## progress

超级强大的标签，可以显示进度。

max代表最大值，value代表目前的进度。不用加单位，直接写数字就行了。

```html
<progress value="90" max="100"></progress>
```

<progress value="90" max="100"></progress>

## small

通常用于免责声明、条款等.



# 媒体

## audio

-  src：音乐的相对路径，可以是本地的url也可以是服务器的地址
-  controls：显示播放器
-  autoplay：自动播放，必须加上muted才能自动播放
-  preload：何时进行预加载
   - auto：浏览器自动决定
   - metadata：浏览器不会缓存，但是对于音轨和时长这样的元数据会进行预加载
   - none：不进行预加载，直到用户激活控件
-  muted：设置静音
-  loop：循环播放
-  poster 设置封面图像

```html
<audio src="001.mp3" controls autoplay loop preload="auto">您的浏览器不支持 audio 标签。</audio>
```

<audio src="001.mp3" autoplay controls id ="music">您的浏览器不支持 audio 标签。</audio>



有的格式浏览器并不支持mp3，所以需要使用source标签来匹配多种格式的音源

```html
<audio controls preload="metadata" >
    <source src="./audio/bgm/晨曦.mp3">
    <source src="./audio/bgm/晨曦.ogg">
</audio>
```





## img

- src：图片的相对路径
- alt：如果图片加载失败，就会显示里面的文字

```html
<img src="" alt="加载失败！">
```





# 事件属性

一般都放在body里面。

```html
<body onload="load()">
```



# 自定义属性

在H5中，如果想要设置自定义属性，需要用`data-`开头，而且必须赋值



# 通用属性

- hidden

  让标签隐藏，但是要注意，这个玩意实际上就是display：none

- contenteditable

  让文档可以编辑

- draggable="true"

  让元素可以拖拽





