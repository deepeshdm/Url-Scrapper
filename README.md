### Scrapping 500K Urls from Web using Scrapy

Below are the commands to run the spider locally :
```
git clone https://github.com/deepeshdm/Url-Scrapper.git
pip install scrapy
scrapy crawl spider1
```

The spider crawls and finds https urls on the webpage and continues to do so recursively and saves each url inside the "dataset.txt" file. The dataset.txt file in this repo contains about 500k urls scrapped using the same spider. Below are some of it's stats :
```
start_url : "https://www.tensorflow.org/"
total pages scrapped : 8155
total urls obtained : 500420
total time taken : 80 minutes
```
