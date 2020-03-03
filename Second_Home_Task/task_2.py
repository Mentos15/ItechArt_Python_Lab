def task_2(num):
    dict = {1: "копейка",
            2: "копейки",
            5: "копеек"}
    if num % 10 == 0 or 4 < num % 10 <= 9 :
        return dict.get(5)
    elif num % 10 == 1:
        if num % 100 ==11:
            return dict.get(5)
        else:
            return dict.get(1)
    else:
        return dict.get(2)


if __name__ == "__main__":
    print(task_2(0))
