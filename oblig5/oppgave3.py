import sys

def sort(array):
    lengde = len(array)

    if lengde <= 1:
        return array
    
    midtpunkt = lengde // 2
    array1 = sort(array[:midtpunkt])
    array2 = sort(array[midtpunkt:])

    return merge(array1, array2)

def merge(array1, array2):
    sortert = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            sortert.append(array1[i])
            i += 1
        else:
            sortert.append(array2[j])
            j += 1

    #Hvis det er flere elementer igjen
    while i < len(array1):
        sortert.append(array1[i])
        i += 1

    #Hvis det er flere elementer igjen
    while j < len(array2):
        sortert.append(array2[j])
        j += 1

    return sortert


def main():
    filnavn = sys.argv[1]
    fil_liste = []

    try:
        with open(filnavn, 'r') as fil:
            for line in fil:
                tall = int(line.strip())
                fil_liste.append(tall)
    except FileNotFoundError:
        print(f"Feil: Finner ikke filen {filnavn}")
        return

    
    sort_liste = sort(fil_liste)

    skriv_til_fil = filnavn.split(".")[0] + "_out.txt"

    #f = open(skriv_til_fil, "x")
    #f.close()

    with open(skriv_til_fil, 'w') as ny_fil:
        for tall in sort_liste:
            ny_fil.write(f"{tall}\n")

    
    print(f"Sortert fil er skrevet til {skriv_til_fil}")


if __name__ == "__main__":
    main()