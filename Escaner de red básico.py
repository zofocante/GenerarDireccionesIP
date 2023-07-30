import socket
import sys
import platform 
import os 
from datetime import datetime 

while True: 
    usuario = input("""\n¿Que quieres escanear? 
1) Toda tu SUBRED 
2) Una SUBRED en especifico
3) Un HOST en especifico
4) Salir de la ejecución

[1/2/3/4] Opción: """)
    
    # DATO ENTEGRADO POR EL PROGRAMA
    if usuario == "1":
        # FUNCIÓN PARA EL ESCANEO DE DIRECCIONES IP
        def get_Host_name_IP():
            
            # Se halla la dirección IP de nuestro host 
            try: 
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                host_ip = s.getsockname()[0] #192.168.1.11/24
                s.close()
            except: 
                print("No se puede obtener el nombre de host y la IP")
                
            ipDividida = host_ip.split('.')
            
            # Creación de un prefijo de la red y su rango
            try: 
                red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.' 
                comienzo = int(input("\nIngresa el número de comienzo de la subred [Ejemplo: 1]: ")) # 1
                fin = int(input("Ingresa el número donde termina la subred [Ejemplo: 20]: ")) # 20
            except: 
                print("Error !!!") 
                sys.exit(1)  
                    
            # Comprobación del sistema operativo
            if (platform.system()=="Windows"):
                ping = "ping -n 1"
            else:
                ping = "ping -c 1" 
            
            # Tiempo de inicio
            tiempoInicio = datetime.now() 

            print("\n[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin), "\n") # 192.168.1.1 - 20
            
            # Recorre el rango de direcciones IP deseadas
            for subred in range(comienzo, fin+1): # 1, 21 → 1,2,3,4, ... 20
                direccion = red+str(subred) # 192.168.1.1. 192.168.1.2, ...., 192.168.1.20
                response = os.popen(ping+" "+direccion) 
                mac = os.popen("arp -a"+" "+direccion+" "+"-v") 
                for line in response.readlines(): 
                    if ("ttl" in line.lower()): 
                        mac_e_ipp = mac.readlines()
                        print("IP ACTIVA:", direccion)
                        print("MÁS DETALLE:", mac_e_ipp)
                        print()
                        break 
            
            tiempoFinal = datetime.now() 
            tiempo = tiempoFinal - tiempoInicio 
            print("[*] El escaneo ha durado %s"%tiempo) 
            
        get_Host_name_IP() 
        
    # DATO ENTREGADO POR EL USUARIO
    elif usuario == "2":
        ip = input("\nIngresa una SUBRED [Ejemplo: 192.168.1.0]: ") 
        ipDividida = ip.split('.')
        
        # Se verifica la IP dada por el usuario  
        try: 
            red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.' 
            comienzo = int(input("\nIngresa el número de comienzo de la subred [Ejemplo: 1]: ")) 
            fin = int(input("Ingresa el número donde termina la subred [Ejemplo: 20]: ")) 
        except: 
            print("Error !!!") 
            sys.exit(1) 
        
        # Comprobación del sistema operativo
        if (platform.system()=="Windows"):
            ping = "ping -n 1"
        else : 
            ping = "ping -c 1" 
    
        tiempoInicio = datetime.now()
        
        print("\n[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin), "\n") 
        
        # Recorre el rango de direcciones IP deseadas  
        for subred in range(comienzo, fin+1): 
            direccion = red+str(subred) 
            response = os.popen(ping+" "+direccion)
            mac = os.popen("arp -a"+" "+direccion+" "+"-v")
            for line in response.readlines(): 
                if ("ttl" in line.lower()):  
                    mac_e_ipp = mac.readlines()
                    print("IP ACTIVA:", direccion)
                    print("MÁS DETALLE:", mac_e_ipp)
                    print()
                    break 
                
        # Tiempo del final y su duración    
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio 
        print("[*] El escaneo ha durado %s"%tiempo) 
    
    # El USUARIO BUSCA UNA IP o HOST EN ESPECIFICO
    elif usuario == "3":
        try: 
            ip = input("\nIngresa una IP [Ejemplo: 192.168.1.20]: ")
        except: 
            print("No ejecuto bien la IP")
    
        # Comprobación del sistema operativo
        if (platform.system()=="Windows"):
            ping = "ping -n 1"
        else: 
            ping = "ping -c 1" 
    
        tiempoInicio = datetime.now()
                
        # Recorre el rango de direcciones IP deseadas  
        response = os.popen(ping+" "+ip)
        mac = os.popen("arp -a"+" "+ip+" "+"-v")
        for line in response.readlines(): 
            if "ttl" in line.lower():  
                mac_e_ipp = mac.readlines()
                print()
                print("IP ACTIVA:", ip)
                print("MÁS DETALLE:", mac_e_ipp) 
            elif "inaccesible" in line.lower(): 
                print("\n[*] No esta ACTIVO la IP: {}\n".format(ip))
                break           
        
        # Tiempo del final y su duración    
        tiempoFinal = datetime.now()
        tiempo = tiempoFinal - tiempoInicio 
        print("[*] El escaneo ha durado %s"%tiempo)
         
        
    elif usuario == "4": 
        print("\nOK, se termina la sesión") 
        break
    
    # DATO ERRADO ENTREGADO       
    else: 
        print("!!! Haz marcado incorrectamente, vuelve a intentarlo..\n")