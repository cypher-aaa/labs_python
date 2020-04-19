import argparse


def count_bits(number):
    """Функция считает количество 1-иц в двоичном представлении number."""
    count = 0
    while (number):
        number &= (number-1)
        count += 1
    return count


def main():
    """Если число меньше 1 или не натуральное, то программа выводит 'Нет'.
    Если количество 1, подсчитанных через count_bits(), равно 1, то выводит
    'Да'. В иных случаях, программа выводит 'Нет'.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="enter n")
    args = parser.parse_args()
    if args.n:
        try:
            num = float(args.n)
            if(num < 1 or num % 1 != 0):
                print("Нет.")
            elif (count_bits(int(num)) == 1):
                print("Да.")
            else:
                print("Нет.")
        except ValueError:
            print("Некорректный ввод.")
    else:
        print("Введите число:")
        while (True):
            try:
                num = float(input())
                if (num < 1 or num % 1 != 0):
                    print("Нет.")
                elif (count_bits(int(num)) == 1):
                    print("Да.")
                else:
                    print("Нет.")
                break
            except ValueError:
                print("Пожалуйста, введите одно число.")


if __name__ == "__main__":
    main()
