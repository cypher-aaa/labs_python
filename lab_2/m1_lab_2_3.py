import argparse
from sys import stdout


def status_bar(current, final):
    curr = int(current/(final/20))
    status = '[' + '#'*curr + '-'*(20-curr) + ']'
    stdout.write("\r" + status + " " + "{:,}".format(current) + " out of " +
                 "{:,}".format(final) + " lines")
    stdout.flush()


def merge_line(line):
    if ' ' in line:
        line = line.split()

    if len(line) > 1:
        mid = len(line)//2
        left = line[:mid]
        right = line[mid:]

        merge_line(left)
        merge_line(right)

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

        line = " ".join(line)

    return line


def merge_file(file):
    flag = False
    if type(file) != list:
        file = file.readlines()
        flag = True

    if len(file) > 1:
        mid = len(file)//2
        left = file[:mid]
        right = file[mid:]

        merge_file(left)
        merge_file(right)

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
            for line in file:
                f.write(merge_line(line))
                f.write('\n')
                status_bar(file.index(line), len(file))
            status_bar(len(file), len(file))


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
