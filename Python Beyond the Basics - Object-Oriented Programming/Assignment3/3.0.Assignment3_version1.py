class ConfigDict():
    def __init__(self,filename):
        self.filename = filename
        self.temp_dictionary = {}
        with open(self.filename) as fh:
            for line in fh:
                self.temp_dictionary[line.split('=')[0]] = line.split('=')[1]
                
    def __getitem__(self,key):
        return self.temp_dictionary.__getitem__(key)

    def __setitem__(self,key,value): 
        self.temp_dictionary.__setitem__(key,value)
        with open(self.filename,'a') as fh:
            fh.write(f'{key}={self.temp_dictionary.__getitem__(key)}\n')

    def keys(self):
        return self.temp_dictionary.keys()

    def __repr__(self):
        return str(self.temp_dictionary)

        
 