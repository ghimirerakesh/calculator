
#import calculator
print('''Welcome to calculate''')
def again():

    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calc module
    if calc_again == 'Y':
            print('Welcome to calculate again')
            print(something())

    # If user types N, say good-bye to the user and end the program
    elif calc_again == 'N':
        print('Have a nice day!')
        exit()

    # If user types another key, run the function again
    else:
        print("Invalid Inputs! Please press Y for calculate again and N to exit")
        again()

def something():

    operator = input(''' Which operation do you want to compute...
                        + is for addition
                        - is for substraction
                        * is for multiplication
                        / is for the division
                        ''')

    if(operator.isalnum()):
        print("Please Enter the operator to calculate")
        print(again())
    else:
        pass



    #Taking inputs from the user

    a = input('Enter first number: ')
    if(a.isdigit()):
        a = int(a)
        pass
    else:
        print("Please Enter a Numeric Value")
        print(again())
    b = input('Enter second number: ')
    if(b.isdigit()):
        b = int(b)
        pass
    else:
        print("Please Enter a Numeric Value")
        print(again())

    #performing the operations based on the user operators
    if operator == '+':
        print("The Addition is ::")
        print('{} + {}'.format(a, b))
        print(a+b)

    elif operator == '-':
        print("The Substraction is ::")
        print('{} - {}'.format(a, b))
        print(a-b)
    elif operator == '*':
        print("The Multiplication is ::")
        print('{} * {}'.format(a, b))
        print(a*b)
    elif operator == '/':
        print("The Division is ::")
        print('{} / {}'.format(a, b))
        print(a/b)
    else:
        print("Invalid please type operator to calculate")
        again()
    #calling the again func from calculator
    again()
something()
