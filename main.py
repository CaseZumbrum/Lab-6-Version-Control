
'''
Written by: Case Zumbrum

encode() encodes an integer password by increasing each integer by 3

Input:
    password (String): password to be encoded, all characters must be integers and there should be 8 digits

Return:
    encoded_password (String): encoded password
'''
def encode(password):
    encoded_password = ''
    for char in password:
        if char == '7':
            encoded_password += str(0)
        elif char == '8':
            encoded_password += str(1)
        elif char == '9':
            encoded_password += str(2)
        else:
            encoded_password += str(int(char)+3)
    return encoded_password


#written by Soomin Kim
def decode(password):
    l = []
    for i in password:
        if i == '2':
            l.append(str(9))
        elif i == '1':
            l.append(str(8))
        elif i == '0':
            l.append(str(7))
        else:
            l.append(str(int(i)-3))
    return ''.join(l)


'''
Written by: Case Zumbrum
'''

if __name__ == "__main__":
    while True:
        choice = int(input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option:"))
        if choice == 1:
            password = input("Please enter your password to encode:")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
        else:
            exit()
