
import requests
from bs4 import BeautifulSoup
import json

URL = "https://quotes.toscrape.com/"

try:
    response = requests.get(
        URL,
        timeout=10,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    for item in soup.select(".quote"):
        quote = item.select_one(".text")
        author = item.select_one(".author")

        if quote and author:
            results.append({
                "quote": quote.get_text(strip=True),
                "author": author.get_text(strip=True)
            })

    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    with open("quotes.txt", "w", encoding="utf-8") as file:
        for item in results:
            file.write(
                item["quote"] + "\n"
                + "Author: " + item["author"] + "\n\n"
            )

    print("Quotes collected:", len(results))
    print("Saved to quotes.json and quotes.txt")

except requests.RequestException as error:
    print("Request failed:", error)

except OSError as error:
    print("File error:", error)
  
