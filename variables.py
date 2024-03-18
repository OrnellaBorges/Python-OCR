

# LES VARIABLES

# Variable de type 'string' (chaine de caractere)
mon_nom = 'Pierre'

# Variable de type 'integer' (nombre entier)
mon_nombre = 10

# Variable de type 'float' (nombre a virgule)
mon_nombre_a_virgule = 3.1415


prenom = "mika à "
age = 39

#CONCATENER DES VARIABLES

# Convertir l'entier en chaîne de caractères
# On ne peut pas concaténer un int avec une string c'est interdit en python 
age_str = str(age)

# Concaténer les chaînes de caractères
# attention les espace ne sont pas pris en compte 
concat = prenom + age_str + " ans"

print(prenom)
print(concat)

livre = "Gatsby le Magnifique"
print(livre)

#mutation
livre = "Beloved"
print(livre)

age = 30 
print(age)

age2 = 10
age2 = age 
print(age2)

nom = "Doe"
prenom = "John"

print(f"Bonjour je m'appelle {prenom} {nom} et j'ai {age} ans.")

