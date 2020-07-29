# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.com/Digital-Music-Last-30-Days/s?rh=n%3A163856011%2Cp_n_date_first_available_prime%3A8456645011']

    def parse(self, response):
        # store instance of AmazontutorialItem class
        items = AmazontutorialItem()
        
        # .get() SAME AS .extract_first()
        # .getall() SAME AS .extract()
        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_musician = response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()
        
        for n,m,i in zip(product_name, product_musician, product_imagelink):
            items['product_name'] = n
            items['product_musician'] = m
            items['product_imagelink'] = i
   
            yield items
        
        str_next_page = response.css("li.a-last a::attr(href)").get()
        
        next_page = 'https://www.amazon.com/Digital-Music-Last-30-Days/s?i=digital-music&rh=n%3A163856011%2Cp_n_date_first_available_prime%3A8456645011&page=' + str(AmazonSpiderSpider.page_number) + '&qid=1585249905&ref=sr_pg_1' 
        # QuoteSpider.page_number is a class variable
        if str_next_page is not None:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse) 
    
# we can bypass user restrictions with user agents AND proxies (can combine into hybrid method)
# this is a commit btw
