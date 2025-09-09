# Umjesto pisanja vise istih ili slicnih linija koda, koristimo for ili while petlje.
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')
# print('Pero Peric')

# range(start, stop, step) 
#   - > start = prvi broj raspona koji je UKLJUCEN u raspon
#   - > stop = zadnji broj raspona koji NIJE UKLJUCEN u raspon
#   - > step = predstavlja korak

# range(start, stop)
# range(start, stop, 1) isto kao i ovo gore
#   - > start = prvi broj raspona koji je UKLJUCEN u raspon
#   - > stop = zadnji broj raspona koji NIJE UKLJUCEN u raspon
#   - > step = predstavlja korak, a kada nije naveden onda je step = 1

# range(stop) -> start 
# range(0, stop, 1) isto kao i ovo gore
#   - > start = prvi broj raspona koji je UKLJUCEN u raspon, a kada nije naveden start = 0
#   - > stop = zadnji broj raspona koji NIJE UKLJUCEN u raspon
#   - > step = predstavlja korak, a kada nije naveden onda je step = 1

for number in range(10): # generira brojeve u rasponu od 0 do 9
    print('Pero Peric', number)