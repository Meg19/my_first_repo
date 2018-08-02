# This is a basic calculater
''' This is a multiline comment. '''

userName = input("Hello there user, what is your name? ")
print("Hi " + userName)



while True:
    number_one = input("please enter a number")
    number_two = input("please enter another number")

    number_one = int(number_one)
    number_two = int (number_two)
    total=number_one + number_two
    print(total)

    print("total is: " + str(total))
