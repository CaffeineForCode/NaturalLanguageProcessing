import nltk
from nltk.corpus import words
puzzle_letter = nltk.FreqDist('mrigank')
obligatory = 'r'
wordlist = words.words()
print ([w for w in wordlist if len(w) >= 7
    and obligatory in w
    and nltk.FreqDist(w) <= puzzle_letter])
