#operateur de comparaison qui permettent de verifier une condition 
#renvoit true ou false 

print("hello" == "helo") # retourne false
print("hello" == "Hello") # retourne false les majuscule comptent dans python 
print (4 > 5)# retourne false
print (5 > 4)# retourne true
print (5 != 4)# retourne true != différent de 


#structures de control : utilise les condition avec des variables 
#statements : if else elif

age = input("rentre ton age stp")

if int(age) == 20: 
    print ("tu as 20 ans")
else: 
    print("tu n'as pas 20 ans")
    
poids = input("donne ton poids")

if int(poids) < 40 : 
    print("tu es maigre")
elif int(poids) >= 120:
    print("surpoid") 
elif int(poids) == 100:
    print("attention tu est presque en surpoids")
else:
    print("tu as un poids normal")
    
    ensoleille = True
if ensoleille:
    print("on va à la plage !")
else:
    print("on reste à la maison !")



    ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")


    #verifier des conditions multiple avec des opérateurs 


    avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")

    #definir des conditions complexes

    nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    # autoriser plus d’invités
else:
    # ne pas autoriser plus d’invités

    fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.")