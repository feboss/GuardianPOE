import requests
url = "https://www.pathofexile.com/api/trade/search/Ultimatum"

headers = {    
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Content-Type": "application/json",
    }

data = '{ "query":{"status":{"option":"online"},"type":"Inscribed Ultimatum","stats":[{"type":"and","filters":[]}],"filters":{"ultimatum_filters":{"disabled":false,"filters":{"ultimatum_input":{"option":"Exalted Orb"}}}}},"sort":{"price":"asc"}}'
resp = requests.post(url,  headers=headers, data=data)
resp = resp.json()

stringa = ""

for x in range(10):
    stringa += resp["result"][x] + ","
stringa = stringa[:-1]


risposta = requests.get("https://www.pathofexile.com/api/trade/fetch/" +stringa + "?query=" +resp["id"], headers=headers)
print(risposta)

risposta = risposta.json()
for x in risposta["result"]:
    print (x["item"]["properties"][2]["values"][1][0])
    print (x["item"].get("note","NO NOTE"))
    print (x["listing"]["whisper"])
    print ("\n")