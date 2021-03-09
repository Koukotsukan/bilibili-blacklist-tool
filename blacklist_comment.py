"""
@Time    : 7 Jan, 2018
@Author  : Koukotsukan
"""
import requests
from time import sleep
import json
import bvdecoder
import re
import os

with open('cookies.json', 'r') as f:
    cookie = f.read()

black_url = "https://api.bilibili.com/x/relation/modify"
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}


def collect(av, rules):
    with open("blacklists.txt", "w") as f:
        f.write("{\"blacklists\": [")
    try:
        for n in range(1, 9400):
            url = "https://api.bilibili.com/x/v2/reply?type=1&oid=" + av + "&pn=" + str(n)
            print("第" + str(n) + "页")
            reply = requests.get(url, headers=headers)
            reply.raise_for_status()
            content = reply.text
            s = json.loads(content)
            for i in range(20):
                comment = s['data']['replies'][i]
                if re.findall(rules, comment['content']['message']):
                    print("第" + str(i) + "个")
                    keys = re.findall(rules, comment['content']['message'])
                    username = comment['member']['uname']
                    mid = comment['member']['mid']
                    content = comment['content']['message']
                    with open("blacklists.txt", "a") as f:
                        f.write(
                            "{\"username\":\"" + str(username).replace("\n", "'") + "\",\"mid\":\"" + str(mid).replace(
                                "\n", "") + "\",\"content\":\"" + str(content).replace("\n",
                                                                                       "") + "\",\"keywords\":\"" + str(
                                keys).replace("\n", "") + "\"},")
                    print(username, mid, content, keys)
            if n % 20 == 0:
                sleep(5)
    except:
        print("已到达最后一页")
        confirm = input('确认拉黑以上用户吗?(确认请输入yes)：\n')
        with open("blacklists.txt", "r") as refile:
            r = refile.read()
            new = r.rstrip(',') + "]}"
            with open("blacklists.txt", "w") as newfile:
                newfile.write(new)
                black_num = new.count("username")
                s = json.loads(new)
                if confirm == "yes":
                    for i in range(black_num):
                        black_mid = s['blacklists'][i]['mid']
                        un = s['blacklists'][i]['username']
                        blacklist(black_mid, un)
                    os.system('pause')
                else:
                    print("任务取消")
                    os.system('pause')


def blacklist(data, username):
    print(username, data)
    form_data = {
        "fid": data,
        "act": "5",
        "re_src": "11",
        "jsnp": "jsnp",
        "csrf": "18bf9647ca418e7d1cafcef2b6a02618"
    }
    go = requests.post(black_url, headers=headers, data=form_data)
    print("拉黑状态:" + go.json()['message'])


if __name__ == "__main__":
    bv = input("输入av/bv号：\n")
    if bv.isdigit():
        av = bv
    elif re.search("av", bv):
        av = bv.replace("av", "")
    else:
        av = str(bvdecoder.dec(bv))
    rule = input('请输入正则匹配方法：\n')
    collect(av, rule)
