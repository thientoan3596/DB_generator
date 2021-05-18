import random
import json
import utils as u
from pathlib import Path
import time
from datetime import datetime


parsed = [False]
conf = {}
duration = [0]


def show_conf():
    if parsed[0]:
        json_object = json.dumps(conf, indent=4)
        print(json_object)


if __name__ == "__main__":
    if Path("config.json").is_file():
        with open("config.json") as file:
            temp = json.load(file)
            conf = temp["production"]
            parsed[0] = True
    else:
        print("Unable to locate config.json")

    show_conf()
    pass
elif __name__ == "downtimeGenerator":
    if Path("config.json").is_file():
        with open("config.json") as file:
            temp = json.load(file)
            conf = temp["production"]
            duration[0] = temp["history length"]
            parsed[0] = True
    else:
        print("Unable to locate config.json")
