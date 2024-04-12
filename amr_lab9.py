"""

Andrew Ruiz
"""


def encoder(password):
    if len(password) != 8 or not password.isdigit():
        return "Invalid password"
    encoded = [(int(char) + 3) % 10 for char in password]
    return ''.join(map(str, encoded))


"""
Decode Function Goes Here
"""


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
            encoded_passwrd = encoder(password)
            print("Your Password has been encoded and stored\n\n")
        elif choice == "2":
            print(f"""The encoded password is {encoded_passwrd}, and the original password is {password}\n\n""")
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
