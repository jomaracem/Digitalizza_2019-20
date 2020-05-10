#!"C:\Users\CISCO\AppData\Local\Programs\Python\Python38-32\python.exe"
#!/usr/bin/env python3

###############################################################################################################################################
##  Proyecto: SCRIPT DE CONFIGURACIÓN CSR1000V.                                                                                              ##
##  Curso DEVNET - Beca CISCO    -   PUE  - MODEL DRIVEN PROGRAMMABILITY                                                                     ##
##  Alumno: José Manuel Martín Acemel  - jomaracem@gmail.com                                                                                 ##
##  Fecha: 20/04/20                                                                                                                          ##
###############################################################################################################################################
""" 
FUNCIONES OBLIGATORIAS DE ESTE SCRIPT (CSR1000V):
    OK - Crear un script que permita conectarnos a nuestra Router CSR1000v (bien sea en local o a través del Sandbox) y que, a través de un menú, nos aparezcan 
         una serie de opciones que nos permita realizar las siguientes tareas:
    - Obtener un listado de las interfaces del router (indicar, en modo tabla, el nombre de la interfaz, su IP y MAC)
    OK - Crear Interfaces
    OK - Borrar Interfaces
    - Obtener la tabla de routing y crear una tabla con Identificador (0,1,2...), Red de destino, e Interfaz de salida.
    - Implementar una petición a 2 módulos de yang diferentes compatibles con nuestro router
"""
## Importando modulos .........................................................................................................................
from netmiko import ConnectHandler
from ncclient import manager
import xmltodict
import xml.dom.minidom
import msvcrt
import tabulate
import requests
import urllib.parse
import netmiko
import ncclient
import json
import simplejson
## Logo .......................................................................................................................................
def logo():    
    print("\n\n"+"                             .oOkc.                                          ;kOx'                       ")
    print("                             CISCO.                                          oWMNl                       ")
    print("                             CISCO.                                          oWWNl                       ")
    print("                  ,lo:.      CISCO.      .pue.                   .:km'       oWWNl       ;oo;            ")
    print("                 '0WWNc      CISCO.     .oPUEl                   ;KMWx.      oWWNl      '0MM0,           ")
    print("      .;:;.      ,0WWNc      CISCO.     .dPUEl       .:c:'       ;KMWx.      oWWNl      '0MMK,      .;c;.")
    print("     .dNWNd.     ,0WWNc      CISCO.     .dPUEl      .xWWWO'      ;KMWx.      oWWNl      '0MMK,      cNWNo")
    print("     .kWWWk.     ,0MWNc      CISCO.     .dPUEl      .OWMM0,      ;KMWk.      oWMNl      '0MMK,      lWWWx")
    print("      ;xOx;      .lOOd'      CISCO.      ;pue,      .cO0Oo.      .101:       oWWNl      .lOOl.      ,xOk;")
    print("                             :XMMO.                    .                     oWMNl                       ")
    print("                             .:oo,                                           .ldc.                       ")
    print("                                                                                                         ")
    print("                                                                                                         ")
    print("                  ..;looool:.    .;llc.      .;cooooo:.         .,,becas,'       .':looool:'.            ")
    print("                .lOXWWWNNNWK;    .OMMX;     :0NWNKOO0x'       ,DIGITALIZAd.    .lONWWWNNWWWNOl.          ")
    print("               ,ONMW0o;''',;.    .OMMX;    .OMWW0:....      .oXWWNx:,'',;'    ;0WWWOc;'';lONWWO,         ")
    print("              .dWWMK;            .OMWX;    .c0XNNX0xo;.     ;KMWNd.          .xWWWO'      .kWWWo.        ")
    print("               oWWWXc            .OMWX;      .';cokXWN0x;   ;KMWWx.          .xWWW0;      ;0WWNo         ")
    print("               .dNWWXklc:cll.    .OMMX;     ';''',oKMWXKc   .c0WWN0dlcccl;    'xNWWKxlcclxXWWNx.         ")
    print("                 ;dOXNWWWWWK,    .OWWK;    .xNNXXNWNKx;..     .cxKNWWWWWNd.    .,o0XWWWWWNX0d;.          ")
    print("                   ..,;::;;'      ';;,.     .;;;:;;'.            .';;:;;,.        ..,;;:;,..             ","\n\n\n")
    return
## Titulo de script .........................................................................................................................
def titulo():
    print("\n"+"    NETWORKING_CSR1000V\n"+"    "+"-"*19)
## Parametros de conexion .................................................................................................................
#SSH..................................................
con_ssh=ConnectHandler(
    device_type='cisco_ios',
    host='sbx-iosxr-mgmt.cisco.com',
    port=8181,
    username='admin',
    password='C1sco12345')
def show_start():
    print("Enviando show startup-config")
    output=con_ssh.send_command("show startup-config")
    print("Configuración de arranque:\n{}\n".format(output))
    return
# 2 - Mostrar configuración en ejecución ......................................................................................................
def show_run():
    print("Enviando 'show running-config")
    output=con_ssh.send_command("show running-config")
    print("Configuración en ejecución:\n{}\n".format(output))
    return
# 3 - Mostrar versiones OS ....................................................................................................................
def show_ver():
    print("Enviando 'show version")
    output=con_ssh.send_command("show version")
    print("versión del OS de cisco: \n{}\n".format(output))
    return
# 4 - Mostrar estado resumido de interfaces ...................................................................................................
def show_interface():
    print("Enviando 'sh ip int brief'...\n")
    output=con_ssh.send_command("show ip int brief")
    print("Estado y configuración ip de las interfaces:\n{}\n".format(output))
    return
# 5 - Mostrar estado interfaces ...............................................................................................................
def show_ip_route():
    print("Enviando 'sh ip route'...")
    output=con_ssh.send_command("show ip route")
    print("Tabla de enrutamiento:\n{}\n".format(output))
    return
# 6 - Configurar nueva interface ...............................................................................................................
def new_interface():
    n_interface=input("Introduzca la interface: ")
    n_ip=input("Introduzca la dirección ip : ")
    n_mask=input("Introduzca la mascara de red: ")
    n_descript=input("Introduzca una descripción para la interface: ")
    sp=(" ")
    config_commands = [
    "int"+sp+n_interface,
    "ip address"+sp+n_ip+sp+n_mask,
    "description"+sp+n_descript,
    "no shutdown"]
    output=con_ssh.send_config_set(config_commands)
    print("Se configurarón los siguientes paramotros de las interfaces:\n{}\n".format(output))
    return
# 7 - Eliminar interface .......................................................................................................................
def del_interface():
    d_interface=input("introduzca la interface que desea eliminar : ")
    sp=(" ")
    config_commands = [
    "no int"+sp+d_interface
    ]
    output=con_ssh.send_config_set(config_commands)
    print("Se elimino la interface:\n{}\n".format(output))
    return
# 8 - Cambiar estado administrativo de las interfaces  .........................................................................................
def adm_interface():
    sp=(" ")
    a_interface=input("introduzca la interface a la que desea cambiar su valor administrativo : ")
    output=con_ssh.send_command("show interface"+sp+a_interface)
    print("El estado actual de"+sp+a_interface+sp+": \n{}\n".format(output))
    a_cambiest=input("introduzca 1 para activar la interfaz, 2 para desactivarla administrativamente: ")
    if (a_cambiest=="1"):
        config_commands = [
        "interface"+sp+a_interface,
        "no shutdown",
        "exit"]
        output=con_ssh.send_config_set(config_commands)
    if (a_cambiest=="2"):
        config_commands = [
        "interface"+sp+a_interface,
        "shutdown",
        "exit"]
        output=con_ssh.send_config_set(config_commands)
    
    output=con_ssh.send_command("show interface"+sp+a_interface)
    print("El estado actual de"+sp+a_interface+sp+": \n{}\n".format(output))
    return
# 9 - Mensaje de advertencia en el acceso al router ............................................................................................
def banner():
    mensaje=input("Introduzca el mensaje de advertencia a mostrar tras establecer conexión con el router. ")
    config_commands = [
        "banner motd # "+mensaje+" #",
        "exit"]
    output=con_ssh.send_config_set(config_commands)
    print("Solicitando guardado de la configuración activa...\n{}\n".format(output))
    return
# 10 - Cifrado de contraseñas almacenadas ......................................................................................................
def encrypt():
    cifrer=input("Este proceso cifrara todas las contraseñas almacenadas de forma irreversible.\n Pulse enter para salir sin aplicar o introduzca uno 1 pulse enter para aplicar. ")
    if cifrer=="1":
        config_commands = [
            "service password-encryption",
            "exit"]
        output=con_ssh.send_config_set(config_commands)
        print("Cifrando contraseñas...\n{}\n".format(output))
    else:
        exit   
    return
# 11 - Guardar configuracion en proceso a la memoria ...........................................................................................
def save_run():
    output=con_ssh.send_command("wr")
    print("Solicitando guardado de la configuración activa...\n{}\n".format(output))
    return
# 12 - ping ....................................................................................................................................
def ping():
    direccion=input("Introduzca la ip donde desea realizar el ping en remoto, debe estar delimitada por puntos ")
    sp=(" ")
    print("Eviando paquetes -_-_-_-_-")
    output=con_ssh.send_command("ping"+sp+direccion)
    print("PING:\n{}\n".format(output))
    return
# N0 - MODELOS YANG COMPATIBLES ..................................................................................................................
def yanin1():
    print(" Estableciendo conexión....")
    m = manager.connect(
        host="ios-xe-mgmt.cisco.com",
        port=10000,
        username="developer",
        password="C1sco12345",
        hostkey_verify=False
        )
    print(" - Capabilities compatibles con este dispositivo. (Modelos YANG):")
    for capability in m.server_capabilities:
        print(capability)
    return
# N1 - OBTENER INTERFAZ DEL ROUTER EN TABLA IP - INTERFAZ - MAC ................................................................................
def yanint():
    ## variable de ManagerConenect.................................................................... 
    requests.packages.urllib3.disable_warnings()
    api_url = "https://10.10.20.48/restconf/data/interfaces/interface"
    basic_auth=("developer","C1sco12345")
    headers={
        "Accept":"application/yang-data+json",
        "Content-Type":"application/yang-data+json"
        }
    resp = requests.get(api_url,auth=basic_auth, headers=headers, verify=False)
    resp_json = resp.json()
#data=json.dumps(resp_json["Cisco-IOS-XE-interfaces-oper:interface"],indent=4)
    lista=[]
    i=0
    for item in resp_json["Cisco-IOS-XE-interfaces-oper:interface"]:
        i += 1
        host = [
                i,
                item["name"],
                item["phys-address"],
                item["description"],
                item["ipv4"],
                item["ipv4-subnet-mask"],
                ]
        lista.append(host)

    table_header = [
                    "Nº",
                    "NOMBRE",
                    "MAC",
                    "DESCRIPCCIÓN",
                    "IPV4",
                    "MASC.RED"
                    ]
    print("\n\n     - INVENTARIO DE RED:")
    print(tabulate(lista,
                headers=(table_header),
                tablefmt='fancy_grid',
                stralign="center",
                floatfmt=".0f"))    
    return
# N1 - OBTENER INTERFAZ DEL ROUTER EN TABLA IP - INTERFAZ - MAC ................................................................
def yaninr():
    ## DEFINIR CONEXION ............................................................
    con=manager.connect(
        host="10.10.20.48",
        port=10000,
        username="developer",
        password="C1sco12345",
        hostkey_verify=True)
    ## FILTRO ........................................................................
    netconf_filter="""
    <filter>
        <native xmlns="https://cisco.com//Cisco-IOS-XE-route-map?module=Cisco-IOS-XE-route-map&revision=2018-12-05"/>
    </filter> """
    ## RECOGER CAPABILITIES ...........................................................
    netconf_reply=con.get_config(source="running", filter=netconf_filter)
    ## IMPRIMIENDO
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    return
# Interacciones del Usuario ....................................................................................................................
def cabecera():
    logo()
    titulo()
    print(" - Este script le permite revisar el estado de su enrutador y ejecutar cambios.\n\n"," - Elija una opción de la lista para continuar: \n")
    print(" 1  - Mostrar configuración de arranque.")
    print(" 2  - Mostrar configuración en ejecución.")
    print(" 3  - Mostrar versiones OS.")
    print(" 4  - Mostrar estado resumido de interfaces.")
    print(" 5  - Mostrar estado de interfaces.")
    print(" 6  - Configurar nueva interfaz.")
    print(" 7  - Eliminar interfaz.")
    print(" 8  - Cambiar estado administrativo de una interface.")
    print(" 9  - Establecer mensaje de advertencia en el inicio.")
    print(" 10 - Cifrar contraseñas almacenadas.")
    print(" 11 - Guardar configuración en proceso a la memoria.")
    print(" 12 - PING")
    print(" 13 - Mostrar capabilities YANG compatibles.")
    print(" 14 - Mostar interfaces - YANG.")
    print(" 15 - Mostrar rutas - YANG.")
    print(" 0  - Salir")
    inter_user=input("\n"+" Introduzca el numero de la operación que desea ejecutar: ")
    if (inter_user=="1"):
        show_start()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="2"):
        show_run()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="3"):
        show_ver()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="4"):
        show_interface()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="5"):
        show_ip_route()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="6"):
        new_interface()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="7"):
        del_interface()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="8"):
        adm_interface()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="9"):
        banner()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="10"):
        encrypt()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="11"):
        save_run()
        print("\n"," Presione una tecla para continuar")
        save_run()
        cabecera()
    if (inter_user=="12"):
        ping()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="13"):
        yanin1()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="14"):
        yanint()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()
    if (inter_user=="15"):
        #yaninr()
        print("\n"," Presione una tecla para continuar")
        msvcrt.getch()
        cabecera()        
    if (inter_user=="0"):
        exit 
################################################################################################################################################
# ARRANQUE SCRIPT ..............................................................................................................................     
cabecera()


