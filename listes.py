
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]

#obtenir le premier element de la liste 
print(plateformes_sociales[0]) #Facebook

#obtenir le dernier element de la liste 

print(plateformes_sociales[-1]) # Twiter

"""
Les indices fonctionnent aussi avec les chaînes de caractères !
En fait, les chaînes de caractères sont juste des listes de caractères.
Chaque caractère correspond à un indice qui va de zéro à la longueur de la chaîne.

Par exemple, dans la chaîne  langage  = "PYTHON"  ,  langage[2] 
vous renverra  "T" . Tout simplement parce que l’indice 2 dans le mot "PYTHON" est le "T".
Ou bien, avec l’indice de la position inverse, vous devez utiliser
langage[-4]  pour accéder à  "T"  .
"""
langage_de_programation = "PYTHON"

print(langage_de_programation[2])
print(langage_de_programation[-4])

#MODIFIER LES ELEMENTS D'UNE LISTE 

"""
Pour modifier une case d'une liste, il suffit d'utiliser l'indice de la case que l'on souhaite modifier, et d'y affecter la nouvelle valeur à l'aide de l'opérateur d'affectation (=), tout comme pour une variable."""
plateformes_sociales[2] = "Linkedin"

print(plateformes_sociales)

#Ajoutez, retirez et triez les listes 

#AJOUTER

plateformes_sociales.append("TikTok")
print(plateformes_sociales) # ["Facebook", "Instagram", "Snapchat", "Twitter", "TikTok"]

#AJOUTER
plateformes_sociales.remove("Facebook")
print(plateformes_sociales) #['Instagram', 'linkedin', 'Twitter', 'TikTok']

#connaitre la longueur d'un liste 
print(len(plateformes_sociales))

#trier la liste 
print(plateformes_sociales.sort())