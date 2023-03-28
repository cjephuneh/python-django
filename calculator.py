num1 = int(input('Enter first number: '))
num2 = int(input('Enter the second number: '))
op = input('Enter the operator: ')

if op == '+':
    print (num1 + num2)

elif op == '-':
    print(num1-num2)

elif op == '%':
    print(num1 % num2)

elif op == '*':
    print(num1 * num2)

elif op == '/':
    print(num1 / num2)



else:
    print("Invalid Operator")