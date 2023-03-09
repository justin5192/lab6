# My name is Justin Williamson and my lab 6 partner is Cole Jank!

def encode(password):
    converted_string = ''
    for i in password:
        if int(i) <= 6:
            converted_string += str(int(i) + 3)
        else:
            converted_string += str(int(i) - 7)

    return converted_string


def decode(password):
    decoded_pw = ''
    for i in password:
        if int(i) >= 3:
	    decoded_pw += str(int(i) - 3)
	else:
	    decoded_pw += str(int(i) + 7)

    return decoded_pw


def menu():
    print('Menu\n--------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def main():
    menu()
    option = int(input('Please enter an option: '))

    while option != 3:
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')

            menu()
            option = int(input('Please enter an option: '))

        if option == 2:
            original_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {original_password}')

            menu()
            option = int(input('Please enter an option: '))

if __name__ == '__main__':
    main()
