from random import randint
#kui panna import lõppu *, siis importib kõike
check = randint(0,9)
#check = randint(0,9) genereerib iga kord uue kontrollarvu

def loto():
#def-ga me defineerime fun-ni
    number = input("Sisesta üks täisarv 0-9: ")
    if number.isdigit():
#isdigit = on number
        print(check)
        number = int(number)
        if number < check:
            print("Sisestatud number on väiksem, kui kontrollarv")
            loto()
        elif number > check:
            print("Sisestatud number on suurem, kui kontrollarv")
            loto()
#elif on nagu else if
        else:
            print("Palju õnne! Minge auhinnale järgi.")
    else:
        print("Numbrit taheti sa igavene tainas")
        loto()

loto()
#viimane loto() kutsub def loto f-ni välja.