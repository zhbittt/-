#!/usr/bin/python
# -*- coding: utf-8 -*-
class UrlManager:
    def __init__(self):
        self.newurls=set()
        self.oldurls=set()
        self.pagelist=set()

    def add_url(self,newurl):
        '''
        添加小说章节的url
        :return:
        '''
        if newurl not in self.oldurls:
            self.newurls.add(newurl)

    def add_urls(self,newurls):
        '''
        添加多个小说章节的url
        :param newurls:
        :return:
        '''
        if len(newurls)==0:return
        for url in newurls:
            self.add_url(url)

    def get_url(self):
        '''
        取出一个小说章节的url
        :return:
        '''
        try:
            url = self.newurls.pop()
            if url is not None:
                self.oldurls.add(url)
                return url
        except KeyError:
            pass


    def has_oldurls(self):
        '''
        返回已爬小说章节的数量
        :return:
        '''
        return len(self.oldurls)





