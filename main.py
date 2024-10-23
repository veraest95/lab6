#Adolfo Vera
def encode(password):
    pw_encode = ""
    for item in password:
        pw_encode = pw_encode + str((int(item) + 3) % 10)
    return pw_encode
'''
def decode(encoded_password):
    pw_decode = ""
    for item in encoded_password:
        pw_decode = pw_decode + str((int(item) + 7) % 10)
    return pw_decode
'''
if __name__ == "__main__":
    encoded_password = ""
    decoded_password = ""
    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        option = int(input(" Please enter an option:"))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is: {encoded_password}, and the original password is: {decoded_password}.")
        elif option == 3:
            break

