import json


config = '''
   {
       "data name":"data.json",
       "history length":200,
       "down time":{
           "rate":0.4,
           "count":4,
           "reasons":["Service","Broken Machine","Others","Uncategorized"]
       },
       "production":{
           "input per hour": 100,
           "max defect rate":{
               "process a": 0.15,
               "process b": 0.2,
               "process c": 0.1
           }
       }
   }   
'''

with open("config.json", "w") as f:
    data = json.loads(config)
    json.dump(data, f, indent=4)
