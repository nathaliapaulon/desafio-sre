# Use uma imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY app/requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que a aplicação usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
