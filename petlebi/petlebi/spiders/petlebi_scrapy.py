
from typing import Any
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, Response

# Define a Scrapy spider for crawling pet-related product information from petlebi.com
class PetspiderSpider(CrawlSpider):
    name = "petspider"  # Unique identifier for the spider
    allowed_domains = ["www.petlebi.com"]  # Restrict crawl to this domain
    start_urls = ["https://www.petlebi.com/"]  # Initial URL to start crawling from
    
    # Parses the start URL and schedules requests for each category and page number
    def parse_start_url(self, response):
        categories = ['kedi', 'kopek', 'kus', 'kemirgen']  # Define product categories to scrape
        
        # Loop through each category and page, generating URLs to follow
        for category in categories:
            for i in range(1, 105):  # Iterate through page numbers (up to max page number)
                yield response.follow(f'https://www.petlebi.com/{category}-petshop-urunleri?page={str(i)}', callback=self.parse_product)

    # Parses product listing pages and schedules requests to product detail pages
    def parse_product(self, response):
        products = response.css('div.search-product-box ')  # Select all product boxes in the page
        
        # Extract product URLs and schedule parsing of product details
        for product in products:
            product_url = product.css('a').attrib['href'],
            url_str = ''.join(map(str, product_url))  # Convert tuple to string
            yield response.follow(url_str, callback=self.parse_productdetail)

    # Parses the product detail page and extracts product information
    def parse_productdetail(self, response):
        # Extract and yield product details including name, URL, category, price, etc.
        yield{
            'name': response.css('h1.product-h1::text').get(),
            'product_url': response.url,
            'product_category': response.xpath('/html/body/div[3]/div[1]/div/div/div[1]/ol/li[3]/a/span//text()').get(),
            'price': response.css('span.new-price::text').get(),
            'brand': response.xpath('//*[@id="hakkinda"]/div[1]/div[2]/span/a//text()').get(),
            'SKT': response.xpath('//*[@id="hakkinda"]/div[4]/div[2]//text()').get(),
            'Barkod': response.xpath('//*[@id="hakkinda"]/div[3]/div[2]//text()').get(),
            'Description': str(response.xpath('//*[@id="productDescription"]//text()').extract()).replace("\n", '').replace('\n', ''),
            'image': response.css('a#photoGallery.MagicZoom').attrib['href'],  
        }
