# File Replication System

## Overview
This project implements a simple file replication system using the RPC pattern. The system allows for creating, modifying, and deleting files in a destination directory based on operations performed in a source directory.

## Project Structure
file_replication/
│
├── src/
│ ├── init.py
│ ├── dataclasses.py
│ ├── replication_server.py
│ ├── client.py
│
├── tests/
│ ├── init.py
│ ├── test_replication.py
│
├── config/
│ ├── settings.json
│
├── .gitignore
├── README.md
└── requirements.txt

## How to Run

### Running the Server
1. Open a terminal.
2. Navigate to the `src` directory.
3. Run the server:
    ```sh
    python replication_server.py
    ```

### Running the Client
1. Open a terminal.
2. Navigate to the `src` directory.
3. Run the client:
    ```sh
    python client.py
    ```

### Running the Tests
1. Open a terminal.
2. Navigate to the `tests` directory.
3. Run the tests:
    ```sh
    python -m unittest test_replication.py
    ```

## Dependencies
- Python 3.x
- xmlrpc










Your Task
Implement the File Replication Logic in replication_server.py.
Complete the Client Code in client.py to make RPC calls to the server.
Write Unit Tests in test_replication.py to verify the file replication functionality.
Run the Project using the instructions in README.md and ensure everything works as expected.
Additional Tips
Start by implementing the core file replication logic.
Move on to integrating the client and server using RPC.
Finally, focus on writing thorough unit tests to cover various scenarios.
This setup should give you a comprehensive hands-on experience. If you need any further guidance or run into any issues, feel free to ask!