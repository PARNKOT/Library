# Сортировка выбором.
# Выполняется через два цикла.
# 1) Выбрать первый элемент и присвоить его значение переменной smallest
# 2) Итеративно выбираем каждый следующий элемент и сравниваем его со smallest
# 3) Если текущий элемент меньше smallest, то присваиваем smallest текущее значение
# 4) В конце цикла меняем места элемент, выбранный на этапе 1 с элементом под индексом smallest
# 5) Вернуться к пункту 1 и выбрать следующий элемент


def selection_sort(iter_obj):
    for current_index in range(len(iter_obj)):
        smallest_index = current_index
        for i in range(current_index + 1, len(iter_obj)):
            if iter_obj[i] < iter_obj[smallest_index]:
                smallest_index = i
        iter_obj[current_index], iter_obj[smallest_index] = iter_obj[smallest_index], iter_obj[current_index]
