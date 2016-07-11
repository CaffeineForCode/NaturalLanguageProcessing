'''
Project Name : EventExtarction
Created By : mrigankmittal
Date : 7/01/16
Purpose : Extracting useful information from the text using nltk , you can change grammar for other information retrieval
'''

import nltk
from nltk.corpus import stopwords


# Used when tokenizing words
sentence_re = r'(?:(?:[A-Z])(?:.[A-Z])+.?)|(?:\w+(?:-\w+)*)|(?:\$?\d+(?:.\d+)?%?)|(?:...|)(?:[][.,;"\'?():-_`])'

lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.stem.porter.PorterStemmer()

grammar = r"""
    NBAR:
        {<NN.*|JJ>*<NN.*>}# Nouns and Adjectives, terminated with Nouns
        {<CD*>}#Time or date

    NP:
        {<NBAR>}
        {<NBAR><IN><NBAR>}
        # Above, connected with in/of/etc...
"""
chunker = nltk.RegexpParser(grammar)
stopwords = stopwords.words('english')


def leaves(tree):
    """Finds NP (nounphrase) leaf nodes of a chunk tree."""
    for subtree in tree.subtrees(filter = lambda t: t.label()=='NP'):
        yield subtree.leaves()


def normalise(word):
    """Normalises words to lowercase and stems and lemmatizes it."""
    word = word.lower()
    word = stemmer.stem_word(word)
    word = lemmatizer.lemmatize(word)
    return word


def acceptable_word(word):
    """Checks conditions for acceptable word: length, stopword."""
    accepted = bool(2 <= len(word) <= 40 and word.lower() not in stopwords)
    return accepted


def get_terms(tree):
    for leaf in leaves(tree):
        term = [normalise(w) for w,t in leaf if acceptable_word(w) ]
        yield term


def get_noun(text):
    tokens = nltk.regexp_tokenize(text, sentence_re)
    postoks = nltk.tag.pos_tag(tokens)
   # print(postoks) # to print all the generated tokens

    #build POS tree
    tree = chunker.parse(postoks)
    terms = get_terms(tree)

    events = []
    for term in terms:
        np = ""
        for word in term:
            np += word + " "
        if np != "":
            events.append(np.strip())
    return events


if __name__ == '__main__':
    text = """Let's plan to hangout this weekend on Jul 16th at 8pm at TimeSquare NewYork
    and I am going with George for a meeting this Friday to Washington."""
    events=get_noun(text)
    print(events)