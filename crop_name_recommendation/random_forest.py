from sklearn.ensemble import RandomForestClassifier
import os
from os.path import join
from django.conf import settings
import pandas as pd
import numpy as np

class RandomForest():
    
    dataset_path=""
    dataset=None
    
    def dataset_headers(self,dataset):
        """
        To get the dataset header names
        :param dataset: loaded dataset into pandas DataFrame
        :return: list of header names
        """
        return list(dataset.columns.values)
    
    def __init__(self):
        self.dataset_path = join(settings.STATIC_ROOT,'dataset.csv')
    
    def runRandomForestAlgo(self,testData):
        self.dataset = pd.read_csv(self.dataset_path)
        training_features = ['Soil Type', 'Soil depth(cm)', 'ph', 'Bulk density Gm/cc', 'Ec (dsm-1)', 'Organic carbon (%)', 'Soil moisture retention  (%)', 'Available water capacity(m/m)', ' Infiltration rate cm/hr', ' Clay %']
        
        target=' Crops to be taken'
        #ENCODE STRING DATA INTO INTEGER
        soil_type=np.unique(self.dataset['Soil Type'])
        soil_type_mapping={label:idx for idx,label in enumerate(soil_type)}
        
        self.dataset['Soil Type']=self.dataset['Soil Type'].map(soil_type_mapping)
        crops_to_be_taken = np.unique(self.dataset[' Crops to be taken'])
        crops_to_be_taken_mapping={label:idx for idx,label in enumerate(crops_to_be_taken)}
        print(crops_to_be_taken_mapping)
        self.dataset[' Crops to be taken']=self.dataset[' Crops to be taken'].map(crops_to_be_taken_mapping)
        X=self.dataset[training_features]
        
        XX = np.array(X)
        
        y=self.dataset[target]
        Y=np.array(y)
        clf = RandomForestClassifier(max_depth=2, random_state=0)
        clf.fit(XX,Y) 
        
        reTest = ""
        for soil_t,soil_type_index_value in soil_type_mapping.items():
            if soil_t == testData.split(",")[0]:
                reTest=soil_type_index_value
                
        change_str = testData.split(",")[0]
        tData = testData.replace(change_str,str(reTest))        
        tArray =[float(d) for d in tData.split(",")]  
        
        print(clf.feature_importances_)
        output = clf.predict([tArray])
        print(output)
        class_label_name=""
        for crop_name,crop_name_index_value in crops_to_be_taken_mapping.items():
            if crop_name_index_value == output:
                class_label_name=crop_name
        
        print(class_label_name)
        return class_label_name
    
if __name__ == "__main__":
    testData = [0,100,7.7,1.5,1.9,0.3,35,0.26,1.3,44]
    randomForest = RandomForest()
    analysis_label = randomForest.runRandomForestAlgo(testData)

# =============================================================================
# t=[[2,3,4,5],[2,3,4,5],[1,2,3,3],[2,2,2,2]]
# s=[0,1,2,2]
# clf = RandomForestClassifier(max_depth=2, random_state=0)
# clf.fit(t, s)
# 
# print(clf.feature_importances_)
# 
# print(clf.predict([[1, 3, 2, 2]]))
# =============================================================================
