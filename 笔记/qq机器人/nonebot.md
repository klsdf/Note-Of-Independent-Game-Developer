# 定时任务

这个模块需要手动安装

```
nb plugin install nonebot_plugin_apscheduler
```





```python
from nonebot import require
import nonebot

scheduler = require("nonebot_plugin_apscheduler").scheduler

#每隔2s执行一次
@scheduler.scheduled_job("cron",second=f"*/2"  )
async def _():
    (bot,) = nonebot.get_bots().values() 
    await bot.send_private_msg(user_id= 1796655849,message="测试~")
    
# 中午1点执行
@scheduler.scheduled_job("cron", hour="13",minute="00"  )
async def _():
    (bot,) = nonebot.get_bots().values() 
    await bot.send_private_msg(user_id= 1796655849,message="该吃药啦~")

```





获得群聊信息


[根据搜索结果，你可以使用nonebot框架的`get_group_list`方法来获取qq机器人的所有所在群聊](https://zhuanlan.zhihu.com/p/340849952)[1](https://zhuanlan.zhihu.com/p/340849952)[。你需要先导入nonebot模块，然后创建一个机器人实例，最后调用该方法即可](https://zhuanlan.zhihu.com/p/340849952)[1](https://zhuanlan.zhihu.com/p/340849952)。例如：

```python
import nonebot
bot = nonebot.get_bot()
group_list = await bot.get_group_list()
```

[这样，`group_list`就是一个包含了机器人所在群聊信息的列表](https://zhuanlan.zhihu.com/p/340849952)[1](https://zhuanlan.zhihu.com/p/340849952)。你可以对其进行遍历或筛选等操作。






[根据搜索结果，你可以通过判断机器人在群聊中的角色是否是`admin`或`owner`来判断机器人是否是该群聊的管理员](https://q.qq.com/wiki/FAQ/robot/)[1](https://q.qq.com/wiki/FAQ/robot/)[。你可以使用nonebot框架的`get_group_member_info`方法来获取机器人在群聊中的角色](https://zhuanlan.zhihu.com/p/340849952)[2](https://zhuanlan.zhihu.com/p/340849952)。例如：

```python
import nonebot
bot = nonebot.get_bot()
group_id = 123456 # 群聊ID
member_info = await bot.get_group_member_info(group_id=group_id, user_id=bot.self_id)
role = member_info["role"]
if role == "admin" or role == "owner":
    print("机器人是该群聊的管理员")
else:
    print("机器人不是该群聊的管理员")
```

这样，你就可以查看机器人是否是该群聊的管理员了。



根据搜索结果，你可以使用nonebot框架的`on_request`装饰器来监听加群请求事件，并使用`approve`方法来自动审批通过[1](https://github.com/nonebot/nonebot2)。例如：

```python
import nonebot
from nonebot import on_request
from nonebot.adapters.cqhttp import RequestEvent

request = on_request()

@request.handle()
async def handle_request(bot: nonebot.Bot, event: RequestEvent):
    if event.request_type == "group" and event.sub_type == "add":
        # 自动同意加群请求
        await request.approve()
```

这样，机器人就可以自动审批加群请求了。



[根据搜索结果，你可以使用nonebot框架的`on_request`装饰器来监听添加好友请求事件，并使用`approve`方法来自动审批通过](https://github.com/nonebot/nonebot2/issues/176)[1](https://github.com/nonebot/nonebot2/issues/176)。例如：

```python
import nonebot
from nonebot import on_request
from nonebot.adapters.cqhttp import RequestEvent

request = on_request()

@request.handle()
async def handle_request(bot: nonebot.Bot, event: RequestEvent):
    if event.request_type == "friend":
        # 自动同意添加好友请求
        await request.approve()
```

这样，机器人就可以自动审批添加好友请求了。








单人模块

```python
from nonebot import require

import nonebot

  

scheduler = require("nonebot_plugin_apscheduler").scheduler

  

# @scheduler.scheduled_job("cron",second=f"*/2"  )

# async def _():

#     (bot,) = nonebot.get_bots().values()

#     await bot.send_private_msg(user_id= 1796655849,message="测试~")

  

# async def test():

#     (bot,) = nonebot.get_bots().values()

#     await bot.send_private_msg(user_id= 1796655849,message="测试~")

  

# job = scheduler.add_job(test, 'interval', seconds=3)

  
  
  

# 中午1点

@scheduler.scheduled_job("cron", hour=f"13",minute=f"00"  )

async def _():

    (bot,) = nonebot.get_bots().values()

    await bot.send_private_msg(user_id= 1796655849,message="该吃药啦~")

  
  

# 下午3点

@scheduler.scheduled_job("cron", hour=f"15",minute=f"00"  )

async def _():

    (bot,) = nonebot.get_bots().values()

    await bot.send_private_msg(user_id= 1796655849,message="看书一小时！")

  

# 下午4点

  

@scheduler.scheduled_job("cron", hour=f"16",minute=f"00"  )

async def _():

    (bot,) = nonebot.get_bots().values()

    await bot.send_private_msg(user_id= 1796655849,message="锻炼！~")
```