import json
import downtimeManagement

config_file = "config.json"

config = {}


def main():
    with open(config_file) as file:
        config = json.load(file)
        downtimeManagement.parse_conf(config)
    print(downtimeManagement.generate_down_time(1))
    # print(downtimeManagement.rate[0])


if __name__ == '__main__':
    main()
