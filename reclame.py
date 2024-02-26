from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    kortingsprijs = (prijs - (prijs * korting))
    kortingsprijs1 = format(kortingsprijs, '.2f')
    kortingsprijs2 = kortingsprijs1.replace(".", ",")
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {kortingsprijs2} euro."

def inkomsten_totaal(inkomsten, btw):    
    totaal = sum(inkomsten)
    bedrag = totaal * btw
    bedrag1 = format(bedrag, '.2f')
    bedrag2 = bedrag1.replace(".", ",")
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag2} euro btw betaald dient te worden."

def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return [hoog, laag]

def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    aantal_waarden = len(mijn_lijst)
    bedrag = int(som / aantal_waarden)
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer