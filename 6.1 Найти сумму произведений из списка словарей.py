# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as file:
        data = json.load(file)

    total_sum = 0
    for dictionary in data:
        score = dictionary.get('score', 0)
        weight = dictionary.get('weight', 0)
        product = score * weight
        total_sum += product

    rounded_sum = round(total_sum, 3)
    return rounded_sum


print(task())
