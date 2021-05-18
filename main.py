import json
import downtimeGenerator as dG
import threading

config = {}
end_sim = [False]
cmd = [0]


def main_interface():
    while not end_sim[0]:
        cmd[0] = input("> ")
        process_user_cmd(cmd[0])


def process_user_cmd(key):
    if key == 'q':
        end_sim[0] = True
        dG.terminate[0] = True
        print("ending ...")


thread_downtime = threading.Thread(
    target=dG.downtime_simulator)
thread_main_interface = threading.Thread(target=main_interface)


def main():

    history_log = {}
    with open("data.json") as file:
        history_log = json.load(file)

    # downtime_his = dG.generate_downtime_records()
    # history_log = {"down time": downtime_his}
    # json_object = json.dumps(history_log, indent=4)
    # print(json_object)
    # with open("data.json", "w") as f:
    #     json.dump(history_log, f, indent=4)
    # temp = dG.generate_downtime_record(dG.duration[0])
    # json_object = json.dumps(temp, indent=4)
    # thread_downtime.start()
    # thread_main_interface.start()


if __name__ == '__main__':
    main()
