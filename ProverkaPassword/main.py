import getpass
import string
import random

def NewPassword():
    '''Создание нового пароля'''
    dlinapassword = int(input("Введите длину пароля: "))
    if dlinapassword >= 9:
        newpassword = ""
        for i in range(dlinapassword):
            Digit = random.randint(1, 9)
            StrUpper = chr(random.randint(65, 90))
            StrLower = chr(random.randint(97, 122))
            newpassword = StrUpper + str(Digit) + StrLower
        return newpassword
    else:
        NewPassword()



def PrPassword():
    '''Определение степени защищенности пароля'''
    # Запрос пароля из консоли
    Password = getpass.getpass('Enter the password: ')
    # Определяем количество строчных, прописных букв и цифр
    kol_lower = kol_upper = kol_digits = kol_el = 0
    if len(Password) >= 9:
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
        print(NewPassword())
    # Определяем степень защищенности пароля


PrPassword()
