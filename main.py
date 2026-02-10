from pydoc import source_synopsis

from dotenv import load_dotenv
import os
import requests
import json
import csv
from file_writer import print_articles_by_author
from requests import Response
from exports import export_articles_csv
load_dotenv()

def get_news(q):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": q,
    }

    headers = {
        "X-Api-Key" : API_KEY
    }

    response  = requests.get(url=url, params=params, headers=headers)
    return response


API_KEY = os.getenv("API_KEY")

response = get_news("president")
data = response.json()

articles = data["articles"]

authors = {
    article.get("author")
    for article in articles
    if article.get("author")
}

for author in sorted(authors):
    print(author)


author_name = "Tom Warren"
filtered_articles = print_articles_by_author(articles, author_name)
with open("articles_by_author.json", "w", encoding="utf-8") as f:
    json.dump(filtered_articles, f, indent=4)
export_articles_csv(
    filtered_articles,
    filename="tom_warren_articles.csv",
    include_description=False
)
print(f"Saved {len(filtered_articles)} articles")










