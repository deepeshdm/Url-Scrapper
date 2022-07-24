
# run "scrapy crawl spider1 --nolog" to start spider

import scrapy
from bs4 import BeautifulSoup

class TestSpider(scrapy.Spider):
    
    name = 'spider1'
    start_urls = ['https://www.tensorflow.org/']
    count = 0

    def parse(self, response):
        
        # extract all links from the webpage
        links = response.css("a::attr(href)").extract()
        
        # list of valid urls  
        links = [i for i in links if "https" in i]
        
        print("--------------------------------------")
        print(f"Links Obtained : {len(links)}")
        self.count = self.count + len(links)
        print("COUNT : ", self.count)
        print("--------------------------------------")
        
        if links is not None:
            for link in links:
                # save link into text file
                f = open("dataset.text", "a")
                f.write(link + '\n')
                f.close()
                # schedule the link for crawling
                yield response.follow(link, callback=self.parse)
        
