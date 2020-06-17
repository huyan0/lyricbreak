from bs4 import BeautifulSoup
import requests
from hanziconv import HanziConv
from Song import Song
from Page import Page
from log import errorLogger
import os
class SongParser:
    def __init__(self, url):
        self.url = url
        try:
            res = requests.get(url, timeout=3)
            self.page = BeautifulSoup(res.text,"html.parser")
            self.timeout = False
        except requests.exceptions.RequestException as e:
            errorLogger.exception(f"Error handling web page:{self.url}" + " -- request timeout")
            self.page = BeautifulSoup(open("emptyPage.html",encoding="utf8"),"html.parser")
            self.timeout = True
        self.isSong = url.startswith("https://mojim.com/cny")
        if self.isSong:
            try:
                text = self.page.find(id="fsZx1")
                texts = text.prettify().split("\n")
                # store processed and filtered lyric
                filtered = []
                for s in texts:
                    s =s.strip()
                    if(s == "<ol>"):
                        break
                    if not s.startswith("<") and s.find("：") == -1 and s.find("※") == -1 and not s.startswith("["):
                        filtered.append(s)

                self.artistName = HanziConv.toSimplified(filtered.pop(0))
                self.songName = HanziConv.toSimplified(filtered.pop(0))
                s = ""
                for t in filtered:
                    s = s + t + os.linesep
                # return a string representation of the lyric. each line is separated by
                # \n
                self.lyric = HanziConv.toSimplified(s)
            except:
                self.isSong = False
                errorLogger.exception(f"Error handling web page:{self.url}\n\t{self.page.text}")

        self.relatedPages = self.relatedSongs()

    def createModelObject(self):
        if self.isSong:
            return Song(self.songName, self.artistName, self.lyric)
        else:
            return Page()

    def getRelatedPages(self):
        return self.relatedPages

    def relatedSongs(self):
        resourcePath = "/" + self.url.split("//")[1].split("/")[1]
        baseUrl = self.url.split("//")[0] + "//" + self.url.split("//")[1].split("/")[0]

        b = self.page
        temp = b.find_all('a')

        pages = []
        for s in temp:
            if s.prettify().find("href=\"/cny") != -1 and s.prettify().find("9999.htm") == -1 and s.get("href") != resourcePath or s.prettify().find("href=\"/cnh") != -1 or s.prettify().find("href=\"/cnza") != -1 or s.prettify().find("href=\"/cnzb") != -1 or s.prettify().find("href=\"/cnzc") != -1 or s.prettify().find("href=\"/cnzlha") != -1 or s.prettify().find("href=\"/cnzlhb") != -1 or s.prettify().find("href=\"/cnzlhc") != -1: 
                pages.append(baseUrl + s.get("href"))
        return pages
