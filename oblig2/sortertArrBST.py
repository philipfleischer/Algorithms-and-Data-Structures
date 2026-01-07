import sys

def Binaert_Soeke_Tre(array_sort):
    def lag_Binaert_Tre(venstre, hoyre):
        if venstre > hoyre:
            #return None
            return
        
        midtpunkt = (venstre + hoyre) // 2
        print(array_sort[midtpunkt])
        lag_Binaert_Tre(venstre, midtpunkt - 1)
        lag_Binaert_Tre(midtpunkt + 1, hoyre)

    lag_Binaert_Tre(0, len(array_sort)-1)

def main():
    inp = sys.stdin.read().strip()
    array = list(map(int, inp.split()))
    Binaert_Soeke_Tre(array)

    
if __name__ == "__main__":
    main()




#$ seq 20 | python3 oppgave2.py | java BalanceChecker


#python3 setBST.py < inputs/input_100 | cmp - outputs/output_100