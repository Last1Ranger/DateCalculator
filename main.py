import datetime as dt
a = ""
while a != "Стоп" and a != "стоп":

    firstdate = dt.datetime(int(input("Введите год")), int(input("Введите месяц")), int(input("Введите день")), int(input("Введите часы")), int(input("Введите минуты")))
    secconddate = dt.datetime(int(input("Введите год")), int(input("Введите месяц")), int(input("Введите день")), int(input("Введите часы")), int(input("Введите минуты")))

    print("Эта программа умеет:")  # пердставляется выбор операций
    print("1. Умножать")
    print("2. Делить")
    print("3. Вычислять остаток от деления")
    print("4. Выполнять целочисленное деление")
    print("5. Возводить в степень")
    print("6. Вычитать")
    print("7. Складывать")
    operation = int(input("Введите номер операции: "))
    if operation == 1:  # Операция сравнивается с её номером и выполняется соотвецтвенное действие, вслед за чем
        totaldate = dt.datetime(firstdate.year * secconddate.year, firstdate.month * secconddate.month, firstdate.day * secconddate.day, firstdate.hour * secconddate.hour, firstdate.minute * secconddate.minute)
        print(totaldate)  # происходит вывод итога данной операции
    elif operation == 2:
        print(firstdate / secconddate)
    elif operation == 3:
        print(firstdate % secconddate)
    elif operation == 4:
        print(firstdate // secconddate)
    elif operation == 5:
        print(firstdate ** secconddate)
    elif operation == 6:
        print(firstdate + secconddate)#d
    elif operation == 7:
        print(firstdate - secconddate)
    a = str(input("Хотите продолжить? Если нет, то просто введите Стоп."))

print("Спасибо, что воспользовались нашим калькулятором дат!")