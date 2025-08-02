import struct

def decode_open_connection_request2(data: bytes):
    """Decodifica un paquete Open Connection Request #2 (0x07)."""
    # Nos saltamos el Packet ID (1 byte)
    packet_id = data[0]

    # Nos saltamos el Magic (16 bytes)
    magic = data[1:17]
    
    # La dirección del servidor está en los bytes 17-24
    server_address = data[17:25]

    # Leemos el MTU (2 bytes)
    mtu_size = struct.unpack("!H", data[25:27])[0]
    
    # Leemos el GUID del cliente (8 bytes)
    client_guid = struct.unpack("!q", data[27:35])[0]

    return {
        'packet_id': packet_id,
        'magic': magic,
        'server_address': server_address,
        'mtu_size': mtu_size,
        'client_guid': client_guid
    }
