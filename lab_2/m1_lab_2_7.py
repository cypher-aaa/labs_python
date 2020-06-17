import argparse


def fib(n):
    "Функция находит и возвращает n-ное число Фибоначчи."
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, int(n)+1):
            c = a + b
            a = b
            b = c
        return b


def leonardo(num):
    "Функция находит и возвращает n-ное число Леонардо через Фибоначчи."
    if (num < 0 or num % 1 != 0):
        print("N должно быть натуральным числом или 0!")
    elif (num == 0 or num == 1):
        return 1
    else:
        return (2*fib(num + 1) - 1)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", help="enter n")
    args = parser.parse_args()
    if args.n:
        try:
            if leonardo(float(args.n)):
                print("Ваше число:", leonardo(float(args.n)))
        except ValueError:
            print("Некорректный ввод.")
    else:
        print("Введите n (номер числа Леонардо):", end="")
        while True:
            try:
                res = leonardo(float(input()))
                if res:
                    break
            except ValueError:
                print("Пожалуйста, введите одно число (n).", end="")
        print("Ваше число:", res)


if __name__ == "__main__":
    main()
