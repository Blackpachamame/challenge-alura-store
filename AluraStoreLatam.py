import pandas as pd

url_1 = "https://raw.githubusercontent.com/Blackpachamame/challenge-alura-store/refs/heads/main/base-de-datos-challenge1-latam/tienda_1.csv"
url_2 = "https://raw.githubusercontent.com/Blackpachamame/challenge-alura-store/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url_3 = "https://raw.githubusercontent.com/Blackpachamame/challenge-alura-store/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url_4 = "https://raw.githubusercontent.com/Blackpachamame/challenge-alura-store/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda_1 = pd.read_csv(url_1)
tienda_2 = pd.read_csv(url_2)
tienda_3 = pd.read_csv(url_3)
tienda_4 = pd.read_csv(url_4)

tienda_1.head()