#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import sys
import shutil
import re
import chardet

convertfiletypes = [
  ".xml",
  ".lua",
  ".csd",
  ".py",
  ".html"
  ]

def check_need_convert(filename):
    return filename.endswith(".html")

total_cnt = 0
success_cnt = 0
unkown_cnt = 0
def convert_encoding_to_utf_8(filename):
    print(filename)
    global total_cnt,success_cnt,unkown_cnt
    # Backup the origin file.

    # convert file from the source encoding to target encoding
    content = codecs.open(filename, 'r', encoding='gb2312').read()
    text = content.encode('utf-8')
    if text == "":
        return
    codecs.open(filename, 'w', encoding='UTF-8').write(text.decode('utf-8'))

def convert_dir(root_dir):
    if os.path.exists(root_dir) == False:
        print("[error] dir:",root_dir,"do not exit")
        return
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if check_need_convert(f):
                filename = os.path.join(root, f)
                try:
                    convert_encoding_to_utf_8(filename)
                except Exception as err:
                    print(err)
    print("finish total:",total_cnt,"success:",success_cnt,"unkown_cnt",unkown_cnt)

if __name__ == '__main__':
    convert_dir("./")