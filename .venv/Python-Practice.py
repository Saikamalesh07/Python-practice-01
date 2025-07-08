print("Hello")
A = input("Enter the value for A :   ")
B = input("Enter the value for B :   ")

while True:
    print('Choose an Operation: + - * / ')
    Operation = input('Enter your choice:  ')

    if Operation in ('+', '-', '*', '/'):
        # Valid expression, build the expression and break the loop
        print("Your value is:", A + Operation + B)
        break
    else:
        # Invalid Operation, repeat the loop
        print("Invalid Operation! You have to choose from '+', '-', '*', or '/' only.\n")
