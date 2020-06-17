import argparse
from sys import stdout


def status_bar(final):
    def current_status(current):
        curr = int(current/(final/20))
        status = '[' + '#'*curr + '-'*(20-curr) + ']'
        stdout.write("\r{} {:,} out of {:,} lines".format(status, current,
                                                          final))
        stdout.flush()
    return current_status


def merge_line(line):
    flag = False
    if ' ' in line:
        line = line.split()
        flag = True

    if len(line) > 1:
        mid = len(line)//2
        left, right = merge_line(line[:mid]), merge_line(line[mid:])

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                line[k] = left[i]
                i += 1
            else:
                line[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            line[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            line[k] = right[j]
            j += 1
            k += 1
        
        if flag:
            line = " ".join(line)

    return line


def merge_file(file):
    flag = False
    if type(file) != list:
        file = file.readlines()
        flag = True

    if len(file) > 1:
        mid = len(file)//2
        left, right = merge_file(file[:mid]), merge_file(file[mid:])

        i = j = k = 0

        while i < len(left) and j < len(right):
            if len(left[i]) < len(right[j]):
                file[k] = left[i]
                i += 1
            else:
                file[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            file[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            file[k] = right[j]
            j += 1
            k += 1

    if flag:
        with open('Merge It.txt', 'w') as f:
            print('\tСортировка файла...')
            bar = status_bar(len(file))
            for line in file:
                f.write(merge_line(line))
                if file.index(line) != len(file)-1:
                    f.write('\n')
                bar(file.index(line)+1)
    else:
        return file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="enter name of file to sort")
    args = parser.parse_args()

    name = args.file if args.file else input("Введите имя файла: ")
    with open(name, 'r') as f:
        merge_file(f)
    print("\nTask finished successfully! For results, check 'Merge It.txt'.")


if __name__ == "__main__":
    main()
