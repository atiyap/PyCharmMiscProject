myList = [10, 20, 30]

def print_list():
    try:
        print(myList[5])

    except IndexError:
        print("Index out of bound")

print_list()


def addition():
    try:
        result = 5 + "hello"
        return result

    except TypeError:
        return "String and Integer could not be added"

print(addition())
