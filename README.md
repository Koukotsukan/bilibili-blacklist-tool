# bilibili-blacklist-tool
![GitHub license](https://img.shields.io/github/license/Koukotsukan/bilibili-blacklist-tool?style=flat-square)
### 一个帮助你快速拉黑含有相关关键词或弹幕的用户的工具，兼备反查弹幕UID功能
[English Version](./README_EN.md)
#### 注意！此代码完成于数年前，其代码结构存在严重问题。截止至2021年3月，其核心功能正常使用，但难免会出现奇怪的bug和性能浪费

## 使用需要：
+ python3
  + 依赖包 
    + requests
    + re
    + xmltodict
    + json
    + threading
    + time
    + selenium(可选)
    + os(可选)

## 功能：
+ 反查弹幕发送者UID
+ 一键访问所有弹幕发送者的bilibili主页
+ 一键拉黑含有关键词的弹幕的发送者
+ 一键拉黑含有关键词的评论的发送者

## 待更新功能：
- [ ] 多线程
- [ ] 免cookie登录

## 使用指南：
0. 下载本项目及其依赖到本地目录中（[教程](https://docs.github.com/cn/github/creating-cloning-and-archiving-repositories/cloning-a-repository)）
1. 打开并登录[bilibili](https://www.bilibili.com)，通过[浏览器开发者工具](https://developer.mozilla.org/zh-CN/docs/Tools)，获取自己的cookie
2. 将cookie的值完整复制到本项目的``cookies.json``文件中（使用notepad打开即可）
3. 运行``main.py``

## 免责声明：
本人与上海幻电信息科技有限公司及旗下"bilibili"、"哔哩哔哩"、"b站"无关
