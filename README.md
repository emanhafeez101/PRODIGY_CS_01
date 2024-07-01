# PRODIGY_CS_01
It is a caesar cipher code which encrypts and decrypts your message
Summary of the Caesar Cipher Encryption and Decryption Program
Program Overview:
The Python program implements the Caesar Cipher algorithm to encrypt and decrypt text based on a user-provided shift value.

Functions:

encrypt(text, shift):
Purpose: Encrypts the given text using the Caesar Cipher with a specified shift.
Behavior:
Handles uppercase letters by shifting them within the range of ASCII values for uppercase letters (A-Z).
Handles lowercase letters by shifting them within the range of ASCII values for lowercase letters (a-z).
Non-alphabetic characters (such as punctuation and spaces) remain unchanged in the output.
Parameters:
text: The text message to be encrypted.
shift: The number of positions each letter should be shifted in the alphabet.
decrypt(text, shift):
Purpose: Decrypts the given text that was encrypted using the Caesar Cipher with a specified shift.
Behavior:
Similar to encryption, handles uppercase and lowercase letters appropriately to reverse the encryption process.
Non-alphabetic characters are preserved without any changes.
Parameters:
text: The encrypted text to be decrypted.
shift: The number of positions each letter was shifted during encryption.
Main Execution:

The main() function:
Prompts the user to enter a message (text) and a shift value (shift).
Encrypts the input message using the encrypt() function and displays the encrypted text.
Decrypts the encrypted text using the decrypt() function and displays the decrypted text.
User Interaction:

The program interacts with the user through console input (input() function) to collect the message and shift value.
It provides clear prompts and outputs for the encrypted and decrypted text.
Key Features:

Shift Calculation: Uses modulo arithmetic to wrap around the alphabet, ensuring that shifts beyond Z (or z) circle back to A (or a).
Case Preservation: Maintains the original case of letters (uppercase or lowercase) during both encryption and decryption processes.
Non-alphabetic Characters: Handles non-alphabetic characters (like punctuation marks and spaces) without alteration, preserving message integrity.
