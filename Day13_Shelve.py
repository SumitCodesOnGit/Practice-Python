"""
1. The shelve module in python provides a simple interface for persistent storage of python objects.
2. It allows us to store python objects in a file using dictionary like api, where keys are strings and
   pickable python objects are values.
3. Internally shelve used pickle module to serialize objects before storing them.
4. Key Features:
 a. Dictionary like API: access stored objects using string keys, similar to a regular pyhton dictionary.
 b. Persistent Storage: Data is stored in a file on a disk, allowing it to persist across program executions.
 c. Automatic Serialization
"""
# example
import shelve
""" #open a shelf file
with shelve.open("mydata") as shelf:
    #store data
    shelf['name']='Sumit'
    shelf['age']=27
    shelf['grades']={"math":93,"chemistry":94}

# access data
with shelve.open('mydata') as shelf:
    print(shelf['name'])
    print(shelf['grades']) """
""" # adding another item using writeback=True
import shelve
with shelve.open('mydata',writeback=True) as shelf:
    shelf['grades']['science']=90

# access data
with shelve.open('mydata') as shelf:
    print(shelf['name'])
    print(shelf['grades']) """

import shelve
""" with shelve.open("contacts") as con:
    con['Sumit']={'phone':1234, 'email':'asv@gamil.com'}
    con['Bunty']={'phone':8907, 'email':'dfr@gmail.com'}


with shelve.open('contacts') as c:
    print(c['Sumit'])
    print(c['Bunty']) """
# updating number of sumit      
with shelve.open('contacts', writeback=True) as f:
    f['Sumit']['phone'] = '5643'


with shelve.open('contacts') as c:
    print(c['Sumit'])
    print(c['Bunty'])





