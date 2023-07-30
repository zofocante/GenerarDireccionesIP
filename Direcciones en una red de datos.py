import socket # Importar la libreria  Socket
import ipaddress # Importar la libreria ipaddress 

print("----------------------------------------------------------------")
print("Selección de direcciones en una red de datos.") 
print("----------------------------------------------------------------")
opcion = input("""\n¿Quieres generar direcciones en una red con  
a) Una Dirección IP con Prefijo (mascara de subred) 
b) Solo el prefijo (mascara de subred)? 

Escribe opción [Ejemplo: a o b]: """)

print("\n----------------------------------------------------------------")
while True:
    try: 
        if opcion.lower() == 'a':
            ip = input("\nDirección IP/Prefijo [Ejemplo: 192.168.1.4/24 o 192.168.1.0/24] → ") 
            iface = ipaddress.ip_interface(ip)
            ifacenetwork = ipaddress.IPv4Network(iface.network)
            
            cont = 0
            for addr in iface.network:
                cont+=1 
                
            print()
            print(". Dirección de red (con prefijo):", iface.network)
            print(". Default Gateway (Puerta de enlace predeterminada):", ifacenetwork.network_address + 1)
            print(". Su IP: ",ifacenetwork.network_address + 2)
            print(". Dirección de broadcast:",ifacenetwork.broadcast_address)
            print(". Numero total de IP validos en su red:",ifacenetwork.num_addresses - 2)            
            print(". Total de direcciones en su red:", cont)
            print()
            break
        
        elif opcion.lower() == 'b':
            mask_local = input("\nPrefijo de la red [Ejemplo: 24] → ") 
            mi_pc = socket.gethostname() 
            ip_pc = socket.gethostbyname(mi_pc) # IP de host. 
            
            iface = ipaddress.ip_interface(ip_pc)
            ifacenetwork = ipaddress.IPv4Network(iface.network)
            
            ip_cc = str(ip_pc+'/'+mask_local) # Dar forma en formato str, ejm = 192.168.4.5/24
            ip_form = ipaddress.ip_network(ip_cc,strict = False) # Hallar la red 
            mi_red_t = 32 - int(mask_local)
            mi_red_valid = (2**mi_red_t) - 2
            total_red_valid = (2**mi_red_t)
            
            print()
            print(". Hostname: " + mi_pc) # El nombre de mi Host
            print(". Dirección de red (con prefijo): " + str(ip_form))
            print(". Default Gateway (Puerta de enlace predeterminada): " + ip_pc) 
            print(". Su IP: ", ifacenetwork.network_address + 1) 
            print(". Dirección brodcast: " + str(ip_form.broadcast_address) ) 
            print(". Numero total de IP validos en su red: "+ str(mi_red_valid)) 
            print(". Total de direcciones en su red: " + str(total_red_valid))
            break
    
    except ValueError: 
        print("Error de digitación, trata de tipear otra vez.")