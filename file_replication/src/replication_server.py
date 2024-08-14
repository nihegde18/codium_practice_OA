import os
import json
from xmlrpc.server import SimpleXMLRPCServer
from src.dataclasses import FileOperation

class FileReplicationServer:
    def __init__(self, source_dir: str, dest_dir: str):
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

    def replicate_file(self, file_op: FileOperation) -> bool:
        # TODO: Implement file replication logic
        pass

def load_settings(config_path: str = "config/settings.json"):
    with open(config_path, 'r') as file:
        settings = json.load(file)
    return settings

def start_server(source_dir: str, dest_dir: str, port: int):
    server = SimpleXMLRPCServer(("localhost", port))
    replication_server = FileReplicationServer(source_dir, dest_dir)
    server.register_instance(replication_server)
    print(f"RPC Server listening on port {port}...")
    server.serve_forever()

if __name__ == "__main__":
    settings = load_settings()
    source_directory = settings["source_directory"]
    destination_directory = settings["destination_directory"]
    server_port = settings["server_port"]

    start_server(source_directory, destination_directory, server_port)
