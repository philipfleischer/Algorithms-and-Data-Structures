# Innlevering 4 – Grafalgoritmer på IMDB-data (Høst 2024)

Dette repoet inneholder løsningen min til **Innlevering 4 (Høst 2024)**. Oppgaven går ut på å bygge
og analysere en stor graf basert på IMDB-data, og å anvende klassiske grafalgoritmer på et realistisk
datasett med rundt **100 000 noder og 5 millioner kanter**.

Alle deloppgaver er implementert i henhold til spesifikasjonen.

---

## Datasett

Grafen er bygget fra to TSV-filer:

### `movies.tsv`

Inneholder metadata om filmer:

- `tt-id` (unik film-ID)
- tittel
- rating (0.0–10.0)
- antall stemmer (ignorert i oppgaven)

### `actors.tsv`

Inneholder skuespillere og filmer de har spilt i:

- `nm-id` (unik skuespiller-ID)
- navn
- én eller flere `tt-id`-er

Filmer som forekommer i `actors.tsv` men ikke finnes i `movies.tsv` ignoreres, slik spesifikasjonen krever.

---

## Grafrepresentasjon

Grafen er representert som en **urettet, vektet multigraf**, der:

- **Noder** representerer skuespillere
- **Kanter** representerer filmer to skuespillere har spilt sammen i
- Hver kant er merket med:
  - filmtittel
  - rating (brukt som grunnlag for vekt)

Dette gir en graf som effektivt støtter:

- bredde-først-søk (BFS)
- Dijkstra (vektet korteste vei)
- komponentanalyse

---

## Del 1: Bygging av grafen

Programmet:

1. Leser begge TSV-filene
2. Mapper film-ID-er til metadata (tittel, rating)
3. Leser skuespillere og bygger kanter mellom alle skuespillere som har spilt i samme film
4. Ignorerer filmer uten metadata

For å verifisere korrekthet telles antall noder og kanter i grafen.

Eksempelutskrift:
Nodes: 126196
Edges: 5342530

---

## Del 2: Six Degrees of IMDB (korteste sti)

Det er implementert en prosedyre som, gitt to skuespillere, finner en **korteste sti** mellom dem
(målt i antall filmer/skuespillere).

- Algoritme: **Breadth-First Search (BFS)**
- Grafen er urettet
- Det finnes ofte flere korteste stier – hvilken som returneres er ikke viktig

Utskriften inkluderer:

- skuespillernavn
- filmen som forbinder hvert steg i stien

Eksempel:
Donald Glover
===[ LA Originals (7.2) ] ===> Terry Crews
===[ Inland Empire (6.8) ] ===> Jeremy Irons

---

## Del 3: Chilleste vei (vektet korteste sti)

Her er grafen vektet for å finne den **mest underholdende forbindelsen** mellom to skuespillere.

### Vektfunksjon

For en film med rating `r` brukes vekten:
weight = 10 - r

Dette favoriserer stier som går gjennom filmer med høy rating.

### Algoritme

- **Dijkstra**
- Totalvekten for stien summeres og skrives ut

Eksempel:
Donald Glover
===[ The Martian (8.0) ] ===> Enzo Cilenti
===[ The Man Who Knew Infinity (7.2) ] ===> Jeremy Irons
Total weight: 4.8

---

## Del 4: Komponentanalyse

Grafen analyseres for å finne **sammenhengende komponenter**.

- En komponent er en maksimal mengde noder der alle er nåbare fra hverandre
- Alle komponenter identifiseres
- Resultatet grupperes etter størrelse

Eksempelutskrift:
There are 1 components of size 120030
There are 3 components of size 9
There are 4617 components of size 1

Dette gir innsikt i hvor stor den dominerende komponenten er, og hvor fragmentert resten av grafen er.

---

## Videre utforskning

Oppgaven åpner for videre analyser, blant annet:

- Sammenligning av korteste sti vs. chilleste sti
- Alternative vektfunksjoner (f.eks. basert på stemmetall)
- Robusthet i grafen ved fjerning av filmer
- Hvordan komponentstrukturen endrer seg ved filtrering

Repoet er strukturert slik at slike eksperimenter enkelt kan legges til.

---

## Kjøring

Programmet forventer at `movies.tsv` og `actors.tsv` ligger tilgjengelig lokalt.

Eksempel:
python3 imdb_graph.py movies.tsv actors.tsv

Utskrift for de ulike deloppgavene genereres til stdout.

⸻

## Faglig fokus

    •	Effektiv grafbygging på store datasett
    •	BFS og Dijkstra på realistiske grafer
    •	Vektede og uvektede korteste veier
    •	Komponentanalyse
    •	Praktisk ytelse og skalerbarhet

⸻

## Merknad

Alle deloppgaver er fullstendig implementert i henhold til spesifikasjonen. Koden er skrevet med fokus
på korrekthet, lesbarhet og effektivitet ved store datasett.
