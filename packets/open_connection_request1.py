import struct

def decode_open_connection_request1(data: bytes):
    """Decodifica un paquete Open Connection Request #1 (0x05)."""
    # Nos saltamos el Packet ID (1 byte)
    packet_id = data[0]
    
    # Nos saltamos el Magic (16 bytes)
    magic = data[1:17]

    # Leemos la versión del protocolo RakNet (1 byte)
    raknet_protocol_version = struct.unpack("!B", data[17:18])[0]
    
    # El MTU es la longitud total del paquete
    mtu_size = len(data)
    
    return {
        'packet_id': packet_id,
        'magic': magic,
        'raknet_protocol_version': raknet_protocol_version,
        'mtu_size': mtu_size
    }
