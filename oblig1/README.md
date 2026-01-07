# Innlevering 1 (Høst 2024) — Teque + Analyseoppgaver

Dette repoet inneholder løsningen min til innlevering 1 i høst 2024. Oppgaven består av to deler:

1. **Teque (triple-ended queue)**: implementere en kø som støtter effektiv innsetting i front, midten og bak, samt oppslag med 0-basert indeks.
2. **Analyseoppgaver**: kjøretidsanalyse (Big-O) av operasjonene og analyse av binærsøk over lenkede lister.

Oppgaven er basert på Kattis-problemet **Teque**: https://open.kattis.com/problems/teque

---

## Del 1: Teque

### Problem

Vi skal implementere en datastruktur som støtter følgende operasjoner:

- push_front(x) – sett inn elementet x først
- push_back(x) – sett inn elementet x sist
- push_middle(x) – sett inn elementet x i midten
  Hvis køens størrelse før innsetting er k, settes x inn på posisjon ⌊(k + 1) / 2⌋.
- get(i) – returner/skriv ut elementet på indeks i (0-basert)

Input kan inneholde opptil N = 10^6 operasjoner. Det antas gyldig input, og get vil aldri spørre utenfor gjeldende størrelse.

---

## Løsningsidé

Teque implementeres ved å splitte køen i **to sekvenser** (typisk kalt left og right) slik at:

- left inneholder den første delen av elementene
- right inneholder resten
- Invarianten holdes slik at størrelsene er balanserte:
  - len(left) == len(right) eller len(left) == len(right) + 1

På denne måten kan vi:

- sette inn i front ved å legge i left
- sette inn i back ved å legge i right
- sette inn i middle ved å legge inn på grensen mellom left og right
- hente indeks i ved å slå opp i riktig halvdel (enten left[i] eller right[i - len(left)])

Etter hver push\_\*-operasjon rebalanseres strukturene ved å flytte maks ett element mellom left og right slik at invarianten alltid gjelder.

---

## Operasjoner (kort beskrivelse)

- **push_front(x)**: legg x fremst i left, rebalanser
- **push_back(x)**: legg x bakerst i right, rebalanser
- **push_middle(x)**: legg x på slutten av left (midten), rebalanser
- **get(i)**:
  - hvis i < len(left) → elementet ligger i left
  - ellers → elementet ligger i right med indeks i - len(left)

---

## Kjøretidskompleksitet (verste tilfelle)

Gitt en passende datastruktur for left/right (f.eks. deque/array-deque eller tilsvarende):

- push_front: **O(1)**
- push_back: **O(1)**
- push_middle: **O(1)**
- get(i): **O(1)**

Rebalansering flytter kun et konstant antall elementer per operasjon, og påvirker derfor ikke asymptotisk kompleksitet.

> Merk: Hvis implementasjonen bruker underliggende arrays som av og til må resize, får man amortisert O(1), men verste-fall per enkelt operasjon kan være høyere ved resize. I analyseoppgaven brukes Big-O i verste tilfelle med N ubundet (standard modell), og man diskuterer også betydningen av at N = 10^6 er en konstant i del (d).

---

## Hvorfor vi fjerner begrensningen på N i analyse

I del (c) analyseres operasjoner uten å anta en øvre grense på N. Dette er viktig fordi Big-O beskriver vekst når input kan bli arbitrært stor.
Hvis vi derimot beholder N ≤ 10^6, blir 10^6 en **konstant**, og man kan i teorien si at alt er O(1) over den begrensede inputmengden — noe som skjuler de reelle forskjellene mellom algoritmer/datastrukturer.

---

## Del 2: Binærsøk med lenkede lister (analyse)

Repoet inneholder også analysen av gitt pseudokode for binærsøk over en **lenket liste**.

Kjernen i analysen er at operasjonen A.get(i) på en lenket liste typisk er **O(i)** (må traversere fra start).
Siden binærsøk gjør flere get-kall, blir total kompleksitet betydelig dårligere enn på en array.

Konklusjonen i oppgaven handler om at datastrukturvalg (array vs lenket liste) påvirker kjøretidskompleksitet kraftig selv om “algoritmen” ser lik ut på papiret.

---

## Kjøring (generelt)

Programmet leser fra **stdin** og skriver til **stdout** i samme format som Kattis krever.

Typisk bruk:

- Kjør programmet og gi input via fil eller piping:
  - python3 main.py < input.txt
  - eller tilsvarende for Java

---

## Notater

- Implementasjonen er laget for å håndtere store inputmengder effektivt.
- Output skrives kun for get-operasjoner.
- Indekser er 0-baserte slik spesifikasjonen krever.
