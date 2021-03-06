import json


config = '''
   {
       "history_length":100,
       "downtime":{
           "db_name":"downtime.json",
           "rate":0.4,
           "count":4,
           "reasons":["Service","Broken Machine","Others","Uncategorized"]
       },
       "production":{
           "db_name":"production.json",
           "input_per_hour": 100,
           "max_defect_rate":{
               "process_a": 0.15,
               "process_b": 0.2,
               "process_c": 0.1
           }
       }
   }   
'''

with open("config.json", "w") as f:
    data = json.loads(config)
    json.dump(data, f, indent=4)
