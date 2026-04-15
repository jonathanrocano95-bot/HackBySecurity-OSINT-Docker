import json
import subprocess

def generar_reporte_osint(dominio):
    # Aquí inicio el proceso de recolección para el dominio que he elegido
    print(f"[*] Iniciando mi recolección OSINT para: {dominio}")
    
    # En este paso, ejecuto 'theHarvester' desde mi script. 
    # Le pido que busque en crtsh y bing, y que me guarde un archivo temporal llamado 'temp_data'
    subprocess.run(["theHarvester", "-d", dominio, "-l", "50", "-b", "crtsh,bing", "-f", "temp_data"])

    # Ahora intento leer los resultados que generó la herramienta para poder procesarlos
    try:
        with open("temp_data.json", "r") as f:
            mis_datos_crudos = json.load(f)
    except:
        # Si algo falla o no hay datos, inicializo la lista de hosts vacía para evitar errores
        mis_datos_crudos = {"hosts": []}

    # Aquí es donde construyo la estructura exacta que me pide el esquema del proyecto
    # Estoy organizando la información de forma jerárquica
    mi_reporte_final = {
        "domains": [
            {
                "domain": dominio,
                "subdomains": [],
                "public_emails": [],
                "breached_emails": [],
                "open_ports": [],
                "dorks": []
            }
        ]
    }

    # Recorro cada host encontrado y lo transformo al formato de mi prototipo
    for host in mis_datos_crudos.get("hosts", []):
        nuevo_subdominio = {
            "hostname": host,
            "ip": "0.0.0.0",  # De momento lo dejo así, más adelante integraré resolución de IP
            "status": "alive",
            "source": "theHarvester (Mi Prototipo)"
        }
        # Añado este subdominio a mi estructura final
        mi_reporte_final["domains"][0]["subdomains"].append(nuevo_subdominio)

    # Finalmente, guardo todo en un archivo JSON con el formato oficial
    nombre_del_archivo = f"reporte_final_{dominio}.json"
    with open(nombre_del_archivo, "w") as f:
        json.dump(mi_reporte_final, f, indent=4)
    
    print(f"[+] ¡Hecho! He generado mi reporte en: {nombre_del_archivo}")

# Esta es la parte principal donde mi script empieza a correr
if __name__ == "__main__":
    # Aquí el script se detiene y me pregunta qué dominio quiero investigar.
    # Yo lo escribo manualmente en la terminal (ej: google.com) y pulso Enter.
    mi_objetivo = input("Introduce el dominio a investigar: ")
    generar_reporte_osint(mi_objetivo)
