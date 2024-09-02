from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import tkinter as tk
import socket

# Load the server's public key
with open("public.pem", "rb") as pub_file:
    public_key = pub_file.read()

public_key_obj = RSA.import_key(public_key)

# Encrypt the message function
def encrypt_message(message):
    cipher = PKCS1_OAEP.new(public_key_obj)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Function to send the encrypted message to the server
def send_message():
    message = entry_message.get()
    encrypted_message = encrypt_message(message)

    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.send(encrypted_message)
    client_socket.close()

    label_status.config(text="Message sent to the server.")

# Tkinter GUI for the Client
root = tk.Tk()
root.title("RSA Client")
root.geometry("400x300")  # Set dimensions for the GUI

# Widgets
label_info = tk.Label(root, text="Enter Message to Encrypt:")
label_info.pack(pady=10)

entry_message = tk.Entry(root, width=50)
entry_message.pack(pady=10)

button_encrypt = tk.Button(root, text="Send Encrypted Message", command=send_message)
button_encrypt.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=10)

root.mainloop()

