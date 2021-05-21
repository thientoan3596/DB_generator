import random
import json
import utils as u
from pathlib import Path
import time
from datetime import datetime
from math import floor as round

parsed = [False]
conf = {}
duration = [0]
history_log = {}
production_log = {}
downtime_log = {}
data = {}
terminate = [False]


def parse_conf(config):

    duration[0] = config["history_length"]
    parsed[0] = True


def show_conf():
    if parsed[0]:
        json_object = json.dumps(conf, indent=4)
        print(json_object)


def production_generator():
    _date = u._date(datetime.now())
    production_history = {}
    while duration[0] > 0:
        availability = u._time(24)-find_date_downtime(str(_date-duration[0]))

        totalInput = round(availability.toFloat()*conf["input_per_hour"])

        temprate = 1
        processA_ff = round(
            totalInput*gen_rate(conf["max_defect_rate"]["process_a"]))
        processA_FPY = processA_ff/totalInput
        processA_reworked = round((totalInput - processA_ff)*gen_rate(1))
        processB_input = (processA_ff+processA_reworked)
        processB_ff = round(processB_input *
                            gen_rate(conf["max_defect_rate"]["process_b"]))
        processB_FPY = processB_ff/(processA_ff+processA_reworked)
        processB_reworked = round((processB_input-processB_ff)*gen_rate(1))
        processC_input = (processB_ff+processB_reworked)
        processC_ff = round(processC_input *
                            gen_rate(conf["max_defect_rate"]["process_c"]))
        processC_FPY = processC_ff/(processB_ff+processB_reworked)
        processC_reworked = round((processC_input-processC_ff)*gen_rate(1))
        finishedProducts = processC_reworked+processC_ff
        RTY = processA_FPY*processB_FPY*processC_FPY
        Efficiency = finishedProducts / totalInput
        Theoretical_output = totalInput
        production_history[str(_date-duration[0])] = {"process_a_input": totalInput, "availability": str(availability), "process_a_reworked": processA_reworked, "process_a_fpy": processA_FPY, "process_b_input": processB_input,
                                                      "process_b_reworked": processB_reworked, "process_b_fpy": processB_FPY, "process_c_input": processC_input, "process_c_reworked": processC_reworked, "process_c_fpy": processC_FPY, "output": finishedProducts}
        duration[0] -= 1
    return production_history


def production_simulator():
    """
    Description here
    """
    # Look for current date data
    _date = u._date(datetime.now())
    if str(_date) in production_log:
        pass
    # set variables
    # While not terminate
    while not terminate[0]:
        time.sleep(60)
    pass


def gen_rate(maxrate):
    rate = 2
    if maxrate != 1:
        while rate > maxrate:
            rate = random.random()
        return 1-rate
    else:
        while rate > maxrate:
            rate = random.random()
        return rate


def find_date_downtime(dateStr):
    if dateStr in downtime_log:
        return u._time(downtime_log[dateStr]["total"])
    return u._time()


if __name__ == "__main__":
    if Path("config.json").is_file():
        with open("config.json") as file:
            config = json.load(file)
            parse_conf(config)
        with open("downtime.json") as file:
            downtime_log = json.load(file)
        conf = config["production"]
    else:
        print("Unable to locate config.json")

    # Test Unit
    duration[0] = 3
    temp = production_generator()
    jsonobj = json.dumps(temp, indent=4)
    print(jsonobj)

elif __name__ == "productionGenerator":
    if Path("config.json").is_file():
        with open("config.json") as file:
            config = json.load(file)
            parse_conf(config)
        with open("downtime.json") as file:
            downtime_log = json.load(file)
        conf = config["production"]
    else:
        print("Unable to locate config.json")
