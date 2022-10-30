def romantoInteger(number):
    roman_numbers = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    test_value = 0  # value that contains the last answer

    for x in range(0, len(number)):
        if x + 1 < len(number) and roman_numbers[number[x]] < roman_numbers[number[x + 1]]:
            test_value = test_value - roman_numbers[number[x]]
        else:
            test_value = test_value + roman_numbers[number[x]]

    return test_value


def integerToRoman(number):
    roman_number = [["I", 1], ["IV", 4], ['V', 5], ['IX', 9], ['X', 10],
                    ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400],
                    ['D', 500], ['CM', 900], ['M', 1000]
                    ]

    test_value = ''
    for symbol, value in reversed(roman_number):
        if number // value != 0:
            count = number // value
            test_value = test_value + (symbol * count)
            number = number % value

    return test_value


def isValidNumber(element):
    test_arr1 = []
    for x in element:
        if not (x in test_arr1):
            test_arr1.append(x)
    test_arr2 = []
    for x in test_arr1:
        test_arr2.append(element.count(x))
    bool_test = 0
    for x in test_arr2:
        if x > 3:
            bool_test = bool_test + 1

    if bool_test == 0:
        return True
    else:
        return False


def isValidOp(element):
    arr = ['*', '/', '+', '-']
    if element in arr:
        return True
    else:
        return False


def calculateAnswer(element1, element2, ope):
    last_answer = ''
    if ope == '*':
        x = romantoInteger(element1)
        y = romantoInteger(element2)
        test_value = x * y
        last_answer = integerToRoman(test_value)
    if ope == '/':
        x = romantoInteger(element1)
        y = romantoInteger(element2)
        test_value = x / y
        last_answer = integerToRoman(test_value)
    if ope == '+':
        x = romantoInteger(element1)
        y = romantoInteger(element2)
        test_value = x + y
        last_answer = integerToRoman(test_value)

    if ope == '-':
        x = romantoInteger(element1)
        y = romantoInteger(element2)
        test_value = x - y
        last_answer = integerToRoman(test_value)

    return last_answer


print("-----------რომაული კალკულატორი-------------")
i = 0
bool_test = True
x_value = ''
while bool_test:
    if i == 0:
        element1 = (input('რიცხვი|>  ')).upper()
        while not isValidNumber(element1):
            print('არასწორი ელემენტი!!!!')
            element1 = (input('რიცხვი|>  ')).upper()
        op = input("ოპერატორი|>  ")
        while not isValidOp(op):
            print("არასწორი ოპერაოტრი!!!!")
            op = input("ოპერატორი|>  ")
        element2 = (input('რიცხვი|>  ')).upper()
        while not isValidNumber(element2):
            print('არასწორი ელემენტი!!!!')
            element2 = (input('რიცხვი|>  ')).upper()
        answer = calculateAnswer(element1, element2, op)
        check_test = input("თუ გინდა რომ დაამატო ოპერატორი შეიყვანე 1\nთუ გინდა დასრულება შეიყვანე 0\n|> ")
        if check_test == '0':
            print('პასუხია|>  ' + answer)
            bool_test = False
        else:
            x_value = answer
        i = i + 1
    else:
        op = input("ოპერატორი|>  ")
        while not isValidOp(op):
            print("არასწორი ოპერაოტრი!!!!")
            op = input("ოპერატორი|>  ")
        element = (input('რიცხვი|>  ')).upper()
        while not isValidNumber(element):
            print('არასწორი ელემენტი!!!!')
            element = (input('რიცხვი|>  ')).upper()
        answer = calculateAnswer(x_value, element, op)
        check_test = input("თუ გინდა რომ დაამატო ოპერატორი შეიყვანე 1\nთუ გინდა დასრულება შეიყვანე 0\n|> ")
        if check_test == '0':
            x_value = answer
            print('პასუხია|>  ' + answer)
            bool_test = False
        else:
            x_value = answer
