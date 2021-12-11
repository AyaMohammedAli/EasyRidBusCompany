# Write your awesome code here
import json


def check_data(stuff):
    bus_id, stop_id, stop_name, next_stop, stop_type, a_time, total = 0, 0, 0, 0, 0, 0, 0
    for bit in stuff:
        for key, value in bit.items():
            if key == "bus_id":
                if not isinstance(value, int):
                    bus_id += 1
                    total += 1
            if key == "stop_id":
                if not isinstance(value, int):
                    stop_id += 1
                    total += 1
            if key == "stop_name":
                if not isinstance(value, str):
                    stop_name += 1
                    total += 1
                elif not value:
                    stop_name += 1
                    total += 1
            if key == "next_stop":
                if not isinstance(value, int):
                    next_stop += 1
                    total += 1
            if key == "stop_type":
                acceptable = ["S", "O", "F"]
                if not isinstance(value, str):
                    stop_type += 1
                    total += 1
                elif value:
                    if value not in acceptable:
                        stop_type += 1
                        total += 1
            if key == "a_time":
                if not isinstance(value, str):
                    a_time += 1
                    total += 1
                elif not value:
                    a_time += 1
                    total += 1

    print(f"Type and required field validation: {total} errors")
    print(f"bus_id: {bus_id}")
    print(f"stop_id: {stop_id}")
    print(f"stop_name: {stop_name}")
    print(f"next_stop: {next_stop}")
    print(f"stop_type: {stop_type}")
    print(f"a_time: {a_time}")


user_input = input()
json_string = json.loads(user_input)
check_data(json_string)
