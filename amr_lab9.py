"""

Andrew Ruiz
"""

def encoder(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password"
    encoded = [(int(char) + 3) % 10 for char in password]
    return ''.join(map(str, encoded))

def decoder(password):
    password_list = [int(i) for i in password]
    decoded_password_list = [str((num-3)%10) for num in password_list]
    decoded_password = ''.join(decoded_password_list)
    return decoded_password

def main():
    while True:
        print(f"""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
        choice = input("\nPlease enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your Password has been encoded and stored\n\n")
        elif choice == "2":
            decoded_password = decoder(encoded_password)
            print(f"""The encoded password is {encoded_password}, and the original password is {decoded_password}\n\n""")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
