#1/ Nous allons avoir besoin de permuter deux valeurs d’un tableau à partir de leurs indices.
#Écrire un programme permettant de permuter deux valeurs du tableau myTable
myTable=[12,56,24,11,8,47]
stock1=myTable[1]
myTable[1]=myTable[5]
myTable[5]=stock1

print(myTable)