# 基本结构与语法

- XML必须有一个根节点，名字什么的可以自定义，但是必须有一个。

```xml
<?xml version = "1.0" encoding = "utf-8"?>
<root>
 <name age = "8">笑美</name>
</root>
```

- 大小写敏感
- 标签必须闭合，不能写一半就不写了。
- 注释还是`<!-- -->`
- 对于一些特殊符号需要使用转义字符 



# 与HTML的区别

1. XML用于传输数据，而HTML用于展示结构
2. XML语法要求严格，而HTML比较宽松
3. XML标签都是自定义的，而HTML标签都是官方提供的

# 不解析内容

```xml
 <msg><![CDATA[这里是不解析的内容]]></msg>
```

# DTD

## 内部DTD

```xml-dtd
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE student[
  <!ELEMENT student (name,age)>
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT age (#PCDATA)>
]>

<student>
 <name>岳盛秦</name>
 <age>20</age>
</student>
```

## 外部DTD

```xml-dtd
<?xml version = "1.0" encoding = "utf-8"?>
<!DOCTYPE student SYSTEM "student.dtd" >

<student>
 <name>岳盛秦</name>
 <age>20</age>
</student>
```

dtd文件

```dtd
<!ELEMENT student (name,age)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT age (#PCDATA)>
```



# 附录——XML转义字符表

| 显示结果 | 描述   | 转义字符 | 十进制  |
| -------- | ------ | -------- | ------- |
|          | 空格   | \&nbsp;  | \&#160; |
| <        | 小于号 | \&lt;    | \&#60;  |
| >        | 大于号 | \&gt;    | \&#62;  |
| &        | 与号   | \&amp;   | \&#38;  |
| "        | 双引号 | \&quot;  | \&#34;  |
| '        | 单引号 | \&apos;  | \&#39;  |
| ×        | 乘号   | \&times; | \&#215; |
| ÷        | 除号   | &divde;  | \&#247; |