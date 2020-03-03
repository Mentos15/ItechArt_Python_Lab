def task_4():
    inpt = int(input("Введите размер матрицы"))
    count = 1  # для того, чтобы увеличивать вставляемое число в матрицу
    list = [[0] * inpt for i in range(inpt)]
    help = 0
    for i in range(inpt - 1):

        for j in range(inpt - help):  # верхнюю строку заполняю
            list[i][j + i] = count
            count += 1
        for j in range(i + 1, inpt - i):  # правый столбец заполняю
            list[j][-i - 1] = count
            count += 1

        for j in range(i + 1, inpt - i):  # нижнюю строку заполняю
            list[-i - 1][-j - 1] = count
            count += 1
        for j in range(i + 1, inpt - (i + 1)):  # левуй столбец заполняю
            list[-j - 1][i] = count
            count += 1
        help += 2
    for i in list:
        print(*i)  # распаковка, чтобы были просто числа, без [] и запятых


task_4()
