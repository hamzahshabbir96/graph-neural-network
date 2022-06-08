import numpy as np
import glob
import os
class graphreader:
    def __init__(self,filepath):
        self.adj = np.loadtxt(filepath,skiprows=1)
        self.nnodes = int(open(filepath).readline().rstrip())
        
    
    def printfile(self):
        print(self.adj)
        print(type(self.adj))
        print(self.nnodes)
        print(type(self.nnodes))

class graphreaderbatch:
    def __init__(self,filespath,filelist=False):
        if filelist :
            self.filespaths = filespath['data']
            self.featurespath= filespath['features']
            self.labelspaths = filespath['label']
        else :
            self.filespaths = glob.glob(filespath+"//*graph.txt")
            self.labelspaths = glob.glob(filespath+"//*label.txt")
            self.featurespath = glob.glob(filespath+"//*features.txt")
       
        self.numexamples = len(self.labelspaths)
        self.adj = [] 
        self.nnodes = []
        self.labels = []
        self.features = []
        
        for i in range (len(self.filespaths)):
            self.adj.append(np.loadtxt(self.filespaths[i],skiprows=1))
            self.nnodes.append(int(open(self.filespaths[i]).readline().rstrip()))
            
        for i in range (len(self.featurespath)):
            #np.loadtxt(self.filespaths[i],skiprows=1)
            self.features.append(np.loadtxt(self.featurespath[i]))
            #self.features.append(int(open(self.featurespath[i]).readline().rstrip()))
  

        if len(self.labelspaths) != 0:
            for i in range (len(self.labelspaths)):
                self.labels.append(float(open(self.labelspaths[i]).readline().rstrip()))

       
