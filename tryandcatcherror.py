try:
    x=int(input('Input an Integer: '))
    print(x)
except:
    print('Something went wrong... Please try again')

try:
    x=int(input('Input an Integer: '))
    print(x)
except ValueError:
    print('Value must be an integer')

try:
    x=int(input('Input an Integer: '))
    print(x)
except:
    print('Something went wrong... Please try again')
else:
    print("Nothing went wrong... 3")