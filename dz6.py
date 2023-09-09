# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# def func(array, begin_num,step,hou_num):
#     if hou_num == 0:
#         return array
#     array.append(begin_num)
#     return (func(array, begin_num + step, step, hou_num - 1))

# begin_num = int(input('С какого числа начать -> '))
# step = int(input('C rаким шагом -> '))
# hou_num = int(input('Сколько всего чисел-> '))

# arf_prog = []
# arf_prog = func([],begin_num,step,hou_num)
# print(*arf_prog)

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)



# def func_range (min_d,max_d,spek_list,my_list_index=list()):

#     for i in range(len(spek_list)):
#         if min_d <= spek_list[i] <= max_d:
#             my_list_index.append(i)
#     return my_list_index



# spek_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, 7]
# min_d = int(input("введите минимальное ограничение -> "))
# max_d = int(input("введите максимальное ограничение -> "))

# print(func_range(min_d, max_d, spek_list))