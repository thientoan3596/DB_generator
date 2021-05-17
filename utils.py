from random import randrange
from datetime import datetime, timedelta


class _date:
    def __init__(self,day=1,month=1,year=2010):
        self.day=day
        self.month=month
        self.year=year
    def __str__(self):
        return "{:04d}-{:02d}-{:02d}".format(self.year,self.month,self.day)
    def __add__(self,days):
        temp = datetime(self.year,self.month,self.day)-timedelta(days=days)
        return _date(temp.day,temp.month,temp.year)

def generate_time(starting_time="00:00"):
    hh = randrange(get_hour(starting_time), 23)
    if hh == get_hour(starting_time):
        mm = randrange(get_min(starting_time)+1, 59)
    else:
        mm = randrange(59)
    return int_to_str(hh,mm)


def generate_a_time_invertal(starting_time="00:00"):
    starting = generate_time(starting_time)
    ending = generate_time(starting)
    return {"start": starting, "end": ending}


def find_delta_time(start_end_time):
    start = str_to_timedelta(start_end_time["start"]) 
    end = str_to_timedelta(start_end_time["end"])
    duration  =end -start
    return timedelta_to_str(duration)

def int_to_str(hh,mm):
    return "{:02d}:{:02d}".format(hh,mm)
def timedelta_to_str(timedel):
    return f"{timedel.seconds // (3600)}:{(timedel.seconds%3600)//60}"
def str_to_timedelta(str):
    return timedelta(hours=get_hour(str),minutes=get_min(str))
    
def get_hour(str):
    return int(str[:-3])
def get_min(str):
    return int(str[-2:])
