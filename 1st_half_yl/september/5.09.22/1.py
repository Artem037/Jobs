pirate1 = input()
pirate2 = input()
if pirate1 == pirate2:
    print('ничья')
elif (pirate1 == 'камень' and pirate2 == 'ножницы' or pirate1 == 'бумага' and pirate2 == 'камень'
        or pirate1 == 'ножницы' and pirate2 == 'бумага'):
    print('первый')
else:
    print('второй')
