import csv
from collections import defaultdict, deque

def les_filmer(film_fil):
    filmer = {}
    id_tittel = {}

    with open(film_fil, 'r') as fil:
        reader = csv.reader(fil, delimiter='\t')
        for deler in reader:
            tt_id = deler[0]
            tittel = deler[1]
            rating = float(deler[2])
            filmer[tt_id] = rating
            id_tittel[tt_id] = tittel

    return filmer, id_tittel

def les_actors(actor_fil):
    actors = defaultdict(list)
    id_navn = {}
    with open(actor_fil, 'r') as fil:
        reader = csv.reader(fil, delimiter = '\t')
        for deler in reader:
            nm_id = deler[0]
            navn = deler[1]
            filmer = deler[2:]
            actors[nm_id] = filmer
            id_navn[nm_id] = navn
    return actors, id_navn

def bygg_graf(filmer, actors):
    graf = defaultdict(set)
    film_array = defaultdict(list)

    for nm_id, array_filmer in actors.items():
        graf[nm_id]
        for tt_id in array_filmer:
            if tt_id in filmer:
                film_array[tt_id].append(nm_id)

    for tt_id, actor_film in film_array.items():
        rating = filmer[tt_id]
        for i in range(len(actor_film)):
            for j in range(i + 1, len(actor_film)):
                actor1 = actor_film[i]
                actor2 = actor_film[j]
                graf[actor1].add((actor2, tt_id, rating))
                graf[actor2].add((actor1, tt_id, rating))
    return graf

def kort_sti_fra(graf, start_actor):
    foreldre = {start_actor: None}
    queue = deque([start_actor])

    while queue:
        midl_actor = queue.popleft()
        for nabo_actor, film_id, rating in graf[midl_actor]:
            if nabo_actor not in foreldre:
                foreldre[nabo_actor] = (midl_actor, film_id, rating)
                queue.append(nabo_actor)
    return foreldre

def kort_sti_mellom(graf, start_actor, end_actor):
    foreldre = kort_sti_fra(graf, start_actor)
    
    if end_actor not in foreldre:
        return None

    sti = []
    midl_actor = end_actor
    while midl_actor != start_actor:
        prev_actor, film_id, rating = foreldre[midl_actor]
        sti.append((prev_actor, midl_actor, film_id, rating))
        midl_actor = prev_actor
    
    sti.reverse()
    return sti

def kort_sti(graf, filmer, actor1, actor2):
    return kort_sti_mellom(graf, actor1, actor2)

def skriv_sti(sti, film_titler, actors):
    print(f"{actors[sti[0][0]]}")
    for actor1, actor2, film_id, rating in sti:
        print(f"===[ {film_titler[film_id]} ({rating}) ] ===> {actors[actor2]}")

def main():
    actor_fil = "actors.tsv"
    film_fil = "movies.tsv"
    filmer, titler_id = les_filmer(film_fil)
    actors, navn_id = les_actors(actor_fil)
    graf = bygg_graf(filmer, actors)

    ant_noder = len(graf)
    ant_kanter = sum(len(kanter) for kanter in graf.values()) // 2
    print(f"Oppgave 1 \n\nNodes: {ant_noder} \nEdges: {ant_kanter}")

    par_kort_sti = [
        ("nm2255973", "nm0000460", "Donald Glover", "Jeremy Irons"),
        ("nm0424060", "nm8076281", "Scarlett Johansson", "Emma Mackey"),
        ("nm4689420", "nm0000365", "Carrie Coon", "Julie Delpy"),
        ("nm0000288", "nm2143282", "Christian Bale", "Lupita Nyong'o"),
        ("nm0637259", "nm0931324", "Tuva Novotny", "Michael K. Williams")
    ]
    print("Oppgave 2\n")
    for actor1, actor2, navn1, navn2 in par_kort_sti:
        print(f"\nKorteste sti fra {navn1} til {navn2}:")
        sti = kort_sti(graf, filmer, actor1, actor2)
        if sti:
            skriv_sti(sti, titler_id, navn_id)
        else:
            print(f"Ingen sti funnet mellom {navn1} og {navn2}.")

if __name__ == "__main__":
    main()