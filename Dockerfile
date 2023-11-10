FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Substitua 'sua_api_key' pela chave válida da API OpenWeatherMap
ENV API_KEY='9220ecc19c465eadd174cfb7a9a9c464'
ENV CITY='London'

# Agende a execução periódica com base em uma variável de ambiente
ENV CRON_SCHEDULE='0 * * * *'  # A cada hora

CMD ["sh", "-c", "python main.py"]
