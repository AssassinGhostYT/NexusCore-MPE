import struct

def create_pong_packet(client_timestamp, server_guid):
    """Construye un paquete Unconnected Pong para 1.21.94."""
    # Define tus constantes aquí
    UNCONNECTED_PONG_ID = 0x1c
    MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"
    MOTD_NAME = "NexusCore-MPE"
    MOTD_PROTOCOL_VERSION = 819
    MOTD_GAME_VERSION = "1.21.94"
    MOTD_PLAYER_COUNT = 0
    MOTD_MAX_PLAYERS = 20
    MOTD_WORLD_NAME = "World"
    MOTD_GAMEMODE = "Survival"
    MOTD_IPV4_PORT = 19132

    server_info_string = f"MCPE;{MOTD_NAME};{MOTD_PROTOCOL_VERSION};{MOTD_GAME_VERSION};{MOTD_PLAYER_COUNT};{MOTD_MAX_PLAYERS};{server_guid};{MOTD_WORLD_NAME};{MOTD_GAMEMODE};1;{MOTD_IPV4_PORT};"

    server_info_bytes = server_info_string.encode('utf-8')

    pong_packet = bytes([UNCONNECTED_PONG_ID])
    pong_packet += struct.pack("!Q", client_timestamp)
    pong_packet += struct.pack("!q", server_guid)
    pong_packet += MAGIC
    pong_packet += struct.pack("!H", len(server_info_bytes))
    pong_packet += server_info_bytes

    return pong_packet
