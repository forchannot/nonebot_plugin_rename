# [nonebot_plugin_rename](https://github.com/forchannot/nonebot_plugin_rename)

通过定时任务更改bot所在群自己的群名片,内置了几种常见的群名片,欢迎**pr**新的群名片!
<!-- TOC -->
* [nonebot_plugin_rename](#nonebotpluginrename)
  * [简介](#简介)
  * [许可](#许可)
  * [安装方法](#安装方法)
  * [安装依赖](#安装依赖)
  * [插件命令](#插件命令)
  * [插件配置项](#插件配置项)
  * [常见问题](#常见问题)
  * [鸣谢](#鸣谢)
<!-- TOC -->

## 简介

通过定时任务更改bot所在群自己的群名片

## 许可

[GPL-3.0](https://github.com/forchannot/genshin_artifact/blob/main/LICENSE)

## 安装方法

打开你nonebot根目录的pyproject.toml文件，找到下列代码中`plugin_dirs =`一项，将本项目git clone(或者直接Download Zip并解压)到该代码指示的目录去，推荐使用git clone

```
[tool.nonebot]
plugins = []
plugin_dirs = ["src/plugins"]
```

## 安装依赖

进入你的机器人所在的虚拟环境，到本项目根目录执行`pip install -r requirements.txt`


## 插件命令

| 命令概述             | 使用方法                                 |
| -------------------- | ---------------------------------------- |
| 设置群名片           | 设置群名片 序号(需空格),序号为空则为删除 |
| 所有群名片列表的图片 | 查看群名片列表                           |
| 查看当前群名片的设置 | 查看当前群名片                           |

## 插件配置项

| 配置项                | 描述           | 类型 |
| --------------------- | -------------- | ---- |
| set_group_card_hour   | 间隔时间(小时) | int  |
| set_group_card_minute | 间隔时间(分钟) | int  |

**请注意不要将二者都设为0!!!!!!**

## 常见问题

Q:启动报错有关`nonebot_plugin_apscheduler`

A：**首先检查依赖**是否安装在你bot的虚拟环境中,随后在你的机器人的`bot.py`文件中`nonebot.load_from_toml("pyproject.toml")`上面增加一行`nonebot.load_plugin("nonebot_plugin_apscheduler")`，使得`nonebot_plugin_apscheduler`先于本插件启动

Q:No module named xxx

A:安装依赖到你的机器人虚拟环境中，见[安装依赖](#安装依赖)



## 鸣谢

[**自动化插件**的群名片修改js版](https://github.com/Nwflower/auto-plugin/tree/master/model/autoGroupName)

[**小派蒙**的获取系统信息](https://github.com/CMHopeSunshine/LittlePaimon/blob/Bot/LittlePaimon/utils/status.py)
