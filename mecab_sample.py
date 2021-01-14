import MeCab


tagger = MeCab.Tagger()
tagger.parse('') # this is for avoiding a bug in .parseToNode()

# parsing sentence 
node = tagger.parseToNode('すもももももももものうち')

while node:
    # output .surface is 形態素 .feature is 品詞
    print(node.surface, node.feature)
    node = node.next
