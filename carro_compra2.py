from carro_compra_funcion import *
from funcion_tabla import tabla

compras=[
    {'prod':"samsung",'cant':5,'precio':50000},
    {'prod':"apple",'cant':2,'precio':80000},
    {'prod':"microsoft",'cant':3,'precio':60000}
]

# mostrar_productos(compras)
tabla(compras)

print(f"la cantidad de productos es {cantidad_productos(compras)} ")
print(f"La suma total es :{total(compras)}")