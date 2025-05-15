import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests

lista_palabras = ["bicicleta", "celular", "nissan", "yamaha", "television", "dulces", "botilitos","camisas"]
palabra = random.choice(lista_palabras)
headers = {"User-Agent": UserAgent().random}


url = f"https://www.amazon.com/s?k={palabra}" 
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    respuesta = soup.find_all("div", {"data-component-type": "s-search-result"})

    print(f"Palabra clave: {palabra}")
    print("Resultado:\n")
    cont = 0
    for res in respuesta:
        if cont == 5:
            break
        palabra_clave = res.find("h2")
        nombre = palabra_clave.text.strip() if palabra_clave else "Título no disponible"
        precio_producto = res.find("span", class_="a-price-whole")
        if precio_producto:
            precio= precio_producto.text.strip()
        else:
            precio = "Precio no disponible"

        print(f"{cont + 1}. {nombre}\n   Precio: {precio}\n")
        cont += 1
else:
    print("Error Amazon:", response.status_code)
