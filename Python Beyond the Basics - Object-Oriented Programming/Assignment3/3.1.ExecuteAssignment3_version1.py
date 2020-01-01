from Assignment3correct import ConfigDict
aa=ConfigDict('config_file.txt')


print('sql query value is ', aa['sql_query'])
print('email value is ', aa['email_to'])
print('number of retries value is ', aa['num_retries'])
print('setting new field value')
aa['database1'] = 'sql_server'
print('retrieving db value ', aa['database'])
print('retrieving db value 1', aa['database1'])


