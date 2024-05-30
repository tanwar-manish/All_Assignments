import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.kotsovolos.gr"]
    start_urls = ["http://www.kotsovolos.gr/"]

    headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }

    custom_settings = {
    'DOWNLOAD_DELAY': 4
    }


    def parse(self, response):
        data = response.json()['catalogEntryView']
        for i in data:
            uniqueid = i["uniqueID"]
            name = i["name"]
            url = i["UserData"][0]['seo_url']
            price = i["price_EUR"]

            yield{'UniqueID': uniqueid,
                'Name' : name,
                'URL' : url,
                'Price' : price        
                }
