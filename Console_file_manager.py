import sys
import os
import platform
from functions import foldernames,filenames
while True:
    print('1- создать папку;')
    print('2- удалить(файл / папку);')
    print('3- копировать(файл / папку);')
    print('4- просмотр содержимого рабочей директории;')
    print('5-сохранить содержимое рабочей директории в файл')
    print('6- посмотреть только папки;')
    print('7- посмотреть только файлы;')
    print('8- просмотр информации об операционной системе;')
    print('9- создатель программы;')
    print('10- играть в викторину;')
    print('11- мой банковский счет;')
    print('12- смена рабочей директории;')
    print('13- выход.')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        folder_name = input('Введите название папки: ')
        if not folder_name.endswith('.py'):
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                pass
            else:
                print('Такая папка уже существует.')
                pass
        else:
            pass
    elif choice == '2':
        from functions import menu_item,remove_file,delete_folder,copy_file,copy_folder
        menu_item(a=remove_file,b=delete_folder)

    elif choice == '3':
        from functions import menu_item, remove_file, delete_folder, copy_file, copy_folder
        menu_item(a=copy_file,b=copy_folder)

    elif choice == '4':
        print(os.listdir())
        pass
    elif choice == '5':
        with open('listdir.txt', 'w') as f:
            f.write(f'files: ')
            f.writelines(','.join(filenames()))
            f.write(f'\ndirs: ')
            f.writelines(','.join(foldernames()))

        with open('listdir.txt', 'r') as f:
            result = f.read()
            print(result)
        pass
    elif choice == '6':
        print(foldernames())
        pass
    elif choice == '7':
        print(filenames())
        pass
    elif choice == '8':
        print('My OS is', sys.platform, '(', os.name, ')')
        print(platform.uname())
        pass
    elif choice == '9':
        print('Салухов Александр - 37 лет.')
        pass
    elif choice == '10':
        from functions import victory
        victory()
        pass
    elif choice == '11':
        from functions import my_bank_account
        my_bank_account()
        pass
    elif choice == '12':
        directory_name = input('Введите название папки или путь до неё : ')
        os.chdir(directory_name)
        print(os.getcwd())
        pass
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню: ')
