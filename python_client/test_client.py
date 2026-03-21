import pytest
import socket
import json
import threading
import time

def test_tcp_client_connection():
    def mock_server():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('localhost', 9002))
        sock.listen(1)
        sock.settimeout(2)
        try:
            conn, _ = sock.accept()
            conn.recv(1024)
            conn.send(b'{"status":"ok"}\n')
            conn.close()
        except:
            pass
        finally:
            sock.close()
    
    server_thread = threading.Thread(target=mock_server)
    server_thread.daemon = True
    server_thread.start()
    time.sleep(0.1)
    
    from main import TCPClient
    client = TCPClient('localhost', 9002)
    client.connect()
    response = client.send("test", "data")
    client.close()
    
    assert response["status"] == "ok"

def test_rust_import():
    try:
        import rust_class_lib
        processor = rust_class_lib.DataProcessor("Test")
        assert processor.get_count() == 0
    except ImportError:
        pytest.skip("rust_class_lib not installed")
