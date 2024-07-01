def encrypt(text, shift):
    enc_text = ""
    for char in text:
        if char.isupper():
            enc_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            enc_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            enc_text += char
    return enc_text

def decrypt(text, shift):
    decrypt_text = ""
    for char in text:
        if char.isupper():
            decrypt_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypt_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypt_text += char
    return decrypt_text

def main():
    text = input("Enter your message which you want to encrypt: ")
    shift = int(input("Enter the shift value: "))
   
    encrypted_text = encrypt(text, shift)
    print("The encrypted text is:\n" + encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, shift)
    print("The decrypted text is: " + decrypted_text)

if __name__ == "__main__":
    main()
