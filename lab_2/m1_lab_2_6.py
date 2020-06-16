from json import dumps


def from_json(text):
    if text.endswith(".txt"):
        with open(text, 'r') as f:
            line = f.readline()
            return from_json(line)
    else:
        if text.startswith(("{", "[")):
            return json_object(text)

        elif text == 'true':
            return True

        elif text == 'false':
            return False

        elif text == 'null':
            return None

        else:
            return eval_str(text)


def eval_str(string: str) -> (int, float, str):
    if string.replace('.', '').isdigit():
        sign = ""
    elif string[1:].replace('.', '').isdigit():
        sign = "-"
        string = string[1:]
    else:
        return string[1:-1]

    numDict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
    num = 0

    if "." in string:
        string = string.split(".")
        num = eval_str(string[0]) + eval_str(string[1])/10**len(string[1])
    else:
        string = [char for char in string]
        count = len(string)
        for elem in string:
            count -= 1
            for key in numDict:
                if elem == key:
                    num += numDict[key] * 10**count
                    break

    return -num if sign else num


def json_object(string: str) -> (list, dict):
    new_object = {} if string[0] == "{" else []
    string = string[1:-1]
    array = []
    old = 0

    while True:
        new = string.find(', ', old)
        while True:
            if new == -1:
                array.append(string[old:])
                break
            elif string[old:new].count('[') == string[old:new].count(']') and \
                 string[old:new].count('{') == string[old:new].count('}'):
                    array.append(string[old:new])
                    break
            else:
                new = string.find(', ', new+2)
        if new == -1:
            break
        old = new + 2

    length = len(array)
    i = 0
    while i < length:
        if isinstance(new_object, list):
            array[i] = from_json(array[i])
        else:
            key, value =[from_json(x) for x in array[i].split(': ', 1)]
            new_object.update({key: value})
        i += 1

    return array if isinstance(new_object, list) else new_object


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
    test = dumps(py_obj)
    print(from_json(test))


if __name__ == "__main__":
    main()
