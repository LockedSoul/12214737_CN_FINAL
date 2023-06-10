from socket import *
import os
import time

# Server adress info
serverAddr = ('127.0.0.1', 8080)

# Create TCP socket
sock = socket(AF_INET, SOCK_STREAM)

# Connect to the server
sock.connect(serverAddr)

# Reading the file 
# Get image name
imgName = input("Enter image name: ")

# Open the image file in binary mode
with open(imgName, 'rb') as file:
    # Read the image data
    imgData = file.read()

# Send the image to the server
# Get image size
imgSize = os.path.getsize(imgName)

# Convert the image to a string
imgSizeStr = str(imgSize).encode()

# Set start Time
startTime = time.time()

# Send image size to server
sock.sendall(imgSizeStr)

# Get Response
sock.recv(1024)

# check Latency
latency = time.time() - startTime

# Send image data to the server
sock.sendall(imgData)

# Get Response
sock.recv(1024)

# Over all time
overall = time.time() - startTime

# Close the socket
sock.close()

# Print info
print(f"Latency -> {latency}seconds.")
print(f"Overall time -> {overall} seconds.")