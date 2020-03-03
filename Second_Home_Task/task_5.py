import task_3
import task_2
import task_1
import task_4


def task_5(num):
    lst = num.split('.')
    print(task_3.task_3((lst[0])),end=' ')
    print(task_1.task_1(int(lst[0])),end=' ')
    print(task_4.task_4((lst[1])), end=' ')
    print(task_2.task_2(int(lst[1])), end=' ')



if __name__ == "__main__":

    inpt = input("Введите число типо float через точку(.)")
    task_5(inpt)
