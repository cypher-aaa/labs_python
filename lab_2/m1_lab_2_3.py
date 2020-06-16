import argparse
from sys import stdout


def status_bar(final):
    def current_status(current):
        curr = int(current/(final/20))
        status = '[' + '#'*curr + '-'*(20-curr) + ']'
        stdout.write('\r' + status + " " + "{:,}".format(current) + " out of " +
                     "{:,}".format(final) + " lines")
        stdout.flush()
    return current_status


def merge_line(line):
    flag = False
    if ' ' in line:
        line = line.split()
        flag = True

    if len(line) > 1:
        mid = len(line)//2
        left, right = line[:mid], line[mid:]

        left, right = merge_line(left), merge_line(right)

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
        left, right = file[:mid], file[mid:]
        
        left, right = merge_file(left), merge_file(right)

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
                f.write('\n')
                bar(file.index(line))
            bar(len(file))
    else:
        return file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="enter name of file to sort")
    args = parser.parse_args()
    if(args.file):
        with open(args.file, 'r') as f:
            merge_file(f)
    else:
        name = input("Введите имя файла: ")
        with open(name, 'r') as f:
            merge_file(f)
    print("\nTask finished successfully! For results, check 'Merge It.txt'.")


if __name__ == "__main__":
    main()
