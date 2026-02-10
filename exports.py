import csv


def export_articles_csv(
    articles,
    filename="articles.csv",
    include_description=True
):
    """
    Export NewsAPI articles to a CSV file.

    :param articles: list of article dicts
    :param filename: output CSV filename
    :param include_description: toggle long text field
    """

    fieldnames = [
        "publishedAt",
        "title",
        "author",
        "source",
        "url",
    ]

    if include_description:
        fieldnames.insert(4, "description")

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for a in articles:
            row = {
                "publishedAt": a.get("publishedAt", ""),
                "title": a.get("title", ""),
                "author": a.get("author", ""),
                "source": (a.get("source") or {}).get("name", ""),
                "url": a.get("url", ""),
            }

            if include_description:
                row["description"] = a.get("description", "")

            writer.writerow(row)

    print(f"Exported {len(articles)} articles → {filename}")
