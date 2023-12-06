values = input().split()
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
equality = ["+", "-", "/", "*"]


def add(values):
    number = []
    for i in values:
        if i in numbers:
            number.append(int(i))
    return sum(number)


def subtract(values):
    number = []
    for i in values:
        if i in numbers:
            number.append(int(i))
    return number[0] - number[1]

def multiply(values):
    number = []
    for i in values:
        if i in numbers:
            number.append(int(i))
    return number[0] * number[1]

def divide(values):
    number = []
    for i in values:
        if i in numbers:
            number.append(int(i))
    return number[0] // number[1]


def calculator(values):
    try:
        for i in values:
            if '+' in values:
                result = add(values)
            elif '-' in values:
                result = subtract(values)
            elif '*' in values:
                result = multiply(values)
            elif '/' in values:
                result = divide(values)

        return result

    except:
        return 'throws Exception'


print(calculator(values))
