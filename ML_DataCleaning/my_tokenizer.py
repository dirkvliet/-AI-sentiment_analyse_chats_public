import spacy
from  spacy.lang.nl.stop_words import STOP_WORDS
from spacy.lang.nl import Dutch

nlp = spacy.load("nl_core_news_sm")
parser = Dutch()
stopwords = list(STOP_WORDS)

def my_tokenizer(sentence):
    """
    functie to remove interpunctie, numbers, stopwords and set words to lower
    parameter sentence/text
    returns array of words
    """
    #interpunctie tekens
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~1234567890'''
    #split string in words and tekens
    mytokens = parser(sentence)
    #remove interpunctie tekens en stop words and to lower
    mytokens = [str(word).lower() for word in mytokens if not str(word) in stopwords and not str(word) in punc]
    return mytokens
