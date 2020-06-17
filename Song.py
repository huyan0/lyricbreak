import json
import jieba
import util
from pypinyin import pinyin, Style

class Song:
    def __init__(self, songName, artistName, lyric):
        self.songName = songName
        self.artistName = artistName
        self.lyric = lyric
        self.phrasePinyinDict = util.lyricToPinYi(self.lyric)

    def getSongName(self):
        return self.songName
    def getArtistName(self):
        return self.artistName
    def getLyric(self):
        return self.lyric
    def getName(self):
        return util.sanitizeName(self.artistName)+"-"+ util.sanitizeName(self.songName)

    def storeToFileSystem(self, filename, append):
        file = open(filename, ("w+","a+")[append],encoding="utf8")
        json.dump(self.__dict__, file, indent=4, ensure_ascii=False)
        file.close()

    def write(self):
        file = open(self.getSongName(), "w+")
        file.write(self.getLyric())
        file.close()
