# PRODIGY_CS_01
##Ciesar Cipher 

This project implements a simple graphical user interface (GUI) for encrypting and decrypting text using the Caesar Cipher algorithm. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

![image](https://github.com/JJo6/PRODIGY_CS_01/assets/87189227/7fabc887-f6af-40c6-8e9d-1e3b61e78b2c)


**Files:**
Caesar cipher.py: Contains the implementation of the Caesar Cipher algorithm, including functions for encryption and decryption it also Implements the GUI using the Tkinter library in Python. It provides text input fields for the message and shift value, buttons to encrypt and decrypt the message, and a text widget to display the result.

**Time Complexity:**
The time complexity of the Caesar Cipher encryption and decryption algorithms implemented in caesar_cipher.py is O(n), where n is the length of the input text. This is because the algorithm iterates over each character in the input text once.

**How to Run:**
To run the program:

Make sure you have Python installed on your system.
Download or clone the repository containing the code.
Navigate to the directory where caesar_cipher_.py is located using the command line.
Run the program by executing the command: python caesar_cipher_.py.
The GUI window will open, allowing you to input text and perform encryption or decryption.

![image](https://github.com/JJo6/PRODIGY_CS_01/assets/87189227/e0964a76-11d6-4b08-87a0-3d4ded4a771a)

![image](https://github.com/JJo6/PRODIGY_CS_01/assets/87189227/08e84ffb-3755-4408-ab57-2118e6d78d6b)


**Notes:**
The program handles both uppercase and lowercase letters in the input text.
Shift values can be positive or negative integers.
Non-alphabetic characters in the input text remain unchanged during encryption and decryption.

**Additional Considerations:**
Error handling: Ensure proper handling of invalid input values, such as non-integer shift values.
Testing: Perform thorough testing to validate the correctness of encryption and decryption operations.
Documentation: Provide detailed comments within the code to explain its functionality and usage.
