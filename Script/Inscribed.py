# Ricerca sul trade i vari inscribed ultimatum che hanno un valore di vendita più basso della ricompensa
#
import requests

url = "https://www.pathofexile.com/api/trade/search/Ultimatum"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
           "Content-Type": "application/json"}


def stampa(x):
    #
    print("{n} - {c} {v}".format(n=x["item"]["properties"][2]["values"][1][0], c=str(x["listing"]["price"].get("amount", "NO PRICE")), v=str(x["listing"]["price"].get("currency", "NO PRICE"))))
    print(x["listing"]["whisper"])


def filtra(arrayRisposte):
    # Filtra le risposte del server stampando solo ciò che ci interessa
    for y in arrayRisposte:
        for x in y["result"]:
            # INSCRIBED ULTIMATUM X1 EXALTED
            if(x["item"]["properties"][2]["values"][1][0] == "x1"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 0.9 and x["listing"]["price"].get("currency", "NO PRICE") == "exalted"):
                    stampa(x)
            if(x["item"]["properties"][2]["values"][1][0] == "x1"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 130 and x["listing"]["price"].get("currency", "NO PRICE") == "chaos"):
                    stampa(x)

            # INSCRIBED ULTIMATUM X2 EXALTED
            if(x["item"]["properties"][2]["values"][1][0] == "x2"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 2 and x["listing"]["price"].get("currency", "NO PRICE") == "exalted"):
                    stampa(x)
            if(x["item"]["properties"][2]["values"][1][0] == "x2"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 300 and x["listing"]["price"].get("currency", "NO PRICE") == "chaos"):
                    stampa(x)

            # INSCRIBED ULTIMATUM X4 EXALTED
            if(x["item"]["properties"][2]["values"][1][0] == "x4"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 3.6 and x["listing"]["price"].get("currency", "NO PRICE") == "exalted"):
                    stampa(x)
            if(x["item"]["properties"][2]["values"][1][0] == "x4"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 600 and x["listing"]["price"].get("currency", "NO PRICE") == "chaos"):
                    stampa(x)

            # INSCRIBED ULTIMATUM X8 EXALTED
            if(x["item"]["properties"][2]["values"][1][0] == "x8"):
                if((x["listing"]["price"].get("amount", "NO PRICE")) < 7.4 and x["listing"]["price"].get("currency", "NO PRICE") == "exalted"):
                    stampa(x)


def search(ricerca):
    # Per cercare inviamo una richiesta POST al sito con un oggetto json contenente la query
    # Per avere l'effettuale lista di oggetti sul trade bisogna fare una seconda richiesta
    # con tutti gli elementi(id) ritornati dal POST, separati da una virgola
    # ENG:
    # To search send a POST request to https://www.pathofexile.com/api/trade/search/YOUR_LEAGUE
    # with a json object containing your query.
    # To get the accual listings you have to perform a second request to https://www.pathofexile.com/api/trade/fetch/RESULT_LINES_HERE?query=ID_HERE
    # where RESULT_LINES_HERE is all the elements in the returned result array joined by comma (,) and the query parameter is the string returned as ID.
    # ----------------------------------------------------------------

    # Facciamo un post inviando la nostra ricerca
    resp = requests.post(url,  headers=headers, data=ricerca).json()

    # Carichiamo i vari id 10 alla volta perché sono l'elemento massimo che il GET prende
    lista_di_id = []
    dieci_id = ""
    i = 0
    for x in resp["result"]:
        i += 1
        dieci_id += x + ","
        if (i % 10 == 0):
            lista_di_id.append(dieci_id)
            dieci_id = ""
    # Cancelliamo l'ultimo carattere dall'insieme delle stringhe, che corrisponde alla virgola
    lista_di_id = [x[:-1] for x in lista_di_id]

    # Facciamo un get con 10 id
    risposte = []
    for x in lista_di_id:
        risposta = requests.get("https://www.pathofexile.com/api/trade/fetch/" + x + "?query=" + resp["id"], headers=headers).json()
        risposte.append(risposta)
    return risposte


# Ricerca Chaos
risposta = search('{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}}},"trade_filters":{"filters":{"price":{"option":"chaos"}}}}},"sort":{"price":"asc"}}')
filtra(risposta)
# Ricerca max 5.9 exa
risposta = search('{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","max":5.9}}}}},"sort":{"price":"asc"}}')
filtra(risposta)
# Ricerca DA 6 EXA in su
risposta = search('{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","min":6}}}}},"sort":{"price":"asc"}}')
filtra(risposta)
