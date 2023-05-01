FROM python:3.9

# Define um diretório de trabalho
WORKDIR /backend


# Atualiza o pip
RUN pip install --upgrade pip

# Instala o pacote virtualenv
RUN pip install virtualenv

# Cria um ambiente virtual
RUN virtualenv venv

# Ativa o ambiente virtual
RUN python source venv/bin/activate

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt /backend/
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do seu aplicativo para o diretório de trabalho
COPY . /backend/

# Exponha a porta em que o seu aplicativo será executado
EXPOSE 8000

# Inicie o seu aplicativo com o seguinte comando
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



