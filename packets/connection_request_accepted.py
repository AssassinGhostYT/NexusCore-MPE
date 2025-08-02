import socket
import struct

def create_connection_request_accepted_packet(client_addr: tuple, request_time: int, accepted_time: int):
    """Construye un paquete Connection Request Accepted (0x10)."""
    CONNECTION_REQUEST_ACCEPTED_ID = 0x10
    
    # El formato es: ID (1) + Client Address (16) + System Index (2) + Request Time (8) + Accepted Time (8)
    
    packet = bytes([CONNECTION_REQUEST_ACCEPTED_ID])
    
    # Escribimos la dirección del cliente (16 bytes, formato RakNet)
    packet += bytes([0x04]) # Tipo de IP (IPv4)
    packet += socket.inet_aton(client_addr[0])
    packet += struct.pack("!H", client_addr[1])
    packet += bytes([0] * 9) # Relleno para que la dirección sea de 16 bytes
    
    packet += struct.pack("!H", 0) # System Index (0 works fine)
    packet += struct.pack("!q", request_time)
    packet += struct.pack("!q", accepted_time)

    return packet
