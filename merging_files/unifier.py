import operator
import os

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


def writing_to_file(my_data, my_file):
    '''
    Функция структурированно записывает в файл информацию (если файла с таким именем нет, то создает его)
    :param my_data: Словарь с информацией
    :return: Абсолютный путь к записанному файлу
    '''
    with open(my_file, 'w', encoding='utf-8') as f:
        for file in my_data:
            for key, value in file.items():
                f.write(key + '\n')
                f.write(str(len(value)) + '\n')
                for elem in value:
                    f.write(elem.strip() + '\n')
    file_path = os.path.join(os.getcwd(), my_file)
    return file_path

print(writing_to_file(get_info(['1.txt', '2.txt', '3.txt']), 'result.txt'))