from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import tkinter as tk
import socket
import threading

# Generate RSA Key Pair
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save keys to files
with open("private.pem", "wb") as priv_file:
    priv_file.write(private_key)
with open("public.pem", "wb") as pub_file:
    pub_file.write(public_key)

# Load the private key
private_key_obj = RSA.import_key(private_key)

# Global variable to hold the encrypted message received from the client
encrypted_message_global = None

# Decrypt the message function
def decrypt_message():
    global encrypted_message_global
    if encrypted_message_global:
        cipher = PKCS1_OAEP.new(private_key_obj)
        decrypted_message = cipher.decrypt(encrypted_message_global)
        label_decrypted.config(text=f"Decrypted Message: {decrypted_message.decode()}")
    else:
        label_decrypted.config(text="No message received.")

# Function to handle incoming connections and receive encrypted data
def receive_data():
    global encrypted_message_global

    # Set up server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    while True:
        conn, addr = server_socket.accept()
        encrypted_message_global = conn.recv(1024)
        conn.close()
        label_status.config(text="Message received. Click Decrypt to decrypt it.")

# Start the server in a separate thread to receive encrypted data
def start_server():
    server_thread = threading.Thread(target=receive_data)
    server_thread.daemon = True
    server_thread.start()

# Tkinter GUI for the Server
root = tk.Tk()
root.title("RSA Server")
root.geometry("400x300")  # Set dimensions for the GUI

# Widgets
label_info = tk.Label(root, text="Waiting for encrypted message from client...")
label_info.pack(pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)
button_decrypt.pack(pady=10)

label_decrypted = tk.Label(root, text="")
label_decrypted.pack(pady=10)

label_status = tk.Label(root, text="No message received yet.")
label_status.pack(pady=10)

# Start the server socket to listen for messages
start_server()

root.mainloop()

