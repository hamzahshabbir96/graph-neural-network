from utils import graphreader,dataset_reader
import numpy as np
import glob

class Preprocess:
    def __init__(self,path,testratio=0.2):
        self.filespaths = glob.glob(path+"//*graph.txt")
        self.critical_temperature_paths = glob.glob(path+"//*critical_temp.txt")
        self.featurespath = glob.glob(path+"//*features.txt")
        self.filelist=True 
        size = len(self.filespaths)

        self.trainindexend = size - int(testratio*size)
        

    def get_data(self):
        trainpaths = {'data':self.filespaths[:self.trainindexend],
                      'label':self.critical_temperature_paths[:self.trainindexend],
                      'features':self.featurespath[:self.trainindexend]}
        testpaths  = {'data':self.filespaths[self.trainindexend:],
                      'label':self.critical_temperature_paths[self.trainindexend:],
                      'features':self.featurespath[self.trainindexend:]}


        traindataset = dataset_reader.graphdataset(trainpaths,self.filelist)
        testdataset = dataset_reader.graphdataset(testpaths,self.filelist)

        return traindataset,testdataset

