# Innlevering 5 – Algoritmer og datastrukturer (IN2010, Høst 2024)

Dette repoet inneholder løsningen min til **Innlevering 5 (obligatorisk)** i IN2010 – Algoritmer
og datastrukturer, høsten 2024.

Innleveringen består av fire selvstendige oppgaver som dekker:

- kjøretidsanalyse
- balanserte søketrær
- sorteringsalgoritmer
- grafalgoritmer på store datasett

Alle oppgaver er fullstendig løst i henhold til spesifikasjonen, og programmene kan kjøres med
én kommando per oppgave.

---

## Innhold

- **Oppgave 1:** Kjøretidsanalyse – binærsøk på lenkede lister
- **Oppgave 2:** Bygging av balanserte binære søketrær
- **Oppgave 3:** Implementasjon av sorteringsalgoritme
- **Oppgave 4:** Six Degrees of IMDB (grafalgoritmer)

---

## Oppgave 1 – Binærsøk med lenkede lister

I denne oppgaven analyseres kjøretidskompleksiteten til en algoritme som forsøker å utføre
binærsøk på en **ordnet lenket liste**.

### Løsning

- Jeg analyserer først kjøretidskompleksiteten til binærsøk isolert
- Deretter analyseres kostnaden ved `get(i)` på en lenket liste
- Resultatet viser at algoritmen i verste fall får **O(n log n)** kjøretid

Oppgaven besvares skriftlig med forklaring og begrunnelse av analysen.

**Fil:**
`oppgave1.md`

---

## Oppgave 2 – Bygge balanserte binære søketrær

Målet er å skrive ut tall i en rekkefølge som gir et **helt balansert binært søketre** ved vanlig
innsetting (uten selvbalansering).

### Del (a): Sortert array → balansert BST

- Algoritmen velger medianen som rot
- Problemet løses rekursivt for venstre og høyre del
- Pseudokode og implementasjon følger samme idé

**Filer:**

- `oppgave2.md`
- `oppgave2a.py`

### Del (b): Kun ved bruk av prioritetskø

- Samme problem løses, men kun med prioritetskøer
- Medianen hentes ved å flytte elementer mellom heap-er
- Implementert med `heapq` (Python)

**Fil:**

- `oppgave2b.py`

---

## Oppgave 3 – Sortering

I denne oppgaven er en sorteringsalgoritme implementert fra bunnen av.

### Valgt algoritme

- **Merge sort**

### Funksjonalitet

- Leser input fra fil (filnavn gitt som kommandolinjeargument)
- Sorterer tallene
- Skriver resultatet til ny fil med `_out`-suffix

### Egenskaper

- Korrekthet for alle gyldige input
- Tidskompleksitet: **O(n log n)** i verste fall

**Fil:**
`oppgave3.py`

---

## Oppgave 4 – Six Degrees of IMDB

I denne oppgaven bygges og analyseres en **stor graf basert på IMDB-data**.

### Grafkonstruksjon

- Noder: skuespillere
- Kanter: filmer de har spilt sammen i
- Grafen er:
  - urettet
  - vektet
  - tillater parallelle kanter

Grafen bygges fra:

- `movies.tsv`
- `actors.tsv`

Skuespillere som refererer til filmer uten metadata ignoreres.

---

### Del 1: Verifikasjon av grafen

Programmet teller antall:

- noder
- kanter

Dette brukes for å kontrollere at grafen er korrekt bygget.

---

### Del 2: Korteste sti (Six Degrees)

- Implementert med **BFS**
- Finner korteste sti mellom to skuespillere
- Skriver ut både noder (skuespillere) og kanter (filmer)

---

### Del 3: Chilleste vei

- Implementert med **Dijkstra**
- Kantvekter beregnes som: `10 - rating`
- Finner mest “underholdende” sti mellom to skuespillere
- Total vektsum skrives ut

---

### Del 4: Komponentanalyse

- Alle sammenhengende komponenter i grafen identifiseres
- Resultatet grupperes etter komponentstørrelse
- Gir innsikt i grafens struktur og fragmentering

**Fil:**
`oppgave4.py`

---

## Kjøring

Hver oppgave kan kjøres separat.

Eksempel:
python3 oppgave3.py inputfil
python3 oppgave4.py movies.tsv actors.tsv

Detaljerte kommandoer er dokumentert i de respektive oppgavefilene.

⸻

## Faglig fokus

Innleveringen dekker sentrale temaer i kurset:
• kjøretidsanalyse
• datastrukturer (BST, heap, graf)
• rekursive algoritmer
• sortering
• BFS og Dijkstra
• praktisk ytelse på store datasett

⸻

## Merknad

Alle oppgaver er løst fullstendig og i henhold til kravene i oppgaveteksten. Koden er skrevet med
fokus på korrekthet, tydelig struktur og faglig presisjon.
