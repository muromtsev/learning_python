import string
import random
import os, sys


def pwdgen(lenght_pwd=10, count_pwd=10, symbols=string.ascii_letters + string.punctuation + string.digits): 
    list_pwd = []
    while count_pwd >= 0:
        pwd = ''
        for _ in range(lenght_pwd):
            pwd += random.choice(symbols)
        list_pwd.append(pwd)
        count_pwd -= 1
    return list_pwd


def create_symbols(id):
    if id == '1':
        return string.ascii_letters
    elif id == '2':
        return string.ascii_letters + string.digits
    elif id == '3':
        return string.ascii_letters + string.digits + string.punctuation
    elif id == '4':
        return ''.join([symbol for symbol in (string.ascii_letters + string.digits + string.punctuation) if symbol not in 'il1Lo0O'])
    elif id == '5':
        return sys.exit()
    else:
        print('Ошибка. Нет такого пункта.')
        

def show_menu():
    
    menu_list = {
        '1': 'Латинские буквы',
        '2': 'Латинские буквы и цифры',
        '3': 'Латинские буквы, цифры и символы',
        '4': 'Исключить неоднозначные символы (il1Lo0O)',
        '5': 'Exit',
    }

    for key, val in menu_list.items():
        print(f"{key}. {val}")


def create_txt_file(date):
    with open('passwdrds.txt', 'w', encoding='utf-8') as file:
        for d in date:
            file.write(d+'\n')


while True:
    os.system('cls')
    print('----- PASSWORD GENERATOR -----')
    
    show_menu()

    menu_id = input('> Выберите пункт меню: ')
    SYMBOLS = create_symbols(menu_id)
    if SYMBOLS:
        os.system('cls')
        print('----- PASSWORD GENERATOR -----')

        LENGHT_PWD = input('> Длина пароля: ')
        COUNT_PWD = input('> Количество паролей: ')
        if LENGHT_PWD.isdigit() and COUNT_PWD.isdigit():
            LENGHT_PWD = int(LENGHT_PWD)
            COUNT_PWD = int(COUNT_PWD)
        else:
            print('[INFO] Необходимо ввести число')
            sys.exit()

        os.system('cls')

        pwds = pwdgen(lenght_pwd=LENGHT_PWD, count_pwd=COUNT_PWD, symbols=SYMBOLS)

        print('----- PASSWORD GENERATOR -----')
        print('-'*20) 
        print(*pwds, sep='\n')
        print('-'*20)
        
        print(*['--[INFO]--', '1. Меню', '2. Записать в txt-файл', '3. Выход'], sep='\n')
        question = input('> ')

        if question == '1':
            os.system('cls')
            show_menu()
        elif question == '2':
            create_txt_file(pwds)
            sys.exit()
        elif question == '3':
            os.system('cls')
            sys.exit()
        else:
            sys.exit()
