
---

# P2P File Transfer

This project implements a peer-to-peer (P2P) file transfer system using TCP sockets in Python. The system consists of a client program and a server program. The client program allows users to select a file and send it to the server for storage, while the server program listens for incoming file transfers and saves the received files.

## Prerequisites

- Python 3.x

## Usage

### Server

1. Run the server script (`server.py`) on the machine where you want to receive the files.

    ```bash
    python server.py
    ```

2. The server will start listening for incoming connections on the specified IP address and port.

    - By default, the server is configured to listen on `localhost` (127.0.0.1) and port `8080`. You can modify these values in the `serverAddr` variable in the code if needed.

3. When a client connects and sends a file, the server will receive and save the file in its local directory.

    - The received files will be saved in the same directory as the server script. The file name will be prefixed with the current timestamp to ensure uniqueness.

### Client

1. Run the client script (`client.py`) on the machine where you want to send a file from.

    ```bash
    python client.py
    ```

2. The client program will display a menu where you can choose the file to send.

    - The available options in the menu correspond to different file types (e.g., PNG, JSON, CSV).

3. Select the appropriate option for the file you want to send.

4. Enter the file name when prompted. The file should be located in the same directory as the client script, or you can provide the full file path.

    - If the file is not in the same directory, make sure to provide the correct file path relative to the client script or the absolute file path.

5. The client program will establish a connection with the server and send the file. Once the file is successfully sent, the client will display a success message.

    - If any errors occur during the file transfer, such as connection issues or file not found errors, the client program will display an appropriate error message.

6. After the file transfer is complete, you can choose to send another file or exit the client program.

## Cisco Packet Tracer Example

Below is the supposed connections where the server.py is running on the cloud server and clients accessing it from their PCs.
![Screenshot 2023-06-09 235445](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/ec19abb0-68b8-47be-8f23-43b2f847aeef)

This one down below is much simpler. Here Clients are connected just by switch and either of the play role of server and a client.
![Screenshot 2023-06-09 235628](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/4c6683d1-f3cb-41e2-8ec1-aff09d5ea919)

## Troubleshooting

- If the client is unable to connect to the server, ensure that the server is running and listening on the correct IP address and port. Check for any firewall or security settings that may be blocking the connection.

- If the file transfer fails or the program stops due to a timeout error, check the following:
    - Verify that the file exists and is accessible.
    - Ensure that the file path and name are entered correctly.
    - Double-check the code for any potential errors or bugs.

---
# Exp(experiment) Files

This is a simple client-server application that allows you to transfer an image file from a client to a server using TCP/IP sockets.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone the repository or copy the client and server code into separate files on your local machine.

2. Run the server code on the machine where you want to receive the image.

   ```bash
   $ python expServer.py
   ```

3. Run the client code on the machine where the image is located.

   ```bash
   $ python eexpClient.py
   ```
---
Below is the order of interaction of the experimental client and server.

![Screenshot 2023-06-11 063618](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/e28e291c-6633-497d-b521-0fe8d3e22cac)

---

## Usage

1. When you run the client code, it will prompt you to enter the image name. Provide the name of the image file you want to transfer.

2. The client will establish a connection with the server and start transferring the image file.

3. The server will save the received image file in its local directory with a unique name based on the current timestamp.

4. Once the image transfer is complete, both the client and server will display the latency (time taken for the server to respond to the image size) and the overall time (time taken for the complete transfer).

5. The transferred image file will be saved in the server's local directory.

## WireShark Results
![Screenshot 2023-06-11 073730](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/4597da64-bbc5-43d7-a223-82d57491149e)
Up here a single, entire process from connection to the closing of the sockets.

## Customization

- You can modify the server address and port in both the client and server code to match your specific configuration.

- The code provided is designed to transfer image files, but you can adapt it to transfer other types of files by changing the file handling and data encoding/decoding accordingly.

## Acknowledgments

This application is based on the client-server socket programming concepts in Python.

## Troubleshooting

- Ensure that the client and server are running on separate machines or in separate Python processes on the same machine.

- Verify that the image file you are trying to transfer exists and is accessible by the client.

- Check for any firewall or network configurations that may be blocking the communication between the client and server.

If you encounter any issues or have any questions, please feel free to contact the project contributors.

That's it! You now have a basic README file for your client-server image transfer application. Feel free to customize it further based on your specific requirements and project details.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
