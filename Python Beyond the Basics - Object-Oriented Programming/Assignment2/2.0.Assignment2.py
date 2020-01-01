from abc import ABCMeta, abstractmethod
from datetime import datetime
import csv

class WriteFile(metaclass = ABCMeta): #class name should be noun
    @abstractmethod
    def WriteFile(self,file):
        pass

    #can use shared functions 

class Logfile(WriteFile):
    def __init__(self,text_file):
        self.text_file = text_file #variable can be instantiated with a constant

    def WriteFile(self,text):
        str = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}" + '\t' + f'{text}\n'
        with open(self.text_file, 'a') as f:
            f.write(str)


class DelimFile(WriteFile):
    def __init__(self,csv_file, delim= ','):
        self.csv_file = csv_file
        self.delim = delim

    def WriteFile(self,text):
        with open(self.csv_file, 'a') as f:
            writer = csv.writer(f, delimiter = self.delim)
            writer.writerow(text)