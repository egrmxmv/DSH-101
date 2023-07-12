numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
empty_None = numbers[4]
left_numbers = (numbers[:4])
right_numbers = (numbers[5:])
quantity_numbers = len(numbers)
sum_numbers_without_empty_None = sum(left_numbers + right_numbers)
new_empty_None = sum_numbers_without_empty_None / quantity_numbers
new_numbers = numbers
numbers[4] = new_empty_None
print("Измененный список:", numbers)
