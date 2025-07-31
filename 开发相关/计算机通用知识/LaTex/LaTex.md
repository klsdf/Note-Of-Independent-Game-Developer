# LATEX

 本书并非指导你如何成为一个专业LaTeX 程序员，或者排版方面的专家，

 本书仅限于写学术类笔记，或者排版对格式没有严格要求的论文。

 本书目的在于让0基础的人能迅速熟练使用LaTeX ，并且直接复制书里的代码使用。

 本书不会有过多理论讲解，你直接用就对了，以实用方便为最终目标。 

# 基本知识

虽然LaTex功能强大,但是它本身非常笨重,学习起来也并不是非常轻松,要说记笔记首选的还是markdown,但是对于一些专业性的文章或者对样式要求严格的学术书籍,LaTex绝对是不二之选.

## 发展史

## 基本结构

在学习理论之前,我们首先来看看LaTex的基本结构

```latex
\documentclass{ctexart}
\title{标题}
\author{作者}
\date{日期}
\begin{document}
  \maketitle
  \tableofcontents
  hello world
\end{document}
```

虽然此时你并不能理解每一项的含义,不过你应该基本上能明白LaTex的语法了.

LaTex文章的内容从`\begin{document}`开始,在`\end{document}`结束,前面可以进行别的设定.详细的请看**文档**那一章节.



## 常用控制台命令

​		texdoc相关

-  调用符号大全

  ```shell
  texdoc symbols  
  ```

-   调出class和package编写指南

  ```shell
  texdoc  clsguide 
  ```


# 文档设置

## 文档类型

latex有四种文档类型,分别为

1. article:支持part，section，subsection 等，但没有 chapter，可以有摘要，摘要紧接标题头位于第一页上。
2. report:可以有 part，chapter，section，subsection 等，也有摘要，且摘要位于单独一页上，有页码。
3. book:可以有 part，chapter，section，subsection 等，但没有摘要。
4. beamer:做PPT用的

但是很麻烦的一点就是这四个标准文档类型都不支持中文,为了让广大中国同志们也能使用,官方又出了四个的中文文档类.分别对应上面的四个标准文档类.

1. ctexart
2. ctexrep
3. ctexbook
4. ctexbeamer

我们在使用这些文档类的时候,只需要引用即可.

```latex
\documentclass{ctexart}

\documentclass{ctexrep}

\documentclass{ctexbook}

\documentclass{ctexbeamer}
```

## 支持中文文档

我们选用的ctexart自带中文支持,但是如果你选用的其他文档类型不支持中文,记得引用宏包.有的时候,中文文档可能会导致bug,只能添加宏包.

```latex
\usepackage{ctex}
```

## 文档标题

这个是用来写你文章标题的,只有写了这个你才能编辑标题内容否则不显示.

```latex
\maketitle
```
下面这个就是标题的具体内容,很简单,一目了然
```latex
\title{标题}
\author{作者}
\date{日期}
```

## 文档摘要

因为摘要一般都是在标题下面的,所以请把代码放在`\maketitle`后面.

```latex
\begin{abstract}
该部分内容是放置摘要信息的。
\end{abstract}
```

## 目录

只要加了这句就有目录了,放在`\begin{document}`之前就行

```latex
\tableofcontents
```



# 文档内容

## 标准文档结构

latex分为多级标题,可以用代码简单设置,编译器会自动帮你排序,很方便.但是要注意,下面这些并不是所有文档类型都支持的,使用前建议查看一下当前文档类支持哪些标题.

```latex
\part{部分}
\chapter{章节}
\section{一级标题}
\subsection{二级标题} 
\subsubsection{三级标题}
\paragraph{段落}
\subparagraph{子段落}
```

这个标题默认居中,如果不想居中可以设置左对齐,同样的,记住有关设置的都要放在`\begin{document}`之前.

```latex
%section左对齐
\ctexset{
section = {
    format = \raggedright\Large\bfseries,
    }
}
```

## 自定义文档结构

虽然latex给的默认结构已经足够多了,但是个别情况下还是存在不够用的情况,比如说想要四级标题和五级标题.那么就得自己自定义了.

**注意!!!!!本语法不支持中文文档,请使用英文文档,之后再加入ctex宏包.**

```latex
\documentclass{book}
\usepackage{ctex}
```



```latex
%请在\begin{document}之前把下面的代码粘过去

%使用宏包expl3
\usepackage{expl3}

\makeatletter
\renewcommand\subparagraph{
  \@startsection{subparagraph}{5}{\z@}
    {-3.25ex \@plus1ex \@minus .2ex}
    {1em}
    {\normalfont\normalsize\bfseries}}

\ExplSyntaxOn
\int_new:N \l_sec_offset_int
\newcommand\setXsecOffset[1]{ \int_set:Nn \l_sec_offset_int {#1} }
\newcommand\addXsecOffset[1]{ \int_add:Nn \l_sec_offset_int {#1} }

\newcommand\xsection[1]{
  \xsection:x { \int_eval:n {#1 + \l_sec_offset_int} }
}

\cs_new:Nn \xsection:n
  {
    \int_case:nnF {#1}
      {
        {-1}{\part}
        {0}{\chapter}
        {1}{\section}
        {2}{\subsection}
        {3}{\subsubsection}
        {4}{\paragraph}
        {5}{\subparagraph}
      }
      {
        \int_compare:nTF {#1 <= \l_sec_maxdp_int}
          {
            \@startsection{xsec #1}{#1}{\z@}
              {-3.25ex \@plus1ex \@minus .2ex}
              {1em}
              {\normalfont\normalsize\bfseries}
          }
          {
            \PackageError{PATCH}{Too~ deep~ sectioning~ command~ used.}{}
          }
      }
  }
\cs_generate_variant:Nn \xsection:n {x}

\int_new:N \l_sec_maxdp_int
\int_set:Nn \l_sec_maxdp_int {5}

\newcommand\extendSectionLevelTo[1]{
  \int_step_inline:nnn {\l_sec_maxdp_int + 1} {#1}
    {
      \newcounter{xsec ##1}
      \int_compare:nTF {##1 = \l_sec_maxdp_int + 1}
        { \counterwithin{xsec ##1}{subparagraph} }
        { \counterwithin{xsec ##1}{xsec \int_eval:n{##1 - 1}} }
      \@namedef{xsec ##1 mark}{\@gobble}
    }
  \int_set:Nn \l_sec_maxdp_int {#1}
  \setcounter{secnumdepth}{#1}
}
\ExplSyntaxOff
\makeatother
```

下面的使用方法:

```latex
\begin{document}
%自己添加最大标题数量
\extendSectionLevelTo{10}

\part{部分}
\chapter{章节}
\section{一级标题}
\subsection{二级标题} 
\subsubsection{三级标题}
\paragraph{段落}
\subparagraph{子段落}

\xsection{6}{title}
\xsection{7}{title}
\xsection{8}{title}
\xsection{9}{title}
\xsection{10}{title}

%重置标题深度
\addXsecOffset{1}
\xsection{1}{title}
\xsection{2}{title}

\setXsecOffset{0}
\xsection{1}{title}
\xsection{2}{title}
\end{document}
```



# 文字

# 列表


## 无序列表

```latex
%需要添加宏包：
\usepackage{enumerate}

\begin{itemize}
	\item 无序列表内容
\end{itemize}
```

## 有序列表

```latex
%需要添加宏包：
\usepackage{enumerate}

\begin{enumerate}[i)]
	\item 12345.
\end{enumerate}
```

# 代码块

```latex
\begin{lstlisting}[language={tex}]
\end{lstlisting}
```

## 常见语言



# 图片

```latex
\begin{figure}[ht]
\centering
\includegraphics[scale=缩放因子]{图片的名字}
\caption{对图片的描述}
\label{fig:图片的引用名}
%注意图片要放在tex同目录下。
```

# 表格
