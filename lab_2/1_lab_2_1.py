from math import ceil, sqrt


def sqrt_decomp(array, l, r):
    "preprocessing"
    arr_len = len(array)
    b_len = ceil(sqrt(arr_len))
    blocks = [0] * b_len
    for i in range(arr_len):
        blocks[i // b_len] += array[i]

    "calculating the sum"
    res, cl, cr = 0, l//arr_len, r//arr_len
    if cl == cr:
        for i in range(l, r+1):
            res += array[i]
    else:
        for i in range(l, (cl+1)*arr_len):
            res += array[i]
        for i in range(cl+1, cr):
            res += blocks[i]
        for i in range(cr*arr_len, r+1):
            res += array[i]
    return res


def check_arr(array):
    try:
        arr = [float(x) for x in array.split()]
        if len(arr) < 2:
            print("Должно быть хотя бы два элемента.", end="")
        else:
            return arr
    except ValueError:
        print("Убедитесь, что все элементы массива - числа.", end="")
    return []


def check_limits(lim, arr):
    try:
        limits = [float(x) for x in lim.split()]
        if len(limits) != 2:
            print("Должно быть ровно 2 границы!", end="")
        elif limits[0] >= limits[1]:
            print("Границы не упорядочены (левая правая)!", end="")
        elif limits[0] < 0 or limits[1] >= len(arr):
            print("Границы выходят за пределы массива!", end="")
        elif limits[0] % 1 != 0 or limits[1] % 1 != 0:
            print("Границы должны быть целочисленными!", end="")
        else:
            limits = [int(x) for x in lim.split()]
            return limits
    except ValueError:
        print("Границы должны быть числами!", end="")
    return []


def manual():
    """Ручной ввод массива и границ."""
    print("Введите массив чисел:", end="")
    while True:
        arr = check_arr(input())
        if arr:
            break

    print("Введите границы суммы (left right):", end="")
    while True:
        limits = check_limits(input(), arr)
        if limits:
            break

    print("Сумма на отрезке", limits, ":",
          sqrt_decomp(arr, limits[0], limits[1]))


def from_file():
    """Считывание данных из файла. Массив находиться в одной строчке,
    границы - в другой. Например:
    1 2 3 4 5 6 7 8 9
    2 5
    """
    print("Введите путь к файлу:", end="")
    while True:
        try:
            with open(input(), "r") as f:
                arr = check_arr(f.readline())
                limits = check_limits(f.readline(), arr)
                if arr and limits:
                    print("Сумма на отрезке", limits, ":",
                          sqrt_decomp(arr, limits[0], limits[1]))
            break
        except FileNotFoundError:
            print("Введите корректный путь к файлу!")


def main():
    print("Выберите способ ввода (1 - вручную, 2 - чтение из файла, quit - выход):", end="")
    while True:
        menu = input()
        if menu == "1":
            manual()
            break
        elif menu == "2":
            from_file()
            break
        elif menu == "quit":
            print("Terminating program...")
            raise SystemExit
        else:
            print("Некорректный ввод.", end="")


if __name__ == "__main__":
    main()
