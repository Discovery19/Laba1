# TODO  Напишите функцию count_letters
def count_letters(text):
    map_ = {}
    for letter in text:
        if letter.isalpha():
            if letter in map_:
                map_[letter] += 1
            else:
                map_[letter] = 1
    return map_


def calculate_all_letters(text):
    result = sum(1 for i in text if i.isalpha())
    return result


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict, num_letters):
    map_ = {}
    for key, value in dict.items():
        map_[key] = format(value / num_letters, ".2f")
    return map_


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dict_of_letters = count_letters(main_str.lower())
letters_number = calculate_all_letters(main_str)

# TODO Распечатайте в столбик букву и её частоту в тексте
dict_of_frequency = calculate_frequency(dict_of_letters, letters_number)
for key, value in dict_of_frequency.items():
    print(f"{key}: {value}")
