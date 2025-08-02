import struct

def create_resource_pack_stack_packet():
    """Construye un paquete ResourcePackStack (0x85)."""
    RESOURCE_PACK_STACK_ID = 0x85

    # El formato es: ID (1) + Must Accept (bool, 1) + Behavior Packs Count (short, 0) + Resource Packs Count (short, 0) + Game Version (string) + Experiments (bytes) + Experiments Toggle (bool, 0)

    # Para simplificar, enviaremos un stack vacío.
    packet = bytes([RESOURCE_PACK_STACK_ID])
    packet += struct.pack("!?", True) # Must Accept
    packet += struct.pack("!H", 0) # Behavior Packs Count
    packet += struct.pack("!H", 0) # Resource Packs Count
    packet += bytes([0x00]) # No hay experimentos
    packet += bytes([0x00]) # No hay experimentos toggle
    return packet
