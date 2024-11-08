temps = int(input("Donner le nombre de minutes écouler depuis le début du mois :"))
temps = int(temps)
jour = temps / 1440
jour = int(jour)
temps = temps - jour * 1440
heure = temps / 60
heure = int(heure)
temps = temps - heure * 60
minute = temps
print("nous sommes le", jour, " novembre, il est", heure ," h :", minute, " min")