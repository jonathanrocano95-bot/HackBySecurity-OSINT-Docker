# HackBySecurity-OSINT-Docker
Prototipo de herramienta OSINT basada en Docker  para prácticas profesionales
# Prototipo de Automatización OSINT - Hack By Security

Este repositorio contiene el desarrollo de mi prototipo para la fase de reconocimiento pasivo, diseñado como parte del Plan Director de Seguridad. La herramienta utiliza contenedores Docker para garantizar un entorno aislado, seguro y fácil de desplegar por cualquier miembro del equipo de auditoría.

## 🚀 Objetivo del Proyecto
El objetivo principal es automatizar la recolección de inteligencia de fuentes abiertas (OSINT) sobre dominios corporativos. Mi prototipo identifica subdominios expuestos y prepara la información para análisis posteriores de vulnerabilidades, cumpliendo con los estándares de documentación técnica exigidos en el máster.

## 🛠️ Herramientas Integradas
Para este prototipo he seleccionado y configurado las siguientes tecnologías:
* **theHarvester**: Para la recolección de subdominios y correos electrónicos desde fuentes como CRTsh y Bing.
* **Docker**: Para la contenedorización de cada herramienta, asegurando que las dependencias no entren en conflicto.
* **Python 3**: He desarrollado un script procesador que actúa como "cerebro" para normalizar los datos al formato JSON oficial.

## 📁 Estructura del Repositorio
He organizado el proyecto de forma modular para facilitar su escalabilidad:
* `/theHarvester`: Contiene el Dockerfile con la receta de instalación de la herramienta.
* `/Sherlock`: (En desarrollo) Dockerfile para la búsqueda de perfiles en redes sociales.
* `procesador_osint.py`: Mi script personalizado para la gestión de datos y generación de reportes.
* `prueba_osint.json`: Un ejemplo real de los resultados obtenidos durante mis pruebas.

## ⚙️ Instalación y Uso

### 1. Construir la imagen
Desde la terminal de la VM, me sitúo en la carpeta del proyecto y ejecuto:
```bash
docker build -t osint-tool:v1-harvester ./theHarvester
