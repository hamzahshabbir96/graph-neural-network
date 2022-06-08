import numpy as np
import glob
import os
class graphreader:
    def __init__(self,filepath):
        self.adjacent_matrix = np.loadtxt(filepath,skiprows=1)
        self.number_of_nodes = int(open(filepath).readline().rstrip())
        
    
    def printfile(self):
        print(self.adjacent_matrix)
        print(type(self.adjacent_matrix))
        print(self.number_of_nodes)
        print(type(self.number_of_nodes))

class graphreaderbatch:
    def __init__(self,filespath,filelist=False):
        if filelist :
            self.filespaths = filespath['data']
            self.featurespath= filespath['features']
            self.critical_temperature_paths = filespath['label']
        else :
            self.filespaths = glob.glob(filespath+"//*graph.txt")
            self.critical_temperature_paths = glob.glob(filespath+"//*label.txt")
            self.featurespath = glob.glob(filespath+"//*features.txt")
       
        self.numexamples = len(self.critical_temperature_paths)
        self.adjacent_matrix = [] 
        self.number_of_nodes = []
        self.critical_temperature_ = []
        self.features = []
        
        for i in range (len(self.filespaths)):
            self.adjacent_matrix.append(np.loadtxt(self.filespaths[i],skiprows=1))
            self.number_of_nodes.append(int(open(self.filespaths[i]).readline().rstrip()))
            
        for i in range (len(self.featurespath)):
            #np.loadtxt(self.filespaths[i],skiprows=1)
            self.features.append(np.loadtxt(self.featurespath[i]))
            #self.features.append(int(open(self.featurespath[i]).readline().rstrip()))
  

        if len(self.critical_temperature_paths) != 0:
            for i in range (len(self.critical_temperature_paths)):
                self.critical_temperature_.append(float(open(self.critical_temperature_paths[i]).readline().rstrip()))
