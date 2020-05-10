#!"C:\Users\CISCO\AppData\Local\Programs\Python\Python38-32\python.exe"
#!/usr/bin/env python3

###############################################################################################################################################
##  Proyecto: SCRIPT DE CONFIGURACIÓN APIC-EM                                                                                                ##
##  Curso DEVNET - Beca CISCO    -   PUE  - MODEL DRIVEN PROGRAMMABILITY                                                                     ##
##  Alumno: José Manuel Martín Acemel  - jomaracem@gmail.com                                                                                 ##
##  Fecha: 20/03/20                                                                                                                          ##
###############################################################################################################################################
"""
- FUNCIONES OBLIGATORIAS DE ESTE SCRIPT (APIC-EM):
    OK - Crear un programa que permita conectarse con el controlador APIC-EM de Cisco
    OK - El usuario tendrá que escoger la opción que quiera (no tendrá que especificar la url a mano)
    OK - Añadir, como mínimo, 4 funcionalidades
"""
## Importando modulos .........................................................................................................................
import msvcrt
import json
import requests
from tabulate import*
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
    print("                   ..,;::;;'      ';;,.     .;;;:;;'.            .';;:;;,.        ..,;;:;,..             \n\n\n")
    return
## Solcicitud ticket APIC-EM ..................................................................................................................
def get_ticket():
    ok=True
    requests.packages.urllib3.disable_warnings()
    api_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket")
    headers = {
        "content-type":"application/json",
        "X-Auth-Token": ""
    }
    body_json = {
        "username" : "devnetuser",
        "password" : "Xj3BDqbU"
    }
    # Respuesta solicitud ..............................................................
    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
    codresp=resp.status_code
    if codresp==200:
        print(" Estado nueva solicitud de ticket: Petición resuelta con exito.")
    else:
        print("\n   Estado nueva solicitud de ticket: ¡Algo salió mal! ...\n")
        print("     - Codigo de error: ",resp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    # print("El numero de ticket es: ", serviceTicket)
    return serviceTicket
    # Aplicando Token APIC-EM ........................................................
## 1 - Solicitud de información de inventario de dispositivos APIC-EM .........................................................................
def inf_device():
    name_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device")
    ticket=get_ticket()
    tokheaders={
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    deviceresp=requests.get(name_url,headers=tokheaders,verify=False)
    coderephostdevice=deviceresp.status_code
    if coderephostdevice==200:
            print("    \nAplicando token: Aplicado con exito.\n\n\n")
    else:
        print("\n     Error aplicando el token ...\n")
        print("     - Codigo de error: ",deviceresp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    responsedevice_json = deviceresp.json()
    devlist=[]
    i = 0
    print("\n - Inventario de dispositivos: \n\n")
    for item in responsedevice_json["response"]:
        i += 1
        host = [
                i,
                item["family"],
                item["serialNumber"],
                item["type"],
                item["macAddress"],
                item["hostname"]
                ]
        devlist.append(host)
    table_header = [
                    "Nº",
                    "FAMILIA",
                    "NUM.SERIE",
                    "TIPO",
                    "DIRECCIÓN MAC",
                    "HOSTNAME"
                    ]
    print("\n\n     - INVENTARIO DE RED:")
    print(tabulate(devlist,
                            headers=(table_header),
                            tablefmt='fancy_grid',
                            stralign="center",
                            floatfmt=".0f"))
    return
## 2 - Solicitud de información de host APIC-EM................................................................................................
def inf_host():
    host_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host")
    ticket=get_ticket()
    tokheaders={
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    hostresp=requests.get(host_url,headers=tokheaders,verify=False)
    coderephost=hostresp.status_code
    if coderephost==200:
            print(" \nAplicando token: Aplicado con exito.\n\n")
    else:
        print("\nError aplicando el tocken ...\n")
        print("     - Codigo de error: ",hostresp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    responsehost_json = hostresp.json()
    hostlist=[]
    i = 0
    print("\n - Listado de host: \n\n")
    for item in responsehost_json["response"]:
        i += 1
        host = [
                i,
                item["hostType"],
                item["hostIp"],
                item["hostMac"]
                ]
        hostlist.append(host)
    table_header = [
                    "Nº",
                    "TIPO",
                    "IP",
                    "MAC"
                    ]
    print(tabulate(hostlist,
                            headers=(table_header),
                            tablefmt='pipe',
                            stralign="center",
                            floatfmt=".0f"))
    return
## 3 - flow  ..................................................................................................................................
def flow():
    flow_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis")
    ticket=get_ticket()
    tokheaders={
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    flowresp=requests.get(flow_url,headers=tokheaders,verify=False)
    coderephost=flowresp.status_code
    if coderephost==200:
            print(" \nAplicando token: Aplicado con exito.\n\n")
    else:
        print("\nError aplicando el token ...\n")
        print("     - Codigo de error: ",flowresp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    responseflow_json = flowresp.json()
    flowlist=[]
    print("\n - Analisis de flujo: \n\n")
    i = 0
    for item in responseflow_json["response"]:
        i += 1
        host = [
                i,
                item["sourceIP"],
                item ["destIP"],
                item ["status"]
                ]
        flowlist.append(host)
        table_header = [
                    "Nº",
                    "IP ORIGEN",
                    "IP DESTINO",
                    "ESTADO",
                    ]   
    print( tabulate(flowlist,
                            headers=(table_header),
                            tablefmt='orgtbl',
                            stralign="center",
                            floatfmt=".0f"))
    return
## 4 - VLAN detectadas en APIC-EM ..............................................................................................................
def vlan():  
    vlan_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/topology/vlan/vlan-names")

    ticket=get_ticket()
    tokheaders={
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    resp=requests.get(vlan_url,headers=tokheaders,verify=False)
    codevlan=resp.status_code
    if codevlan==200:
            print(" \nAplicando token: Aplicado con exito.\n\n")
    else:
        print("\nError aplicando el token ...\n")
        print("     - Codigo de error: ",resp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    responsevlan = resp.json()["response"]
    print("\n- Listado VLAN localizadas: \n\n"+"Nº   VLAN:\n"+"--","-"*9)
    for i, item in enumerate (responsevlan,1):
        print(str(i)+":",item)
    return
## 5 - TOPOLOGIA FISICA  en APIC-EM ............................................................................................................
def topof():
    topof_url=("https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/topology/physical-topology")
    ticket=get_ticket()
    tokheaders={
        "content-type": "application/json",
        "X-Auth-Token": ticket
    }
    topofresp=requests.get(topof_url,headers=tokheaders,verify=False)
    coderephost=topofresp.status_code
    if coderephost==200:
            print(" \nAplicando token: Aplicado con exito.\n\n")
    else:
        print("\nError aplicando el token ...\n")
        print("     - Codigo de error: ",topofresp.status_code," Vuelve a intentarlo mas tarde. \n","    - Si el problema persiste contacte con el Centro Atencion Usuarios.\n\n",">>> Puse una tecla para salir.")
        return msvcrt.getch()
    responsetopof = topofresp.json()
    topoflist=[]
    print("\n\n - Topología fisica: \n")
    i = 0
    for item in responsetopof["response"]["nodes"]:
        i += 1
        host = [
                i,
                item["deviceType"],
                item ["label"],
                item ["ip"],
                item["nodeType"],
                item["family"]
                ]
        topoflist.append(host)
        table_header = [
                        "Nº",
                        "TIPO DE DISPOSITIVO",
                        "ETIQUETA",
                        "IP",
                        "TIPO NODO",
                        "FAMILIA"
                    ]   
    print( tabulate(topoflist,
                            headers=(table_header),
                            tablefmt='fancy_grid',
                            stralign="center",
                            floatfmt=".0f"))
    return
# Interacciones del Usuario ....................................................................................................................
def cabecera():                                                                                        
    ## Titulo de script ........................................................................................................................
    logo()
    print("\n            C O N F I G U R A D O R  -  A P I C - E M\n"+"     "+"-"*55)
    ## Descripcion de script ...................................................................................................................
    print("\n\n"+"     - Este script le permite realizar tareas de networking en su APIC-EM  : \n")
    print("     1  - Mostrar inventario de dispositivos.")
    print("     2  - Mostrar información de host.")
    print("     3  - Mostrar analisis de flujo.")
    print("     4  - Mostrar vlan localizadas.")
    print("     5  - Mostrar topologia fisica de la red.")
    print("     0  - Salir\n")
    inter_user=input("\n"+"    Introduzca el numero de la operación que desea ejecutar y pulse enter: ")
    if (inter_user=="1"):
        inf_device()
        print("\n\nPresione una tecla para continuar\n\n")
        msvcrt.getch()
        cabecera()
    if (inter_user=="2"):
        inf_host()
        print("\n\nPresione una tecla para continuar\n\n")
        msvcrt.getch()
        cabecera()
    if (inter_user=="3"):
        flow()
        print("\n\nPresione una tecla para continuar\n\n")
        msvcrt.getch()
        cabecera()
    if (inter_user=="4"):
        vlan()  
        print("\n\nPresione una tecla para continuar\n\n")
        msvcrt.getch()
        cabecera()
    if (inter_user=="5"):
        topof()  
        print("\n\nPresione una tecla para continuar\n\n")
        msvcrt.getch()
        cabecera()
    if (inter_user=="0"):
        exit 
################################################################################################################################################
# ARRANQUE SCRIPT ..............................................................................................................................     
cabecera()