# API

## 发送私聊消息

`send_private_msg`



**参数**

| 字段名        | 数据类型 | 默认值  | 说明                                                         |
| ------------- | -------- | ------- | ------------------------------------------------------------ |
| `user_id`     | int64    | -       | 对方 QQ 号                                                   |
| `group_id`    | int64    | -       | 主动发起临时会话时的来源群号(可选, 机器人本身必须是管理员/群主) |
| `message`     | message  | -       | 要发送的内容                                                 |
| `auto_escape` | boolean  | `false` | 消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 `message` 字段是字符串时有效 |



**响应数据**

| 字段名       | 数据类型 | 说明    |
| ------------ | -------- | ------- |
| `message_id` | int32    | 消息 ID |





```python
## 私聊
from nonebot.adapters.onebot.v11 import Message,GroupMessageEvent,MessageSegment,Bot
test  =  on_keyword({"测试"},rule=_checkerInGroup)
@test.handle()
async def _(bot :Bot):
    await bot.send_private_msg(user_id= 1796655849,message="test")

```

## 发送群消息

终结点：`/send_group_msg`

**参数**

| 字段名        | 数据类型 | 默认值  | 说明                                                         |
| ------------- | -------- | ------- | ------------------------------------------------------------ |
| `group_id`    | int64    | -       | 群号                                                         |
| `message`     | message  | -       | 要发送的内容                                                 |
| `auto_escape` | boolean  | `false` | 消息内容是否作为纯文本发送 ( 即不解析 CQ 码 ) , 只在 `message` 字段是字符串时有效 |

**响应数据**

| 字段名       | 数据类型 | 说明    |
| ------------ | -------- | ------- |
| `message_id` | int32    | 消息 ID |



```python
bot.send_group_msg(group_id=529245311,message=今日知识["释义"])
```







## 发送合并转发 ( 群 )

终结点: `/send_group_forward_msg`

**参数**

| 字段       | 类型           | 说明                                                         |
| ---------- | -------------- | ------------------------------------------------------------ |
| `group_id` | int64          | 群号                                                         |
| `messages` | forward node[] | 自定义转发消息, 具体看 [CQcodeopen in new window](https://docs.go-cqhttp.org/cqcode/#合并转发消息节点) |

**响应数据**

| 字段名       | 数据类型 | 说明        |
| ------------ | -------- | ----------- |
| `message_id` | int64    | 消息 ID     |
| `forward_id` | string   | 转发消息 ID |







## 群组单人禁言

终结点：`/set_group_ban`

**参数**

| 字段名     | 数据类型 | 默认值    | 说明                             |
| ---------- | -------- | --------- | -------------------------------- |
| `group_id` | int64    | -         | 群号                             |
| `user_id`  | int64    | -         | 要禁言的 QQ 号                   |
| `duration` | number   | `30 * 60` | 禁言时长, 单位秒, 0 表示取消禁言 |



该 API 无响应数据



```python
test  =  on_fullmatch({"禁言测试"},rule=_checkerInGroup)
@test.handle()
async def _(bot :Bot):
    await bot.set_group_ban(group_id=529245311,user_id=2265910938,duration=30*60)


test  =  on_fullmatch({"禁言解除"},rule=_checkerInGroup)
@test.handle()
async def _(bot :Bot):

    await bot.set_group_ban(group_id=529245311,user_id=2265910938,duration=0*60)
```







## 设置群名

终结点：`/set_group_name`

**参数**

| 字段名       | 数据类型 | 说明   |
| ------------ | -------- | ------ |
| `group_id`   | int64    | 群号   |
| `group_name` | string   | 新群名 |

提示

该 API 无响应数据



```python
word = on_fullmatch ({"设置群名称"},rule=_checkerInGroup)
@word.handle()
async def _(event:GroupMessageEvent,bot:Bot):
    await bot.set_group_name(group_id=361574391,group_name= "莲华同好会")
    await word.finish(Message("好滴~"))
```





## 设置群组专属头衔

终结点：`/set_group_special_title`

**参数**

| 字段名          | 数据类型 | 默认值 | 说明                                                         |
| --------------- | -------- | ------ | ------------------------------------------------------------ |
| `group_id`      | int64    | -      | 群号                                                         |
| `user_id`       | int64    | -      | 要设置的 QQ 号                                               |
| `special_title` | string   | 空     | 专属头衔, 不填或空字符串表示删除专属头衔                     |
| `duration`      | number   | `-1`   | 专属头衔有效期, 单位秒, -1 表示永久, 不过此项似乎没有效果, 可能是只有某些特殊的时间长度有效, 有待测试 |

提示

该 API 无响应数据



```python

```







## 群打卡

终结点：`/send_group_sign`

| 字段名     | 数据类型 | 说明 |
| ---------- | -------- | ---- |
| `group_id` | int64    | 群号 |



> **提示**
>
> 该 API 无响应数据



```python
test  =  on_fullmatch({"打卡测试"},rule=_checkerInGroup)
@test.handle()
async def _(bot :Bot):

    await bot.send_group_sign(group_id=529245311)
```









# CQ 码 / CQ Code

## QQ表情

```
[CQ:face,id=123]
```



## 语音

```
[CQ:record,file=http://baidu.com/1.mp3]
```





## 视频

> go-cqhttp-v0.9.38 起开始支持发送，需要依赖ffmpeg



```
[CQ:video,file=http://baidu.com/1.mp4]
```





## @某人

```
[CQ:at,qq=10001000]
[CQ:at,qq=123,name=不在群的QQ]
[CQ:at,qq=all]
```

当qq找不到人时，会搜索群中的name





## 链接分享

（有问题）

```
[CQ:share,url=https://hat-soft.top/,title=帽子社]
```



## 音乐分享

```
[CQ:music,type=163,id=1809485951]
```

type可以取值：qq` `163` `xm，分别表示使用 QQ 音乐、网易云音乐、虾米音乐。

id代表音乐id

```python
 await test.finish(Message(f"[CQ:music,type=163,id=1809485951]"))
```

