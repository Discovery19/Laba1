# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, split_participant=','):
    participants_first_group = participants_first_group.split(split_participant)
    participants_second_group = participants_second_group.split(split_participant)
    return sorted(set(participants_first_group).intersection(set(participants_second_group)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
right_list = ["Петров", "Сидоров"]
print(right_list)
list_ = find_common_participants(participants_first_group, participants_second_group, '|')
print(list_)
if list_ == right_list:
    print("Функция работает верно")
