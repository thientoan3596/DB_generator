import json


config = '''
   {
       "history length":365,
       "down time":{
           "rate":0.4,
           "count":4,
           "reasons":["Service","Broken Machine","Others","Uncategorized"]
       },
       "production":{
           "input per hour": 100,
           "defect rate":{
               "process 1": 0.12,
               "process 2": 0.1,
               "process 3": 0.13
           }
       }
   }   
'''

with open("config.json", "w") as f:
    data = json.loads(config)
    json.dump(data, f, indent=4)
