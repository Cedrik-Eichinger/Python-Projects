import random as r 

tot = "false"
energie = 10
gold = 0
item_liste=[]
maulwurf = "normal"
junge = "normal"

def intro():
    print("Wilkommen im verwunschenen Wald.\nDeine Aufgabe ist es möglichst viel Gold zu erbeuten, aber Obacht ist geboten!")
    print("In diesem Wald lauern eine Menge Gefahren, die dir Gold abziehen oder dich sogar umbringen können.")
    choice1()

def choice1():
    print("Vor dir liegen drei Möglichkeiten.\nMöchtest du 1. auf einen hohen Felsen links von dir klettern? 2. geradeaus in den Wald laufen 3. dem Fluss am Waldrand folgen?")
    eingabe = input("1, 2 oder 3")
    if eingabe == "1":
        felsen()
    elif eingabe == "2":
        wald()
    elif eingabe =="3":
        fluss()
    else:
        print("Keine gültige Eingabe!\n")
        choice1()

def felsen():
    global tot, energie
    z = r.randint(1, 10)
    if z == 1:
        print("\nDu bist beim Versuch hochzuklettern heruntergefallen und gestorben.\nGAME OVER!")
        tot = "true"
        end()
    elif z > 1:
        print("\nDu bist auf den Felsen geklettert und findest eine alte abgenutzte Schaufel.")
        item_liste.append("schaufel")
        energie -= 1
        print("Ansonsten findest du nichts und entscheidest dich wieder herunterzuklettern.")
        print("Nun hast du nurnoch die Optionen: \n2. geradeaus in den Wald zu laufen oder 3. dem Fluss am Waldrand zu folgen.")
        eingabe = input("2 oder 3?")
        if eingabe == "2":
            wald()
        elif eingabe == "3":
            fluss()

def fluss():
    global maulwurf, gold, energie
    print("\nDu folgst dem Fluss am Waldrand und stößt auf einen großen Maulwurfshügel.\nMöchtest du 1. versuchen zu buddeln oder 2. ihn ignorieren und weitergehen?")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        maulwurf = "sauer"
        if "schaufel" in item_liste:
            z=r.randint(1, 10)
            if z > 1:
                print("Du benutzt deine Schaufel zum buddeln im Maulwurfshügel und findest 10 Goldklumpen.\nAllerdings zerbricht die Schaufel und du verlierst Energie.\nMöchtest du weiterbuddeln? 1.Ja 2.Nein")
                gold += 10
                energie -= 1
                item_liste.remove("schaufel")
                eingabe2 = input("1 oder 2?")
                if eingabe2 == "1":
                   weiterbuddeln()
                elif eingabe2 == "2":
                    fluss2()
            else:
                print("Du benutzt deine Schaufel zum buddeln im Maulwurfshügel, du findest nichts, die Schaufel zerbricht und du verlierst Energie.\nMöchtest du weiterbuddeln? 1.Ja 2.Nein")
                eingabe5 = input("1 oder2?")
                if eingabe5 == "1":
                    weiterbuddeln()
                else:
                    fluss2()
        else:
            z2=r.randint(1, 10)
            if z2 > 9:
                print("Du buddelst mit deinen Händen im Maulwurfshügel, verbrauchst Energie, aber findest 10 Goldklumpen im Hügel.\nMöchtest du weiterbuddeln? 1.ja 2.Nein")
                gold += 10
                energie -= 1
                eingabe3 = input("1 oder 2?")
                if eingabe3 == "1":
                    weiterbuddeln()
                else:
                    fluss2()
            else:
                print("Du buddelst mit deinen Händen im Maulwurfshügel, verbrauchst Energie und findest nichts.\nMöchtest du weiterbuddeln? 1.ja 2.Nein")
                energie -= 1
                eingabe4 = input("1 oder 2?")
                if eingabe4 == "1":
                    weiterbuddeln()
                else:
                    fluss2()


    elif eingabe == "2":
        fluss2()
    
def weiterbuddeln():
    global energie
    print("\nDu buddelst weiter mit deinen Händen im Maulwurfshügel, aber findest leider nichts, sondern hast nur Energie verschwendet")
    energie -= 1
    fluss2()

def fluss2():
    print("\nDu läufst weiter am Fluss entlang und siehst auf der anderen Seite etwas golden glitzern.\nMöchtest du 1. versuchen über Steine zu springen um den Fluss zu überqueren oder 2. weitergehen?")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        überqueren()
    else:
        see()
    
def überqueren():
    global energie, gold
    print("\nDu überquerst den Fluss indem du von Stein zu Stein springst und erreichst die andere Seite.\nDas hat eine Menge Energie gekostet, aber das goldene glitzern war tatsächlich 1Goldklumpen")
    gold += 1
    energie -= 2
    see()

def see():
    print("\nDu kommst an einen großen wilden See, mit einer Insel in der Mitte.\nAußerdem erblickst du in der Ferne einen Händler.\nMöchtest du 1. zum Händler gehen oder 2. versuchen zur Insel zu schwimmen.")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        print("\nDu schländerst langsam zum Händler am See.\nEr sagt zu dir:'Wilkommen, hier kommen nicht oft Leute vorbei, du darfst allerdings nur ein Item kaufen!' und bietet dir folgende Auswahl an:")
        händler()
    else:
        schwimmen()

def händler():
    global gold
    print("1. einen rostigen Metalldetektor für 5Goldklumpen\n2. ein paar Schwimmflügel für 3Goldklumpen\n3. einen Schutzhelm für 1Goldklumpen\n4. Nichts kaufen ")
    print(f"Du hast aktuell {gold} Goldklumpen.")
    if gold < 1:
        print("Du hast leider kein Gold um etwas zu kaufen.")
        after_händler()
    elif gold > 0:
        eingabe = input("1, 2, 3 oder 4?")
        if eingabe == "1":
            if gold > 4:
                print("Du kaufst den rostigen Metalldetektor, aber wo gehst du nun weiter?")
                gold -= 5
                item_liste.append("Metalldetektor")
                after_händler()
            else:
                print("Du hast nicht genug Gold dafür!")
                händler()
        elif eingabe == "2":
            if gold > 2:
                print("Du kaufst das paar schwimmflügel, aber wo gehst du nun weiter?")
                gold -= 3
                item_liste.append("Schwimmflügel")
                after_händler()
            else:
                print("Du hast nicht genug Gold dafür!")
                händler()
        elif eingabe == "3":
            print("Du kaufst den Schutzhelm, aber wo gehst du nun weiter?")
            gold -= 1
            item_liste.append("Helm")
            after_händler()
        else:
            print("Du entschließt dich nichts zu kaufen, aber wo gehst du nun weiter?")
            after_händler()

def after_händler():
    print("\nMöchtest du nun 1. dem Weg des Händlers weiter folgen oder 2. versuchen zur Insel zu schwimmen?")
    eingabe2 = input("1 oder 2?")
    if eingabe2 == "1":
        händlerweg()
    else:
        schwimmen()


def schwimmen():
    global energie, tot
    if "Schwimmflügel" in item_liste:
        print("\nDu ziehst deine Schwimmflügel an und versuchst zur Insel zu schwimmen.\nDie Strömungen sind extrem stark, aber du schaffst es durch deine Schwimmflügel zur Insel!")
        energie -= 1
        insel()
    else:
        z=r.randint(1, 2)
        if z == 1:
            print("\nDu versuchst durch den See zur Insel zu schwimmen.\nDie Strömungen sind extrem stark und du kommst geradeso mit einem imensem Energieverlust bei der Insel an.")
            energie -= 5
            insel()
        else:
            print("\nDu versuchst durch den See zur Insel zu schwimmen.\nDie Strömungen sind extrem stark, du versuchst dagegen anzukämpfen, aber wirst mitgerissen und ertrinkst.\nGAME OVER!")
            tot = "true"
            end()

def insel():
    global gold, energie, junge
    print("Auf der Insel angekommen schaust du dich um und erblickst einen kleinen gruselig aussehenden Jungen, der unter einem Apfelbaum steht und auf die Äpfel starrt.")
    print("Außerdem siehst du ein kleines Floß, welches am Strand der kleinen Insel liegt, mit dem du auf die andere Seite fahren könntest\nWas tust du? 1. Auf den Jungen zugehen 2. mit dem Floß rüberfahren")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        print("\nDu gehst auf den Jungen zu und er spricht dich an:'Hey du, bitte hol mir einen Apfel', während er immernoch die Äpfel anstarrt\nWie reagierst du? 1. abweisend 2. hilfsbereit")
        eingabe2 = input("1 oder 2?")
        if eingabe2 == "1":
            print("\nDu weisst den Jungen ab und fährst stattdessen mit dem Floß auf die andere Seite des Sees\nBeim rüberfahren bemerkst du, dass deine gesammten Goldreserven fehlen.\nhat sie etwas jemand geklaut?")
            gold = 0
            after_insel()
        else:
            print("\nDu möchtest dem Jungen helfen und kletterst für ihn auf den Baum, um Äpfel zu holen.")
            z=r.randint(1, 10)
            if z < 6:
                print("Du hast erfolgriech einen Apfel vom Baum geholt!")
                item_liste.append("Apfel")
            else:
                print("Du hast erfolgreich zwei Äpfel vom baum geholt!")
                item_liste.append("Apfel")*2
            print("Möchtest du 1. dem Jungen einen Apfel geben oder 2. ihm keinen Apfel geben?")
            eingabe3 = input("1 oder2?")
            if eingabe3 == "1":
                print("\nDu gibst dem Jungen einen Apfel, aber er wirkt seltsam auf dich.\nAufeinmal tut sich vor dir ein Gang auf, du hörst nurnoch die Worte:'oben, links, unten' und der Junge verschwindet!")
                print("Was haben seine Worte zu bedeuten?\nDu untersuchst den sich vor dir aufgetahen Gang und findest dort 10 Goldklumpen.")
                gold += 10
                print("Da sonst sich nichts mehr auf dieser Insel befindet, fährst du mit dem Floß auf die andere Seite des Sees.")
                after_insel()
            else:
                print("\nDu gibst dem Jungen keinen Apfel und bemrkst, dass der Junge anfängt laut zu lachen.\n'DU BIST VERFLUCHT!' hörst du nurnoch bevor der Junge verschwindet.")
                junge = "sauer"
                print("Vor lauter Angst nimmst du dir das Floß und paddelst so schnell wie möglich weg von der Insel, was ordentlich Energie kostet.")
                energie -= 2
    else:
        print("\nDu ignorierst den Jungen, nimmst das Floß und fährst auf die andere Seite des Sees.")
        after_insel()

def after_insel():
    global energie, gold, tot
    print("\nDu befindest dich nun wieder im Wald.\nVor dir liegt eine große Schlucht.")
    if energie < 6:
        print("Leider hast du nicht mehr genug Energie um über die Schlucht zu springen, also musst du außenrum gehen.")
        außenrum()
    else:
        print("Du hast nun die Wahl 1. über die Schlucht springen oder 2. außenrum laufen.")
        eingabe = input("1 oder 2?")
        if eingabe == "1":
            print("\nDu springst über die Schlucht und verbrauchst dabei so gut wie all deine Energiereserven.")
            energie -= 5
            schlucht()
        else:
            print("\nDu entscheidest dich um die Schlucht außenrum zu laufen.")
            außenrum()

def außenrum():
    global gold, junge, energie
    print("Du gehst einen weiten Weg ohne viele Ereignisse.")
    if "Metalldetektor" in item_liste:
        print("Du entscheidest dich deinen Metalldetektor herauszuholen und deine Gegend zu untersuchen.\nDu findest leider nichts.")
    print("Doch dann taucht vor dir ein kleiner grüner Kobold auf!\nMöchtest du 1. den Kobold angreifen oder 2. dem Kobold vertrauen?")
    eingabe = input("1 oder 2?")
    if junge == "sauer":
        print("\nDu wirst auffeinmal wie von einem Fluch zu Boden gedrückt und kannst dich nicht mehr wehren.\nDer Kobold klaut all dein Gold!")
        gold = 0
        after_kobold()
    else:
        if eingabe == "1":
            print("\nDu greifst den Kobold an und verschäuchst ihn!")
            after_kobold()
        else:
            print("\nDu vertraust dem Kobold, aber er nutzt dein Vertrauen aus, greift in deine Tasche und klaut dir 5Goldklumpen.\nNaja was willste machen.")
            gold -= 5
            after_kobold()


def after_kobold():
    print("Du gehst weiter und findest tatsächlich den Ausgang des Waldes!\nDu hast es lebend herrausgeschafft, Glückwunsch!")
    end()

def schlucht():
    global tot, gold, maulwurf, energie
    print("Auf der anderen Seite der Schlucht begenest du dem rießigen, mächtigen Kobold König, des verwunschenen Waldes.\nWillst du 1. dich drumherum schleichen oder 2. den König bekämpfen?")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        if maulwurf == "sauer":
            print("\nDu schleichst dich langsam um den Kobold König herum, doch auffeinaml taucht vor dir ein Maulwurf auf und schreit:'RACHE!!!'")
            print("Der König hört es sofort und springt mit einem hohem Bogen auf dich drauf.\nDer Kobold König hat dich zerquetscht.\nGAME OVER!")
            tot = "true"
            end()
        else:
            print("\nDu schleichst dich um den Kobld König herum und findest raus aus dem Wald.\nDu hast es lebend aus dem verwunschenen Wald geschafft, Glückwunsch!")
            end()
    else:
        print("\nDu gehst auf den Kobold König zu und fängst an ihn du bekämpfen.")
        if maulwurf == "sauer":
            print("Doch auffeinmal taucht unter dir ein Maulwurf auf, bringt dich zum umfallen und schreit:'RACHE!!!'\nDer König nutzt das sofort aus, springt mit einem hohem Bogen auf dich und zerquetscht dich!")
            print("GAME OVER!")
            tot = "true"
            end()
        else:
            if energie > 1:
                print("\nDu schaffst es in einem schweren anstrengendem Kampf mit deinen letzten Energiereserven den Kobold König zu bezwingen und bekommst von ihm 10Goldklumpen.")
                gold += 10
                print("Du bist zufrieden, gehst weiter und kommst raus aus dem Wald.\nDu hast den verwunschenen Wald überlebt, Glückwunsch!")
                end()
            else:
                print("Deine Energiereserven sind verbraucht und du fällst zu Boden.\nDer Kobold König hat dich besiegt.\nGAME OVER!")
                tot = "true"
                end()


def händlerweg():
    global tot, energie, gold
    print("\nDu gehst den Weg des Händlers weiter und stößt auf einen Höhleneingang.\nMöchtest du 1. In die Höhle hineingegehen oder 2. außenrum durch den Wald gehen?")
    eingabe = input("1 oder2?")
    if eingabe == "1":
        print("\nDu gehst in die Höhle hinein und bemerkst, dass die Höhle sehr brüchig von innen wirkt.\nEs fallen Felsbrocken von der Decke!")
        if "Helm" in item_liste:
            print("Die Felsbrocken fallen auf deinen Kopf, doch zum Glück hast du den Schutzhelm gekauft!\nEs war knapp aber du überstehst die gefährliche Situation.")
            energie -= 1
            print("Du gehst weiter durch die Höhle und findest ein art Eingabefeld, indem du 3 Zahlen eingeben kannst.\nWelche Zahlenkombi wählst du?")
            eingabe2 = input("Gebe 3 Zahlen ein.")
            if eingabe2 == "842":
                print("\nDas war die richtige Kombination!\nVor dir öffnet sich eine Schatzkammer mit 20Goldklumpen!")
                gold += 20
                print("Du steckst das Gold in deine Tasche und gehst weiter durch die Höhle, bis du einen Ausgang findest.")
                after_insel()
            else:
                print("Das war leider nicht die richtige Zahlenkombination.\nDu gehst weiter und findest den Ausgang der Höhle")
                after_insel()
        else:
            print("Die Felsbrocken fallen auf deinen Kopf und du kannst dich nicht mehr retten.\nGAME OVER!")
            tot = "true"
            end()
    else:
        neben_höhle()

def neben_höhle():
    global energie, gold
    print("Du gehst neben der Höhle durch den Wald und erblickst ein glitzern auf dem Baum.\nWillst du 1. hochklettern oder 2. es ignorieren?")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        print("\nDu kletterst auf den Baum, was ganz schön anstrengend ist, aber findst dort oben tatsächlich 5 Goldklumpen.\nDu kletterst wieder runter und gehst weiter.")
        gold += 5
        energie -= 2
        after_insel()
    else:
        print("\nDu ignorierst den Baum und gehst weiter.")
        after_insel()


def wald():
    global energie, gold
    print("\nDu gehst in den Wald hinein und triffst auf einen einzelnen alten Wolf. Wie reagierst du?\n1. ihn angreifen 2. ruihg verhalten und ihm vertrauen")
    eingabe = input("1 oder 2?")
    if eingabe == "1":
        print("\nDu versuchst den Wolf anzugreifen und er flüchtet tief in den Wald\nDu gehst deinen Weg weiter durch den Wald.")
        energie -= 1
        see()
    else:
        print("\nDu gehst ruihg auf den Wolf zu und er zeigt vertrauen.\nDer Wolf führt dich zu seinem Versteck indem du 5 Goldklumpen findest\nDu bist erfreut und gehst weiter deinen Weg durch den Wald.")
        gold += 5
        see()


def end():
    if tot == "false":
        print(f"Das Spiel ist vorbei.\nDu hast {gold} Klumpen Gold gesammelt.\nDas Maximum an sammelbaren Goldklumpen ist 34.")
    else:
        print("Du bist beim gieriegen Versuch Gold im verwunschenen zu sammeln gestorben. Bad")

intro()