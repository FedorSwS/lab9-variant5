package main

import (
	"encoding/json"
	"net"
	"testing"
	"time"
)

func TestRequestResponse(t *testing.T) {
	go func() {
		listener, _ := net.Listen("tcp", ":9001")
		defer listener.Close()
		conn, _ := listener.Accept()
		defer conn.Close()
		conn.Write([]byte(`{"status":"ok"}\n`))
	}()
	
	time.Sleep(100 * time.Millisecond)
	
	conn, err := net.Dial("tcp", "localhost:9001")
	if err != nil {
		t.Fatal(err)
	}
	defer conn.Close()
	
	buf := make([]byte, 1024)
	n, _ := conn.Read(buf)
	
	var resp Response
	json.Unmarshal(buf[:n], &resp)
	
	if resp.Status != "ok" {
		t.Errorf("Expected status 'ok', got '%s'", resp.Status)
	}
}

func TestBackgroundProcessor(t *testing.T) {
	bp := NewBackgroundProcessor()
	bp.AddTask("test_task")
	time.Sleep(50 * time.Millisecond)
	bp.Shutdown()
}
