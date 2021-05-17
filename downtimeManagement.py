import random
import math
import json
from datetime import datetime
import utils
from datetime import timedelta
down_time_reasons = []
rate = [1]
reason_count = [0]

parsed = [False]


def parse_conf(conf):
    parse_down_time_rate(conf)
    parse_down_time_reasons(conf)
    parsed[0] = True


def parse_down_time_reasons(config):
    reason_count[0] = config["down time"]["count"]
    i = 0
    while i < reason_count[0]:
        down_time_reasons.append(config["down time"]["reasons"][i])
        i += 1


def parse_down_time_rate(config):
    rate[0] = config["down time"]["rate"]


def generate_down_time(date):
    tickets = []
    if not parsed[0]:
        print("Haven't parse config file")
        return tickets
    while random.random() < rate[0]:
        if tickets == []:
            tickets.append(generate_down_time_info())
        else:
            # print(tickets)
            tickets.append(generate_down_time_info(tickets[-1]["time"]["end"]))
    return tickets


def generate_down_time_info(starting_time="00:00"):
    t = utils.generate_a_time_invertal(starting_time)
    i = utils.find_delta_time(t)
    r = down_time_reasons[random.randrange(0, reason_count[0])]
    return {"time": t, "duration": i, "reason": r}

def generate_downtime_record(duration):
    now = datetime.now()
    while duration>0:
        _date = now - 