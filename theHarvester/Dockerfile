# Imagen base ligera de Python
FROM python:3.12-slim

# Instalamos dependencias del sistema y git
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clonamos Sherlock
RUN git clone https://github.com/sherlock-project/sherlock.git /app

# Nos movemos a la carpeta
WORKDIR /app

# Instalamos los requisitos de Sherlock
RUN pip install .

# Punto de entrada para la herramienta
ENTRYPOINT ["sherlock"]
CMD ["--help"]
