alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def caesar_cipher(message, shift, operation):
    if not message:
        print(f"Please Enter a Message to {operation}\n")
        return
    solution = ""
    for char in message:
        if char in alphabets:
            position = alphabets.index(char)
            if operation == "encrypt":
                new_position = (position + shift) % 26
            elif operation == "decrypt":
                new_position = (position - shift) % 26
            else:
                print("Wrong Operation Requested")
                return
            new_char = alphabets[new_position]
            solution += new_char
        else:
            solution += char
    return solution


if __name__ == "__main__":
    choice = 0
    while choice != 3:
        print("Welcome to CAESAR CIPHER\n\nWhat would you like to do?\n1)Encrypt\n2)Decrypt\n3)Exit\n\n")
        choice = int(input("-> "))
        if choice == 1:
            plaintext = input("Enter Plaintext to Encrypt: ")
            shift_val = int(input("Enter Shift Value: "))
            if not plaintext:
                print("Values were EMPTY\n")
            else:
                ciphertext = caesar_cipher(plaintext, shift_val, "encrypt")
                print(f"CIPHERTEXT: {ciphertext}\n\n")
        elif choice == 2:
            ciphertext = input("Enter Ciphertext to Decrypt: ")
            shift_val = int(input("Enter Shift Value: "))
            if not ciphertext or not shift_val:
                print("Plaintext cannot be EMPTY\n\n")
            else:
                plaintext = caesar_cipher(ciphertext, shift_val, "decrypt")
                print(f"PLAINTEXT: {plaintext}\n\n")
        elif choice == 3:
            print("Exiting")
            exit(0)
        else:
            print("Incorrect Option\n\n")
