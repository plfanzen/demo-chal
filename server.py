#!/usr/bin/env python3
"""
Simple TCP server that asks for a name and prints a greeting with a flag.
"""
import socket


def handle_client(client_socket, address):
    """Handle a single client connection."""
    try:
        print(f"[+] Connection from {address}")
        
        # Ask for name
        client_socket.sendall(b"What's your name?\n")
        
        # Receive name (up to 1024 bytes)
        name = client_socket.recv(1024).decode('utf-8', errors='replace').strip()
        
        if name:
            # Send greeting
            greeting = f"Hello, {name}!\n"
            client_socket.sendall(greeting.encode('utf-8'))
            
            # Send flag
            flag = "PLFANZEN{TEST_SVC_2}\n"
            client_socket.sendall(flag.encode('utf-8'))
            
            print(f"[+] Sent flag to {name} from {address}")
        else:
            print(f"[-] No name received from {address}")
            
    except Exception as e:
        print(f"[-] Error handling client {address}: {e}")
    finally:
        client_socket.shutdown(socket.SHUT_WR)
        client_socket.close()


def main():
    """Start the TCP server on port 3000."""
    host = '0.0.0.0'
    port = 3000
    
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"[*] Server listening on {host}:{port}")
        
        while True:
            # Accept incoming connections
            client_socket, address = server_socket.accept()
            handle_client(client_socket, address)
            
    except KeyboardInterrupt:
        print("\n[*] Server shutting down...")
    except Exception as e:
        print(f"[-] Server error: {e}")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
