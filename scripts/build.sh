#!/bin/bash
set -e

echo "=== Building Lab 9 Project ==="

echo "[1/3] Building Go TCP Server..."
cd go_tcp_server
go build -o ../bin/tcp_server .
cd ..

echo "[2/3] Building Rust Library..."
cd rust_class_lib
maturin develop --release
cd ..

echo "[3/3] Installing Python dependencies..."
pip install -r python_client/requirements.txt

echo "=== Build Complete ==="
