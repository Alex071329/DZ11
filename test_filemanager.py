import os
import shutil
def separator(count):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count
def test_separator():
    assert separator(30) == '*'*30

def author_info():
    return 'Aleksandr Saluhov'
def test_author_info():
    assert author_info() == 'Aleksandr Saluhov'

months = {
    '01': 'января',
    '02': 'февраля',
    '06': 'июня'
}

# соответствие дня и его названия
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '12': 'двенадцатое',
    '26': 'двадцать шестое'
}

# словарь известных людей и из дат рождения
FAMOUS = {
    'А.С. Пушкин': '26.06.1799',
    'Авраам Линкольн': '12.02.1809',
    'Анджелина Джоли': '04.06.1975'
}


def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result
def test_date_to_str():
    assert date_to_str('26.06.1799') == 'двадцать шестое июня 1799 года'


def copy_file(file_name):
    new_file_name = file_name[0:-3] + '_copy.py'
    if new_file_name in os.listdir():
        os.remove(new_file_name)
    shutil.copyfile(file_name,new_file_name)

def test_copy_file():
     copy_file('main.py')
     assert 'main_copy.py' in os.listdir()
     os.remove('main_copy.py')

def copy_folder(folder_name):
    new_folder_name = folder_name + '_copy'
    if new_folder_name in os.listdir():
        os.rmdir(new_folder_name)
    shutil.copytree(folder_name, new_folder_name)

def test_copy_folder():
    copy_folder('main')
    assert 'main_copy' in os.listdir()
    os.rmdir('main_copy')

from functions import foldernames,filenames
def test_foldernames():
    assert 'main' in foldernames()

def test_filenames():
    assert 'listdir.txt' in filenames()