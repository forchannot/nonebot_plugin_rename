# [nonebot_plugin_rename](https://github.com/forchannot/nonebot_plugin_rename)

通过定时任务更改bot所在群自己的群名片,内置了几种常见的群名片并且初步支持了多bot,欢迎**pr**新的群名片!
<!-- TOC -->
* [nonebot_plugin_rename](#nonebotpluginrename)
  * [简介](#简介)
  * [许可](#许可)
  * [安装方法](#安装方法)
  * [安装依赖](#安装依赖)
  * [插件命令](#插件命令)
  * [插件配置项](#插件配置项)
  * [目前已实现的群名片功能](#目前已实现的群名片功能)
  * [PR需知](#pr需知)
  * [常见问题](#常见问题)
  * [鸣谢](#鸣谢)
  <!-- TOC -->
## 简介

通过定时任务更改bot(s)所在群自己的群名片

## 许可

[GPL-3.0](https://github.com/forchannot/genshin_artifact/blob/main/LICENSE)

## 安装方法

打开你nonebot根目录的pyproject.toml文件，找到下列代码中`plugin_dirs =`一项，将本项目git clone(推荐)或者直接Download Zip并解压)到该代码指示的目录去，推荐使用git clone

```
[tool.nonebot]
plugins = []
plugin_dirs = ["src/plugins"]
```

## 安装依赖

进入你的机器人所在的虚拟环境，到本项目根目录执行`pip install -r requirements.txt`


## 插件命令

| 使用方法       | 命令概述                             |
|------------|----------------------------------|
| 设置群名片 序号   | 设置群名片 序号(需空格，可带多个序号)             |
| 查看群名片列表    | 查看当前支持的所有群名片列表的图片                |
| 查看当前群名片    | 查看当前群名片的设置                       |
| 立即更改群名片 序号 | 立即更改当前群组bot名片，后面仅可跟一个序号（bot无返回值） |
| 删除群名片      | 删除当前群组群名片                        |

## 插件配置项

| 配置项                   | 描述              | 类型   |
|-----------------------|-----------------|------|
| set_group_card_hour   | 间隔时间(小时)        | int  |
| set_group_card_minute | 间隔时间(分钟)        | int  |
| use_nickname_front    | 是否在群名片前加上bot名称  | bool |
| self_name             | 自定义前缀(需开启上一个配置) | str  |

**请注意不要将两个间隔时间都设为0!!!!!!**

**由于qq群名片特殊性,间隔太短可能意义并不大反而容易导致风控,建议在30分钟以上**

## 目前已实现的群名片功能
<details>
<summary>一图流</summary>
<img src="https://ghproxy.com/https://raw.githubusercontent.com/forchannot/nonebot_plugin_rename/main/img/img.png" alt="help">
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

## PR需知

**PS:由于本人代码比较烂,很多方法实现都比较复杂,所以对pr不是很友好,如果有更好的方法欢迎pr并指正**

**群名片的生成代码**在/card/文件夹内,每种群名片(或者每类)对应一个文件

当新增一个新的群名片样式时,需要在**以下几个地方**进行修改相应代码使得其生效

* `/utils/card_name.py`内的`name_of_card`和`card_name_list`两个变量按照格式新增你的文件名和对应的描述


## 常见问题

Q:No module named xxx

A:安装依赖到你的机器人虚拟环境中，见[安装依赖](#安装依赖)

Q: Any Bug?

A: 欢迎提issue(Pr)



## 鸣谢

[**自动化插件**的群名片修改js版](https://github.com/Nwflower/auto-plugin/tree/master/model/autoGroupName)

[**小派蒙**的获取系统信息](https://github.com/CMHopeSunshine/LittlePaimon/blob/Bot/LittlePaimon/utils/status.py)
