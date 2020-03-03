def task_1(num):
    if num % 10 == 0 or num % 10 > 4 and num % 10 <= 9:
        return "рублей"
    elif num % 10 == 1:
        if num % 100 == 11:
            return "рублей"
        else:
            return "рубль"
    elif num % 10 > 1 and num % 10 < 5:
        return "рубля"


if __name__ == "__main__":
    print(task_1(131))
