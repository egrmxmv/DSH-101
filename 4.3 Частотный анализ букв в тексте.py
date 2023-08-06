# TODO  Напишите функцию count_letters
def count_letters(text):  # подсчитывает количество каждой буквы в тексте
    letter_count = {}  # создаём пустой словарь
    for char in text:
        if char.isalpha() and char.lower():  # проверяем является ли символ буквой и в нижнем ли регистре они
            lowercase_char = char.lower()
            letter_count[lowercase_char] = letter_count.get(lowercase_char, 0) + 1
    return letter_count  # возращаем словарь


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_count):  # вычисляет частоту каждой буквы и возвращает словарь
    total_letters = sum(letter_count.values())  # суммируем все значения
    frequencies = {}  # создаём пустой словарь
    for letter, count in letter_count.items():
        frequency = count / total_letters
        frequencies[letter] = round(frequency, 2)
    return frequencies

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

# TODO Распечатайте в столбик букву и её частоту в тексте
letter_count = count_letters(main_str)
frequencies = calculate_frequency(letter_count)

for letter, frequency in frequencies.items():
    print(f"{letter}: {frequency:.2f}")
