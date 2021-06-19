import requests,json
from .models import Quote

# Getting the quote base url
base_url=None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']
    
def getQuotes(): 
    # request.urlopen(base_url):
        
        quote = requests.get(base_url).json()
       
        Q = []
        id = quote.get('id')
        author = quote.get('author')
        quote =quote.get('quote')

        quoteObject = Quote(id,author,quote)
        Q.append(quoteObject)
        return Q