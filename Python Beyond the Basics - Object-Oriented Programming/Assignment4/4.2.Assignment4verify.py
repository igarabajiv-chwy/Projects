import sys
from Assignment4 import ConfigDict

ce = ConfigDict('config_file.txt')

if len(sys.argv) == 3:

    key = sys.argv[1]
    value = sys.argv[2]
    print('writing data:  {0}, {1}'.format(key, value))

    ce[key] = value

elif len(sys.argv) == 2:
    print('reading a value')
    key = sys.argv[1]
    print('the value for {0} is {1}'.format(sys.argv[1], ce[key]))

else:
    print('reading data')
    for key in ce.keys():
        print('   {0} = {1}'.format(key, ce[key]))

