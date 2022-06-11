# je crée un texte à trous que l'utilisateur pourra remplir

# Je m'appelle ____, je vie à ____ et j'ai __ ans.
# J'ai connu mon artiste préféré ____ en ____ et son morceau que j'aime tout particulièrement est ____.
# Ma mère s'appelle ____ et mon père ______, j'ai __ frères et soeurs.


nom = input("Ton nom ?")
lieu = input("L'endroit ou tu habites (pays) ?")
age = input("Ton age en années ?")
maman = input("Le nom de ta mère ?")
papa = input("Le nom de ton père ?")
nbrFreresEtSoeurs = input("Ton nombre de frères et soeurs ?")
artiste = input("Ton artiste préféré ?")
anneeArtiste = input("En quelle année tu l'as connu ?")
morceau = input("Ton morceau préféré de cet artiste ?")

madLib = f" Je m'appelle {nom}, je vie à {lieu} et j'ai {age} ans. "
madLib2 = f"J'ai connu mon artiste préféré {artiste} en {anneeArtiste} et son morceau que j'aime tout particulièrement est {morceau}."
madLib3 = f"Ma mère s'appelle {maman} et mon père {papa}, j'ai {nbrFreresEtSoeurs} frères et soeurs. "

print(madLib)
print(madLib2)
print(madLib3)

