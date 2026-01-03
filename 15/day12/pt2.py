from pathlib import Path
import json

with Path("input.txt").open() as f:
    data = json.load(f)


def sum_numbers(json_obj):
    if isinstance(json_obj, dict):
        if "red" in json_obj.values():
            return 0
        return sum(sum_numbers(v) for v in json_obj.values())
    elif isinstance(json_obj, list):
        return sum(sum_numbers(item) for item in json_obj)
    elif isinstance(json_obj, int):
        return json_obj
    return 0


print(sum_numbers(data))
