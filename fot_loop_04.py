'''
Napisite program koji ispisuje trokut tako da su linije stranica prikazane zvjezdicama *.

      *
     **
    * *
   *  *
  *   *
 *    *
*******
'''


# pitajmo korisnika koji znak želi koristiti
hight = int(input("Unesite visinu trokuta: " ))
symbol = str(input('Unesite znak koji želite koristiti za ispis trokuta: ')  )


print(f'{(hight - 1) * ' '}{symbol}')

for number in range(hight - 2):
    space_before = hight - 2 - number
    print(f"{space_before * ' '}{symbol}{' ' * number}{symbol}")


print(f'{symbol * hight}') 

