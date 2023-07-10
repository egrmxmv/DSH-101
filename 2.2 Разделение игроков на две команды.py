list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
team_one = list_players[:3]
team_two = list_players[3:]
print(team_one)
print(team_two)

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]
print(middle_index)
print(first_team)
print(second_team)
