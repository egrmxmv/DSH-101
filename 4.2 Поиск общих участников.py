# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter=','):
    first_group = set(participants_first_group.split(delimiter))
    second_group = set(participants_second_group.split(delimiter))
    common_participants = sorted(list(first_group.intersection(second_group)))
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')

print(f"Общие участники: {common_participants}")
