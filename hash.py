'''
my_dict = dict(dini='001',divi='002')

print(my_dict)
'''

'''
emp_details = {'employees':{'divi':{'ID':'001','salary':'1000','designation':'team leader'},'dini':{'ID':'002',
                                                'salary':'2000','designation':'associate'}}}

print(emp_details)
'''


import pandas as pd

emp_details = {'employees':{'divi':{'ID':'001','salary':'1000','designation':'team leader'},'dini':{'ID':'002',
                                                'salary':'2000','designation':'associate'}}}

df = pd.DataFrame(emp_details['employees'])

print(df)


