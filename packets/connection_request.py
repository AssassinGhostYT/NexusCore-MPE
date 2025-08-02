import struct

def decode_connection_request(data: bytes):
    """Decodifica un paquete Connection Request (0x09)."""
    # Nos saltamos el Packet ID (1 byte)
    packet_id = data[0]
    
    # Leemos el GUID del cliente (8 bytes)
    client_guid = struct.unpack("!q", data[1:9])[0]
    
    # Leemos el timestamp del cliente (8 bytes)
    client_timestamp = struct.unpack("!q", data[9:17])[0]
    
    # Leemos el flag de seguridad (1 byte)
    secure = data[17]
    
    return {
        'packet_id': packet_id,
        'client_guid': client_guid,
        'client_timestamp': client_timestamp,
        'secure': secure
    }
