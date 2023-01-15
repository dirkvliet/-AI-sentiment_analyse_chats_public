from ML_DataCleaning.DataCleaner import DataCleaner
import numpy as np 
import pickle

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer 
from sklearn.base import TransformerMixin 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from ML_DataCleaning.Predictors import predictors
from ML_DataCleaning.my_tokenizer import my_tokenizer

import spacy
import time
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('nl_core_news_lg')
nlp.add_pipe('spacytextblob')


class NerModel:
    def __init__(self):
        """
        NerModel is de machinelearning class it has function to used complete spacy models to do named entity reconition
        """

    def getlocations(self, dataframe):
        """
        function to get locations geografisch locations from messages in dataframe 
        parameter dataframe with a least a column message
        return array with locations unsorted and unidentified
        """
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exist in given dataframe")

        docs = [nlp(headline) for headline in dataframe['message']]

        locations = []
        for doc in docs:      
            for ent in doc.ents:
                if ent.label_ in ["LOC", "GPE"]:
                    locations.append(str(ent.text).lower())
        return locations

        
    def getentities(self, dataframe):
        """
        function to get entities person and organisations from messages in dataframe 
        parameter dataframe with a least a column message
        return array with entities unsorted and unidentified
        """
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exist in given dataframe")

        docs = [nlp(headline) for headline in dataframe['message']]

        entities = []
        for doc in docs:      
            for ent in doc.ents:
                if ent.label_ in ["PERSON", "ORG"]:
                    entities.append(str(ent.text).lower())
        return entities


    def getverbs(self, dataframe):
        """
        function to get verbs from messages in dataframe 
        parameter dataframe with a least a column message
        return array with verbs unsorted and unidentified
        """
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exist in given dataframe")

        docs = [nlp(headline) for headline in dataframe['message']]

        verbs = []
        for doc in docs:      
            for token in doc:
                if(token.pos_ == 'VERB'):
                    verbs.append(str(token).lower())
        return verbs
   
  


