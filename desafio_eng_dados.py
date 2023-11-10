import requests
from bs4 import BeautifulSoup

# Função para obter dados da API OpenWeatherMap
def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Função para obter dados do site Toscrape
def get_books_data():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = [book.text.strip() for book in soup.find_all("h3")]
    return books

# Função para agregar os dados
def aggregate_data(weather_data, books_data):
    # Exemplo simples de agregação: unindo os dados em um dicionário
    aggregated_data = {"weather": weather_data, "books": books_data}
    return aggregated_data

# Substitua 'sua_api_key' pela chave da API OpenWeatherMap
api_key = '9220ecc19c465eadd174cfb7a9a9c464'
city = 'London'  # Você pode alterar para a cidade de sua escolha

# Coletando dados da API
weather_data = get_weather_data(api_key, city)

# Coletando dados do site
books_data = get_books_data()

# Agregando os dados
aggregated_data = aggregate_data(weather_data, books_data)

# Apresentando os dados (neste caso, em formato de dicionário)
print(aggregated_data)
