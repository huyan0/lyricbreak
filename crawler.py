from SongParser import SongParser
from log import logger
import time
from util import lyricToPinYi
import jieba
import json
import time
from Song import Song
class Crawler:
    def __init__(self, url, maximum):
        self.crawledPages = []
        self.maximum = maximum
        self.url = url
        self.repeatedCrawl = 0
        self.totalUrlInspected = 0
        self.starTime = time.time()
        self.time = time
        self.queue = []
        self.songs = 0
    def hasCrawled(self, url):
        return url in self.crawledPages

    def start(self):
        self.totalUrlInspected +=1
        self.queue.append(self.url)
        self.crawlSongs()
        self.finishParsing()

    def crawlSongs(self):
        while len(self.queue) > 0 and len(self.crawledPages) < self.maximum:
            startUrl = self.queue.pop(int(len(self.queue)/2))
            if len(self.crawledPages) < self.maximum and not self.hasCrawled(startUrl):
                logger.info(f"Crawling page: {startUrl}")
                p1 = SongParser(startUrl)
                s = p1.createModelObject()
                s.storeToFileSystem("lyrics/" + s.getName() + ".json", False)
                if p1.timeout == False:
                    self.crawledPages.append(startUrl)
                    if s.__class__.__name__ == "Song":
                        self.songs+=1
                    for p in p1.getRelatedPages():
                        if not self.hasCrawled(p) and p not in self.queue:
                            self.totalUrlInspected +=1
                            self.queue.append(p)
                else:
                    logger.error("Page timeout: " + startUrl + "\n waiting for connection...")
                    time.sleep(5);
                    self.queue.append(startUrl)
            elif self.hasCrawled(startUrl):
                logger.info(f"Encoutered parsed page: {startUrl}")
                self.repeatedCrawl+=1

    def finishParsing(self):
        l = len(self.crawledPages)
        time = self.time.time() - self.starTime
        logger.info(f"Crawling finished\nTotal Pages Parsed: {l}\nSongs Found: {self.songs}\nRepeated Crawl:{self.repeatedCrawl}\nTotal URL Inspected: {self.totalUrlInspected}\nRun time: {time}")
