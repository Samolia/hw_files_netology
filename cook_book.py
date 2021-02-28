def create_cook_book_from_file(file_name):
    '''
    Функция формирует словарь из прочитанного файла
    :param file_name: Имя файла для чтения
    :return: Словарь - кулинарная книга
    '''
    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure']
    with open(file_name, encoding='UTF-8') as f:
        for line in f:
            dish = line.strip()
            amount_ingridients = int(f.readline())
            ingridient_of_list = []
            for ingridient in range(amount_ingridients):
                internal_dict = (dict(zip(keys, f.readline().strip().split('|'))))
                internal_dict['quantity'] = int(internal_dict['quantity'])
                ingridient_of_list.append(internal_dict)
            cook_book[dish] = ingridient_of_list
            f.readline()
    return cook_book