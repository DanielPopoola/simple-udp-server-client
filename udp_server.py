import socket
import datetime

def run_udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket to an address
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    print(f"UDP server listening on {server_address}")


    try:
        while True:
            # Wait for a message
            message, client_address = server_socket.recvfrom(1024)

            # Process the message
            print(f"Recieved from {client_address}:  {message.decode()}")

            # Send response back
            response = f"Server received: {message.decode()} at {datetime.datetime.now()}"
            server_socket.sendto(response.encode(), client_address)

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_udp_server()
