import argparse
from sys import stdout
from random import choice, choices
from string import ascii_letters


def generate_word(l):
    w_length = choice(range(l[0], l[1] + 1))
    word = "".join(choices(ascii_letters, k=w_length))
    return word


def generate_line(k, l):
    w_count = choice(range(k[0], k[1] + 1))
    line = " ".join([generate_word(l) for x in range(w_count)])
    return line


def generate_file(name, size_mb, k, l):
    print("Генерация файла...")
    size_b = int(1024**2*size_mb)
    f_size = 0
    with open(name, "w+") as f:
        bar = status_bar(size_b)
        while f_size < size_b:
            bar(f_size)
            new_line = generate_line(k, l)
            new_word = generate_word(l)
            if f_size + len(new_line) <= size_b:
                f.write(new_line)
                f_size += len(new_line)
                if f_size + 2 <= size_b:
                    f.write("\n")
                    f_size += 2
            elif f_size + len(new_word) <= size_b:
                f.write(new_word)
                f_size += len(new_word)
                if f_size + 1 <= size_b:
                    f.write(" ")
                    f_size += 1
            else:
                tail = size_b - f_size
                if tail in range(l[0], l[1] + 1):
                    new_word = generate_word((tail, tail))
                    f.write(new_word)
                    f_size += len(new_word)
                else:
                    f.write(" " * tail)
                    f_size += tail
        bar(f_size)
    print("\n"+"All done!")


def status_bar(final):
    def current_status(current):
        curr = int(current/(final/20))
        status = '[' + '#'*curr + '-'*(20-curr) + ']'
        stdout.write('\r' + status + " " + "{:,}".format(current) + " out of " +
                     "{:,}".format(final) + " bytes")
        stdout.flush()
    return current_status


def check_name(name):
    if name.endswith(".txt"):
        try:
            f = open(name, "w")
            f.close()
            return name
        except OSError:
            print("Некорректное имя файла!", end="")
    else:
        print("Имя файла должно заканчиваться на '.txt'!", end="")
    return None


def check_size(size):
    try:
        size = float(size)
        if size > 0:
            return size
        else:
            print("Размер файла должен быть положительным!", end="")
    except ValueError:
        print("Некорректный ввод!", end="")
    return None


def check_k(k):
    try:
        if k:
            k = tuple(map(int, k.split(',')))
            if k[0] <= k[1]:
                return k
            else:
                print("Введите числа по порядку!", end="")
        else:
            k = (10, 100)
            return k
    except ValueError:
        print("Некорректный ввод!", end="")
    return None


def check_l(l):
    try:
        if l:
            l = tuple(map(int, l.split(',')))
            if l[0] <= l[1]:
                return l
            else:
                print("Введите числа по порядку!", end="")
        else:
            l = (3, 10)
            return l
    except ValueError:
        print("Некорректный ввод!", end="")
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="enter name")
    parser.add_argument("--size", help="enter size")
    parser.add_argument("--k", help="enter k (optional)")
    parser.add_argument("--l", help="enter l (optional)")
    args = parser.parse_args()
    if args.name:
        name = check_name(args.name)
        size = check_size(args.size)
        k = check_k(args.k)
        l = check_l(args.l)
        if (name and size and k and l):
            generate_file(name, size, k, l)
    else:
        print("Введите имя файла (расширение - .txt): ", end="")
        while True:
            name = check_name(input())
            if name:
                break
        print("Введите размер файла (Mb):", end="")
        while True:
            size = check_size(input())
            if size:
                break
        print("Введите k через запятую ('ввод' для значения по умолчанию):",
              end="")
        while True:
            k = check_k(input())
            if k:
                break
        print("Введите l через запятую ('ввод' для значения по умолчанию):",
              end="")
        while True:
            l = check_l(input())
            if l:
                break
        generate_file(name, size, k, l)


if __name__ == "__main__":
    main()
