def to_json(obj, file=''):
    if file:
        with open(file, 'w') as f:
            f.write(to_json(obj))
    else:
        if isinstance(obj, dict):
            string = "{"
            for elem in obj:
                string += to_json(elem) + ": " + to_json(obj[elem])
                if elem != list(obj)[-1]:
                    string += ", "
                else:
                    string += "}"
            return string
        elif isinstance(obj, (list, tuple)):
            string = "["
            for elem in obj:
                string += to_json(elem)
                if obj.index(elem) != len(obj)-1:
                    string += ", "
                else:
                    string += "]"
            return string
        elif isinstance(obj, str):
            return '"' + obj + '"'
        elif isinstance(obj, type(None)):
            return 'null'
        elif isinstance(obj, bool):
            if obj is True:
                return 'true'
            else:
                return 'false'
        elif isinstance(obj, (int, float)):
            return num_to_str(obj)
        else:
            raise ValueError


def split_num(num):
    array = []
    sign = ""
    if num < 0:
        sign = "-"
        num = -num
    elif num == 0:
        array = [0]
    temp = num
    while(temp):
        digit = temp % 10 // 1
        array = [digit] + array
        temp //= 10

    if isinstance(num, float):
        array += ["."]
        if num % 1 == 0:
            array += [0]
        else:
            temp = num
            while temp % 1 != 0:
                temp *= 10
                digit = temp % 10 // 1
                array += [digit]
    if sign:
        array = [sign] + array

    return array


def num_to_str(num):
    numDict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    num = split_num(num)
    string = ""
    for elem in num:
        if elem == "." or elem == "-":
            string += elem
        for key in numDict:
            if numDict[key] == elem:
                string += key
                break

    return string


def main():
    py_obj = {
      "name": "John",
      "age": 30,
      "married": True,
      "divorced": False,
      "children": ("Ann", "Billy"),
      "pets": None,
      "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
      ]
    }

    print(to_json(py_obj))
    to_json(py_obj, 'Json.txt')


if __name__ == "__main__":
    main()
