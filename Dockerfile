# Usa una imagen base de Python
FROM python:3.12-alpine

# Establece el directorio de trabajo
WORKDIR /app

ENV FLASK_ENV=production

# Copia el Pipfile y Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Instala las dependencias
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copia el resto de la aplicación
COPY . .

# Expone el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
