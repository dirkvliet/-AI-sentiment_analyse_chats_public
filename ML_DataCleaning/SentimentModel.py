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


class SentimentModel:
    def __init__(self):
        """
        SentimentModel is de machinelearning class it has function to create and use machinelearning allgorithme's
        """
        self.dataCleaner = DataCleaner()

    def setupPipeLine(self):
        # Vectorization
        vectorizer = CountVectorizer(tokenizer = my_tokenizer, ngram_range=(1,1)) 
        classifier = LinearSVC()

        # Using Tfidf
        tfvectorizer = TfidfVectorizer(tokenizer = my_tokenizer)

        # Create the  pipeline to clean, tokenize, vectorize, and classify using"Count Vectorizor"              
        self.pipeline = Pipeline([("cleaner", predictors()), ('vectorizer', vectorizer), ('classifier', classifier)])
   
    def trainPipeLine(self, x_train, y_train):
        # Fit our data
        self.pipeline.fit(x_train,y_train)

    def testPipeline(self, x_test):
        return np.array(self.predict(x_test).astype(int))

    def setPipeLineAsModel(self):
        self.model = self.pipeline()

    def loadExsistingModel(self, path):
        self.model = pickle.load(open(path, 'rb'))

    def predictDataFrame(self, df):
        """
        predict dataframe needs a dataframe with column message in it
        """
        x = df['message']
        prediction = self.model.predict(x)
        df = df.assign(prediction=prediction)
        return df

    def saveExsistingModel(self, path):
        pickle.dump(self.model, open(path, 'wb'))

  


