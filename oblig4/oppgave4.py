import csv
from collections import defaultdict, deque
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

def k_stoerrelse(graf, start_node, besøkt):
    #k står for komponent
    #Bruker bredde-først søk
    queue = deque([start_node])
    besøkt.add(start_node)
    stoerrelse = 0
    komponent_noder = []

    #Hvis noden ikke finnes, returner stoerrelse av komponenten som 1
    if not graf[start_node]:
        return 1
    
    while queue:
        #Ta node ut av køen
        node = queue.popleft()
        #Øker stoerrelsen for hver node i komponenten
        stoerrelse += 1
        #Legger noden i komponent listen
        komponent_noder.append(node)
        #Kun interessert i actor nm-id
        for nabo, _, _, _ in graf[node]:
            if nabo not in besøkt:
                besøkt.add(nabo)
                queue.append(nabo)
    return stoerrelse


def k_finn(graf):
    #finn komponent(er)
    besøkt = set()
    komponent_stoerrelser = defaultdict(int)
    
    for node in graf:
        if node not in besøkt:
            #Stoerrelse --> bredde-først søk med egen funksjon
            stoerrelse = k_stoerrelse(graf, node, besøkt)
            #Øker representasjonen av antall komponenter grafen har
            komponent_stoerrelser[stoerrelse] += 1
    return komponent_stoerrelser


def k_skriv_ut(komponent_stoerrelser):
    for stoerrelse, antall in sorted(komponent_stoerrelser.items(), reverse=True):
        print(f"There are {antall} components of size {stoerrelse}")

def main():
    actor_fil = "actors.tsv"
    film_fil = "movies.tsv"
    
    filmer, titler_id = les_filmer(film_fil)
    actors, navn_id = les_actors(actor_fil)
    graf = bygg_graf(filmer, actors)

    komponent_stoerrelser = k_finn(graf)
    print("Oppgave 4\n")
    k_skriv_ut(komponent_stoerrelser)

if __name__ == "__main__":
    main()