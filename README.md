<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://ghproxy.com/https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://ghproxy.com/https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-rename

_✨ 通过定时任务更改bot所在群自己的群名片,内置了几种常见的群名片并且初步支持了多bot,欢迎**pr**新的群名片! ✨_

<a href="https://raw.githubusercontent.com/nonebot/nonebot2/master/LICENSE">
    <img src="https://img.shields.io/github/license/forchannot/nonebot_plugin_rename" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-rename">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-rename.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-yellow.svg" alt="python">

</div>

<!-- TOC -->
* [nonebot-plugin-rename](#nonebot-plugin-rename)
  * [📖简介](#简介)
  * [🔐许可](#许可)
  * [💿 安装方法](#-安装方法)
  * [🏷️插件命令](#插件命令)
  * [⚙️插件配置项](#插件配置项)
  * [🎉目前已实现的群名片功能](#目前已实现的群名片功能)
  * [🧐PR需知](#pr需知)
  * [🔥鸣谢](#鸣谢)
<!-- TOC -->

## 📖简介

通过定时任务更改bot(s)所在群自己的群名片

## 🔐许可

[MIT](https://github.com/forchannot/nonebot-plugin-rename/blob/main/LICENSE)

## 💿 安装方法

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-rename
</details>

<details>
<summary>pip</summary>

    pip install nonebot-plugin-rename

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_rename"]

```
[tool.nonebot]
plugins = []
plugin_dirs = ["src/plugins"]
```
</details>



## 🏷️插件命令

| 使用方法       | 命令概述                             |
|------------|----------------------------------|
| 设置群名片 序号   | 设置群名片 序号(需空格，可带多个序号)             |
| 查看群名片列表    | 查看当前支持的所有群名片列表的图片                |
| 查看当前群名片    | 查看当前群名片的设置                       |
| 立即更改群名片 序号 | 立即更改当前群组bot名片，后面仅可跟一个序号（bot无返回值） |
| 删除群名片      | 删除当前群组群名片                        |
| 设置所有群名片    | 为当前机器人所在所有群设置群名片，仅限超管私聊          |

## ⚙️插件配置项

| 配置项                           | 描述                  | 类型   |
|-------------------------------|---------------------|------|
| set_group_card_hour           | 间隔时间(小时)            | int  |
| set_group_card_minute         | 间隔时间(分钟)            | int  |
| use_nickname_front            | 是否在群名片前加上bot名称      | bool |
| self_name                     | 自定义前缀(需开启上一个配置)     | str  |
| is_one_bot_set_all_group_card | 是否允许与bot会话可以设置所有群名片 | bool |

**请注意不要将两个间隔时间都设为0!!!!!!**

**由于qq群名片特殊性,间隔太短可能意义并不大反而容易导致风控,建议在30分钟以上**

## 🎉目前已实现的群名片功能
<details>
<summary>一图流</summary>
<img src="https://cdn.staticaly.com/gh/forchannot/mypicgo@main/20230418/image.1l16rm6rtbkw.jpg" alt="help">
</details>

<details>
<summary>时间</summary>
<pre>
-- 高考时间
-- 原神版本剩余时间
-- 北京时间
-- 古代计时制时间
</pre>
</details>

<details>
<summary>热搜</summary>
<pre>
-- B站热搜
-- 微博热搜
-- 抖音热搜
-- 百度热搜
-- 知乎热搜
-- 今日头条热搜
</pre>
</details>

<details>
<summary>一言</summary>
<pre>
-- 每日(次)一言
</pre>
</details>

<details>
<summary>系统状态</summary>
<pre>
-- 系统内存和cpu信息
-- Bot收发消息汇总
</pre>
</details>

## 🧐PR需知

**PS:由于本人代码比较烂,很多方法实现都比较复杂,所以对pr不是很友好,如果有更好的方法欢迎pr并指正**

**群名片的生成代码**在/card/文件夹内,每种群名片(或者每类)对应一个文件

当新增一个新的群名片样式时,需要在**以下几个地方**进行修改相应代码使得其生效

* 在`/card/__init__.py`内导入你的包
* 在`/utils/card_name.py`内的`card_list`按照格式新增你的文件名和对应的描述以及导包


## 🔥鸣谢

[**自动化插件**的群名片修改js版](https://github.com/Nwflower/auto-plugin/tree/master/model/autoGroupName)

[**小派蒙**的获取系统信息](https://github.com/CMHopeSunshine/LittlePaimon/blob/Bot/LittlePaimon/utils/status.py)
