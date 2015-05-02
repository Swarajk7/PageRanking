# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
import scrapy
from nitrkl.items import NitrklItem
from scrapy.utils.url import urljoin_rfc
from scrapy.utils.response import get_base_url
import urlparse

class NitrklSpiderSpider(CrawlSpider):
    name = "nitrkl_spider"
    allowed_domains = ["cet.edu.in"]
    start_urls = (
        'http://www.cet.edu.in/',
    )
    rules = (
        Rule(SgmlLinkExtractor(deny = ('mondaymorning','ethesis','alumni'),allow=('')),callback='parse_items',follow=True),)
     
    def parse_items(self, response):
        a = response.url
        '''filename = a.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        links=response.xpath('//a')
        baseurl = get_base_url(response)
        print baseurl
        zz=''
        for link in links:
            args = link.xpath('@href').extract()
            obj = NitrklItem()
            obj['sourceurl']=a
            for arg in args:
                url=arg
                if ":" not in arg: url = urljoin_rfc(baseurl, arg.strip())
                obj['link']=url
                yield obj
            #print 'Link number %d points to url %s' % args
