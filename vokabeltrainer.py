import random
import sqlite3

vokabeln=[]

def init_db():
    conn = sqlite3.connect('vokabeln.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vokabeln (
        id INTEGER PRIMARY KEY,
        vokabel TEXT NOT NULL,
        uebersetzung TEXT NOT NULL,
        correct_attempts INTEGER DEFAULT 0,
        attempts INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def main_menu():
    while True:
        print("\n---Der Vokabeltrainer---")
        print("1. Vokabel hinzufügen\n2. Vokabeln abfragen\n3. Statistik anzeigen\n4. Beenden")
        eingabe=input()
        if eingabe=="1":
            add_vokabel()
        elif eingabe=="2":
            train()
        elif eingabe=="3":
            statistik()
        elif eingabe=="4":
            end()
        else:
            print("Ungültige Eingabe")
            

        
def add_vokabel():
    vokabel = input("Neue Vokabel: ").lower()
    übersetzung = input("Übersetzung: ").lower()

    conn=sqlite3.connect('vokabeln.db')
    cursor=conn.cursor()
    cursor.execute("INSERT INTO vokabeln (vokabel, uebersetzung) VALUES (?, ?)",
(vokabel, übersetzung))
    conn.commit()
    conn.close()
    
    print("Vokabel erfolgreich hinzugefügt!")
    return

def train():
    conn = sqlite3.connect('vokabeln.db')
    cursor = conn.cursor()
    try:
        while True:
            cursor.execute("SELECT * FROM vokabeln")
            vokabeln = cursor.fetchall()

            if not vokabeln:
                print("Du musst erst Vokabeln hinzufügen.")
                return
    
            wort=random.choice(vokabeln)
            print(f"\nWas ist die Übersetzung von {wort[1]}?    ('stop' zum beenden) ")
            translation=eingabe=input().lower()

            if translation==wort[2]:
                print("Korekkt!")
                cursor.execute("UPDATE vokabeln SET correct_attempts = correct_attempts + 1, attempts = attempts + 1 Where id = ?", (wort[0],))
            elif translation=="stop":
                print("")
                conn.commit()
                return
            else:
                print(f"Falsch, die richtige Antwort ist '{wort[2]}'")
                cursor.execute("UPDATE vokabeln SET attempts = attempts + 1 Where id = ?", (wort[0],))
    finally:
        conn.close()
    

def statistik():
    conn = sqlite3.connect('vokabeln.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(attempts), SUM(correct_attempts) FROM vokabeln")
    result = cursor.fetchone()
    conn.close()

    if result[0] is None:
        print("Keine Vokabeln vorhanden.")
        return

    total_attempts, correct_attempts = result
    print("Statistik:")
    print(f"Du wurdest insgesamt {total_attempts}mal abgefragt und hast davon {correct_attempts}mal richtig geantwortet.")

def end():
    print("\nAuf Widersehen\n")
    exit()

if __name__ == "__main__":
    init_db()
    main_menu()