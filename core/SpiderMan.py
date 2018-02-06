#!/usr/bin/python
# -*- coding: utf-8 -*-
from gevent import spawn,monkey,joinall;monkey.patch_all()
from concurrent.futures import ThreadPoolExecutor

from core.UrlManager import UrlManager
from core.Htmldown import Htmldown
from core.Htmlparser import Htmlparser
# from core.DataOutput import DataOutput

class SpiderMan:
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=Htmldown()
        self.parser=Htmlparser()
        # self.output=DataOutput()

    def index_work(self):
        '''
        爬取凌霄主页
        '''
        url = 'http://www.lingxiaozhishang.com'
        self.manager.oldurls.add(url)
        html_dict = self.downloader.down_page(url)
        if html_dict is None:
            # raise print("爬取主页出错了")
            print("爬取主页出错了")
            return None

        new_urls = self.parser.parser_index(html_dict["text"],url)
        self.manager.add_urls(new_urls)
        print("爬取 主页 + 所有文章url 完成")


    def async(self):
        '''
        开启协程
        '''
        self.index_work()
        pool = ThreadPoolExecutor(10)
        while True:
            url = self.manager.get_url()
            if url is None:
                break
            pool.submit(self.downloader.down_page,url).add_done_callback(self.parser.parser_page)
        pool.shutdown(wait=True)
        print("完了-----------------------")

