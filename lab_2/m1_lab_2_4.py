import argparse


def flatten_it(array):
    for elem in array:
        if type(elem) != list:
            yield elem
        elif elem == array:
            raise ValueError
        else:
            for x in flatten_it(elem):
                    yield x


def output(array):
    try:
        result = [x for x in flatten_it(eval(array))]
        print('Flattened array:', result)
    except ValueError:
        print("Ошибка! Бесконечный цикл вложенности.")


def main():
    # При запуске с аргументами командной строки
    # массив вводится в кавычках. Например:
    # "[1, 2, [3, 4, 5], [6, [7, 8]]]"
    parser = argparse.ArgumentParser()
    parser.add_argument("--arr", help="enter array to linearize")
    args = parser.parse_args()

    output(args.arr if args.arr else input("Введите массив: "))


if __name__ == "__main__":
    main()
