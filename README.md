## P2P File Transfer Suing TCP Protocol


This code provides a file transfer system with a server and client component. The server listens for incoming connections and handles client requests to receive files, while the client allows users to send files (image, CSV, JSON) to the server. The server and client communicate using sockets.

## Prerequisites

- Python 3.x
- Required modules: socket, json, threading, time, csv, PIL

## Server

### Usage

1. Make sure you have Python installed on your system.

2. Save the server code in a file named `server.py`.

3. Open a terminal or command prompt and navigate to the directory where `server.py` is located.

4. Run the server using the following command:
   ```
   python server.py
   ```

5. The server will start running and display a message: "Server initialized".

6. The server will listen for incoming connections on IP address `127.0.0.1` (localhost) and port `8080`.

7. The server will handle client connections concurrently, allowing multiple clients to connect simultaneously.

8. When a client connects, the server will receive the client's data, including client name, file name, and file type.

9. The server will send an acknowledgment message ("OK") back to the client.

10. The server will receive the file data in chunks until no more data is received.

11. The server will measure the latency of the file transfer.

12. Depending on the file type received, the server will perform different operations:
    - If the file type is "image", the server will reconstruct the image from the received data, display it, and save it to a file.
    - If the file type is "csv", the server will save the received data to a CSV file and print the content of the file row by row.
    - If the file type is "json", the server will save the received data to a JSON file and print the JSON data.

13. The server will continue listening for new client connections indefinitely until terminated.

Note: This code assumes a local server configuration. Modify the `serverIP` and `serverPort` variables to suit your specific network setup if needed.

## Client

### Usage

1. Make sure you have Python installed on your system.

2. Save the client code in a file named `client.py`.

3. Open a terminal or command prompt and navigate to the directory where `client.py` is located.

4. Run the client using the following command:
   ```
   python client.py
   ```

5. The client will prompt you to enter your name.

6. The client will display a menu with the following options:
   - Send Image: Choose this option to send an image file to the server.
   - Send CSV: Choose this option to send a CSV file to the server.
   - Send JSON: Choose this option to send a JSON file to the server.
   - Exit: Choose this option to exit the program.

7. Depending on your choice, follow the instructions to enter the file name for the corresponding file type.

8. The client will attempt to establish a connection with the server using the IP address `127.0.0.1` (localhost) and port `8080`.

9. If the connection is successful, the client will send the file's metadata (name, fileName, fileType) to the server as a JSON-encoded string.

10. The client will wait for a response from the server. If the response is "OK", the file data will be sent to the server.

11. If any errors occur during file handling or the connection process, appropriate error messages will be displayed.



12. After sending the file, the client will return to the menu to allow for sending additional files or choosing to exit.

Note: Ensure that the server is running before running the client. Modify the `serverIP` and `serverPort` variables in the client code to match the server's IP address and port if they differ.

Feel free to customize and extend the code to meet your requirements.

## Sisco Packet Tracer Proposed Examples

![Screenshot 2023-06-09 235445](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/e1f26476-0653-4f47-9ca9-b1a8efe5e1f0)

Here we have 3 user connected to the cloud running on the server using cable modems. Our client programm could be running on clients and server programm on cloud.




![Screenshot 2023-06-09 235628](https://github.com/LockedSoul/12214737_CN_FINAL/assets/75694554/29f8101d-003a-46ed-9097-809e23ab9988)

In this case we 3 users are connected just via home router device and each user has client and server intances running inside.

