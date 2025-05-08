print ("bienvenidos al entrenamiento con python")

"""
descuento en una compra:

si compras mas de $1000, obtioenes un decuento del 20%
"""
#pedir datos por teclado al usuario int (entero) float (decimales) str(cadena de texto) bool(boleano 1 o 0)
compra = float(input ("ingrese el valor de su compra: "))
des1 = float(0.20)
des2 = float(0)
if (compra >= 1000):
    des2 = compra*des1
    print (f"el descuento total es: {des2}")
    print (f"el total a pagar es: {compra-des2}")
else: print ("no es posible acceder al descuento")