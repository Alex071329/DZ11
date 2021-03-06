import os
import shutil
import pickle
def add_separators(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('-' * 200)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('-' * 200)
        return result

    # возвращается функция inner с новым поведением
    return inner

@ add_separators
def victory():
    famous_people = {
        'А.С.Пушкин': '06.06.1799',
        'Л.Н.Толстой': '09.09.1828',
        'М.Ю.Лермонтов': '15.10.1814',
        'Н.В.Гоголь': '01.04.1809',
        'И.С.Тургенев': '09.11.1818',
        'И.А.Крылов': '13.02.1769',
        'Ф.М.Достоевский': '11.11.1821',
        'А.П.Чехов': '29.11.1860',
        'М.А.Булгаков': '15.05.1891',
        'И.А.Бунин': '22.10.1870'
    }
    import random
    numbers = list(famous_people.items())
    result = random.sample(numbers, 5)
    new_result = dict(result)
    print(list(new_result))
    right = 0
    not_right = 0
    for date_of_birth in new_result.values():
        data = input('Введите  дату рождения в формате dd.mm.yyyy : ')
        months = {
            '01': 'января',
            '02': 'февраля',
            '03': 'марта',
            '04': 'апреля',
            '05': 'мая',
            '06': 'июня',
            '07': 'июля',
            '08': 'августа',
            '09': 'сентября',
            '10': 'октября',
            '11': 'ноября',
            '12': 'декабря'
        }
        days = {
            "01": "первое",
            "02": "второе",
            "03": "третье",
            "04": "четвертое",
            "05": "пятое",
            "06": "шестое",
            "07": "седьмое",
            "08": "восьмое",
            "09": "девятое",
            "10": "десятое",
            "11": "одинадцатое",
            "12": "двенадцатое",
            "13": "тринадцатое",
            "14": "четырнадцатое",
            "15": "пятнадцатое",
            "16": "шестнадцатое",
            "17": "семнадцатое",
            "18": "восемнадцатое",
            "19": "девятнадцатое",
            "20": "двадцатое",
            "21": "двадцать первое",
            "22": "двадцать второое",
            "23": "двадцать третье",
            "24": "двадцать четвертое",
            "25": "двадцать пятое",
            "26": "двадцать шестое",
            "27": "двадцать седьмое",
            "28": "двадцать восьмое",
            "29": "двадцать девятое",
            "30": "тридцатого",
            "31": "тридцать первого"
        }
        day, month, year = date_of_birth.split('.')
        if data in new_result.values():
            right += 1
        else:
            print(days[day], months[month], year, 'года')
            not_right += 1
    print('Количество правильных ответов : ', right)
    print('Количество неправильных ответов : ', not_right)
    print('Попробуйте начать сначала!')
    pass
if __name__ == '__main__':
    victory()



@ add_separators
def my_bank_account():
    list_nambers = []
    shopping = []
    purchase_history = []
    if not os.path.exists('balance.data'):
        with open('balance.data', 'wb') as f:
            remainder = 0
            pickle.dump(remainder, f)
    if not os.path.exists('history.data'):
        with open('history.data', 'wb') as f:
            history = []
            pickle.dump(history, f)


    def product(title, price):
        balance = sum(list_nambers) - sum(shopping)
        if purchase == title:
            balance -= price
            shopping.append(price)
            purchase_history.append((title, price))

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. остаток на счете')
        print('5. выход')

        with open('balance.data', 'rb') as f:
            remainder = pickle.load(f)
        balance = sum(list_nambers) - sum(shopping) + remainder
        with open('history.data', 'rb') as f:
            history = pickle.load(f)
        history += purchase_history

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                check = 0
                namber = input('Введите сумму на сколько пополнить счет: ')
                if int(namber) > 0:
                    check += int(namber)
                    list_nambers.append(check)
                    pass
                else:
                    pass
            except:
                print('Вы ввели не число.')
        elif choice == '2':
            try:
                namber = int(input('Введите сумму покупки: '))
                if namber > balance:
                    print('Денег не хватает.')
                    pass
                else:
                    purchase = input('Введите название покупки(молоко,хлеб,масло): ')
                    product('молоко', 60)
                    product('хлеб', 40)
                    product('масло', 130)
                    pass
            except:
                print('Вы ввели не число.')
        elif choice == '3':
            print(history)
            pass
        elif choice == '4':
            print('Всего на счете: ', balance)
            pass
        elif choice == '5':
            with open('balance.data', 'wb') as f:
                pickle.dump(balance, f)
            with open('history.data', 'wb') as f:
                pickle.dump(history, f)
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    my_bank_account()


def menu_item(a,b):
    while True:
        print('1- фаил ;')
        print('2- папка;')
        print('3- выход.')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            a()
            pass
        elif choice == '2':
            b()
            pass
        elif choice == '3':
            break
        else:
            print('Неверный пункт меню: ')

def remove_file():
    try:
        file_name = input('Введите название файла: ')
        os.remove(file_name)
    except:
        print('Такого файла не существует.')
def delete_folder():
    try:
        folder_name = input('Введите название папки: ')
        os.rmdir(folder_name)
    except:
        print('Такой папки не существует.')

if __name__ == '__main__':
    menu_item(a = remove_file,b = delete_folder)

def copy_file():
    try:
        file_name = input('Введите название файла: ')
        new_file_name = file_name[0:-3] + '_copy.py'
        shutil.copy(file_name,new_file_name)
    except:
        print('Такого файла не существует.')
def copy_folder():
    try:
        folder_name = input('Введите название папки: ')
        new_folder_name = folder_name + '_copy'
        shutil.copytree(folder_name, new_folder_name)
    except:
        print('Такой папки не существует.')


if __name__ == '__main__':
    menu_item(a = copy_file,b = copy_folder)

def filenames():
    result = [item for item in os.listdir() if os.path.isfile(item)]
    #for item in os.listdir():
     #   if os.path.isfile(item):
      #      result.append(item)
    return result
def foldernames():
    result1 = [item for item in os.listdir() if os.path.isdir(item)]
    #for item in os.listdir():
    #    if os.path.isdir(item):
    #       result1.append(item)
    return result1