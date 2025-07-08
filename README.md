# Simple UDP Server-Client Communication

A basic UDP (User Datagram Protocol) server-client implementation in Python demonstrating connectionless communication.

## What This Does

- **Server**: Listens for incoming UDP messages and sends back acknowledgments
- **Client**: Sends messages to the server and displays responses
- **Protocol**: Uses UDP for fast, connectionless communication

## Files

- `udp_server.py` - UDP server that listens on localhost:12345
- `udp_client.py` - UDP client that sends messages to the server

## How to Run

1. **Start the server** (in terminal 1):
   ```bash
   python udp_server.py
   ```

2. **Run the client** (in terminal 2):
   ```bash
   python udp_client.py
   ```

3. **Test it**:
   - Type messages in the client terminal
   - Watch server responses
   - Type 'quit' to exit client

## Key UDP Concepts Demonstrated

- **Connectionless**: No handshake required
- **Fast**: Minimal overhead
- **Stateless**: Each message is independent
- **Unreliable**: No delivery guarantee (though works fine on localhost)

## Example Output

**Server Terminal:**
```
UDP server listening on ('localhost', 12345)
Received from ('127.0.0.1', 54321): Hello Server!
```

**Client Terminal:**
```
Enter message (or 'quit' to exit): Hello Server!
Server response: Server received: Hello Server! at 2025-07-08 14:30:15.123456
```

## UDP vs TCP

- **UDP**: Fast, connectionless, no delivery guarantee
- **TCP**: Reliable, connection-based, guaranteed delivery
- **Use UDP for**: Real-time games, video streaming, DNS lookups
- **Use TCP for**: Web browsing, file transfers, email
