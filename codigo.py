import requests
import numpy as np
import pandas as panda
from bs4 import BeautifulSoup

x = 25
y = np.sqrt(x)
print(y)

def get_wikipedia_summary(query):
    """Obtiene el resumen de una búsqueda en Wikipedia."""
    url = f"https://en.wikipedia.org/wiki/{query}"
    response = requests.get(url)

    if response.status_code != 200:
        return "Lo siento, no pude obtener información en Wikipedia."

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')

    if paragraphs:
        return paragraphs[0].text
    return "No se encontró información."

def main():
    print("Bienvenido al chatbot de Wikipedia. ¿Sobre qué tema te gustaría saber más?")
    while True:
        user_input = input("Tu pregunta (o 'salir' para terminar): ")
        if user_input.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Usar la entrada del usuario como consulta
        query = user_input.replace(' ', '_')
        summary = get_wikipedia_summary(query)
        print(summary)

if __name__ == "__main__":
    main()
