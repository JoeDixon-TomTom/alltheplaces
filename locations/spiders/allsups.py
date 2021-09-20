# -*- coding: utf-8 -*-
import json
import re

import scrapy

from locations.items import GeojsonPointItem
from locations.hours import OpeningHours


class AllsupsSpider(scrapy.Spider):
    name = "allsups"
    allowed_domains = ["allsups.com"]
    start_urls = [
        'https://allsups.com/wp-json/acf/v3/business_locations?_embed&per_page=1000',
    ]

    def parse(self, response):
        stores = json.loads(response.body_as_unicode())

        for store in stores:
            properties = {
                'ref': store["acf"]["internal_store_code"],
                'name': store["acf"]["business_name"],
                'addr_full': store["acf"]["address_line_1"],
                'city': store["acf"]["city"],
                'state': store["acf"]["state"],
                'postcode': store["acf"]["postal_code"],
                'country': store["acf"]["country"],
                'lat': store["acf"]["latitude"],
                'lon': store["acf"]["longitude"],
                'phone': store["acf"]["primary_phone"]
            }

            yield GeojsonPointItem(**properties)