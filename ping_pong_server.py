import socket
import struct
import time
import uuid
import os
import ctypes

# Importa las funciones de los nuevos archivos de paquetes
from packets.unconnected_pong import create_pong_packet
from packets.open_connection_reply1 import create_open_connection_reply1_packet
from packets.open_connection_reply2 import create_open_connection_reply2_packet
from packets.resource_pack_stack import create_resource_pack_stack_packet

# --- CONFIGURACIÓN DEL SERVIDOR ---
MOTD_PROTOCOL_VERSION = 819
MOTD_GAME_VERSION = "1.21.94"
MOTD_NAME = "NexusCore-MPE"
MOTD_PLAYER_COUNT = 0
MOTD_MAX_PLAYERS = 20
MOTD_WORLD_NAME = "World"
MOTD_GAMEMODE = "Survival"
MOTD_IPV4_PORT = 19132

# Un GUID fijo para el servidor
SERVER_GUID = 0x123456789ABCDEF0

# --- CONSTANTES DEL PROTOCOLO ---
UNCONNECTED_PING_ID = 0x01
OPEN_CONNECTION_REQUEST1_ID = 0x05
OPEN_CONNECTION_REQUEST2_ID = 0x07
RESOURCE_PACK_CLIENT_RESPONSE = 0x84
RESOURCE_PACK_STACK_ID = 0x85

def run_server():
    try:
        lib_path = os.path.join(os.getcwd(), "target", "debug", "libnexuscore_mpe.so")
        if os.path.exists(lib_path):
            print("Biblioteca Rust cargada con éxito.")
            rust_lib = ctypes.CDLL(lib_path)
            rust_lib.rust_add.restype = ctypes.c_int32
            print(f"Resultado de la llamada a la función de Rust: {rust_lib.rust_add(10, 20)}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0", MOTD_IPV4_PORT))
        print(f"🛠️ Servidor NexusCore-MPE (Python) iniciado en 0.0.0.0:{MOTD_IPV4_PORT}")

        while True:
            data, addr = sock.recvfrom(2048)

            if not data:
                continue

            packet_id = data[0]
            print(f"📦 Recibido paquete de {addr} con ID: {hex(packet_id)} (Longitud: {len(data)} bytes)")

            if packet_id == UNCONNECTED_PING_ID:
                if len(data) >= 9:
                    client_timestamp = struct.unpack("!Q", data[1:9])[0]
                    print(f"🔍 Recibido Unconnected Ping de {addr} con tiempo: {client_timestamp}")

                    pong_data = create_pong_packet(client_timestamp, SERVER_GUID)
                    sock.sendto(pong_data, addr)
                    print(f"📤 Enviado Unconnected Pong a {addr}!")
            elif packet_id == OPEN_CONNECTION_REQUEST1_ID:
                if len(data) >= 18:
                    protocol_version = struct.unpack("!B", data[17:18])[0]
                    mtu = len(data)
                    print(f"🤝 Recibido Open Connection Request #1 de {addr} (Protocolo Cliente: {protocol_version}, MTU: {mtu})")

                    reply1_data = create_open_connection_reply1_packet(SERVER_GUID, mtu)
                    sock.sendto(reply1_data, addr)
                    print(f"📤 Enviado Open Connection Reply #1 (0x06) a {addr}!")
            elif packet_id == RESOURCE_PACK_CLIENT_RESPONSE:
                print(f"🤝 Recibido Resource Pack Client Response (0x84) de {addr}. Respondiendo con el ResourcePackStack.")
                stack_data = create_resource_pack_stack_packet()
                sock.sendto(stack_data, addr)
                print(f"📤 Enviado ResourcePackStack (0x85) a {addr}!")
            else:
                print(f"📝 Recibido paquete desconocido (ID: {hex(packet_id)}) de {addr}. Longitud: {len(data)} bytes. Raw Hex: {data.hex()}")

    except KeyboardInterrupt:
        print("Deteniendo servidor...")
    except FileNotFoundError:
        print(f"Error: No se encontró la biblioteca de Rust en {lib_path}. Asegúrate de que hayas compilado la librería con `cargo build`.")
    except Exception as e:
        print(f"❌ Error en el servidor: {e}")

if __name__ == "__main__":
    run_server()