package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"net"
	"strings"
	"sync"
	"time"
)

type Request struct {
	Command string `json:"command"`
	Data    string `json:"data"`
}

type Response struct {
	Status    string `json:"status"`
	Result    string `json:"result"`
	Timestamp string `json:"timestamp"`
}

type BackgroundProcessor struct {
	taskQueue chan string
	wg        sync.WaitGroup
}

func NewBackgroundProcessor() *BackgroundProcessor {
	bp := &BackgroundProcessor{
		taskQueue: make(chan string, 100),
	}
	go bp.processBackground()
	return bp
}

func (bp *BackgroundProcessor) processBackground() {
	for task := range bp.taskQueue {
		time.Sleep(10 * time.Millisecond)
		fmt.Printf("[Background] Processed: %s\n", task)
	}
	bp.wg.Done()
}

func (bp *BackgroundProcessor) AddTask(task string) {
	bp.wg.Add(1)
	bp.taskQueue <- task
}

func (bp *BackgroundProcessor) Shutdown() {
	close(bp.taskQueue)
	bp.wg.Wait()
}

func handleConnection(conn net.Conn, processor *BackgroundProcessor) {
	defer conn.Close()
	reader := bufio.NewReader(conn)
	
	for {
		input, err := reader.ReadString('\n')
		if err != nil {
			return
		}
		
		input = strings.TrimSpace(input)
		var req Request
		json.Unmarshal([]byte(input), &req)
		
		processor.AddTask(req.Data)
		
		resp := Response{
			Status:    "success",
			Result:    fmt.Sprintf("Received: %s", req.Data),
			Timestamp: time.Now().Format(time.RFC3339),
		}
		
		respJSON, _ := json.Marshal(resp)
		conn.Write(append(respJSON, '\n'))
	}
}

func main() {
	processor := NewBackgroundProcessor()
	
	listener, err := net.Listen("tcp", ":9000")
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer listener.Close()
	
	fmt.Println("TCP Server started on port 9000")
	
	for {
		conn, err := listener.Accept()
		if err != nil {
			continue
		}
		go handleConnection(conn, processor)
	}
}
