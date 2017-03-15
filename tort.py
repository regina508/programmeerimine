from math import *

pikkus = input("Sisesta pikkus tükkides: ")
laius = input("Sisesta laius tükkides: ")
k6rgus = input("Sisesta kõrgus tükkides: ")
tk_pakk = input("Mitu tükki on ühes pakis: ")

def pakke():
    tk_arv = int(pikkus)*int(laius)*int(k6rgus)
    pakk_arv = tk_arv/int(tk_pakk)
#print ("Sul on vaja " +str(round(pakk_arv+0.49))+" pakki")
#seda kasutame siis, kui ei importi midagi math-st
    print ("Sul on vaja " +str(ceil(pakk_arv))+" pakki")
#ceil ümmardab täisarvuni suuremale poole (math import puhul)
#floor ümmardab väiksemale poole ehk
#print ("Sul on vaja " +str(floor(pakk_arv))+" pakki")

#round ümmardamine, round(pakk_arv+0.49) ümmardab täisarvuni
#0.5 ei tohi kasut., kuna selle puhul kohe ümmardab suuremale poole
    
pakke()