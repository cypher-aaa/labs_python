import argparse


def count_bits(number):
    """Функция считает количество 1-иц в двоичном представлении number."""
    count = 0
    while (number):
        number &= (number-1)
        count += 1
    return count


def is_power(num):
    """Если число меньше 1, не натуральное или количество единиц в его
    двоичном представлении не равно 1, то функция возвращает
    False. В иных случаях - True.
    """
    if (num < 1 or num % 1 != 0 or count_bits(int(num)) != 1):
        return False
    else:
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="enter n")
    args = parser.parse_args()
    if args.n:
        try:
            if (is_power(float(args.n))):
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
                if (is_power(num)):
                    print("Да.")
                else:
                    print("Нет.")
                break
            except ValueError:
                print("Пожалуйста, введите одно число.")


if __name__ == "__main__":
    main()
