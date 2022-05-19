import os
import shutil
import glob
import sys
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
    print('11- выход.')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        folder_name = input('Введите название папки: ')
        if not folder_name.endswith('.py'):
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
                print(os.listdir())
                pass
            else:
                print('Такая папка уже существует.')
                pass
        else:
            pass
    elif choice == '2':
        while True:
            print('1- фаил ;')
            print('2- папка;')
            print('3- выход.')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                folder_name = input('Введите название файла: ')
                os.remove(folder_name)
                print(os.listdir())
                pass
            elif choice == '2':
                folder_name = input('Введите название папки: ')
                os.rmdir(folder_name)
                print(os.listdir())
                pass
            elif choice == '3':
                break
            else:
                print('Неверный пункт меню: ')
    elif choice == '3':
        while True:
            print('1- фаил ;')
            print('2- папка;')
            print('3- выход.')

            choice = input('Выберите пункт меню: ')
            if choice == '1':
                folder_name = input('Введите название файла: ')
                new_folder_name = folder_name[0:-3] + '_copy.py'
                shutil.copy(folder_name,new_folder_name)
                print(os.listdir())
                pass
            elif choice == '2':
                folder_name = input('Введите название папки: ')
                new_folder_name = folder_name + '_copy'
                shutil.copytree(folder_name , new_folder_name)
                print(os.listdir())
            elif choice == '3':
                break
            else:
                print('Неверный пункт меню: ')

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
        break
    else:
        print('Неверный пункт меню: ')
