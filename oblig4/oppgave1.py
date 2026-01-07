#Film: tt‐id, Tittel, Rating, Antall Stemmer ------->>>> Dette er kanter
#Skuespiller: nm‐id, Navn, tt‐id1, tt‐id2, ... ------>>> Dette er noder
#TSV-filer er skilt med tab
import csv
from collections import defaultdict

def les_filmer(film_fil):
    filmer = {}
    id_titel = {}
    with open(film_fil, 'r') as fil:
        re = csv.reader(fil, delimiter='\t')
        for deler in re:
            tt_id = deler[0]
            tittel = deler[1]
            rating = float(deler[2])
            filmer[tt_id] = rating
            id_titel[tt_id] = tittel
    #returnerer ordbok filmer: nøkkel-(tt-id) og verdi-rating. 
    # Leverer også ordbok id_tittel: nøkkel-(tt-id) og verdi-tittel
    return filmer, id_titel

def les_actors(actors_fil):
    actors = defaultdict(list)
    id_navn = {}
    with open(actors_fil, 'r') as fil:
        re = csv.reader(fil, delimiter='\t')
        for deler in re:
            nm_id = deler[0]
            navn = deler[1]
            #Film id-er (tt-id)
            filmer = deler[2:]
            actors[nm_id] = filmer
            id_navn[nm_id] = navn
    #returnerer ordbok actors: nøkkel-(nm-id) og verdi-filmer. 
    # Leverer også ordbok id_navn: nøkkel-(nm-id) og verdi-navn.
    return actors, id_navn


def bygg_graf(filmer, actors):
    graf = defaultdict(set)
    #Liste med alle actors som har spilt i en film
    film_til_a = defaultdict(list)

    for nm_id, a_filmer in actors.items():
        #Dette sikrer at ISOLERTE noder blir tatt med!
        graf[nm_id]
        #Løkke for oversikt over hvilke id-er er koblet sammen
        for tt_id in a_filmer:
            if tt_id in filmer:
                film_til_a[tt_id].append(nm_id)

    #Linke sammen actors som har vært i filmen
        #a_i_film --> actor_in_film  
    for tt_id, a_i_film in film_til_a.items():
        rating = filmer[tt_id]
        for i in range(len(a_i_film)):
            for j in range(i + 1, len(a_i_film)):
                actor1 = a_i_film[i]
                actor2 = a_i_film[j]
                #Legg til en edge mellom actor1 og 2
                graf[actor1].add((actor2, tt_id, rating))
                graf[actor2].add((actor1, tt_id, rating))
    return graf


def main():
    actor_fil = "actors.tsv"
    film_fil = "movies.tsv"

    filmer, titler_id = les_filmer(film_fil)
    actors, navn_id = les_actors(actor_fil)
    graf = bygg_graf(filmer, actors)

    ant_noder = len(graf)
    #graf.values() er mengder av actors, deler på 2 for dupli
    ant_kanter = sum(len(kanter) for kanter in graf.values()) // 2
    print(f"Oppgave 1 \n\nNodes: {ant_noder} \nEdges: {ant_kanter}")

if __name__ == "__main__":
    main()














