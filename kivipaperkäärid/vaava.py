import random

print("Tere tulemast!")
print("Täna me mängime 'kivi-paber-käärid'!")
nimi1 = input("Sisestage 1. mängija nimi: ")
nimi2 = input("Sisestage 2. mängija nimi: ")

punktid1 = 0
punktid2 = 0

while True:
    märgid = ["kivi", "käärid", "paber"]
    random.shuffle(märgid)

    valik1 = input(f"{nimi1}, vali märk ({', '.join(märgid)}): ").lower()
    valik2 = input(f"{nimi2}, vali märk ({', '.join(märgid)}): ").lower()

    
    if valik1 == valik2:
        print("Viik! Uuesti.")
    elif (valik1, valik2) in {('paber', 'kivi'), ('kivi', 'käärid'), ('käärid', 'paber')}:
        print(f"{nimi1} võitis vooru!")
        punktid1 += 1
    else:
        print(f"{nimi2} võitis vooru!")
        punktid2 += 1

    print(f"\nPunktitabel: {nimi1} - {punktid1} punkti | {nimi2} - {punktid2} punkti\n")

    vava = input("Kas soovite veel ühe vooru mängida? (jah/ei): ").lower()
    if vava != 'jah':
        break

print("\nMäng lõppes.")
print(f"Punktitabel: {nimi1} - {punktid1} punkti | {nimi2} - {punktid2} punkti")
