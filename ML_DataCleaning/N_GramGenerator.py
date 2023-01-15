from collections import defaultdict
import pandas as pd
import datetime as dt
from ML_DataCleaning.DataCleaner import DataCleaner


class N_GramGenerator:
    def __init__(self):
        """
        N_GramGenerator is class to generate ngram from sentence/text and it has also helper functions
        """
        self.dataCleaner = DataCleaner()

    def generate_N_Grams(self, text,ngram=1):
        """
        generate ngrams from given text parameter ngram specified the number of words where the ngram is ex
        parameter =  text,  ngram = lenght of ngram combination
        return array of n_grams from text
        """
        words = self.dataCleaner.stripsentence(text)
        temp=zip(*[words[i:] for i in range(0,ngram)])
        ans=[' '.join(ngram) for ngram in temp]
        return ans


    def getCountOfNgramCombinationsDescOrder(self, dataframe, ngram=1):
        """
        get table of n_gram used combinations in dataset with number of usage's 
        parameter = dataset with column message in it and optional parameter ngram lenght of ngram combination
        return a pandas dataframe with word combination ordered decent highest number first  
        """
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exsist in given dataframe")
        values=defaultdict(int)
        for text in dataframe.message:
              
              for word in self.generate_N_Grams(text, ngram):
                values[word]+=1
        return pd.DataFrame(sorted(values, key=lambda x:x[1],reverse=True))


    def getFiveMostUsedN_GramCombinationsPerHour(self, dataframe):
        """
        get 5 most used Ngram combination's per hour terminates automatic lowest and highest date and get all N_gram combination between in a frequentie from an hour
        parameter= dataset must have a column date and a column message
        returns pandas dataframe with columns date and mostusedcombinationofwords
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exsist in given dataframe")
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='H').strftime('%Y-%m-%dT%H:00:00.000Z')
        NGramDataFrame = pd.DataFrame(columns=['date', 'mostusedcombinationofwords'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z') == iterator)]     
            mostcommoncombinations = self.getCountOfNgramCombinationsDescOrder(oniterator, 3)
            mostusedcombinationofwords = ""
            count = 0 
            if len(mostcommoncombinations) > 0: 
                for commoncombination in mostcommoncombinations[0]:
                    
                    if(count > 0):
                        mostusedcombinationofwords += ":"
                    mostusedcombinationofwords += commoncombination
                    count += 1
                    if(count >= 5):
                        break
            NGramDataFrame.loc [len(NGramDataFrame.date)] = [iterator, mostusedcombinationofwords] 
        return NGramDataFrame


    def getFiveMostUsedN_GramCombinationsPerDay(self, dataframe):
        """
        get 5 most used Ngram combination's per day terminates automatic lowest and highest date and get all N_gram combination between in a frequentie from an day
        parameter= dataset must have a column date and a column message
        returns pandas dataframe with columns date and mostusedcombinationofwords
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'message' not in dataframe.columns:
            raise Exception("column message doesn't exsist in given dataframe")
        
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='d').strftime('%Y-%m-%dT00:00:00.000Z')
        NGramDataFrame = pd.DataFrame(columns=['date', 'mostusedcombinationofwords'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z') == iterator)]     
            mostcommoncombinations = self.getCountOfNgramCombinationsDescOrder(oniterator, 3)
            mostusedcombinationofwords = ""
            count = 0 
            if len(mostcommoncombinations) > 0: 
                for commoncombination in mostcommoncombinations[0]:
                    
                    if(count > 0):
                        mostusedcombinationofwords += ":"
                    mostusedcombinationofwords += commoncombination
                    count += 1
                    if(count >= 5):
                        break
            NGramDataFrame.loc [len(NGramDataFrame.date)] = [iterator, mostusedcombinationofwords] 
        return NGramDataFrame

        