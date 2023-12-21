import requests
from bs4 import BeautifulSoup
from itertools import zip_longest

NomArticles = []
links = []
base_url = "https://www.tayara.tn/"
url = "https://www.tayara.tn/fr/ads/c/V%C3%A9hicules/?page=1"
result = requests.get(url)
src = result.text

soup = BeautifulSoup(src, "html.parser")
blocks = soup.find_all('article', class_="mx-0")

for block in blocks:
    articles = block.find_all('a', target='_blank')

    # Afficher les liens pour chaque bloc
    for article in articles:
        href = article.get('href')
        if href:
            hrefcomplet = base_url + href
            links.append(hrefcomplet)
# print(links)
            # Effectuer une requête pour récupérer le contenu de la nouvelle page
            result = requests.get(hrefcomplet)

            # Vérifier si la requête a réussi (code d'état HTTP 200)
            if result.status_code == 200:
                src = result.content
                soup = BeautifulSoup(src, "html.parser")
                NomArticle = soup.find('h1', class_="text-gray-700 font-bold text-2xl font-arabic")

                # Vérifier si l'élément est trouvé avant de l'ajouter à la liste
                if NomArticle:
                    NomArticles.append(NomArticle.text)
            else:
                print(f"La requête pour {hrefcomplet} a échoué avec le code d'état {result.status_code}")
print(NomArticles)

# Utilisation de zip_longest pour gérer les listes de longueurs différentes
#for link, nom_article in zip_longest(links, NomArticles):
 #   print(f"Nom de l'article: {nom_article}, Lien: {link}")


