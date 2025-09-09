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
print('Ispis trokuta fiksne visine bez for petlje')
print('*')
print('**')
print('* *')
print('*  *')
print('*   *')
print('*    *')
print('*******')
print()
print()









print('Ispis trokuta fiksne visine pomocu for petlje')
print('*')

for number in range(5):
    print('*' + ' ' * number + '*')

print('*******')
print()
print()












print('Ispis trokuta varijabilne visine pomocu for petlje')

height = int(input('Unesite visinu trokuta: '))
sign = input('Unesi znak: ')

print(sign)
for number in range(height - 2):
    #print('*' + ' ' * number + '*')
    print(f'{sign}{" " * number}{sign}')

#print('*' + '*' * (height - 2) + '*')
print(f'{sign}{sign * (height - 2)}{sign}')
print()
print()