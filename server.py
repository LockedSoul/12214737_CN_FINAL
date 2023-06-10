from socket import *
import os
import time

# Server IP and Port information
serverAddr = ("127.0.0.1", 8080)

# Create server socket
sock = socket(AF_INET, SOCK_STREAM)

# Bind server address to socket
sock.bind(serverAddr)

# Start listening
sock.listen(5)

# server online message
print(f"Server online on [{serverAddr}]")

while True:
    # Change timeout
    sock.settimeout(100)
    # Accept an incoming connections
    clientSock , clientAddr = sock.accept()
    
    # Set socket timeout
    sock.settimeout(10)
    
    # Display connection status
    print(f"Connected to ->{clientAddr}")

    # Receive file extension
    ext = str(clientSock.recv(1024).decode())
    # Respond
    sock.sendall("OK".encode())
    # display process
    print(f'C-> Receiving {ext} file:')

    # Receive file name
    fileName = str(clientSock.recv(1024).decode())
    # Respond
    sock.sendall("OK".encode())
    # display process
    print(f'    Filename: {fileName}')

    # Receive file size
    fileSizeStr = clientSock.recv(1024).decode()
    fileSize = int(fileSizeStr)
    # Respond
    sock.sendall("OK".encode())
    # display process
    print(f'    Size {fileSize}bytes')

    # Recieve the file data
    fileData = b''
    while len(fileData) < fileSize:
        data = clientSock.recv(1024)
        fileData += data
    # Respond
    sock.sendall("OK".encode())

    # Save recieved image file
    fileName = str(time.localtime()) + '_' + fileName + ext

    # Write received image data to a file
    with open(fileName, "wb") as file:
        file.write(fileData)

    print(f"File received and save to [{fileName}]")

    # Close the client socket
    clientSock.close()

# Close the server socket
sock.close()
