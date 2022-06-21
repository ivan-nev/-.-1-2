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

def get_shop_list_by_dishes(dishes, person_count):
    result_book = make_book('spisok.txt')
    result_ingr ={}
    for dish in dishes:
        list_ingr = result_book.get(dish)
        # print (list_ingr)
        for ingr in list_ingr:
            # print(ingr)
            if ingr['ingredient_name'] not in result_ingr.keys():
                 result_ingr[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count }
            else:
                 (result_ingr[ingr['ingredient_name']])['quantity'] += int(ingr['quantity']) * person_count
    return result_ingr



pprint(make_book('spisok.txt'), sort_dicts=False, width=180,)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2),sort_dicts=False, width=180)


# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


            
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