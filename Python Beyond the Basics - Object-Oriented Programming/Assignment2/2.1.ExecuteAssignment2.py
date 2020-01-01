from Assignment2 import Logfile, DelimFile
import time

t0= time.time()

log = Logfile('log_igor.txt')
log.WriteFile('this is a log message')
log.WriteFile('this is another log message')

c = DelimFile('igor_csv.csv',',')
c.WriteFile(['a','b','c','d','e'])
c.WriteFile(['1','2','3','4','5'])

c.WriteFile(['a', 'this, that', 'c', 'd'])

c.WriteFile(['Igor1','Igor2','Igor3','Igor4','Igor5'])
c.WriteFile(['Igor7','Igor8','Igor9','Igor6','Igor6'])
c.WriteFile(['Igor12','Igor13','Igor14','Igo15','Igor16'])
c.WriteFile(['Igor19','Igor20','Igor21','Igor22','Igor23'])

t1= time.time()

print(t1-t0)
