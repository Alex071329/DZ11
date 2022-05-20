import sys
import shutil
import glob
import os
import platform

while True:
    print('1- создать папку;')
    print('2- удалить(файл / папку);')
    print('3- копировать(файл / папку);')
    print('4- просмотр содержимого рабочей директории;')
    print('5- посмотреть только папки;')
    print('6- посмотреть только файлы;')
    print('7- просмотр информации об операционной системе;')
    print('8- создатель программы;')
    print('9- играть в викторину;')
    print('10- мой банковский счет;')
    print('11- смена рабочей директории;')
    print('12- выход.')
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
        print(list(set(os.listdir()) - set(glob.glob('*.py'))))
        pass
    elif choice == '6':
        print(glob.glob('*.py'))
        pass
    elif choice == '7':
        print('My OS is', sys.platform, '(', os.name, ')')
        print(platform.uname())
        pass
    elif choice == '8':
        print('Салухов Александр - 37 лет.')
        pass
    elif choice == '9':
        from functions import victory
        victory()
        pass
    elif choice == '10':
        from functions import my_bank_account
        my_bank_account()
        pass
    elif choice == '11':
        directory_name = input('Введите название папки или путь до неё : ')
        os.chdir(directory_name)
        print(os.getcwd())
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню: ')
