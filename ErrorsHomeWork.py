# Task no 1: Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Hej, can exponent a numbers only')


# Task no 2: Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

try:
    y = 0
    x = 5
    z = x / y
except ZeroDivisionError:
    print('Hej, It looks like you try to divide by 0')
finally:
    print('All Done')


def ask():
    while True:
        try:
            num = int(input('Enter a number'))
        except:
            print("Hej that is not a number")
            continue
        else:
            print('Thanks, it is a number')
            break

    square = num ** 2
    print(f'Your squared number: {square}')

ask()

