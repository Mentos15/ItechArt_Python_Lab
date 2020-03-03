def task_1():
    num = int(input("Введите число"))
    count = 0
    for i in range(0, num+1):
        for j in range(0, i):
            count += 1
            print(i, end=" ")
            if count == num:
                break
        if count == num:
            break
task_1()





