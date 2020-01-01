import os

class ConfigDict(dict):
    def __init__(self,filename):
        self.filename = filename    
        if os.path.isfile(self.filename):
            with open(self.filename) as fh:
                for line in fh:
                    line = line.strip()
                    dict.__setitem__(self,line.split('=')[0], line.split('=')[1])
        else:
            print('No file found')
                    
    def __getitem__(self,key):
        return dict.__getitem__(self,key)

    def __setitem__(self,key,value): 
        dict.__setitem__(self,key,value)
        with open(self.filename,'a') as fh:
            fh.write(f'{key}={dict.__getitem__(self,key)}\n') #dict.__getitem__(self,key) is redundant because key,value are passed as parameters

    def __repr__(self):
        return str(dict(self))