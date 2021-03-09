"""
@Time    : 9 Jan, 2018
@Author  : Koukotsukan
"""
import requests
import bvdecoder
import re
import xmltodict
import json
import crc32_cracker
import threading
import os

with open('cookies.json', 'r') as f:
    cookie = f.read()
with open('space.txt', 'w') as f:
    f.write("")

black_url = "https://api.bilibili.com/x/dm/filter/user/add"
headers = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}


def collect(av, rules):
    with open("blacklists_danmu.txt", "w")as s:
        s.write("{\"blacklists_danmu\": [")
    cid = requests.get(av)
    danmu_id = re.findall(r'cid=(\d+)&', cid.text)[0]
    print(danmu_id)
    danmu_page = requests.get("https://comment.bilibili.com/" + danmu_id + ".xml")
    danmu_dict = xmltodict.parse(danmu_page.text.replace('"', "'").encode('raw_unicode_escape').decode())
    # print (danmu_page.text.encode('raw_unicode_escape').decode())
    danmu_list = json.dumps(danmu_dict).encode('utf-8').decode('unicode_escape').replace("\\", "")
    # print (danmu_list)
    with open("danmulists.txt", "w", encoding="utf-8") as f:
        f.write(danmu_list)
    try:
        for i in range(0, 9400):
            danmu = json.loads(danmu_list)["i"]["d"][i]["#text"]
            userid = re.findall(".*,.*,.*,.*,.*,.*,(.*),", json.loads(danmu_list)['i']['d'][i]['@p'])[0]
            print(userid, danmu)
            if re.findall(rules, danmu):
                # print (danmu,userid)
                blacklist(userid, danmu)
    except:
        print("结束")
        print("-" * 100)
        with open("blacklists_danmu.txt", "r") as sb:
            r = sb.read()
            new = r.rstrip(',') + "]}"
            with open("blacklists_danmu.txt", "w") as nsb:
                nsb.write(new)
                black_num = new.count('userid')
                black_uid = ""

                n = json.loads(new)
                printer(black_num, n)


def printer(black_num, n):
    Threads = []
    for i in range(black_num):
        t = threading.Thread(target=realname, args=(n['blacklists_danmu'][i],))
        t.start()
        Threads.append(t)
    for t in Threads:
        t.join()
    print("共拉黑" + str(black_num) + "人")
    print("-" * 100)
    viewer = input("是否要查看拉黑用户的主页?是请输入1，默认不是:")
    if viewer == "1":
        try:
            import space_agent
        except:
            print("您可能没有安装ChromeDriver，已为您打印链接")
            with open('space.txt', 'r') as file:
                print(file.read())
            os.system('pause')
    else:
        os.system('pause')


def realname(uid):
    crc32_cracker.create_table()
    realname = crc32_cracker.main(uid['userid'])
    print('已屏蔽用户:"' + uid['userid'] + '",内容:"' + uid['content'] + ',"链接:"https://space.bilibili.com/' + realname + '"')
    with open("space.txt", 'a') as f:
        f.write("https://space.bilibili.com/" + realname + "\n")


def blacklist(data, content):
    send_data = {
        "type": "2",
        "filter": data,
        "jsonp": "jsonp",
        "csrf": "18bf9647ca418e7d1cafcef2b6a02618"
    }
    print(requests.post(black_url, data=send_data, headers=headers).text)

    with open("blacklists_danmu.txt", "a") as f:
        f.write('{"userid":"' + str(data) + '","content":"' + str(content) + '"},')
    # print ("已拉黑用户:\"" + str(data) + "\",弹幕内容:\"" + str(content) + "\"")


if __name__ == "__main__":
    bv = input("输入av/bv号：\n")
    if bv.isdigit():
        av = "https://www.bilibili.com/video/av" + bv
    elif re.search("av", bv):
        av = "https://www.bilibili.com/video/av" + bv.replace("av", "")
    else:
        av = "https://www.bilibili.com/video/av" + str(bvdecoder.dec(bv))
    rule = input('请输入正则匹配方法：\n')
    collect(av, rule)
