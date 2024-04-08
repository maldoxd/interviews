# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        def increase_quality(item, increment=1):
            item.quality = min(item.quality + increment, 50)

        def decrease_sell_in(item):
            item.sell_in -= 1

        for item in self.items:
            #Handled exceptions first and leave the loop early
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            if item.name == "Aged Brie":
                increase_quality(item)
                decrease_sell_in(item)
                if item.sell_in < 0:
                    increase_quality(item)
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                increment = 3 if item.sell_in < 6 else 2 if item.sell_in < 11 else 1
                increase_quality(item, increment)
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality = 0
                continue

            #added degradationFactor before perfoming changes to quality
            degradationFactor = -2 if item.name == "Conjured Mana Cake" else -1
            if item.sell_in <= 0: #double the degradation factor after sell_in date
                degradationFactor *= 2
            item.quality = max(item.quality + degradationFactor, 0)
            item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
