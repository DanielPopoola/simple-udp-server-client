import socket

def run_udp_client():
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address
    server_address = ('localhost', 12345)

    try:
        while True:
            message = input("Enter message (or 'quit' to exit): ")

            if message.lower() == 'quit':
                break

            # Send message to server
            client_socket.sendto(message.encode(), server_address)

            # Wait for response
            response, server_addr = client_socket.recvfrom(1024)
            print(f"Server response: {response.decode()}")

    except KeyboardInterrupt:
        print("\nClient shutting down...")
    finally:
        client_socket.close()


if __name__ == "__main__":
    run_udp_client()