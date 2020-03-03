def task_4(num):
    str = ""
    if num[0] == " ":
        print("у вас первый элемент это пробел, вводите число без пробелов")
        return False
    if len(num) == 3:
        str += hundreds(num[0])
        if int(num[1]) == 1 and int(num[2]) >= 0 and int(num[2]) <= 9:
            lens = num[1] + num[2]
            str += tens(lens)
        else:
            str += tens(num[1])
            str += one(num[2])
    elif len(num) == 2:
        if int(num[0]) == 1 and int(num[1]) >= 0 and int(num[1]) <= 9:
            lens = num[0] + num[1]
            str += tens(lens)
        else:
            str += tens(num[0])
            str += one(num[1])
    elif len(num) == 1:
        str += one(num[0])
    else:
        print("Посмотрите не стоит ли пробел после числа ")
        return False
    return str


def hundreds(num):
    dict = {
        1: " сто",
        2: " двести",
        3: " триста",
        4: " четыреста",
        5: " пятьсот",
        6: " шестьсот",
        7: " семьсот",
        8: " восемьсот",
        9: " девятьсот"
    }
    return dict.get(int(num))


def tens(num):
    dict = {
        0: "",
        2: " двадцать",
        3: " тридцать",
        4: " сорак",
        5: " пятьдесят",
        6: " шестьдесят",
        7: " семьдесят",
        8: " восемьдесят",
        9: " девяноста",
        10: " Десять",
        11: " одиннадцать",
        12: " Двенадцать",
        13: " Тринадцатт",
        14: " Четырнадцать",
        15: " Пятнадцать",
        16: " Шестнадцать",
        17: " Семьнадцать",
        18: " Восемьнадцать",
        19: " Девятнадцать"
    }
    return dict.get(int(num))


def one(num):
    dict = {
        0: "",
        1: " одна",
        2: " две",
        3: " три",
        4: " четыре",
        5: " пять",
        6: " шесть",
        7: " семь",
        8: " восемь",
        9: " девять"
    }
    return dict.get(int(num))



if __name__ == "__main__":
    inpt = input("Введите число(не отступая от этого текста)")
    print(task_4(inpt))
