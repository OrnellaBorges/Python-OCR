#Enregistrer des données complexes

nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

print(nouvelle_campagne)

# créer un dictionnaire vide 
taux_de_conversion = {}

#ajouter des élément comme ceci: 
taux_de_conversion["facebook"]= 3.14

print(taux_de_conversion)

#ajouter avec la fonction dict()
#declarer la variable qui va recevoir les données avec comme valeur la fonction dict() 
taux_conversion = dict()
taux_conversion["twitter"]= 3.12

#acceder a la valeur dans le dictionnaire 
print(taux_de_conversion["facebook"])
#>>> 3.14

#MANIPULER LES DICTIONNAIRES

infos_pokemon = {
  "nom": "Salamèche"
  "poids": "3.6 kg"
  "type": "feu"
}
print(infos_pokemon)

#ajouter une nouvelle paire de clé/valeur 
infos_pokemon["niveau"]= "17"
print(infos_pokemon)

infos_pokemon["evolution"] = "dracofeu"


#supprimer une paire de clé/valeur avec del 

del(infos_pokemon["evolution"])
print(infos_pokemon)

