import csv
from collections import defaultdict
import heapq

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
    return actors, id_navn


def bygg_graf(filmer, actors):
    graf = defaultdict(list)
    #Liste med alle actors som har spilt i en film
    film_til_a = defaultdict(list)

    for nm_id, actor_filmer in actors.items():
        graf[nm_id]
        for tt_id in actor_filmer:
            if tt_id in filmer:
                film_til_a[tt_id].append(nm_id)

    # For hver film, koble sammen alle a som har spilt i den filmen
    for tt_id, a_i_film in film_til_a.items():
        rating = filmer[tt_id]
        vekt = 10 - rating
        for i in range(len(a_i_film)):
            for j in range(i + 1, len(a_i_film)):
                actor1 = a_i_film[i]
                actor2 = a_i_film[j]
                #Legg til en edge mellom actor1 og 2, med vekt (10 - rating)
                graf[actor1].append((actor2, tt_id, vekt, rating))
                graf[actor2].append((actor1, tt_id, vekt, rating))
    return graf


def dijkstra_chilleste_vei(graf, start_actor, end_actor):
    #Prioritetskø
    #(økt-vekt, actor, sti)
    queue = [(0, start_actor, [])]
    #Noder visited, set() sånna at det ikke besøkes flere ganger
    visited = set()
    #Best path:
    #foreldre = {}

    #Fortsetter så lenge det er mer igjen i køen
    while queue:
        #Henter elem med lavest vekt?
        oekt_vekt, midl_actor, sti = heapq.heappop(queue)

        #Hvis noden allerede er visited, fortsett videre
        if midl_actor in visited:
            continue

        visited.add(midl_actor)

        #Hvis ferdig, returner stien og vekten
        if midl_actor == end_actor:
            return sti, oekt_vekt

        # Utvid stien med skuespillerens naboer
        for nabo_actor, film_id, vekt, rating in graf[midl_actor]:
            #Sjekker om nabo-noder er besøkt allerede
            if nabo_actor not in visited:
                #Øk vekt --> tidligere vekt og ny vekt av linken
                #Oppdaterer stien
                #Til slutt legges det i prioritetskøen (queue)
                heapq.heappush(queue, (oekt_vekt+vekt, nabo_actor, sti+[(midl_actor, nabo_actor, film_id, rating)]))
    #Hvis det ikke er en sti, return none og vekt
    return None, float('inf')


def skriv_sti(sti, film_titler, actors, total_vekt):
    if not sti:
        print("Ingen sti funnet.")
        return

    print(f"{actors[sti[0][0]]}")
    for actor1, actor2, film_id, rating in sti:
        print(f"===[ {film_titler[film_id]} ({rating}) ] ===> {actors[actor2]}")
    print(f"Total weight: {round(total_vekt, 2)}")


def main():
    skuespiller_fil = "actors.tsv"
    film_fil = "movies.tsv"
    filmer, titler_id = les_filmer(film_fil)
    skuespillere, navn_id = les_actors(skuespiller_fil)
    graf = bygg_graf(filmer, skuespillere)

    par = [
        ("nm2255973", "nm0000460", "Donald Glover", "Jeremy Irons"),
        ("nm0424060", "nm8076281", "Scarlett Johansson", "Emma Mackey"),
        ("nm4689420", "nm0000365", "Carrie Coon", "Julie Delpy"),
        ("nm0000288", "nm2143282", "Christian Bale", "Lupita Nyong'o"),
        ("nm0637259", "nm0931324", "Tuva Novotny", "Michael K. Williams")
    ]
    
    print("Oppgave 3\n")
    #Finn og skriv ut chilleste stier for par
    for actor1, actor2, navn1, navn2 in par:
        print(f"\nChilleste vei fra {navn1} til {navn2}:")
        sti, total_vekt = dijkstra_chilleste_vei(graf, actor1, actor2)
        skriv_sti(sti, titler_id, navn_id, total_vekt)

if __name__ == "__main__":
    main()