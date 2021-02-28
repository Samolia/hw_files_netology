import operator

def get_info(file_names):
    '''
    Функция читает файлы/файл и записывает информацию в словарь
    :param file_names: Имя файла/файлов для чтения
    :return: Словарь, в котором ключ/ключи - имя файла/имена файлов, значение/значения - текст файла/файлов
    '''
    my_data = {}
    for file in file_names:
        with open(file, encoding='utf-8') as f:
            my_data.update({file: f.readlines()})
    my_data_len = {key: len(value) for key, value in my_data.items()}
    sorted_key_list = sorted(my_data_len.items(), key=operator.itemgetter(1))
    my_data = [{item[0]: my_data[item[0]]} for item in sorted_key_list]
    return my_data

