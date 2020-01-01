import os
import pickle

class ConfigDict(dict):
    path = 'C:\\Users\\igarabajiv\\Desktop\\Work\\7.Python\\'

    def __init__(self,filename):
        self.file = self.path+filename+'.pickle'    
        if not os.path.isfile(self.file):
            obj = {}
            with open(self.file,'wb') as fh:
                pickle.dump(obj,fh)
        else:
            with open(self.file,'rb') as fh:
                outfile = pickle.load(fh)
                self.update(outfile)    #update {} class with new object that was dumped out of picked file

    def __getitem__(self,key):
        try:
            return dict.__getitem__(self,key)
        except:
            raise KeyError (key,list(dict.keys(self)))


    def __setitem__(self,key,value): 
        dict.__setitem__(self,key,value)
        with open(self.file, 'wb') as fh:
            pickle.dump(dict(self), fh)
