import socket
import json
import time

try:
    import rust_class_lib
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False
    print("Warning: rust_class_lib not installed")

class TCPClient:
    def __init__(self, host='localhost', port=9000):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
    
    def send(self, command, data):
        request = {"command": command, "data": data}
        self.socket.send((json.dumps(request) + '\n').encode())
        response = self.socket.recv(1024).decode()
        return json.loads(response)
    
    def close(self):
        if self.socket:
            self.socket.close()

def test_rust_class():
    if not RUST_AVAILABLE:
        return None
    processor = rust_class_lib.DataProcessor("TestProcessor")
    result = processor.process("hello world")
    return result

def main():
    print("=== Lab 9 Variant 5 ===\n")
    
    if RUST_AVAILABLE:
        print("[Rust] Testing DataProcessor class:")
        result = test_rust_class()
        print(f"  Result: {result}\n")
    
    print("[Go] Testing TCP Server:")
    try:
        client = TCPClient()
        client.connect()
        response = client.send("process", "test_data")
        print(f"  Response: {response}")
        client.close()
    except Exception as e:
        print(f"  Error: {e}")
        print("  (Make sure Go server is running on port 9000)")

if __name__ == "__main__":
    main()
