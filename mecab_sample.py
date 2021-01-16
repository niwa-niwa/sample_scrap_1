import MeCab
import sys

# get argument
arg = sys.argv[1]

tagger = MeCab.Tagger()
tagger.parse('') # this is for avoiding a bug in .parseToNode()

# open the file and convert it as String
text = open(arg, 'r', encoding='UTF-8').read()

print(text)

node = tagger.parseToNode(text)

while node:
    # output .surface is 形態素 .feature is 品詞
    print(node.surface, node.feature)
    node = node.next
