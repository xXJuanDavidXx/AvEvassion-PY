buf =  b"Insertas el shellcode"



encrypted = bytearray()
key = 0xAA #Llave de cifrado jjsjs

for b in buf:
    encrypted.append(b ^ key)

print("encrypted_buf = bytes([")
for i in range(0, len(encrypted), 10): #Para el rango de 0 a la longitud de encrypted de 10 en 10
    chunk = encrypted[i:i+10] #desde i hasta 10 pocisiones adelante
    print("    " + ", ".join(f"0x{b:02x}" for b in chunk) + ",") #Preparamos la impresion del string en hexadecimal
print("])") 

#Se tiene que copiar el resultado en la variable que almacena el shellcode en thegame















