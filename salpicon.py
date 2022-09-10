cesta = {}
continuar = True
while continuar:
    item = input('Introduce un fruta: ')
    color = input('Introduce el color de la ' + item + ': ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item, color] = precio
    print("\n ****************************")
    print('Lista de las frutas')
    for item, precio in cesta.items():
        print(item, '\t', color, '\t', precio)
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
costo = 0
print('Lista de las frutas')
for item, precio in reversed  (cesta.items()):
    print(item, '\t',color, '\t', precio)
    costo += precio
print('Costo total: ', costo)