def task_2():
    input_ = input("Введите числа через пробел: ")
    input2_ = int(input("Введите число которое хотите найти в первой строке(отсчет от нуля)"))
    list = [int(x) for x in input_.split()]
    print("Идексы на которых стоит второе введенное число: ", end = " ")
    for i in range(len(list)):
        if input2_ == list[i]:
            print(i,end = " ")
task_2()