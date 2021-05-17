import requests

url = "https://www.pathofexile.com/api/trade/search/Ultimatum"
headers = {    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Content-Type": "application/json",
    }

def stampa(x):
    print (x["item"]["properties"][2]["values"][1][0])
    print (str(x["listing"]["price"].get("amount","NO PRICE")) + " " +str(x["listing"]["price"].get("currency","NO PRICE"))  )
    print (x["listing"]["whisper"])   

def filtra(arrayRisposte):
    for y in arrayRisposte:
        for x in y["result"]:
            # X1
            if( x["item"]["properties"][2]["values"][1][0] == "x1"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 0.9 and x["listing"]["price"].get("currency","NO PRICE") == "exalted"): 
                    stampa(x)
            if( x["item"]["properties"][2]["values"][1][0] == "x1"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 130 and x["listing"]["price"].get("currency","NO PRICE") == "chaos"):
                    stampa(x)

            # X2
            if( x["item"]["properties"][2]["values"][1][0] == "x2"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 2 and x["listing"]["price"].get("currency","NO PRICE") == "exalted"):
                    stampa(x)
            if( x["item"]["properties"][2]["values"][1][0] == "x2"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 300 and x["listing"]["price"].get("currency","NO PRICE") == "chaos"):
                    stampa(x)

            # X4
            if( x["item"]["properties"][2]["values"][1][0] == "x4"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 3.6 and x["listing"]["price"].get("currency","NO PRICE") == "exalted"): 
                    stampa(x)
            if( x["item"]["properties"][2]["values"][1][0] == "x4"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 600 and x["listing"]["price"].get("currency","NO PRICE") == "chaos"):
                    stampa(x)

            # X8
            if( x["item"]["properties"][2]["values"][1][0] == "x8"):
                if( (x["listing"]["price"].get("amount","NO PRICE")) < 7.4 and x["listing"]["price"].get("currency","NO PRICE") == "exalted"):
                    stampa(x)   

def search(ricerca):
    resp = requests.post(url,  headers=headers, data=ricerca).json()

    lista_di_id = []
    dieci_id = ""
    i=0
    for x in resp["result"]:
        i+=1
        dieci_id += x + ","
        if (i%10 == 0):
            lista_di_id.append(dieci_id)
            dieci_id = ""
    
    # Cancelliamo l'ultimo carattere dall'insieme delle stringhe, che corrisponde alla virgola
    lista_di_id = [x[:-1] for x in lista_di_id]

    risposte = []
    for x in lista_di_id:
        risposta = requests.get("https://www.pathofexile.com/api/trade/fetch/" +x+ "?query=" +resp["id"], headers=headers).json()
        risposte.append(risposta)
    
    return risposte



#RICHIESTA CHAOS
#{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}}},"trade_filters":{"filters":{"price":{"option":"chaos"}}}}},"sort":{"price":"asc"}}
#RICHIESTA MAX 5.9EXA
#{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","max":5.9}}}}},"sort":{"price":"asc"}}
#RICHIESTA DA 6 EXA
#{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","min":6}}}}},"sort":{"price":"asc"}}

#Ricerca Chaos
risposta = search('{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}}},"trade_filters":{"filters":{"price":{"option":"chaos"}}}}},"sort":{"price":"asc"}}')
filtra(risposta)
#ricerca max 5.9
risposta = search('{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","max":5.9}}}}},"sort":{"price":"asc"}}')
filtra(risposta)
#Ricerca DA 6 EXA
risposta = search('{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","min":6}}}}},"sort":{"price":"asc"}}')
filtra(risposta)



             