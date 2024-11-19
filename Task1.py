def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result

# User input
print("Caesar Cipher Program")
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Perform encryption or decryption
if choice in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift_value, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice. Please type 'encrypt' or 'decrypt'.")
