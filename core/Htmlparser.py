#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

class Htmlparser:

    def parser_index(self,html_conf,url):
        soup = BeautifulSoup(html_conf, 'html.parser')

        list_a = soup.find(class_="chapterlist").find_all('a')
        new_urls=[]
        for a in list_a:
            #url=http://www.lingxiaozhishang.com
            #/book/439.html
            new_url ="%s%s"%(url,a.attrs["href"])
            new_urls.append(new_url)
        return new_urls


    def parser_page(self,html_conf):
        '''
        解析小说章节页面
        :param html_conf:
        :return:
        '''
        html_conf =html_conf.result()["text"]
        soup=BeautifulSoup(html_conf,'html.parser')
        title = soup.find('h1').get_text()
        text = soup.find(id="BookText").get_text()

        filepath = "F:\Python_project\Article\db\%s.txt"%title
        with open(filepath,"w") as f:
            f.write(text)


