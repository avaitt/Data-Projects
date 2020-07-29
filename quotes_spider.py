# -*- coding: utf-8 -*-
#I MADE ANOTHER COMMIT HERE
"""
Created on Mon Mar 23 13:14:57 2020

@author: Adhvaith Vijay
"""

import scrapy
from ..items import QuotetutorialItem


# =============================================================================
# # inherit from scrapy.Spider
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = ['http://quotes.toscrape.com/']
#     
#     # self reference (we want to reference instance inside the class), and response (source code of website we want to scrape)
#     def parse(self, response):
#         
#         # instance variable 
#         items = QuotetutorialItem()
#         
#         '''
#         # get ONLY the text NOT <title>
#         # css selector
#         # a selector is simply a condition (css selectors AND xpath selectors)
#         title = response.css('title::text').extract() # go to the source code and look for title tag and extract
#         
#         yield {'titletext': title} # return and shows the title tag as a dictionary 
#         '''
#         
#         # output information one block at a time
#         
#         all_div_quotes = response.css('div.quote') # this is a list so we can extract 
#         
#         for quotes in all_div_quotes:
#             title = quotes.css(".text::text").extract()
#             author = quotes.css(".author::text").extract()
#             tag = quotes.css(".tag::text").extract()
#             
#             
#             # used the blueprint of the class to ensure the title, author, and class are stored in proper containers
#             # NEXT STEP: storing scraped data in a JSON/CSV/XML file etc.
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#             
#             yield items
#             # goes to pipelines.py file 
# =============================================================================

# =============================================================================
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = ['http://quotes.toscrape.com/']
#   
#     def parse(self, response):
#     
#         items = QuotetutorialItem()
#      
#         all_div_quotes = response.css('div.quote') # this is a list so we can extract 
#        
#         for quotes in all_div_quotes:
#             title = quotes.css(".text::text").extract()
#             author = quotes.css(".author::text").extract()
#             tag = quotes.css(".tag::text").extract()
#         
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#             
#             yield items
#             
#         
#         # value of the 2nd page
#         # get the attribute of href (i.e. /page/2/)
#         next_page = response.css("li.next a::attr(href)").get() # .get() gets VALUE of Next
#         
#         if next_page is not None: # if Next page value is empty
#             # go to the next_page and go back to parse and scrape all quotes from that page (recursive)
#             # callback = self.parse moves us back to def parse
#             yield response.follow(next_page, callback = self.parse) 
# =============================================================================
            
# =============================================================================
# # Scraping Websites with Pagination (like with Amazon)
# class QuoteSpider(scrapy.Spider):
#     name = 'quotes'
#     start_urls = ['http://quotes.toscrape.com/page/1/']
#     page_number = 2
# 
#     def parse(self, response):
#         
#         items = QuotetutorialItem()
#         all_div_quotes = response.css('div.quote') 
#         for quotes in all_div_quotes:
#             title = quotes.css(".text::text").extract()
#             author = quotes.css(".author::text").extract()
#             tag = quotes.css(".tag::text").extract()
#         
#             items['title'] = title
#             items['author'] = author
#             items['tag'] = tag
#             
#             
#             yield items
#             
#         str_next_page = response.css("li.next a::attr(href)").get()
#         
#         next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
#         # QuoteSpider.page_number is a class variable
#         if str_next_page is not None:
#             QuoteSpider.page_number += 1
#             yield response.follow(next_page, callback = self.parse) 
# =============================================================================

# Logging in with Scrappy FormRequest
# Log in -> Scrape data from EACH page -> store

# from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/login']
    page_number = 2
    
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        
        # from_response takes 3 parameters (response, formdata, what do we do after logging in?)
        return FormRequest.from_response(response, formdata = {
                'csrf_token' : token,
                'username' : 'adhvaith.vijay@gmail.com',
                'password' : 'helloworld'
        }, callback = self.start_scraping)
   
    def start_scraping(self, response):
        # open_in_browser(response)
        
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote') 
        for quotes in all_div_quotes:
            title = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
        
            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            
            yield items
            
        str_next_page = response.css("li.next a::attr(href)").get()
        
        next_page = 'http://quotes.toscrape.com/page/' + str(QuoteSpider.page_number) + '/'
        
        if str_next_page is not None:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback = self.start_scraping) 
            


     
# STORE SCRAPED DATA IN A FILE
# scrapy crawl quotes -o items.json    
# scrapy crawl quotes -o items.xml
# scrapy crawl quotes -o items.csv
            
            
# TO RUN CODE
# scrapy crawl quotes 
    
# STEPS FOR EXTRACTING DATA WITH TERMINAL
# (base) C:\Users\Acer>cd .spyder-py3
# (base) C:\Users\Acer\.spyder-py3>cd ScrapyTutorial
# (base) C:\Users\Acer\.spyder-py3\ScrapyTutorial>virtualenv .
# (base) C:\Users\Acer\.spyder-py3\ScrapyTutorial>.\Scripts\activate
# (ScrapyTutorial) (base) C:\Users\Acer\.spyder-py3\ScrapyTutorial>scrapy shell "https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011"

# XPATH
# response.xpath("//title/text()").extract()
# response.xpath("//span[@class='text']/text()").extract()
# response.xpath("//span[@class='text']/text()")[1].extract()
# if using single quotes outside use double inside and vice versa
        
# CSS w/ XPATH
# response.css("li.next a").xpath("@href").extract() 
# In order to crawl all href tags on a webpage:
# response.css("a").xpath("@href").extract()
        
# CSS
# shell controls scrapy in command prompt mode and RUN CODE w/o compiler
# response.css("title::text").extract_first() 
# response.css("span.text::text").extract()
# Use SelectorGadget tool
