#nlp 
import spacy
from  spacy.lang.nl.stop_words import STOP_WORDS
from spacy.lang.nl import Dutch
nlp = spacy.load("nl_core_news_sm")
parser = Dutch()
from cleantext import clean
import re,string

class DataCleaner:
    def __init__(self):
        """
        Datacleaner is class to clean sentence/text
        """
        self.stopwords = list(STOP_WORDS)

    def stripsentence(self, sentence):
        """
        strip sentence is a function wich remove interpunctie, stopwords, and numbers from text
        """
        #punc 
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~1234567890'''
        #split string in words and punc
        mytokens = parser(sentence)
        #remove punc, numbers and stop words and to lower
        mytokens = [str(word).lower() for word in mytokens if not str(word) in self.stopwords and not str(word) in punc and not str(word).isdigit()]
        return mytokens

    def cleanDataFrame(self, dataframe):
        """
        cleans dataframe message column
        clean pattern
            *  clean all entiteits prefixed with # or @ 
            *  Strip all links / urls
            *  remove RD from read tweet
            *  remove all emoji's

        it remove's not empty cells this can be done with method ......
        parameter dataframe to clean 
        returns same dataframe with cleaned column
        """
        if 'Message' not in dataframe.columns:
            raise Exception("column Message doesn't exist in given dataframe")
        for i in range(len(dataframe)):
            dataframe.loc[i : i, "Message"] = self.strip_all_entities(self.strip_links(self.strip_read_tweet(clean(dataframe.loc[i, "Message"], lower=False, no_emoji=True))))
        return dataframe
 
        
    def strip_links(self, text):
        """
        method to strip links from text 
        parameter text
        return text without links
        """
        link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        links         = re.findall(link_regex, text)
        for link in links:
            text = text.replace(link[0], ', ')    
        return text

    def strip_read_tweet(self, text):
        """
        method to strip RD(read tweet) from text
        parameter text
        return text without RD
        """
        rts = re.findall("\ART", text)
        for rt in rts:
            text = text.replace(rt, '')  
        return text

    def strip_all_entities(self, text):
        """
        method to strip entities from text (@entitie or #entitie)
        parameter text
        return text without entities
        """
        entity_prefixes = ['@','#']
        for separator in  string.punctuation:
            if separator not in entity_prefixes :
                text = text.replace(separator,' ')
        words = []
        for word in text.split():
            word = word.strip()
            if word:
                if word[0] not in entity_prefixes:
                    words.append(word)
        return ' '.join(words)

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

    def dropmissingMessages(self, dataframe):
        """
        functie to remove rows wich contains only spaces or empty cells
        parameter dataframe with column message
        returns dataframe without empty cells and space cells in Message column
        """
        dataframe = dataframe.replace(r'^s*$', float('NaN'), regex = True)  # Replace blanks by NaN
        dataframe.dropna(subset=['Message'], inplace=True)     
        return dataframe
