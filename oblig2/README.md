# Innlevering 2 – Effektive mengder og balanserte søketrær (Høst 2024)

Dette repoet inneholder løsningen min til **Innlevering 2** i høst 2024. Oppgaven består av to hoveddeler:

1. Implementasjon av en **mengde (Set)** basert på binære søketrær og AVL-trær
2. Algoritmer for å **bygge balanserte binære søketrær** fra sortert input

Alle programmene leser input fra **stdin** og skriver output til **stdout**, nøyaktig som spesifisert i oppgaveteksten.

---

## Del 1: Effektive mengder (Set)

### Problem

Vi skal implementere en abstrakt datatype `Set` som støtter følgende operasjoner:

- `contains(x)` – sjekk om `x` finnes i mengden
- `insert(x)` – legg til `x` (ingen duplikater)
- `remove(x)` – fjern `x` hvis det finnes
- `size()` – returner antall elementer i mengden

Mengden:

- har **ingen rekkefølge**
- inneholder **ingen duplikater**
- skal forbli uendret dersom man forsøker å fjerne et element som ikke finnes

Antall operasjoner kan være opptil **10⁶**, så effektivitet er viktig.

---

### Implementasjon 1: Binært søketre (BST)

Mengden er implementert som et **binært søketre**:

- `contains`, `insert` og `remove` har kjøretid **O(log n)** _så lenge treet er balansert_
- `size` er **O(1)** ved å holde styr på antall noder eksplisitt

Denne implementasjonen viser hvordan et vanlig BST kan brukes som mengde, samt hvilke begrensninger som oppstår dersom treet blir skjevt.

---

### Implementasjon 2: AVL-tre

I den andre versjonen er BST-et erstattet med et **AVL-tre**, som er selvbalanserende:

- Rotasjoner brukes etter innsetting og fjerning for å holde høydeforskjellen ≤ 1
- Garantert **O(log n)** kjøretid for `contains`, `insert` og `remove`
- `size` forblir **O(1)**

Denne implementasjonen sikrer stabil ytelse uavhengig av inputrekkefølge.

---

## Del 2: Bygge balanserte binære søketrær

I denne delen skal vi **konstruere et helt balansert binært søketre**, gitt at:

- input består av **sorterte heltall**
- ingen tall forekommer mer enn én gang
- treet bygges ved **vanlig BST-innsetting** (ingen selvbalansering)

Oppgaven løses ved å skrive ut tallene i en **spesiell rekkefølge**, slik at resultatet blir balansert.

---

### Del 2a: Balansert BST fra sortert array

Her brukes en klassisk rekursiv strategi:

- Velg **midt-elementet** som rot
- Gjør det samme rekursivt for venstre og høyre del
- Skriv ut elementene i den rekkefølgen de skal settes inn

Dette garanterer at treet blir helt balansert når elementene settes inn i et vanlig BST.

**Inkludert i repoet:**

- Pseudokode for algoritmen
- Full implementasjon i Java/Python
- Leser input fra stdin og skriver korrekt rekkefølge til stdout

---

### Del 2b: Balansert BST ved bruk av heap

I denne varianten er det kun tillatt å bruke **heap(er)** som datastruktur:

- Alle input-elementer legges først på en heap
- Algoritmen bruker kun:
  - `push / offer`
  - `pop / poll`
  - `size / len`
- Én eller flere heaper kan brukes

Løsningen simulerer samme “midt-valg”-strategi, men utelukkende ved hjelp av heap-operasjoner.

**Inkludert i repoet:**

- Pseudokode for heap-basert algoritme
- Full implementasjon i Java/Python

---

## Kjøring

Alle programmene kan kjøres fra terminal og leser input fra standard input:

python3 program.py < input.txt
eller tilsvarende for Java.

Output skrives direkte til standard output og kan sammenlignes med de publiserte testfilene.

⸻

## Fokusområder i oppgaven

• Effektiv datastrukturdesign
• Forskjellen mellom vanlige BST og selvbalanserende trær
• Tidskompleksitet og garanterte vs. antatte grenser
• Algoritmisk konstruksjon av balanserte trær
• Begrensninger i valg av datastrukturer (heap-oppgaven)

⸻

## Merknad

Alle deloppgaver er implementert fullstendig og i tråd med spesifikasjonen. Løsningene er laget med fokus på korrekthet, effektivitet og klar struktur.
