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

def filtro(arrayRisposte):
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

    arrayStringaID = []
    stringaID = ""
    i=0
    for x in resp["result"]:
        i+=1
        stringaID += x + ","
        if (i%10 == 0):
            arrayStringaID.append(stringaID)
            stringaID = ""

    # Cancelliamo l'ultimo carattere dall'insieme delle stringhe, che corrisponde alla virgola
    for i in range(len(arrayStringaID)):
        arrayStringaID[i] = arrayStringaID[i][:-1]

    arrayRisposte = []
    for x in arrayStringaID:
        risposta = requests.get("https://www.pathofexile.com/api/trade/fetch/" +x+ "?query=" +resp["id"], headers=headers).json()
        arrayRisposte.append(risposta)
    
    return arrayRisposte



#RICHIESTA CHAOS
#{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}}},"trade_filters":{"filters":{"price":{"option":"chaos"}}}}},"sort":{"price":"asc"}}
#RICHIESTA MAX 5.9EXA
#{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","max":5.9}}}}},"sort":{"price":"asc"}}
#RICHIESTA DA 6 EXA
#{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","min":6}}}}},"sort":{"price":"asc"}}


#Ricerca Chaos
ricerca = '{"query":{"status":{"option":"online"},"stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}}},"trade_filters":{"filters":{"price":{"option":"chaos"}}}}},"sort":{"price":"asc"}}'
risposta = search(ricerca)
filtro(risposta)
#ricerca max 5.9
ricerca = '{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","max":5.9}}}}},"sort":{"price":"asc"}}'
risposta = search(ricerca)
filtro(risposta)
#Ricerca DA 6 EXA
ricerca = '{"query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[],"disabled":false}],"filters":{"ultimatum_filters":{"filters":{"ultimatum_input":{"option":"Exalted Orb"}},"disabled":false},"trade_filters":{"filters":{"price":{"option":"exa","min":6}}}}},"sort":{"price":"asc"}}'
risposta = search(ricerca)
filtro(risposta)



             