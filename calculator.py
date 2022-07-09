def calculator():
    """
    Simple calculator, takes three inputs: two numbers and the operator. 
    Only works with integers.    
    """
    while True:
        print('<-- Calculator -->')
        print('- Integers only -')
        try:
            a = int(input('First number: '))
            c = input('Operation: ')
            b = int(input('Second number: '))
        except ValueError:
            print('*Enter a valid operation.*')
            continue
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            try:
                print(a / b)
            except ZeroDivisionError:
                print('Cannot divide by 0.')
                continue
        else:
            print('*Enter a valid operation.*')
            continue
        keep = input('Continue? Y/N: ').upper()
        if keep != 'Y':
            print('Exit.')
            break

        
