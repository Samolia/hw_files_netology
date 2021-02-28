from pprint import pprint

from cook_book import create_cook_book_from_file

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    '''
    Функция считает количество ингредиентов, необходимых для приготовления выбранных блюд
    :param cook_book: функция, формирующая словарь из прочитанного файла
    :param dishes: Названия блюд из словаря 'cook_book'
    :param person_count: Количество персон -> порций.
    :return: Название и количество необходимых ингредиентов
    '''
    list_by_dishes = {}
    for dish in dishes:
        for value in cook_book[dish]:
            value['quantity'] *= person_count
            keys = value['ingredient_name']
            values = {'measure': value['measure'], 'quantity': value['quantity']}
            if keys in list_by_dishes:
                list_by_dishes[keys]['quantity'] += value['quantity']
            else:
                list_by_dishes.update({keys: values})
    return list_by_dishes

pprint(get_shop_list_by_dishes(create_cook_book_from_file('recipes.txt'), ['Фахитос', 'Омлет'], 2))