from nltk.corpus import wordnet as wn

print(wn.synsets('car')[0].lemma_names())
dog = wn.synsets('dog')[0]
print(dog.definition())