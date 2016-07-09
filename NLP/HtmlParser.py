from urllib import request
from  nltk import word_tokenize
from bs4 import BeautifulSoup
import nltk

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read()
print(html[:60])
raw = BeautifulSoup(html,"html.parser").get_text()
tokens = word_tokenize(raw)
print(tokens)
tokens = tokens[110:400]
text = nltk.Text(tokens)
print(text.concordance('gene'))