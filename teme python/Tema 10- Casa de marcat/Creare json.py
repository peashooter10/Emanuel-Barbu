import json

dictionar={}

#date de intrare in json...
date={
  "bancnote": [
    { "valoare": 50, "stoc": 30 },
    { "valoare": 20, "stoc": 40 },
    { "valoare": 10, "stoc": 60 },
    { "valoare": 5, "stoc": 75 },
    { "valoare": 1, "stoc": 100 }
  ],
  "produse": [
    #fructe și legume
    { "nume": "Mere", "pret": 5},
    { "nume": "Banane", "pret": 10},
    { "nume" : "Portocale", "pret": 10},
    { "nume" : "Cartofi", "pret": 3},
    { "nume" : "Morcovi", "pret":5},
    { "nume": "Rosii", "pret":10},
    #produse de panificație
    { "nume": "Paine alba", "pret": 3 },
    {"nume": "Paine neagra", "pret": 4},
    {"nume": "Paine integrala", "pret": 5},
    {"nume": "Bagheta", "pret": 4},
    #lactate, brânzeturi, ouă
    { "nume": "Lapte", "pret": 11 },
    {"nume": "Oua","pret":10},
    {"nume":"Cascacal","pret":12},
    #dulciuri
    { "nume": "Ciocolata", "pret": 5 },
    {"nume": "Inghetata", "pret":15},
    {"nume": "Bomboane", "pret":14},
    #bauturi
    { "nume": "Apa", "pret": 3 },
    {"nume": "Suc", "pret": 9},
    { "nume": "Cafea boabe", "pret": 55 },
    #snack-uri
    { "nume": "Chipsuri", "pret": 8 },
    {"nume": "Tortilla", "pret": 5},
    {"nume": "Covrigei", "pret":10},
    {"nume": "Samanta", "pret":7},
  ],
}

def initializare_dictionar():
  global dictionar
  with open('date.json', 'w') as f:
      json.dump(date, f)
  with open('date.json') as f:
      dictionar = json.load(f)

  bancnote=dictionar["bancnote"]
  produse=dictionar["produse"]
  for i in range(len(produse)):
    print(produse[i])

initializare_dictionar()