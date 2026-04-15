# Usamos la misma versión de Ubuntu que tienes en tu VM
FROM ubuntu:24.04

# Evitamos que el instalador nos haga preguntas durante la creación
ENV DEBIAN_FRONTEND=noninteractive

# Instalamos las herramientas básicas necesarias
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clonamos la herramienta directamente en la carpeta /app
RUN git clone https://github.com/laramies/theHarvester.git /app

# Nos movemos a esa carpeta
WORKDIR /app

# Instalamos theHarvester y todas sus dependencias modernas
RUN pip3 install . --break-system-packages

# Configuramos el contenedor para que al arrancar use la herramienta directamente
ENTRYPOINT ["theHarvester"]
CMD ["-h"]
