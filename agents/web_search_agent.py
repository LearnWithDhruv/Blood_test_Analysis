import requests
from bs4 import BeautifulSoup

class WebSearchAgent:
    def search(self, queries):
        articles = []
        for query in queries:
            response = requests.get(f"https://www.google.com/search?q={query}")
            soup = BeautifulSoup(response.text, 'html.parser')
            for item in soup.find_all('h3'):
                title = item.text
                link = item.find_parent('a')['href']
                articles.append({'title': title, 'link': link})
        return articles

# Example usage:
if __name__ == "__main__":
    search_agent = WebSearchAgent()
    queries = ['high cholesterol diet recommendations', 'glucose control tips']
    articles = search_agent.search(queries)
    print(articles)
