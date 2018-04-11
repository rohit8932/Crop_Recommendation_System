# -*- coding: utf-8 -*-
import os
from os.path import join
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import nltk

class NaiveBayes():
    data = []
    records = []
    def  __init__(self):
        dataset_path = join(settings.STATIC_ROOT,'dataset.csv')
# =============================================================================
#         current_dir_path=os.path.dirname(os.path.realpath(__file__))
#         print("Current directory :: ",current_dir_path)
#         dataset_path = os.path.join(current_dir_path,"dataset.csv")
# =============================================================================
        print("Current dataset path :: ",dataset_path)
        with open(dataset_path  ) as pf:
            for record in pf:
                line = record.split(",")
                line_total = len(line)
                current_record = ""
                counter=0
                for current in line[:line_total-1]:
                    current_record += current
                    if counter != (line_total-2):
                         current_record +=","
                         
                    counter += 1
# =============================================================================
#                 print("Create line :: ",current_record)    
#                 print("TOTAL RECORD IN LINE :: ",line_total)
# =============================================================================
                self.data.append((current_record,line[len(line)-1]))
# =============================================================================
#                 print("Class Label :: ",line[len(line)-1])
# =============================================================================
                
        for (words,class_label) in self.data:
            words_filtered = [e for e in words.split(",") if len(e)>=3]
            self.records.append((words_filtered,class_label))
        
    def get_words_in_records(self,records):
        all_words = []
        for (words, sentiment) in records:
            all_words.extend(words)
        return all_words

    def get_word_features(self,wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features 
    
    def extract_features(self,document):
        document_words = set(document)
        features = {}
        for word in document_words:
            features['contains(%s)' % word] = (word in document_words)
        return features

    
    def run_naive_bayes_algorithm(self,test_records):
        #word_features = self.get_word_features(self.get_words_in_tweets(self.records))
        training_set = nltk.classify.apply_features(self.extract_features, self.records)
        classifier = nltk.NaiveBayesClassifier.train(training_set)
        result = classifier.classify(self.extract_features(test_records.split(",")))
# =============================================================================
#         print("Result :: ",result)
# =============================================================================
        return result
    
     
if __name__=="__main__":
    nave_bayes = NaiveBayes() 
    #TEST DATASET---------------------------------==>class label
    #Laterite soil,20,5.5,1.7,0.5,0.3,25,0.06,15,18==>potato
    #Deep black soil,100,7.7,1.5,1.9,0.3,35,0.26,1.3,44==>Soyabean
    result=nave_bayes.run_naive_bayes_algorithm("Deep black soil,100,7.7,1.5,1.9,0.3,35,0.26,1.3,44")
    print("Result :: ",result)
        