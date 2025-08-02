import struct
import uuid

def create_open_connection_reply1_packet(server_guid, mtu):
    """Construye un paquete Open Connection Reply #1 (0x06)."""
    OPEN_CONNECTION_REPLY1_ID = 0x06
    MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    reply1_packet = bytes([OPEN_CONNECTION_REPLY1_ID])
    reply1_packet += MAGIC
    reply1_packet += struct.pack("!q", server_guid)
    reply1_packet += bytes([0x00]) # No hay seguridad
    reply1_packet += struct.pack("!H", mtu) # MTU
    return reply1_packet