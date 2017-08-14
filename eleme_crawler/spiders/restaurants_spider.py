import scrapy
import json
import urllib.parse


class RestaurantsSpider(scrapy.Spider):
    base_url = 'https://www.ele.me/restapi/shopping/restaurants/'

    name = 'restaurants'

    def start_requests(self):
        qs = urllib.parse.urlencode({
            'geohash': 'wtw377jp3gd',
            'latitude': 31.17497,
            'longitude': 121.43883,
            'limit': 1
        })
        url = "{}?{}".format(self.base_url, qs)
        yield scrapy.Request(url)

    def parse(self, response):
        return json.loads(response.body)
