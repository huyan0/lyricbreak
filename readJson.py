import json
import jieba
from util import toPinYin
# cannot set 'w+' here because open will overwrite the original file
io = open('lyrics/周杰伦-三年二班(Vcd).json', encoding="utf8")
a = json.load(io)
l = jieba.cut_for_search(a['lyric'],HMM=True)

print(toPinYin(l))
