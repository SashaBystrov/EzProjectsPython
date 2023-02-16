import getpass
import string
import random
import time

def NewPassword():
    '''Создание нового пароля'''
    time.sleep(1)
    print("Обработка...")
    time.sleep(2)
    print("Создаем новый пароль!")
    time.sleep(1)
    dlinapassword = int(input("Введите длину пароля: "))
    listpas = []
    if dlinapassword >= 7:
        for i in range(dlinapassword // 2):
            Digit = listpas.append(random.randint(1, 9))
            StrUpper = listpas.append(chr(random.randint(65, 90)))
            StrLower = listpas.append(chr(random.randint(97, 122)))
        return listpas[0:dlinapassword]
    else:
        print("Минимальная длина пароля - 7 символов")
        NewPassword()



def PrPassword():
    '''Определение степени защищенности пароля'''
    # Запрос пароля из консоли
    Password = str(input("Введите пароль: "))
    #Password = getpass.getpass('Enter the password: ')
    # Определяем количество строчных, прописных букв и цифр
    kol_lower = kol_upper = kol_digits = kol_el = 0
    if len(Password) >= 7:
        for char in list(Password):
            if char.islower():
                kol_lower += 1
                if kol_lower >= 2:
                    kol_el += 1
            elif char.isupper():
                kol_upper += 1
                if kol_upper >= 3:
                    kol_el += 1
            elif char in string.digits:
                kol_digits += 1
                if kol_upper >= 2:
                    kol_el += 1

    else:
        print("Ваш пароль небезопасен!")
        print(NewPassword())
    # Определяем степень защищенности пароля


PrPassword()
