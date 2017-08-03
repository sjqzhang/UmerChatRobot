# coding:utf-8


import sys
from pyltp import *
from nltk.parse import *

reload(sys)
sys.setdefaultencoding("utf-8")

sents = "游泳是一种很好的锻炼方式"
print "原文："
print sents
seg_model = "/home/singing/ltp_data_v3.4.0/cws.model"
pos_model = "/home/singing/ltp_data_v3.4.0/pos.model"
par_model = "/home/singing/ltp_data_v3.4.0/parser.model"

seg = Segmentor()
pos = Postagger()
par = Parser()

pos.load(pos_model)
seg.load(seg_model)
par.load(par_model)

# 分词
words = seg.segment(sents)
print "分词结果："
print "/ ".join(words)
# 词性标注
postags = pos.postag(words)

print "词性标注:"
for i,j  in zip(words,postags):
    print i + "(" + j +")",

# 句法解析
arcs = par.parse(words, postags)
length =len(arcs)
conll = ""
for i in xrange(length):
    if arcs[i].head == 0:
        arcs[i].relation = "ROOT"
    conll += "\t" + words[i]+ "(" +postags[i] + ")" +"\t" +postags[i] + "\t" \
        + str(arcs[i].head) + "\t" + arcs[i].relation + "\n"

conlltree = DependencyGraph(conll)
tree = conlltree.tree()
tree.draw()
