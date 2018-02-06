#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
class Htmldown:
    def  down_page(self,url):
        '''
        下载网页内容
        '''
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
        r=requests.get(url,headers=headers)
        r.encoding='utf8'
        if r.status_code==200:
            return r.text



