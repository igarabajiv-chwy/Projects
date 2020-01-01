import os

class KeyError(Exception):
    def __init__(self,*args):
        if args:
            self.key = args[0]
            self.message = args[1]
        else:
            self.message = ''

    def __str__(self):
        if self.message:
            return f'Failure reason: Requested key {self.key} could not be found. Keys available are {self.message}.'
        else:
            return f'Failure reason: Cannot find requested key.'


class ConfigDict(dict):
    def __init__(self,filename):
        self.filename = filename    
        if not os.path.isfile(self.filename):
            raise FileNotFoundError('File name or path provided does not exist') #does not create new dictionary if provided file does not exist in the filepath
        else:
            with open(self.filename) as fh:
                for line in fh:
                    line = line.strip()     #strip emtpy spaces
                    if line != '':          #skip empty lines
                        dict.__setitem__(self,line.split('=')[0], line.split('=')[1]) 
                    
    def __getitem__(self,key):
        try:
            return dict.__getitem__(self,key)
        except:
            raise KeyError (key,list(dict.keys(self)))


    def __setitem__(self,key,value): 
        dict.__setitem__(self,key,value)
        with open(self.filename,'a') as fh:
            fh.write(f'{key}={dict.__getitem__(self,key)}\n') #dict.__getitem__(self,key) is redundant because key,value are passed as parameters

    def __repr__(self):
        return str(dict(self))