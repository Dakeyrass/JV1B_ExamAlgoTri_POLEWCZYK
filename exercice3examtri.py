#3/ Écrire un programme implémentant le tri à bulles complet, permettant de trier totalement
#un tableau grâce à l’algorithme du tri à bulles. On pourra se servir de la permutation, ainsi
#que de la réponse à la question précédente.

myTable=[12,56,24,11,8,47]
plusgrandnombre=myTable[5]
emplacement=0
for y in range (len(myTable)):
    plusgrandnombre=myTable[y]
    emplacement=y
    for n in range (y,len(myTable)):
        if(myTable[n]>plusgrandnombre):
            plusgrandnombre=myTable[n]
            emplacement=n

            stock1=myTable[emplacement]
            myTable[emplacement]=myTable[y]
            myTable[y]=stock1

print(myTable)  

#Je sais qu'il aurait fallu que les valeurs "remontent", mais là je me retrouve juste avec un tableau organisé dans l'ordre décroissant..c'est un peu embêtant mais c'est tout ce que j'ai réussi à faire (fonctionnant correctement.) 

#Je ne sais pas si il fallait laisser les tests donc les voilà quand même. 
'''myTable=[12,56,24,11,8,47]
for i in range (len(myTable)):
    if(myTable[i]>myTable[5]):
        stock1=myTable[5]
        myTable[5]=myTable[i]
        myTable[i]=stock1
    if(myTable[i]>myTable[4]):
            stock2=myTable[i]
            myTable[i]=myTable[4]
            myTable[4]=stock2
    if(myTable[i]>myTable[3]):
            stock2=myTable[i]
            myTable[i]=myTable[3]
            myTable[3]=stock2
    if(myTable[i]>myTable[2]):
            stock2=myTable[i]
            myTable[i]=myTable[2]
            myTable[2]=stock2
    if(myTable[i]>myTable[1]):
            stock2=myTable[i]
            myTable[i]=myTable[1]
            myTable[1]=stock2
    if(myTable[i]>myTable[0]):
            stock2=myTable[i]
            myTable[i]=myTable[0]
            myTable[0]=stock2

print(myTable)'''
#stratégie abandonnée car beaucoup trop longue..et je me suis perdue dans toutes les comparaisons à faire. (une fois que i a été comparé avec chaque case, le fait de devoir 
#recomparer les cases (le tableau est en partie dans l'ordre mais le 8 reste à la fin..))
        

'''myTable=[12,56,24,11,8,47]

plusgrandevaleur = myTable[5]
emplacement = 0
for i in range(len(myTable)):
    if(myTable[i]>plusgrandevaleur):
        plusgrandevaleur = myTable[i]
        emplacement = i


stock1=myTable[emplacement]
myTable[emplacement]=myTable[5]
myTable[5]=stock1

plusgrandevaleur = myTable[4]
emplacement = 1
for i in range(,len(myTable)):
    if(myTable[i]>plusgrandevaleur):
        plusgrandevaleur = myTable[i]
        emplacement = i


stock1=myTable[emplacement]
myTable[emplacement]=myTable[4]
myTable[4]=stock1

print(myTable)'''
