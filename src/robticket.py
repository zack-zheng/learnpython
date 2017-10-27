#!/usr/bin/env python
# encoding=utf-8

from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def getList():
    req = request.Request('')
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    html = request.urlopen(req).read()
    return html

print(getList())