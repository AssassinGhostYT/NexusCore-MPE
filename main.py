import ctypes
import os

# La ruta de la biblioteca Rust compilada.
# El nombre del archivo es 'libnexuscore_mpe.so' (snake_case).
lib_path = os.path.join(os.getcwd(), "target", "debug", "libnexuscore_mpe.so")
 
try:
    rust_lib = ctypes.CDLL(lib_path)
except FileNotFoundError:
    print(f"Error: No se encontró la biblioteca de Rust en {lib_path}. Asegúrate de que hayas compilado la librería con `cargo build`.")
    exit(1)

# Configurar el tipo de retorno de la función
rust_lib.rust_add.restype = ctypes.c_int32

print("Llamando a la función de Rust...")
result = rust_lib.rust_add(10, 20)
print(f"Result from Rust: {result}")