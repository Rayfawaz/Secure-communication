### Secure Communication Channel Using RSA Encryption

In this project, I developed a secure communication channel between a client and a server using RSA encryption for message encryption and decryption. The project was implemented with Python, utilizing the Tkinter library for a graphical user interface (GUI) and socket programming for communication between the client and the server. The server automatically received encrypted messages from the client, but the decryption was performed manually by clicking a "Decrypt" button.

#### Key Components

1. **RSA Encryption**:
   - The server generated an RSA key pair (private and public keys).
   - The public key was shared with the client, while the server kept the private key for decrypting messages.
   
2. **Socket Communication**:
   - The server listens for incoming messages on a specific port (`localhost:12345`).
   - The client sent encrypted messages to the server over the socket connection.
   
3. **Manual Decryption**:
   - After receiving an encrypted message, the server GUI allows manual decryption by clicking a button.
   
4. **GUI Interface**:
   - The client and server both has basic GUIs built with Tkinter.
   - The GUIs were defined with specific dimensions (400x300 pixels) for simplicity and clarity.
   
#### Running the Program

To run this project, clone it from my GitHub repository and follow these steps:

1. **Cloning the Repository**:
   - First, Clone the repository containing the server and client code using the following command:
   
    _git clone https://github.com/Rayfawaz/Secure-communication.git_
   

2. **Installing Dependencies**:
   -  Ensure that Python and the required libraries (Tkinter and PyCryptodome) are installed. On Kali Linux, Install the dependencies using:

   _sudo apt-get install python3-tk_
   
   _pip install pycryptodome_
  

4. **Running the Server**:
   - After navigating to the project directory, start the server by running the `server-crypto.py` script in one terminal:

   _python3 server-crypto.py_
  

   This opens the server’s GUI and starts listening for messages.

5. **Running the Client**:
   - In a separate terminal, run the client by executing the `client-crypto.py` script:

   _python3 client-crypto.py_
  

   This opens the client’s GUI where you can enter a message, encrypt it using the server’s public key, and send it to the server.

6. **Communication and Decryption**:
   - The client sends the encrypted message to the server over a socket connection. The server receives the message automatically and displays a status update in the GUI. You then clicked the "Decrypt" button on the server GUI to manually decrypt and display the original message.

This project demonstrated the fundamentals of secure communication using RSA encryption, with socket-based communication and a user-friendly GUI for interaction.


