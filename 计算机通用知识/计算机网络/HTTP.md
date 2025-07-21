- HTTP协议规定请求从客户端发出，服务端响应请求并返回。也就是说，请求一定是客户端发出的。

# HTTP报文的结构

## 请求报文



1. 请求行：包括请求方法，URL和HTTP协议版本
2. 请求头：比如Content-Type
3. 空行
4. 请求体

```http
POST /test/test HTTP/1.1
cache-control: no-cache
Content-Security-Policy: script-src 'self' 'unsafe-eval'; object-src 'self';
Content-Type: text/javascript
ETag: "lrbYVvrQm1CeOyeByuRHGi3AuIc="
Last-Modified: Fri, 11 Mar 2022 16:42:11 GMT
```



请求方法：

- GET
- POST
- HEAD：HEAD方法与GET方法相同，但没有响应体，仅传输状态行和标题部分。这对于恢复相应头部编写的元数据非常有用，而无需传输整个内容。

## 响应报文

1. 状态行
2. 响应报文
3. 空行
4. 响应体





状态码

2开头表示成功

3开头表示重定向 304可以使用浏览器缓存

4开头 客户端错误 404服务器拒绝或者找不到资源

5开头 服务端错误 500服务器内部出错



# HTTP无状态

如果服务器记录所有主机的信息，那么数据量太大了，所以HTTP是无状态的，服务器不会记录客户端的信息、

HTTP是无状态的协议，协议对于所有请求和相应不做持久化处理。也就是说每次主机发送的请求服务器都认为是一台新机器发来的。但是诸如购物网站等，需要跳转到新的页面也要继续保持登录状态，所以引入了Cookie技术。

在请求首部加上cookie。

# HTTP2.0多了哪些内容？

- 数据通过二进制传输，不在使用文本形式
- 多路复用，建立连接之后可以一次发送多个HTTP请求
- 压缩头部
- 支持 server push

# HTTP默认80端口



# HTTPS



# HTTP与TCP



- HTTP1.1中，默认TCP为持久连接。
- 如果发送完了，客户端发送`Connection: close`结束TCP连接
