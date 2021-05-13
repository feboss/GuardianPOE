import requests, json 

def stampaGemma(indicei):
   #print (data["lines"][indice])   
   print (data["lines"][indicei].get("name","NOT FOUND"))   
   print (data["lines"][indicei].get("corrupted","False"))   
   print (data["lines"][indicei].get("gemLevel","NOT FOUND"))
   print (data["lines"][indicei].get("gemQuality","NOT FOUND"))
   print (data["lines"][indicei].get("chaosValue","NOT FOUND"))
   print (data["lines"][indicei].get("exaltedValue","NOT FOUND"))

def stampaventiventi():
   # STAMPA gemme 20 20 non corrotte e non alternative
   print ("\nGemme 20 - 20, non corrotte, non alternative e non awakened\n")
   for x in data["lines"]:
      if not x["name"].startswith("Divergent") and not x["name"].startswith("Anomalous") and not x["name"].startswith("Awakened") and not x["name"].startswith("Phantasmal"):
         if x.get("corrupted","False") == "False":
            if x.get("gemLevel","0") == 20 and x.get("gemQuality","0") == 20:
               print("{n} : {c} Chaos - {e} exa".format(n=x["name"], c=x["chaosValue"], e=x["exaltedValue"]))

def stampaAwakened():
   # STAMPA gemme 1 0 Awakened non corrotte
   print ("\nGemme Awakened 1 - 0, non corrotte\n")
   for x in data["lines"]:
      if x["name"].startswith("Awakened"):
         if x.get("corrupted","False") == "False":
            if x.get("gemLevel","0") == 1 and x.get("gemQuality",0) == 0:
               print("{n} : {c} Chaos - {e} exa".format(n=x["name"], c=x["chaosValue"], e=x["exaltedValue"]))

def stampaAwakenedFull():
   # STAMPA gemme 5 20 Awakened non corrotte
   print ("\nGemme Awakened 5 - 20, non corrotte\n")
   for x in data["lines"]:
      if x["name"].startswith("Awakened"):
         if x.get("corrupted","False") == "False":
            if x.get("gemLevel","0") == 5 and x.get("gemQuality",0) == 20:
               print("{n} : {c} Chaos - {e} exa".format(n=x["name"], c=x["chaosValue"], e=x["exaltedValue"]))

def main():
   stampaventiventi()
   stampaAwakened()
   stampaAwakenedFull()


response = requests.get("https://poe.ninja/api/data/ItemOverview?league=Ultimatum&type=SkillGem&language=en")
data = response.json()
main()


