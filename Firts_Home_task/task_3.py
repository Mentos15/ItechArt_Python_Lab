def task_3():
    inpt = input("Вводите матрицу строками  и числами через пробел в конце напишите 'end' без кавычек")
    matrix = []
    k = 0

    while inpt != "end":
        matrix.append([])
        list = [int(x) for x in inpt.split()]
        for c in range(len(list)):
            matrix[k].append(list[c])
        if len(list) != len(matrix[k-1]):
            print("Несоответствие количества элементов в строках")
            return False
        k += 1
        inpt = input()

    for r in matrix:
        print(r)
    print("Полученная матрица")
    matrix2 = []
    for i in range(len(matrix)):
        matrix2.append([])
        for y in range(len(matrix[i])):
            a = matrix[i][y - 1] + matrix[i][y] + matrix[i - 1][y] + matrix[(i + 1) % len(matrix[i])][y] + matrix[i][
                (y + 1) % len(matrix[y])]
            matrix2[i].append(a)

    for r in matrix2:
        print(r)
task_3()