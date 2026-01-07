import csv
from collections import defaultdict, deque

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

def kort_sti_fra(graf, start_actor):
    #Start noden til slutten (som er None nå)
    #Bruker et bredde-først søk i def-en
    foreldre = {start_actor: None}
    queue = deque([start_actor])

    while queue:
        midl_actor = queue.popleft()
        for nabo_actor, film_id, rating in graf[midl_actor]:
            #Hvis noden ikke er i stien:
            if nabo_actor not in foreldre:
                #Setter noden i stien
                foreldre[nabo_actor] = (midl_actor, film_id, rating)
                #Legger noden i køen
                queue.append(nabo_actor)
    return foreldre

def kort_sti_mellom(graf, start_actor, end_actor):
    foreldre = kort_sti_fra(graf, start_actor)
    
    #Hvis stien ikke finnes:
    if end_actor not in foreldre:
        return None

    sti = []
    #Starter på slutten
    midl_actor = end_actor
    #Så lenge vi ikke er i mål-noden:
    while midl_actor != start_actor:
        #Info om den noden som var før
        prev_actor, film_id, rating = foreldre[midl_actor]
        #Legger til lenken mellom nodene, samt info om filmen de var med i + rating
        sti.append((prev_actor, midl_actor, film_id, rating))
        #Fortsetter til midl_actor = start_actor
        midl_actor = prev_actor
    
    #Snur stien for riktig rekkefølge
    sti.reverse()
    return sti

def kort_sti(graf, filmer, actor1, actor2):
    #Laget denne funksjonen fordi det virket oversiktlig
    return kort_sti_mellom(graf, actor1, actor2)

def skriv_sti(sti, film_titler, actors):
    print(f"{actors[sti[0][0]]}")
    #Trenger ikke actor1 bytt til '_'
    for actor1, actor2, film_id, rating in sti:
        print(f"===[ {film_titler[film_id]} ({rating}) ] ===> {actors[actor2]}")

def main():
    actor_fil = "actors.tsv"
    film_fil = "movies.tsv"
    filmer, titler_id = les_filmer(film_fil)
    actors, navn_id = les_actors(actor_fil)
    graf = bygg_graf(filmer, actors)
    
    #Skriver ut korteste stier for følgende skuespillere:
    par_kort_sti = [
        ("nm2255973", "nm0000460", "Donald Glover", "Jeremy Irons"),
        ("nm0424060", "nm8076281", "Scarlett Johansson", "Emma Mackey"),
        ("nm4689420", "nm0000365", "Carrie Coon", "Julie Delpy"),
        ("nm0000288", "nm2143282", "Christian Bale", "Lupita Nyong'o"),
        ("nm0637259", "nm0931324", "Tuva Novotny", "Michael K. Williams")
    ]
    
    print("Oppgave 2\n")
    #Finn og skriv ut korteste stier
    for actor1, actor2, navn1, navn2 in par_kort_sti:
        print(f"\nKorteste sti fra {navn1} til {navn2}:")
        sti = kort_sti(graf, filmer, actor1, actor2)
        if sti:
            skriv_sti(sti, titler_id, navn_id)
        else:
            print(f"Ingen sti funnet mellom {navn1} og {navn2}.")

# Kjør programmet
if __name__ == "__main__":
    main()














