# Innlevering 3 – Trær og sortering (Høst 2024)

Dette repoet inneholder løsningen min til **Innlevering 3 (Høst 2024)**. Oppgaven består av tre hoveddeler:

1. Finne sti i et tre (Kattunge / Kitten – Kattis)
2. Implementasjon av flere sorteringsalgoritmer
3. Eksperimenter og analyse av sammenligninger, bytter og kjøretid

Alle programmene er implementert i henhold til spesifikasjonen og leser input fra **stdin** eller fil der dette er påkrevd.

---

## Del 1: Kattunge! – sti i et tre

### Problem

En kattunge sitter fast i en node i et tre. Gitt en beskrivelse av treet og noden kattungen befinner seg i, skal programmet skrive ut **stien fra denne noden til roten**.

Input:

- Første linje: noden hvor kattungen sitter
- Deretter linjer på formen:
  `a b1 b2 ... bn`
  hvor `a` er forelder til `b1, b2, ..., bn`
- Siste linje er alltid `-1`

Det er garantert at input beskriver et gyldig tre, og at hver node har nøyaktig én forelder (unntatt roten).

---

### Løsning

- Input parses til en **forelder-tabell / mapping** som lagrer forelder for hver node
- Fra startnoden (kattungen) følges forelder-pekere iterativt helt til roten
- Stien skrives ut i korrekt rekkefølge

Denne løsningen er effektiv og enkel:

- Tidskompleksitet: **O(n)** for parsing, **O(h)** for å finne stien
- Plasskompleksitet: **O(n)**

Oppgaven er kompatibel med Kattis-formatet (`kitten`).

---

## Del 2: Sorteringsalgoritmer

### Implementerte algoritmer

Følgende sorteringsalgoritmer er implementert:

- **Insertion sort**
- **Merge sort**
- To valgfrie algoritmer fra forelesning
  (minst én med kjøretid **O(n log n)**)

Alle algoritmene:

- Sorterer identisk input
- Produserer samme sorterte output
- Bruker egne sammenlignings- og bytteoperasjoner for å telle operasjoner

---

### Korrekthet

For små inputfiler genereres én outputfil per algoritme, navngitt som: \_.out
For eksempel:

- example_insertion.out
- example_merge.out

Alle outputfiler inneholder sorterte tall i samme format som input, og brukes for å verifisere korrekthet mellom algoritmene.

---

## Del 3: Sammenligninger, bytter og tid

### Målinger

For hver sorteringsalgoritme telles:

- Antall **sammenligninger**
- Antall **bytter**
- Total **kjøretid i mikrosekunder**

Tiden måles eksplisitt rundt selve sorteringen.

---

### Eksperimentoppsett

Gitt en inputfil med `n` elementer, utføres **n + 1 sorteringer per algoritme**:

- Sortering av tom liste
- Sortering av 1 element
- Sortering av 2 elementer
- …
- Sortering av `n` elementer

Resultatene samles i én CSV-fil per inputfil: \_results.csv
Format: n, alg1_cmp, alg1_swaps, alg1_time, alg2_cmp, alg2_swaps, alg2_time, …

CSV-filene kan åpnes i regnearkverktøy (Excel, Numbers, etc.) for videre analyse og plotting.

---

## Eksperimenter og refleksjon

Ved hjelp av de genererte CSV-filene er det mulig å analysere:

- Samsvar mellom observert kjøretid og teoretisk kompleksitet (Big-O)
- Forholdet mellom sammenligninger, bytter og faktisk kjøretid
- Hvilke algoritmer som fungerer best for:
  - svært små input
  - svært store input
  - ulike typer inputdata
- Eventuelle overraskende eller ikke-intuitive funn

Eksperimentene er reproduserbare ved å bruke samme inputfiler og algoritmekombinasjoner.

---

## Kjøring

### Del 1 (Kattunge)

python3 kitten.py < input.txt

Sortering
python3 sort.py input.txt

Dette genererer både sorterte outputfiler og en samlet CSV-fil med målinger.

⸻

## Fokus i oppgaven

    •	Trær og graf-liknende datastrukturer
    •	Klassiske sorteringsalgoritmer
    •	Eksperimentell analyse av algoritmer
    •	Forskjellen mellom teoretisk og praktisk ytelse
    •	Strukturert måling og dokumentasjon av algoritmisk oppførsel

⸻

## Merknad

Alle deloppgaver er implementert fullstendig og i tråd med spesifikasjonen. Koden er strukturert for lesbarhet, korrekthet og enkel videre eksperimentering.
