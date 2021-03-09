"""
@Time    : 9 Jan, 2018
@Author  : Koukotsukan
"""
import blacklist_comment
import blacklist_damaku
import re
import bvdecoder

if __name__ == "__main__":
    with open("cookies.json", "r") as n:
        cookies = n.read()
        print(cookies)
        choice = input("拉黑评论请输入1，拉黑弹幕请输入2(默认2)：\n")
        if choice == "1":
            bv = input("输入av/bv号：\n")
            if bv.isdigit():
                av = bv
            elif re.search("av", bv):
                av = bv.replace("av", "")
            else:
                av = str(bvdecoder.dec(bv))
            rule = input('请输入正则匹配方法：\n')
            blacklist_comment.collect(av, rule)
        else:
            bv = input("输入av/bv号：\n")
            if bv.isdigit():
                av = "https://www.bilibili.com/video/av" + bv
            elif re.search("av", bv):
                av = "https://www.bilibili.com/video/av" + bv.replace("av", "")
            else:
                av = "https://www.bilibili.com/video/av" + str(bvdecoder.dec(bv))
            rule = input('请输入正则匹配方法：\n')
            blacklist_damaku.collect(av, rule)


            choice = input("拉黑评论请输入1，拉黑弹幕请输入2(默认2)：\n")
            if choice == "1":
                bv = input("输入av/bv号：\n")
                if bv.isdigit():
                    av = bv
                elif re.search("av", bv):
                    av = bv.replace("av", "")
                else:
                    av = str(bvdecoder.dec(bv))
                rule = input('请输入正则匹配方法：\n')
                blacklist_comment.collect(av, rule)
            else:
                bv = input("输入av/bv号：\n")
                if bv.isdigit():
                    av = "https://www.bilibili.com/video/av" + bv
                elif re.search("av", bv):
                    av = "https://www.bilibili.com/video/av" + bv.replace("av", "")
                else:
                    av = "https://www.bilibili.com/video/av" + str(bvdecoder.dec(bv))
                rule = input('请输入正则匹配方法：\n')
                blacklist_damaku.collect(av, rule)

