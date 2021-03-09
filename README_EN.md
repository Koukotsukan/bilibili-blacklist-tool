# bilibili-blacklist-tool
![GitHub license](https://img.shields.io/github/license/Koukotsukan/bilibili-blacklist-tool?style=flat-square)
### A tool to help you quickly blacklist users with relevant keywords or pop-ups, with a counter-checking UID function
![中文版](./README.md)
#### Attention! This project was completed several years ago, and there are serious problems with its structure. As of March 2021, the core functionality works fine, but there are inevitably strange bugs and performance wastes

## Usage requires
+ python3
  + dependency packages 
    + requests
    + re
    + xmltodict
    + json
    + threading
    + time
    + selenium (optional)
    + os (optional)

## Function
+ find related damaku sender's UID
+ One-click access to the bilibili homepage of all related damaku senders
+ One-click to blacklist senders of keyworded damaku
+ One-click to blacklist senders of keyworded comments

## Features to be updated
- [ ] Multi-threading
- [ ] Cookie-free login

## User's guide
0. Download this project and its dependencies to the local directory (![tutorial](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
1. Open and login to ![bilibili](https://www.bilibili.com) and get your own cookie via ![Browser Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)
2. Copy the full cookie value into the ``cookies.json`` file of this project (you can use notepad to open it)
3. Run ``main.py``

## Disclaimers
I am not affiliated with bilibili, B站 or 哔哩哔哩
