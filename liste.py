liste = []
nom=input("donner le nom")
while nom.upper()!="DONE":
    liste.append(nom)
    nom=input("donner un nom(DONE pour arreter):")
liste.sort()
print(liste)
