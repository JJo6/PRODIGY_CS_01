import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def encrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = encrypt(message, shift)
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, encrypted_message)
    result_text.config(state=tk.DISABLED)

def decrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = decrypt(message, shift)
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, decrypted_message)
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create and place widgets
message_label = tk.Label(root, text="Message:")
message_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

message_entry = tk.Entry(root, width=50)
message_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

shift_label = tk.Label(root, text="Shift value:")
shift_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

shift_entry = tk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=1, column=2, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=1, column=3, padx=5, pady=5)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

result_text = tk.Text(root, height=5, width=50, state=tk.DISABLED)
result_text.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

# Run the application
root.mainloop()
