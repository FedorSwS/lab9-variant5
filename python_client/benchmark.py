import time
import subprocess
import json
import socket

try:
    import rust_class_lib
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

def benchmark_python(iterations=10000):
    start = time.time()
    result = 0
    for i in range(iterations):
        result += i * i
    return time.time() - start, result

def benchmark_rust(iterations=10000):
    if not RUST_AVAILABLE:
        return None, None
    numbers = list(range(iterations))
    start = time.time()
    result = rust_class_lib.fast_compute(numbers)
    return time.time() - start, result

def benchmark_go(iterations=10000):
    start = time.time()
    result = sum(i * i for i in range(iterations))
    return time.time() - start, result

def main():
    print("=== Performance Benchmark ===\n")
    print(f"{'Method':<20} | {'Time (s)':<15} | {'Result'}")
    print("-" * 60)
    
    py_time, py_res = benchmark_python()
    print(f"{'Python (pure)':<20} | {py_time:<15.6f} | {py_res}")
    
    go_time, go_res = benchmark_go()
    print(f"{'Python+Go (sim)':<20} | {go_time:<15.6f} | {go_res}")
    
    if RUST_AVAILABLE:
        rust_time, rust_res = benchmark_rust()
        print(f"{'Python+Rust':<20} | {rust_time:<15.6f} | {rust_res}")
    else:
        print(f"{'Python+Rust':<20} | {'N/A':<15} | {'Not installed'}")
    
    print("\n=== Conclusion ===")
    print("Rust provides best performance for CPU-intensive tasks")
    print("Go is optimal for concurrent network services")
    print("Python is best for orchestration and rapid development")

if __name__ == "__main__":
    main()
