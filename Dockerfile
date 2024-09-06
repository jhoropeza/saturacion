FROM python:3.8.0

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y actualizar pip
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar todos los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto 8080
EXPOSE 80

# Usar CMD en lugar de ENTRYPOINT para mayor flexibilidad
CMD ["python", "app.py"]
