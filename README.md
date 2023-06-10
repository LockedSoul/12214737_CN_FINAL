
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

## Troubleshooting

- If the client is unable to connect to the server, ensure that the server is running and listening on the correct IP address and port. Check for any firewall or security settings that may be blocking the connection.

- If the file transfer fails or the program stops due to a timeout error, check the following:
    - Verify that the file exists and is accessible.
    - Ensure that the file path and name are entered correctly.
    - Double-check the code for any potential errors or bugs.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
