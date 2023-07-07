import wikipedia

def get_wiki_article(article):
    try:
        return f'{wikipedia.summary(article)}{wikipedia.page(article).links}'
    except wikipedia.WikipediaException:
        print("Нет такой страницы")