import json


config = '''
   {
       "down time":{
           "rate":0.7,
           "count":4,
           "reasons":["Service","Broken Machine","Others","Uncategorized"]
       }
   }   
'''

with open("config.json", "w") as f:
    data = json.loads(config)
    json.dump(data, f, indent=4)
