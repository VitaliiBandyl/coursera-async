import json
import functools


def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input_data = func(*args, **kwargs)
        json_data = json.dumps(input_data)
        return json_data
    return wrapper


@to_json
def get_data():
    return {
        'data': 42
    }


print(get_data())
