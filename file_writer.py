def print_articles_by_author(articles, target_author):
    target_author = target_author.strip().lower()
    filtered = []

    for article in articles:
        author = article.get("author")

        if not author:
            continue

        if target_author not in author.lower():
            continue

        print(article["publishedAt"], "-", article["title"])
        print("Author:", author)
        print("Source:", article["source"]["name"])
        print(article["url"])
        print(article["description"])
        print()

        filtered.append(article)

        return filtered