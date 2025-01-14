from locations.storefinders.storemapper import StoremapperSpider


class GuessAUSpider(StoremapperSpider):
    name = "guess_au"
    item_attributes = {"brand": "Guess", "brand_wikidata": "Q2470307"}
    key = "7404"

    def parse_item(self, item, location):
        item.pop("email")
        item.pop("website")
        yield item
