import re
from pypinyin import pinyin,Style
from log import logger
import jieba
from Word import Word
def sanitizeName(str):
    pattern = r"[\/\\\:\*\?\"\<\>\|]"
    return re.sub(pattern, "_", str)

def toPinYin(word):
    result = pinyin(word, style=Style.FINALS_TONE3,errors="ignore")
    return result

def lyricToPinYi(lyric):
    wordList = []
    slicedLyric = jieba.cut_for_search(lyric,HMM=True)
    for phrase in slicedLyric:
        #wordList.append((Word(phrase, pinyin(phrase, style=Style.FINALS_TONE3,errors="ignore"))).__dict__)
        wordList.append(phrase)
    return wordList

def validateUrl(str):
    pattern = r"^https://mojim.com/cn.+\.htm"
    if not re.compile(pattern).match(str):
        logger.error("Invalid URL")
        return False
    return True
