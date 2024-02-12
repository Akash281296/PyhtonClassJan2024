def encrypt(text, shift):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
 
    return result


text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (an integer): "))
cipher_text = encrypt(text, shift)
print("Encrypted text:", cipher_text)