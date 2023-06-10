from socket import *
import os
import time

# Extensions
ext = ['.png', '.json', '.csv']

# Server IP and Port information
serverAddr = ("127.0.0.1", 8080)

# Create client socket
sock = socket(AF_INET, SOCK_STREAM)

# Set socket timeout
sock.settimeout(10)

# Function to check weather servers is listening
def serverStat(sock):
    
    if sock.recv(1024).decode()=="OK":
        return True
    return False

# Function to send file
def sendFnc(ext, fileName, fileSize, fileData):

    # Prosecces status
    endm = 'Succeseed'
    # Try to connect to server
    try:
        sock.connect(serverAddr)
    except Exception as error:
        print(f"Connection ERROR: {error}")
        menu()
 
    # Convert the image to a string
    fileSizeStr = str(fileSize).encode()

    # try to send file
    try:

        # Send file ext info
        print(ext)
        extStr = str(ext).encode()
        sock.send(extStr)
        if not serverStat(sock):
            raise Exception("Server Stoped Responding")
        
        print('name')

        # Send file name
        sock.sendall(fileName.encode())
        if not serverStat(sock):
            raise Exception("Server Stoped Responding")
        
        print('size')
        
        # Send image size to server
        sock.sendall(fileSizeStr)
        if not serverStat(sock):
            raise Exception("Server Stoped Responding")
        
        # Send image data to the server
        print('data')
        
        sock.sendall(fileData)
        if not serverStat(sock):
            raise Exception("Server Stoped Responding")
    # Display error message if Exception is raised
    except Exception as error:
        print(f"File Sending ERROR: {error}")
        endm = 'Failed'
    # End message
    print(f"Proccess {endm}")
    # Close the socket
    sock.close()
    # return to main menu
    menu()

# Function to get file data
def fileFnc(ext):
    # Get image address
    fileName = input('Enter file name: ')
    # Try accessing the file
    try:
        # Check if file types match
        if not fileName.endswith(ext):
            raise Exception("File Type Mismatch")
        # Open the image file in binary mode
        with open(fileName, 'rb') as file:
            # Read the image data
            fileData = file.read()
        
    # if image file not found raise exception
    except Exception as error:
        print(f"ERROR: {error}")
        # ask totry again or cancel
        opt = input("1. Try again | []. Cancel : ")
        # Act upon choice
        if opt == '1':
            fileFnc(ext)
        else:
            print("Invalid option.\n")
            menu()

    # Send the image to the server
    # Get image size
    fileSize = os.path.getsize(fileName)

    sendFnc(ext=ext, fileName=fileName, fileSize=fileSize, fileData=fileData)


# Main menu function
def menu():
    # Display menu
    print()
    print("=======_Menu_=======")
    print("Choose the option:")
    print("1. Send PNG file")
    print("2. Send JSON file")
    print("3. Send CSV file")
    print("4. Exit")
    # Get client choice
    option = input("Your option (1~4): ")
    if option == '1':
        fileFnc(ext[0])
    elif option == '2':
        fileFnc(ext[1])
    elif option == '3':
        fileFnc(ext[2])
    elif option == '4':
        return
if __name__ == '__main__':
    menu()

