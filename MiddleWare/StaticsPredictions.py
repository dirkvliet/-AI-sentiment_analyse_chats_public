import pandas as pd
import json
import datetime as dt
from ML_DataCleaning.DataCleaner import DataCleaner
from ML_DataCleaning.N_GramGenerator import N_GramGenerator

class StaticsPrediction:
    def __init__(self):
        """
        static Prediction is class to generate statics from predicted data
        """
        self.N_GramGenerator =  N_GramGenerator()
    
    def sentimentPredictionPerDay(self, dataframe):
        """
        get table per day the messagecount, negatiefcount, neutralcount, positiefcount, 5 mostusedwordcombinations as list
        parameter= dataset must have a column date, Prediction, en Message 
        returns pandas dataframe 
        |   date                | messagecount  | negatief_count  |  neutral_count  |  positief_count | mostusedwordcombinations
        --------------------------------------------------------------------------------------------------------------------------
        | 25-09-2022T00:00.0000 | 45            | 6               | 10              | 15              | [test testen, test testen]
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'Prediction' not in dataframe.columns:
            raise Exception("column Prediction doesn't exsist in given dataframe")
        
        if 'Message' not in dataframe.columns:
            raise Exception("column Message doesn't exsist in given dataframe")
        
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='d').strftime('%Y-%m-%dT00:00:00.000Z')
        StaticsDataFrame = pd.DataFrame(columns=['date', 'messagecount', 'negatief_count', 'neutral_count', 'positief_count', 'mostusedwordcombinations'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z') == iterator)]     
            d1 = oniterator["Message"]
            d2 = oniterator[(oniterator["Predicted"]==1)]
            d3 = oniterator[(oniterator["Predicted"]==2)]
            d4 = oniterator[(oniterator["Predicted"]==3)]
            mostcommoncombinations = self.N_GramGenerator.getCountOfNgramCombinationsDescOrder(oniterator, 1, 3)
            mostusedcombinationofwords = list()
            count = 0 
            if len(mostcommoncombinations) > 0: 
                for commoncombination in mostcommoncombinations[0]:
                    mostusedcombinationofwords.append(commoncombination)
                    count += 1
                    if(count >= 5):
                        break
                    
            data = [pd.to_datetime(oniterator['date']).dt.strftime('%Y-%m-%dT00:00.0000').iloc[0], len(d1), len(d2), len(d3), len(d4), mostusedcombinationofwords]   
            StaticsDataFrame.loc[len(StaticsDataFrame.date)] = data
        return StaticsDataFrame

    def sentimentPredictionPerHour(self, dataframe):
        """
        get table per hour the messagecount, negatiefcount, neutralcount, positiefcount, mostusedwordcombinations
        parameter= dataset must have a column date, Prediction, en Message 
        returns pandas dataframe 
        |         date          | messagecount  | negatief_count  |  neutral_count  |  positief_count | mostusedwordcombinations
        -------------------------------------------------------------------------------------------------------------
        | 25-09-2022T20:00.0000 | 45            | 6               | 10              | 15              | [test testen, test testen]
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'Prediction' not in dataframe.columns:
            raise Exception("column Prediction doesn't exsist in given dataframe")
        
        if 'Message' not in dataframe.columns:
            raise Exception("column Message doesn't exsist in given dataframe")
        
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='d').strftime('%Y-%m-%dT%H:00:00.000Z')
        StaticsDataFrame = pd.DataFrame(columns=['date', 'messagecount', 'negatief_count', 'neutral_count', 'positief_count', 'mostusedwordcombinations'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z') == iterator)]     
            d1 = oniterator["Message"]
            d2 = oniterator[(oniterator["Predicted"]==1)]
            d3 = oniterator[(oniterator["Predicted"]==2)]
            d4 = oniterator[(oniterator["Predicted"]==3)]
            mostcommoncombinations = self.N_GramGenerator.getCountOfNgramCombinationsDescOrder(oniterator, 1, 3)
            mostusedcombinationofwords = list()
            count = 0 
            if len(mostcommoncombinations) > 0: 
                for commoncombination in mostcommoncombinations[0]:
                    mostusedcombinationofwords.append(commoncombination)
                    count += 1
                    if(count >= 5):
                        break
                    
            data = [pd.to_datetime(oniterator['date']).dt.strftime('%Y-%m-%dT%H:00.0000').iloc[0], len(d1), len(d2), len(d3), len(d4), mostusedcombinationofwords]   
            StaticsDataFrame.loc[len(StaticsDataFrame.date)] = data
        return StaticsDataFrame


    def getMessageCountPerHour(self, dataframe):
        """
        get table per hour the messagecount
        parameter= dataset must have a column date en Message 
        returns pandas dataframe 
        |         date          | messagecount  | 
        ----------------------------------------
        | 25-09-2022T20:00.0000 | 45            |
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'Message' not in dataframe.columns:
            raise Exception("column Message doesn't exsist in given dataframe")
        
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='d').strftime('%Y-%m-%dT%H:00:00.000Z')
        StaticsDataFrame = pd.DataFrame(columns=['date', 'messagecount'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT%H:00:00.000Z') == iterator)]     
            d1 = oniterator["Message"]
           
            data = [iterator.replace('Z', ''), len(d1)]   
            StaticsDataFrame.loc[len(StaticsDataFrame.date)] = data
        return StaticsDataFrame


    def getMessageCountPerDay(self, dataframe):
        """
        get table per day the messagecount
        parameter= dataset must have a column date en Message 
        returns pandas dataframe 
        |         date          | messagecount  | 
        ----------------------------------------
        | 25-09-2022T00:00.0000 | 45            |
        """
        if 'date' not in dataframe.columns:
            raise Exception("column date doesn't exsist in given dataframe")
        
        if 'Message' not in dataframe.columns:
            raise Exception("column Message doesn't exsist in given dataframe")
        
        
        lowestDate = min(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))
        higestDate = max(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z'))

        time_range =  pd.date_range(lowestDate, higestDate, freq='d').strftime('%Y-%m-%dT00:00:00.000Z')
        StaticsDataFrame = pd.DataFrame(columns=['date', 'messagecount'])

        for iterator in time_range:
            #print(iterator)
            oniterator = dataframe[(pd.to_datetime(dataframe['date']).dt.strftime('%Y-%m-%dT00:00:00.000Z') == iterator)]     
            d1 = oniterator["Message"]
           
            data = [pd.to_datetime(oniterator['date']).dt.strftime('%Y-%m-%d').iloc[0], len(d1)]   
            StaticsDataFrame.loc[len(StaticsDataFrame.date)] = data
        return StaticsDataFrame
  
    def calculatePercentage(self, numberOfRows, TotalRows):
        """
        calculate percentage rows t.o.v total rows
        parameter numberofrows, totalrows
        returns calculated percentage of rows from the total rows
        """
        return ((numberOfRows / TotalRows) * 100)

