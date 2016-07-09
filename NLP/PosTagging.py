import nltk
import json
import nltk.tag, nltk.chunk
rawtext = open("info.txt").read()
sentences = nltk.sent_tokenize(rawtext) # NLTK default sentence segmenter
sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
sentences = [nltk.tag.pos_tag(sent) for sent in sentences] # NLTK POS tagger
print (sentences)
pattern = 'NP: {<DT>?<JJ>*<NN>}' # define a tag pattern of an NP chunk
NPChunker = nltk.RegexpParser(pattern) # create a chunk parser
result = NPChunker.parse(sentences[0]) # parse the example sentence
print (result.draw())