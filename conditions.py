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
    