from pprint import pprint

def make_book(file_name):
    with open(file_name, encoding='utf-8') as cook_obj:
        result_book = {}
        for line in cook_obj:
            dish = line.strip()
            num_ingr = int(cook_obj.readline())
            list_ing =[]
            for i in range(num_ingr):
                dict_ingr = {}
                ingr = ((cook_obj.readline()).strip()).split(' | ')
                # print (ingr)
                dict_ingr['ingredient_name'] = ingr[0]
                dict_ingr['quantity'] = ingr[1]
                dict_ingr['measure'] = ingr[2]
                list_ing.append(dict_ingr)
            result_book[dish] = list_ing
            cook_obj.readline()
    return result_book

pprint(make_book('spisok.txt'), sort_dicts=False, width=180,)
            


            
# Омлет
# 3
# Яйцо | 2 | шт
# Молоко | 100 | мл
# Помидор | 2 | шт

# Утка по-пекински
# 4
# Утка | 1 | шт
# Вода | 2 | л
# Мед | 3 | ст.л
# Соевый соус | 60 | мл

# 'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
# ],