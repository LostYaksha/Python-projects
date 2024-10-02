def simple_calculator(num1, num2, operation):
    if operation == '+':
        return (num1) + (num2)
    elif operation == '-':
        return (num1) - (num2)
    elif operation == '*':
        return (num1) * (num2)
    elif operation == '/':
        if num2 == 0:
            return 'Error'
        else:
            return (num1) / (num2)
    else:
        return 'Error, unknown operation.'


num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
operation = input('choose an operation (+, -, *, /): ')

print(simple_calculator(num1, num2, operation))