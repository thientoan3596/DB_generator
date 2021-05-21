import random
import json
from datetime import datetime
import time
import utils
from pathlib import Path
down_time_reasons = []
rate = [1]
parsed = [False]

# Parse
duration = [0]
config = {}
system_status = {}
cache = []
terminate = [False]


def parse_conf():
    reason_count = config["downtime"]["count"]
    i = 0
    while i < reason_count:
        down_time_reasons.append(config["downtime"]["reasons"][i])
        i += 1
    rate[0] = config["downtime"]["rate"]
    duration[0] = config["history_length"]
    parsed[0] = True


def generate_down_time():
    tickets = []
    if not parsed[0]:
        print("Haven't parse config file")
        return tickets
    daily_total_down_time = utils._time()
    while random.random() < rate[0]:
        if tickets == []:
            tickets.append(generate_down_time_info())
        else:
            tickets.append(generate_down_time_info(
                utils._time(tickets[-1]["time"]["end"])))
        daily_total_down_time += utils._time(tickets[-1]["duration"])
        if utils._time(tickets[-1]["time"]["end"]).hour == 22:
            break
    return tickets, daily_total_down_time


def generate_down_time_info(starting_time=utils._time(0, 0)):
    """
    Starting_time is lowest limit for time generation
    """
    t = utils.generate_a_time_invertal(starting_time)
    i = str(utils._time(t["end"])-utils._time(t["start"]))
    r = down_time_reasons[random.randrange(0, len(down_time_reasons))]
    return {"time": t, "duration": i, "reason": r}


def generate_downtime_records():
    _now = utils._date(datetime.now())
    down_time_log = {}
    while duration[0] > 0:
        _date = _now-duration[0]
        daily_tickets, daily_total_down_time = generate_down_time()
        if daily_tickets != []:
            # down_time_log.append({"date": str(
            #     _date), "detail": daily_tickets, "total down time": str(daily_total_down_time)})
            down_time_log[str(_date)] = {
                "total": str(daily_total_down_time), "detail": daily_tickets}
        duration[0] -= 1

    return down_time_log


def downtime_simulator():
    """
    terminate is key to turn off sys
    Down rate is 0.01, go back online rate is 0.08
    """
    # while loop at every 30 sec normal
    # Do rate check every 1 minute
    system_status["action rate"] = 0.001
    system_status["is down"] = False
    system_status["overnight down"] = False
    system_status["log"] = {}
    system_status["down count "] = 0
    counter = 0
    while not terminate[0]:
        if random.random() < system_status["action rate"] and system_status["is down"] == False:
            turn_off_sys()
        elif random.random() < system_status["action rate"] and system_status["is down"] == True:
            turn_on_sys()
        if system_status["is down"] and utils._time(datetime.now()) == utils._time(23, 59):
            turn_on_sys()
            system_status["overnight down"] = True
            time.sleep(60)
            turn_off_sys()
        time.sleep(60)
    print("Simulation is terminated")
    # json_object = json.dumps(system_status, indent=4)
    # print(json_object)


def turn_off_sys():
    """
    put sys to offline
    """
    system_status["action rate"] = 0.008
    system_status["is down"] = True
    if str(utils._date(datetime.now())) not in system_status["log"]:
        system_status["log"][str(utils._date(datetime.now()))] = {}
        system_status["log"][str(utils._date(
            datetime.now()))]["total"] = "00:00"
        system_status["log"][str(utils._date(
            datetime.now()))]["detail"] = []
    cache.append({"time": {"start": str(utils._time(datetime.now()))}})


def turn_on_sys():
    """
    put sys online
    """
    system_status["rate"] = 0.0008
    system_status["is down"] = False

    cache[-1]["time"]["end"] = str(utils._time(datetime.now()))
    cache[-1]["duration"] = str(utils._time(
        cache[-1]["time"]["end"])-utils._time(cache[-1]["time"]["start"]))
    if system_status["overnight down"]:
        cache[-1]["reason"] = system_status['log'][str(
            utils._date(datetime.now())-1)]['detail'][-1]['reason']
        system_status["overnight down"] = False
    else:
        cache[-1]["reason"] = down_time_reasons[random.randrange(
            0, len(down_time_reasons))]
    system_status["log"][str(utils._date(datetime.now()))]["total"] = str(utils._time(
        system_status["log"][str(utils._date(datetime.now()))]["total"])+utils._time(cache[-1]["duration"]))

    system_status["log"][str(utils._date(datetime.now()))
                         ]["detail"].append(cache[-1])


# test unit
if __name__ == "__main__":
    pass
    # config_file = "config.json"
    # with open(config_file) as file:
    #     config = json.load(file)
    #     parse_conf(config)
    # temp = generate_downtime_record(duration[0])
    # # print(temp)
    # key = '2021-05-14'
    # if key in temp:
    #     print(temp[key]["total down time"])
    # else:
    #     print("not available")
    # # json_object = json.dumps(temp, indent=4)
    # # print(json_object)
elif __name__ == "downtimeGenerator":
    if Path("config.json").is_file():
        with open("config.json") as file:
            config = json.load(file)
            parse_conf()
    else:
        print("Unable to locate config.json")
