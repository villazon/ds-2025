# Imagen base ligera
FROM python:3.11-slim

# Crear directorio de la app
WORKDIR /app

# Copiar solo los archivos necesarios
COPY app.py /app/

# Instalar Flask (solo lo necesario)
RUN pip install --no-cache-dir -r requirements.txt

# El servicio escucha en 5000
EXPOSE 5000

# Ejecutar la app
CMD ["python", "app.py"]
