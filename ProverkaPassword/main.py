import string
import random
import sys
import time
import pyperclip

def NewPassword():
    '''Создание нового пароля'''
    print("\033[35m{}".format("Обработка..."))
    time.sleep(2)
    print("Создаем новый пароль!")
    time.sleep(1)
    dlinapassword = int(input("Введите длину пароля(минимальаня длина - 7 символов): "))
    if dlinapassword >= 7:
        '''Создаем 5 уникальных паролей'''
        k = 1
        SavePassword = ""
        while k != 6:
            Password = ""
            for i in range(dlinapassword):
                Digit = random.randint(1, 9)
                StrUpper = chr(random.randint(65, 90))
                StrLower = chr(random.randint(97, 122))
                Password += StrUpper + str(Digit) + StrLower
            SavePassword = Password[0:dlinapassword]
            print("\033[33m{}-{}".format( k, Password[0:dlinapassword]))
            k += 1
        pyperclip.copy(SavePassword[0:dlinapassword])
        print("\033[34m{}".format("Последний пароль был скопирован в буфер обмена!"))
        print("ПРОГРАММА ЗАВЕРШЕНА ")
        sys.exit()
    else:
        print("\033[31m{}".format("Ошибка! Минимальная длина пароля - 7 символов"))
        NewPassword()

def PrPassword():
    '''Определение степени защищенности пароля'''
    Password = str(input("\033[32m{}".format("Введите пароль: ")))
    # Определяем количество строчных, прописных букв и цифр
    kol_lower = kol_upper = kol_digits = kol_el = 0
    if len(Password) >= 7:
        for char in list(Password):
            if char in string.ascii_lowercase:
                kol_lower += 1
            elif char in string.ascii_uppercase:
                kol_upper += 1
            elif char in string.digits:
                kol_digits += 1
        if kol_lower >= 2 and kol_upper >= 3  and kol_digits >= 2:
            print("\033[33m{}".format("Ваш пароль безопасен! \n ПРОГРАММА ЗАВЕРШЕНА"))
            sys.exit()
        else:
            print("\033[31m{}".format("Ваш пароль небезопасен!"))
            NewPassword()
    else:
        print("\033[31m{}".format("Ваш пароль небезопасен!"))
        NewPassword()

if __name__ == "__main__":
    print("\033[31m{}".format("PROGRAMME SECURITY PASSWORDS"))
    print("\033[3m\033[34m{}".format("ФУНКЦИИ: \n 1) Проверить пароль на безопасность \n 2) Создать новый пароль"))
    nomer = int(input("Выберите действие - "))
    if nomer == 1:
        PrPassword()
    elif nomer == 2:
        NewPassword()
    else:
        print("\033[31m{}".format("Error! Invlaid value! "))
