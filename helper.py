def decoreer(tekst = ""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
        bedrag_pp1 = format(bedrag_pp, '.2f')
        bedrag_pp2 = bedrag_pp1.replace(".", ",")
    except:
        bedrag_pp2 = "??"
    uitvoer = f"Het bedrag per persoon is {bedrag_pp2} euro."
    return uitvoer

def onderstreep(tekst = ""):
    lengte = len(tekst)
    uit = []
    uit.append(tekst)
    uit.insert(1, (lengte * "="))
    return uit

def som(dictionary):
    totaal = 0
    for v in dictionary.values():
        totaal += v
    return totaal