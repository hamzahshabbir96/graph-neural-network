import glob
import numpy as np
from utils import graphreader 
class graphdataset:
    def __init__(self,path,filelist=False):
        reader = graphreader.graphreaderbatch(path,filelist)
        self.adjacent_matrix = np.array(reader.adjacent_matrix)
        self.labels = np.array(reader.labels)
        self.nnodes = np.array(reader.nnodes)
        self.features = np.array(reader.features)
        self.indexinepoch = 0
        self.epochcompleted = 0
        self.numexamples = int(len(self.adjacent_matrix))

    def next_dataset(self,batchsize,shuffle=True):
        start = self.indexinepoch
        if start == 0 and self.epochcompleted == 0 :
            idx = np.arange(0,self.numexamples)
            np.random.shuffle(idx)
            self.adjacent_matrix    = self.adjacent_matrix[idx]
            self.labels = self.labels[idx]
            self.nnodes = self.nnodes[idx]
            self.features = self.features[idx]
        
        if start+batchsize <= self.numexamples:
            self.indexinepoch += batchsize
            end = self.indexinepoch
            adjacent_matrixbatch = self.adjacent_matrix[start:end]
            labelsbatch = self.labels[start:end]
            nnodesbatch = self.nnodes[start:end]
            featuresbatch = self.features[start:end]
        
            return adjacent_matrixbatch,nnodesbatch,labelsbatch,featuresbatch

        else :
            self.epochcompleted += 1
            restnumexamples = self.numexamples - start
            
            adjacent_matrixrest = self.adjacent_matrix[start:self.numexamples]
            labelsrest  = self.labels[start:self.numexamples]
            nnodesrest = self.nnodes[start:self.numexamples]
            featuresrest = self.features[start:self.numexamples]

            idx0 = np.arange(0,self.numexamples)
            np.random.shuffle(idx0)
            self.adjacent_matrix = self.adjacent_matrix[idx0]
            self.labels = self.labels[idx0]
            self.nnodes = self.nnodes[idx0]
            self.features = self.features[idx0]
            
            start = 0
            self.indexinepoch = batchsize - restnumexamples
            end = self.indexinepoch
            
            adjnew = self.adjacent_matrix[start:end]
            labelsnew = self.labels[start:end]
            nnodesnew = self.nnodes[start:end]
            featuresnew = self.features[start:end]

            adjacent_matrixbatch = np.concatenate((adjacent_matrixrest,adjacent_matrixnew),axis=0)
            labelsbatch = np.concatenate((labelsrest,labelsnew),axis=0)
            nnodesbatch = np.concatenate((nnodesrest,nnodesnew),axis=0)
            featuresbatch = np.concatenate((featuresrest,featuresnew),axis=0)
           
            
            return adjacent_matrixbatch,nnodesbatch,labelsbatch,featuresbatch
    def getall(self):
        print(self.adjacent_matrix)
        return self.adjacent_matrix,self.nnodes,self.labels,self.
