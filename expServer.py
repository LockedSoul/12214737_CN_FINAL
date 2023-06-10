from socket import *
import os
import time

# Define server address
serverAddr = ("127.0.0.1", 8080)

# Create a TCP socket
sock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the server address
sock.bind(serverAddr)

# Listen for incoming connections
sock.listen(5)

# Display status
print(f"Server online on [{serverAddr}]")


# Accept an incoming connections
clientSock , clientAddr = sock.accept()

# Display connection status
print(f"Connected to ->{clientAddr}")

# Receive image size
imgSizeStr = clientSock.recv(1024).decode()
imgSize = int(imgSizeStr)

# Response
clientSock.sendall("OK".encode())

# Recieve the image data
imgData = b''
while len(imgData) < imgSize:
    data = clientSock.recv(1024)
    imgData += data

# Response
clientSock.sendall("OK".encode())

# Save recieved image file
imgName = str(time.time()) + '.json'

# Write received image data to a file
with open(imgName, "wb") as file:
    file.write(imgData)

print(f"Image received and save to [{imgName}]")

# Close the client socket
clientSock.close()

# Close the server socket
sock.close()