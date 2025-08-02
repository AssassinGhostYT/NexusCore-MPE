import socket
import struct
import uuid

def create_open_connection_reply2_packet(server_guid, client_addr, mtu):
    """Construye un paquete Open Connection Reply #2 (0x08)."""
    OPEN_CONNECTION_REPLY2_ID = 0x08
    MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    ip_bytes = socket.inet_aton(client_addr[0])
    port_bytes = struct.pack("!H", client_addr[1])

    reply2_packet = bytes([OPEN_CONNECTION_REPLY2_ID])
    reply2_packet += MAGIC
    reply2_packet += struct.pack("!q", server_guid)
    reply2_packet += bytes([0x04]) # Tipo de IP (IPv4)
    reply2_packet += ip_bytes
    reply2_packet += port_bytes
    reply2_packet += bytes([0] * 10) # Relleno de 10 bytes para llegar a 16
    reply2_packet += struct.pack("!H", mtu)
    reply2_packet += bytes([0x00]) # No hay encriptación
    return reply2_packet
